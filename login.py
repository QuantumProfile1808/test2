from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFrame, QMessageBox
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtCore import Qt
import sys

uri = "mongodb+srv://fernandezlucasg4:1wtLRd6gxThC1w0p@cluster0.ladvsxc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Window setup
        self.setWindowTitle("Stock System Login")
        self.setFixedSize(400, 300)
        self.setStyleSheet(
            "background: qlineargradient(x1:0,y1:0,x2:1,y2:1, stop:0 #2193b0, stop:1 #6dd5ed);"
        )

        # Central frame container
        frame = QFrame(self)
        frame.setObjectName("frame")
        frame.setStyleSheet(
            "QFrame#frame {"
            "background: white;"
            "border-radius: 5%;"
            "}"
        )
        frame.setFixedSize(350, 250)
        frame.move(25, 25)


        # Logo (optional)
        logo = QLabel(frame)
        pixmap = QPixmap("logo.png")
        if pixmap.isNull():
            logo.hide()
        else:
            logo.setPixmap(pixmap.scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        logo.setAlignment(Qt.AlignCenter)

        # Title label
        title = QLabel("Welcome Back")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)

        # Username input
        self.input_username = QLineEdit()
        self.input_username.setPlaceholderText("Username")
        self.input_username.setFixedHeight(40)
        self.input_username.setStyleSheet(
            "padding: 0 10px; border: 1px solid #ccc; border-radius: 5px;"
        )

        # Password input
        self.input_password = QLineEdit()
        self.input_password.setPlaceholderText("Password")
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_password.setFixedHeight(40)
        self.input_password.setStyleSheet(
            "padding: 0 10px; border: 1px solid #ccc; border-radius: 5px;"
        )

        # Login button
        button_login = QPushButton("Login")
        button_login.setFixedHeight(40)
        button_login.setStyleSheet(
            "QPushButton {"
            "background-color: #2193b0;"
            "color: white;"
            "border-radius: 5px;"
            "}"
            "QPushButton:hover {"
            "background-color: #6dd5ed;"
            "}"
        )
        button_login.clicked.connect(self.handle_login)

        # Layout setup
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        layout.addWidget(logo)
        layout.addWidget(title)
        layout.addWidget(self.input_username)
        layout.addWidget(self.input_password)
        layout.addWidget(button_login)

    def handle_login(self):
        username = self.input_username.text()
        password = self.input_password.text()
        # TODO: Replace with real authentication logic
        if username == "admin" and password == "password":
            QMessageBox.information(self, "Success", "Login successful!")
        else:
            QMessageBox.warning(self, "Error", "Invalid username or password.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
