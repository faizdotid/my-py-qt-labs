import sys
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QLabel, QLineEdit, QWidget

class DialogApp(QDialog):

    def __init__(self, parent: QWidget | None = None, f: Qt.WindowType = Qt.WindowFlags()) -> None:
        super().__init__(parent, f)

        self.setWindowTitle("Name Input Dialog")
        self.setFixedSize(400, 200)

        self.init_ui()

    def init_ui(self):
        self.edit = QLineEdit(self)
        self.edit.setText("What's your name?")
        self.edit.setStyleSheet("""
            QLineEdit {
                font-size: 18px;
                color: #333;
                font-family: Arial;
                border: 2px solid #2980b9;
                border-radius: 10px;
                padding: 10px;
                margin-bottom: 20px;
            }
            QLineEdit:focus {
                border-color: #3498db;
            }
        """)
        self.edit.setPlaceholderText("Enter your name")
        self.edit.selectAll()

        self.button = QPushButton("Submit", self)
        self.button.setStyleSheet("""
            QPushButton {
                font-size: 16px;
                color: white;
                background-color: #2980b9;
                border: 2px solid #2980b9;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #3498db;
                border-color: #3498db;
            }
        """)

        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        self.setLayout(layout)

        self.button.clicked.connect(self.on_submit)

    
    def on_submit(self):
        print(f"Name entered is: {self.edit.text()}")
        self.edit.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = DialogApp()
    dialog.show()
    sys.exit(app.exec())
