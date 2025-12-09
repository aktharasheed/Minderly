# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    CHAT_TIMEOUT = 30  # seconds
    MAX_CONVERSATION_HISTORY = 10
    DEFAULT_RESPONSE = "I'm here to listen and support you. Would you like to tell me more?"
    EMERGENCY_KEYWORDS = [
        'suicide', 'kill', 'die', 'end', 'hurt'
    ]
    EMERGENCY_CONTACTS = {
        'crisis_hotline': '1-800-273-8255',
        'emergency': '911'
    }