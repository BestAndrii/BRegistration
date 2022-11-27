"""Модуль для заппуска программы и обработки главного окна."""


import sys

from sqlite3 import IntegrityError

from des import Interface
from db import handlers as db

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox


class Window(QMainWindow):
    """Класс создаёт главное окно, а интерфейс загружает с модуля des."""

    def __init__(self):
        super().__init__()

        # Загружаем дизайн
        self.ui = Interface()
        self.ui.setup_ui(self)

        self.ui.login.clicked.connect(self.login)
        self.ui.register.clicked.connect(self.registration)

    def show_message(self, title, message: str):
        """Выводит окно с сообщением message с кнопкой OK по центру."""
        QMessageBox.about(self, title, message)

    def login(self):
        """Войти в базу данных."""

        # Получаем введёные пользователем логин и пароль
        login = self.ui.name.text()
        password = self.ui.password.text()

        # Получаем логины из базы данных
        logins = db.get_logins()

        # Проверяем есть ли введёный логин в базе данных
        for log in logins:
            if log[0] == login:
                normal_password = db.get_password(login)

                if password == normal_password:
                    message = "Успешная авторизация в систему!"
                    self.show_message("Успешная авторизация!", message)
                    break

                else:
                    message = f"Вы ввели неверный пароль для пользователя {login}"
                    self.show_message("Неверный пароль", message)
                    break

        else:
            message = "Такого логина нет, попробуйте ещё раз"
            self.show_message("Такого логина нет", message)

    def registration(self):
        """Зарегистрироваться в базу данных."""

        # Получаем введёные пользователем логин и пароль
        login = self.ui.name.text()
        password = self.ui.password.text()

        try:
            # Добавляем логин и пароль в базу
            db.add_items(login, password)

            message = f"Успешная регистрация в базу под логином {login}!"
            self.show_message("Успешная регистрация!", message)

            db.base.commit()

        # Если логин уже существует
        except IntegrityError:
            message = "Такой логин уже существует в базе данных!"
            self.show_message("Логин уже существует", message)


def start_app():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
