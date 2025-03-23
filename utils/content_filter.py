"""
Content filtering utility for child-friendly content
"""

class ContentFilter:
    """Content filter that checks for and replaces inappropriate language"""
    
    # List of inappropriate words to filter
    # This is a basic list - in production you might want to use a more comprehensive library
    INAPPROPRIATE_WORDS = [
        "shit", "fuck", "damn", "hell", "ass", "bitch", "crap", 
        "piss", "dick", "cock", "pussy", "asshole", "bastard", 
        "motherfucker", "bullshit", "horseshit", "jackass"
    ]
    
    @staticmethod
    def contains_inappropriate_language(text):
        """
        Check if text contains inappropriate language
        
        Args:
            text (str): Text to check
            
        Returns:
            bool: True if inappropriate language found, False otherwise
        """
        if not text:
            return False
            
        text_lower = text.lower()
        
        for word in ContentFilter.INAPPROPRIATE_WORDS:
            if word in text_lower:
                return True
                
        return False
    
    @staticmethod
    def filter_text(text):
        """
        Replace inappropriate words with asterisks
        
        Args:
            text (str): Text to filter
            
        Returns:
            str: Filtered text with inappropriate words replaced
        """
        if not text:
            return text
            
        filtered_text = text
        text_lower = text.lower()
        
        for word in ContentFilter.INAPPROPRIATE_WORDS:
            # Find all instances of the word (case insensitive)
            start_index = 0
            while True:
                index = text_lower.find(word, start_index)
                if index == -1:
                    break
                    
                # Replace with asterisks
                replacement = '*' * len(word)
                filtered_text = filtered_text[:index] + replacement + filtered_text[index + len(word):]
                text_lower = text_lower[:index] + replacement + text_lower[index + len(word):]
                
                # Move start index past this replacement
                start_index = index + len(word)
        
        return filtered_text 