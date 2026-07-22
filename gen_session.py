"""
Запустите этот скрипт ОДИН РАЗ локально:
    pip install kurigram
    python gen_session.py

Введите номер телефона и код — получите SESSION_STRING.
Вставьте его в переменные Railway.
"""
from pyrogram import Client

API_ID   = 2040
API_HASH = "b18441a1ff607e10a989891a5462e627"

with Client("my_session", api_id=API_ID, api_hash=API_HASH) as app:
    print("\n✅ SESSION_STRING:\n")
    print(app.export_session_string())
    print("\nСкопируйте строку выше и вставьте в Railway → Variables → SESSION_STRING")
