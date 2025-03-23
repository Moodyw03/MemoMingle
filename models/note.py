from datetime import datetime
from config.supabase import supabase


class Note:
    def __init__(self, title, content, tags=None, user_id=None):
        self.title = title
        self.content = content
        self.dateCreated = datetime.now()  # Set on object creation
        self.tags = tags if tags else []
        self.user_id = user_id

    def insert(self):
        # Set 'lastModified' to the current time on insert
        result = supabase.table("notes").insert(
            {
                "title": self.title,
                "content": self.content,
                "datecreated": self.dateCreated.isoformat(),
                "lastmodified": datetime.now().isoformat(),
                "tags": self.tags,
                "user_id": self.user_id,
            }
        ).execute()
        return result.data[0]['id'] if result.data else None

    @staticmethod
    def find_all(user_id=None):
        result = supabase.table("notes").select("*").eq("user_id", user_id).order("lastmodified", desc=True).execute()
        return result.data

    @staticmethod
    def find_by_id(note_id):
        result = supabase.table("notes").select("*").eq("id", note_id).execute()
        return result.data[0] if result.data else None

    @staticmethod
    def update(note_id, new_data):
        # Update the lastmodified field with current time
        new_data["lastmodified"] = datetime.now().isoformat()
        supabase.table("notes").update(new_data).eq("id", note_id).execute()

    @staticmethod
    def delete(note_id):
        supabase.table("notes").delete().eq("id", note_id).execute()

    @staticmethod
    def search(query, user_id=None):
        # Note: Supabase uses PostgreSQL with different search capabilities
        # Search by title
        title_results = supabase.table("notes").select("*").eq("user_id", user_id).ilike("title", f"%{query}%").execute()
        # Search by content
        content_results = supabase.table("notes").select("*").eq("user_id", user_id).ilike("content", f"%{query}%").execute()
        
        # Combine results (removing duplicates)
        all_results = title_results.data + content_results.data
        unique_ids = set()
        unique_results = []
        
        for note in all_results:
            if note['id'] not in unique_ids:
                unique_ids.add(note['id'])
                unique_results.append(note)
                
        return unique_results
