# # import sqlite3
# #
# # DB_NAME = "feedback.db"
# #
# #
# # def init_db():
# #     conn = sqlite3.connect(DB_NAME)
# #     cursor = conn.cursor()
# #
# #     cursor.execute("""
# #         CREATE TABLE IF NOT EXISTS feedback (
# #             id INTEGER PRIMARY KEY AUTOINCREMENT,
# #             name TEXT,
# #             email TEXT,
# #             feedback TEXT
# #         )
# #     """)
# #
# #     conn.commit()
# #     conn.close()
# #
# #
# # def save_feedback(name, email, feedback):
# #     conn = sqlite3.connect(DB_NAME)
# #     cursor = conn.cursor()
# #
# #     cursor.execute("""
# #         INSERT INTO feedback (name, email, feedback)
# #         VALUES (?, ?, ?)
# #     """, (name, email, feedback))
# #
# #     conn.commit()
# #     conn.close()
#
# import sqlite3
#
# DB_NAME = "feedback.db"
#
#
# def init_db():
#     conn = sqlite3.connect(DB_NAME)
#     cursor = conn.cursor()
#
#     # ✅ Feedback Table
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS feedback (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             email TEXT,
#             feedback TEXT
#         )
#     """)
#
#     # ✅ Chat History Table 🚀🔥
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS chat_history (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             user_message TEXT,
#             bot_response TEXT
#         )
#     """)
#
#     conn.commit()
#     conn.close()
#
#
# def save_feedback(name, email, feedback):
#     conn = sqlite3.connect(DB_NAME)
#     cursor = conn.cursor()
#
#     cursor.execute("""
#         INSERT INTO feedback (name, email, feedback)
#         VALUES (?, ?, ?)
#     """, (name, email, feedback))
#
#     conn.commit()
#     conn.close()
#
#
# # ✅ Save Chat 🚀🔥
# def save_chat(user_message, bot_response):
#     conn = sqlite3.connect(DB_NAME)
#     cursor = conn.cursor()
#
#     cursor.execute("""
#         INSERT INTO chat_history (user_message, bot_response)
#         VALUES (?, ?)
#     """, (user_message, bot_response))
#
#     conn.commit()
#     conn.close()
#
#
# # ✅ Load Chat History 🚀🔥
# def load_chat_history():
#     conn = sqlite3.connect(DB_NAME)
#     cursor = conn.cursor()
#
#     cursor.execute("SELECT user_message, bot_response FROM chat_history")
#
#     rows = cursor.fetchall()
#
#     conn.close()
#
#     return rows

import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

DB_NAME = "feedback.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # ✅ Drop old tables (schema-safe for hackathon 🚀🔥)
    cursor.execute("DROP TABLE IF EXISTS chat_history")

    cursor.execute("""
        CREATE TABLE chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_email TEXT,
            user_message TEXT,
            bot_response TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            password TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            feedback TEXT
        )
    """)

    conn.commit()
    conn.close()


def create_user(name, email, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    hashed_password = generate_password_hash(password)

    try:
        cursor.execute("""
            INSERT INTO users (name, email, password)
            VALUES (?, ?, ?)
        """, (name, email, hashed_password))

        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()


def validate_user(email, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM users WHERE email = ?", (email,))
    row = cursor.fetchone()

    conn.close()

    if row and check_password_hash(row[0], password):
        return True

    return False


def save_chat(user_email, user_message, bot_response):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO chat_history (user_email, user_message, bot_response)
        VALUES (?, ?, ?)
    """, (user_email, user_message, bot_response))

    conn.commit()
    conn.close()


def load_chat_history(user_email):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT user_message, bot_response
        FROM chat_history
        WHERE user_email = ?
    """, (user_email,))

    rows = cursor.fetchall()
    conn.close()

    return rows


def save_feedback(name, email, feedback):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO feedback (name, email, feedback)
        VALUES (?, ?, ?)
    """, (name, email, feedback))

    conn.commit()
    conn.close()