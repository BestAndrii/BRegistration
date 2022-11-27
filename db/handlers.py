"""Обработка запросов в базу данных."""

import sqlite3

# Подключаем базу данных и создаём курсор
base = sqlite3.connect("base.db")
cursor = base.cursor()

# Создаём таблицу пользователей если её нет
request = "CREATE TABLE IF NOT EXISTS users(login PRIMARY KEY, password)"
cursor.execute(request)


# Добавить имя и пароль в базу
def add_items(name: str, password: str):
    """Добавляет имя пользователя name в столбец login,
    а пароль password в столбец password."""
    request = "INSERT INTO users VALUES(?, ?)"
    cursor.execute(request, (name, password))


# Получить пароль
def get_password(user_login: str):
    """Получить пароль пользователя по его логину user_login."""
    request = "SELECT password FROM users WHERE login == ?"
    password = cursor.execute(request, (user_login,)).fetchone()
    return password[0]


# Получить логиги в виде списка
def get_logins():
    request = "SELECT login FROM users"
    logins = cursor.execute(request).fetchall()
    return logins
