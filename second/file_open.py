import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QFileDialog, QDialog, QWidget, QMainWindow
from PySide6.QtGui import QMatrix3x4

class Maim(QDialog):

    def __init__(self, parent: QWidget | None = ..., f: Qt.WindowType = ...) -> None:
        super().__init__(parent, f)

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QWidget()