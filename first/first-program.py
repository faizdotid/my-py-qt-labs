import sys
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtCore import Qt

if __name__ == "__main__":
    app = QApplication(sys.argv)
    label = QLabel("Hello World!")
    label.resize(200, 200)
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    label.setWindowTitle("Hello World")
    label.setStyleSheet("background-color: #e0e0e0; color: #333; font-size: 24px; font-family: Arial;")
    label.setAcceptDrops(True)
    label.show()
    sys.exit(app.exec())