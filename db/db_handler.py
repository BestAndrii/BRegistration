"""Модуль базы данных."""

import sqlite3


base = sqlite3.connect("users.db")

base.execute("CREATE TABLE IF NOT EXISTS data(login PRIMARY KEY, password)")


def get_password(login: str) -> str:
    """Получить пароль по логину."""
    request = "SELECT password FROM data WHERE login == ?"
    password = base.execute(request, (login,)).fetchone()
    return password[0]


def add_user(login: str, password: str) -> None:
    """Добавить пользователя в базу данных."""
    request = "INSERT INTO data VALUES(?, ?)"
    base.execute(request, (login, password))


def exists_user(login: str) -> bool:
    """Опредилить существует пользователь или нет."""
    request = "SELECT login FROM data"
    users = base.execute(request).fetchall()

    for user in users:
        if user[0] == login:
            return True

    return False
