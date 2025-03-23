from datetime import datetime
from config.supabase import supabase
import re


class Note:
    # List of inappropriate words for children's content
    INAPPROPRIATE_WORDS = [
        "badword", "curse", "swear", "profanity", "inappropriate", 
        # Add more inappropriate words here
    ]
    
    def __init__(self, title, content, tags=None, user_id=None):
        self.title = title
        self.content = content
        self.dateCreated = datetime.now()  # Set on object creation
        self.tags = tags if tags else []
        self.user_id = user_id

    def insert(self):
        # Filter content before saving
        filtered_title = self._filter_content(self.title)
        filtered_content = self._filter_content(self.content)
        
        # Set 'lastModified' to the current time on insert
        result = supabase.table("notes").insert(
            {
                "title": filtered_title,
                "content": filtered_content,
                "datecreated": self.dateCreated.isoformat(),
                "lastmodified": datetime.now().isoformat(),
                "tags": self.tags,
                "user_id": self.user_id,
                "has_inappropriate_content": self._contains_inappropriate_content(self.title + " " + self.content)
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
        # Filter content before updating
        if "title" in new_data:
            new_data["title"] = Note._filter_content(new_data["title"])
        
        if "content" in new_data:
            new_data["content"] = Note._filter_content(new_data["content"])
            
        # Check if content contains inappropriate words
        if "title" in new_data or "content" in new_data:
            # Get the note to check combined content
            note = Note.find_by_id(note_id)
            title = new_data.get("title", note.get("title", ""))
            content = new_data.get("content", note.get("content", ""))
            new_data["has_inappropriate_content"] = Note._contains_inappropriate_content(title + " " + content)
        
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
        
    @staticmethod
    def _filter_content(text):
        """Replace inappropriate words with asterisks"""
        if not text:
            return text
            
        filtered_text = text
        for word in Note.INAPPROPRIATE_WORDS:
            # Use word boundaries to match whole words
            pattern = r'\b' + re.escape(word) + r'\b'
            replacement = '*' * len(word)
            filtered_text = re.sub(pattern, replacement, filtered_text, flags=re.IGNORECASE)
            
        return filtered_text
        
    @staticmethod
    def _contains_inappropriate_content(text):
        """Check if text contains any inappropriate words"""
        if not text:
            return False
            
        for word in Note.INAPPROPRIATE_WORDS:
            # Use word boundaries to match whole words
            pattern = r'\b' + re.escape(word) + r'\b'
            if re.search(pattern, text, re.IGNORECASE):
                return True
                
        return False
        
    @staticmethod
    def get_flagged_notes(parent_id):
        """Get all notes from children accounts that contain inappropriate content"""
        # Get all children of the parent
        from models.user import User
        children = User.get_children(parent_id)
        child_ids = [child["id"] for child in children]
        
        if not child_ids:
            return []
            
        # Get all flagged notes from all children
        flagged_notes = []
        for child_id in child_ids:
            result = supabase.table("notes").select("*").eq("user_id", child_id).eq("has_inappropriate_content", True).execute()
            if result.data:
                for note in result.data:
                    # Add child username to each note
                    for child in children:
                        if child["id"] == note["user_id"]:
                            note["child_username"] = child["username"]
                            break
                    flagged_notes.append(note)
                
        return flagged_notes
