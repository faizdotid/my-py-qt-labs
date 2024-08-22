import sys
from PySide6.QtWidgets import QApplication, QPushButton, QStyle
from PySide6.QtCore import Slot

@Slot()
def what_to_do():
    print("Button clicked!")

if __name__ == "__main__":

    app = QApplication(sys.argv)
    button = QPushButton("Click me!")
    button.setStyleSheet("background-color: #232323; border: 1px solid #333; color: #333; font-size: 24px; font-family: Arial; border-radius: 5px; margin: 10px; padding: 10px;")
    button.clicked.connect(what_to_do)
    button.show()
    sys.exit(app.exec())