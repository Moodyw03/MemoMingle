from werkzeug.security import generate_password_hash, check_password_hash
from config.supabase import supabase


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
