import sys
from typing import Optional
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot, Signal, QObject


class Communicate(QObject):
    count = Signal(int)

    def __init__(self, parent: Optional[QObject] = None) -> None:
        super().__init__(parent)
        self.count.connect(self.count_slot)

    @Slot(int)
    def count_slot(self, number: int) -> None:
        print(f"Count is {number}")

    def emit_count(self) -> None:
        self.count.emit(31)  # Emit the signal with a value, e.g., 1

    @Slot()
    def no_arg_slot(self) -> None:
        print("No arguments")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    button = QPushButton("Click me!")
    button.setStyleSheet(
        "background-color: #232323; border: 1px solid #333; color: #333; font-size: 24px; font-family: Arial; border-radius: 5px; margin: 10px; padding: 10px;"
    )
    comm = Communicate()
    button.clicked.connect(comm.emit_count)  # Connect the button click to emit_count
    button.show()
    sys.exit(app.exec())
