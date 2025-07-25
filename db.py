import sqlite3
from datetime import datetime


def init_db():
    conn = sqlite3.connect("finance_bot.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS operations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            amount INTEGER,
            category TEXT,
            data_operation TIMESTAMP,
            flag BOOLEAN
        );
    """)
    conn.commit()
    conn.close()


def insert_operation(user_id: int, amount: int, category: str, is_income: int):
    conn = sqlite3.connect("finance_bot.db")
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO operations (user_id, amount, category, data_operation, flag)
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, amount, category, datetime.now(), int(is_income)))
    conn.commit()
    conn.close()
