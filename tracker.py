from config import KEYWORDS

def match_keywords(text):
    text = text.lower()
    return any(k.lower() in text for k in KEYWORDS)