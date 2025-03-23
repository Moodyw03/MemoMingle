from werkzeug.security import generate_password_hash, check_password_hash
from config.supabase import supabase
from datetime import datetime


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def insert(self):
        result = supabase.table('users').insert({
            'username': self.username,
            'password': self.password
        }).execute()
        return result.data[0]['id'] if result.data else None

    @staticmethod
    def find_by_username(username):
        result = supabase.table('users').select('*').eq('username', username).execute()
        return result.data[0] if result.data else None

    @staticmethod
    def find_by_id(user_id):
        result = supabase.table('users').select('*').eq('id', user_id).execute()
        return result.data[0] if result.data else None

    @staticmethod
    def verify_password(email, password):
        user = User.find_by_username(email)
        if user:
            return check_password_hash(user['password'], password)
        return False

    @staticmethod
    def update_password(user_id, new_password):
        """Update a user's password in the database"""
        hashed_password = generate_password_hash(new_password)
        
        data = supabase.table('users') \
            .update({"password": hashed_password}) \
            .eq("id", user_id) \
            .execute()
        
        return data.data[0] if data.data else None
        
    @staticmethod
    def update_streak(user_id):
        """Update a user's login streak
        If streak columns don't exist yet, just update last_login"""
        user = User.find_by_id(user_id)
        
        if not user:
            return None
            
        try:
            # Get current date
            today = datetime.now().date()
            
            # Get last login date
            last_login = None
            if user.get('last_login'):
                last_login = datetime.fromisoformat(user['last_login'].replace('Z', '+00:00')).date()
            
            streak = user.get('streak', 0)
            highest_streak = user.get('highest_streak', 0)
            
            # Calculate new streak
            if not last_login:
                # First login
                streak = 1
            elif (today - last_login).days == 1:
                # Consecutive day
                streak += 1
            elif (today - last_login).days > 1:
                # Break in streak
                streak = 1
            # If same day, don't change streak
            
            # Update highest streak if needed
            if streak > highest_streak:
                highest_streak = streak
            
            # Update user in database with all streak data
            data = supabase.table('users') \
                .update({
                    "last_login": datetime.now().isoformat(),
                    "streak": streak,
                    "highest_streak": highest_streak
                }) \
                .eq("id", user_id) \
                .execute()
                
            return data.data[0] if data.data else None
            
        except Exception as e:
            # If update fails (likely due to missing columns), just update last_login
            try:
                # Fallback to just updating last_login
                data = supabase.table('users') \
                    .update({
                        "last_login": datetime.now().isoformat()
                    }) \
                    .eq("id", user_id) \
                    .execute()
                return data.data[0] if data.data else None
            except:
                # If even that fails, just return the user
                return user
        
    @staticmethod
    def get_achievements(user_id):
        """Get a user's achievements based on their activity"""
        try:
            user = User.find_by_id(user_id)
            
            if not user:
                return []
                
            achievements = []
            
            # Streak achievements
            streak = user.get('streak', 0)
            if streak >= 3:
                achievements.append({
                    "name": "3-Day Streak",
                    "icon": "🔥",
                    "unlocked": True
                })
            
            if streak >= 7:
                achievements.append({
                    "name": "Weekly Writer",
                    "icon": "📝",
                    "unlocked": True
                })
                
            if streak >= 30:
                achievements.append({
                    "name": "Monthly Master",
                    "icon": "🏆",
                    "unlocked": True
                })
                
            # Note count achievements
            note_count = user.get('note_count', 0)
            if note_count >= 5:
                achievements.append({
                    "name": "Noteworthy",
                    "icon": "📌",
                    "unlocked": True
                })
                
            if note_count >= 20:
                achievements.append({
                    "name": "Prolific Writer",
                    "icon": "✍️",
                    "unlocked": True
                })
                
            if note_count >= 50:
                achievements.append({
                    "name": "Diary Devotee",
                    "icon": "📚",
                    "unlocked": True
                })
                
            # Add achievements that haven't been unlocked yet
            if streak < 3:
                achievements.append({
                    "name": "3-Day Streak",
                    "icon": "🔒",
                    "unlocked": False
                })
                
            if note_count < 5:
                achievements.append({
                    "name": "Noteworthy",
                    "icon": "🔒",
                    "unlocked": False
                })
                
            return achievements
        except Exception:
            # If there's any error (like missing columns), return an empty list
            return []
