from werkzeug.security import generate_password_hash, check_password_hash
from config.supabase import supabase
from datetime import datetime


class User:
    """User model"""

    def __init__(self, username, password, is_parent=False, parent_id=None):
        """Initialize a user with username and password"""
        self.username = username
        self.password = generate_password_hash(password)
        self.is_parent = is_parent
        self.parent_id = parent_id
        self.created_at = datetime.now().isoformat()

    def insert(self):
        """Insert a user into the database"""
        data = supabase.table("users").insert({
            "username": self.username,
            "password": self.password,
            "is_parent": self.is_parent,
            "parent_id": self.parent_id,
            "created_at": self.created_at
        }).execute()

        if len(data.data) > 0:
            return data.data[0]["id"]
        return None

    @staticmethod
    def find_by_username(username):
        """Find a user by username"""
        data = supabase.table("users").select("*").eq("username", username).execute()
        if len(data.data) > 0:
            return data.data[0]
        return None

    @staticmethod
    def get_by_email(email):
        """Find a user by email"""
        data = supabase.table("users").select("*").eq("email", email).execute()
        if len(data.data) > 0:
            return data.data[0]
        return None

    @staticmethod
    def find_by_id(user_id):
        """Find a user by id"""
        data = supabase.table("users").select("*").eq("id", user_id).execute()
        if len(data.data) > 0:
            return data.data[0]
        return None

    @staticmethod
    def verify_password(username, password):
        """Verify a user's password"""
        user = User.find_by_username(username)
        if user and check_password_hash(user["password"], password):
            return True
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
    
    @staticmethod
    def create_child_account(parent_id, username, password):
        """Create a child account linked to a parent account"""
        # Check if parent exists and is a parent account
        parent = User.find_by_id(parent_id)
        if not parent or not parent.get("is_parent", False):
            return None, "Invalid parent account"
            
        # Check if username is already taken
        if User.find_by_username(username):
            return None, "Username already exists"
            
        # Create child account
        child = User(username, password, is_parent=False, parent_id=parent_id)
        child_id = child.insert()
        
        if child_id:
            return child_id, None
        return None, "Failed to create child account"
    
    @staticmethod
    def get_children(parent_id):
        """Get all children accounts for a parent"""
        data = supabase.table("users") \
            .select("*") \
            .eq("parent_id", parent_id) \
            .execute()
            
        return data.data if data.data else []
    
    @staticmethod
    def is_parent_of(parent_id, child_id):
        """Check if user is parent of child"""
        child = User.find_by_id(child_id)
        return child and child.get("parent_id") == parent_id
        
    @staticmethod
    def delete_user(user_id):
        """Delete a user from the database"""
        try:
            # First, check if this user is a parent with child accounts
            children = User.get_children(user_id)
            if children:
                return False, "Cannot delete a parent account with child accounts. Delete child accounts first."
            
            # Delete user's notes first to avoid orphaned records
            from models.note import Note
            notes = Note.find_all(user_id)
            for note in notes:
                Note.delete(note["id"])
            
            # Now delete the user
            result = supabase.table("users").delete().eq("id", user_id).execute()
            
            # Check for successful deletion - Supabase returns empty data list when no matching record
            if result.data is not None:
                return True, "User deleted successfully"
            return False, "User not found or could not be deleted"
        except Exception as e:
            print(f"Error deleting user: {e}")  # Add this for debugging
            return False, f"Error deleting user: {str(e)}"
