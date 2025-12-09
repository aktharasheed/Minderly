# database.py
import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_file="minderly.db"):
        self.db_file = db_file
        self.init_db()

    def init_db(self):
        with sqlite3.connect(self.db_file) as conn:
            c = conn.cursor()
            
            # Create users table
            c.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    phone TEXT UNIQUE NOT NULL,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Create conversations table
            c.execute('''
                CREATE TABLE IF NOT EXISTS conversations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    message TEXT NOT NULL,
                    response TEXT NOT NULL,
                    emotion TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )
            ''')
            conn.commit()

    def create_user(self, name, email, phone):
        try:
            with sqlite3.connect(self.db_file) as conn:
                c = conn.cursor()
                c.execute('''
                    INSERT INTO users (name, email, phone)
                    VALUES (?, ?, ?)
                ''', (name, email, phone))
                user_id = c.lastrowid
                return {"success": True, "user_id": user_id}
        except sqlite3.IntegrityError as e:
            if "UNIQUE constraint failed" in str(e):
                return {"success": False, "error": "Email or phone number already exists"}
            return {"success": False, "error": str(e)}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_user(self, email):
        with sqlite3.connect(self.db_file) as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM users WHERE email = ?', (email,))
            user = c.fetchone()
            
            if user:
                return {
                    "id": user[0],
                    "name": user[1],
                    "email": user[2],
                    "phone": user[3]
                }
            return None

    def log_conversation(self, user_id, message, response, emotion):
        with sqlite3.connect(self.db_file) as conn:
            c = conn.cursor()
            c.execute('''
                INSERT INTO conversations (user_id, message, response, emotion)
                VALUES (?, ?, ?, ?)
            ''', (user_id, message, response, emotion))
            conn.commit()

    def get_user_conversations(self, user_id):
        with sqlite3.connect(self.db_file) as conn:
            c = conn.cursor()
            c.execute('''
                SELECT message, response, emotion, timestamp 
                FROM conversations 
                WHERE user_id = ? 
                ORDER BY timestamp DESC
            ''', (user_id,))
            return c.fetchall()