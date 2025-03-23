"""
Content filtering utility for child-friendly content
"""
import re

class ContentFilter:
    """Content filter that checks for and replaces inappropriate language"""
    
    # List of inappropriate words to filter
    # This is a more comprehensive list
    INAPPROPRIATE_WORDS = [
        # Common profanity
        "shit", "fuck", "damn", "hell", "ass", "bitch", "crap", 
        "piss", "dick", "cock", "pussy", "asshole", "bastard", 
        "motherfucker", "bullshit", "horseshit", "jackass", "cunt",
        "twat", "whore", "slut", "hoe", "tits", "boobs", "wanker",
        "douchebag", "douche", "jerk", "jerkoff", "dumbass", "fag",
        "faggot", "homo", "queer", "retard", "retarded", "nigger",
        "nigga", "spic", "wetback", "chink", "gook", "kike", "paki",
        "dyke", "kyke", "raghead", "negro",
        
        # Partial matches (these will be used with regex boundaries)
        "f*ck", "f**k", "f***", "s***", "sh*t", "b*tch", "a**", 
        "a**hole", "a-hole", "bs", "b.s.", "wtf", "stfu", "fu", 
        "sob", "pos", "mofo", "mf", "mtf", "ftm", "lmfao", "lmao",
        
        # Sexual terms
        "porn", "blowjob", "handjob", "rimjob", "anal", "cum", "cumming",
        "jizz", "masturbate", "dildo", "vibrator", "sex", "sexy",
        "orgasm", "boner", "erection", "horny",
        
        # Drug-related
        "weed", "cocaine", "heroin", "meth", "crack", "lsd", "ecstasy",
        "marijuana", "pot", "dope", "high", "stoned", "junkie"
    ]
    
    # Compile regex patterns for better matching
    WORD_PATTERNS = []
    
    @classmethod
    def _initialize_patterns(cls):
        """Initialize regex patterns for word matching"""
        # Only initialize once
        if cls.WORD_PATTERNS:
            return
            
        # Create word boundary patterns for each word
        for word in cls.INAPPROPRIATE_WORDS:
            # Escape regex special characters
            escaped_word = re.escape(word)
            # Create pattern with word boundaries
            pattern = re.compile(r'\b' + escaped_word + r'\b', re.IGNORECASE)
            cls.WORD_PATTERNS.append((word, pattern))
    
    @classmethod
    def contains_inappropriate_language(cls, text):
        """
        Check if text contains inappropriate language
        
        Args:
            text (str): Text to check
            
        Returns:
            bool: True if inappropriate language found, False otherwise
        """
        if not text:
            return False
        
        # Initialize patterns if needed
        cls._initialize_patterns()
        
        # Check for inappropriate words using regex
        for word, pattern in cls.WORD_PATTERNS:
            if pattern.search(text):
                return True
                
        # Additional check for common phrases or partial matches
        text_lower = text.lower()
        
        # Check for words without boundaries (more aggressive checking)
        for word in cls.INAPPROPRIATE_WORDS:
            if word in text_lower:
                return True
                
        return False
    
    @classmethod
    def filter_text(cls, text):
        """
        Remove inappropriate words from text
        
        Args:
            text (str): Text to filter
            
        Returns:
            str: Filtered text with inappropriate words removed
        """
        if not text:
            return text
            
        # Initialize patterns if needed
        cls._initialize_patterns()
        
        filtered_text = text
        
        # Remove words using regex patterns (more accurate)
        for word, pattern in cls.WORD_PATTERNS:
            # Remove the inappropriate word (replace with empty string)
            filtered_text = pattern.sub('', filtered_text)
        
        # Additional check for words without boundaries
        # This is more aggressive filtering
        text_lower = filtered_text.lower()
        
        for word in cls.INAPPROPRIATE_WORDS:
            # Find all instances of the word (case insensitive)
            start_index = 0
            while True:
                index = text_lower.find(word, start_index)
                if index == -1:
                    break
                    
                # Check if this is a standalone word or part of another word
                # If it's part of another word and we already caught it with regex, skip
                if (index > 0 and text_lower[index-1].isalnum()) or \
                   (index + len(word) < len(text_lower) and text_lower[index+len(word)].isalnum()):
                    # Part of another word, move on
                    start_index = index + len(word)
                    continue
                    
                # Remove the inappropriate word (replace with empty string)
                filtered_text = filtered_text[:index] + '' + filtered_text[index + len(word):]
                text_lower = text_lower[:index] + '' + text_lower[index + len(word):]
                
                # We don't need to update start_index since we removed the word
        
        # Additional cleanup to remove consecutive spaces created by removing words
        filtered_text = ' '.join(filtered_text.split())
        
        return filtered_text 