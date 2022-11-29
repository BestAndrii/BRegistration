import sys

from db.db_handler import *
from des import Intreface

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox


class Window(QMainWindow):
    """Класс создаёт главное окно."""

    def __init__(self) -> None:
        super().__init__()

        # Загружаем дизайн программы
        self.ui = Intreface()
        self.ui.setup_ui(self)

        self.ui.pushButton.clicked.connect(self.registration)
        self.ui.pushButton_2.clicked.connect(self.login)

    def show_message(self, message: str) -> None:
        """Вывести сообщение на экран."""
        msg = QMessageBox()
        msg.setText(message)
        msg.exec_()

    def login(self) -> None:
        """Авторизоваться в аккаунт."""
        # Данные введёние пользователем
        login = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        # Проверяем, существуем ли пользователь
        exists = exists_user(login)

        if exists == True:
            true_password = get_password(login)

            if password == true_password:
                message = "Successful authorization!"
                self.show_message(message)

            else:
                message = "Invalid password"
                self.show_message(message)

        else:
            message = f"User {login} does not exist"
            self.show_message(message)

    def registration(self) -> None:
        """Зарегистрироваться в базу."""
        # Данные введёние пользователем
        login = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        # Проверяем, существуем ли пользователь УЖЕ
        exists = exists_user(login)

        if exists == True:
            message = f"User {login} already exists"
            self.show_message(message)

        else:
            add_user(login, password)

            message = "Successful registration!"
            self.show_message(message)

            base.commit()


def start_app(argv):
    """Запустить программу."""
    app = QApplication(argv)
    window = Window()
    window.show()
    exit(app.exec_())


if __name__ == "__main__":
    start_app(sys.argv)
