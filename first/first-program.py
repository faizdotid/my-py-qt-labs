import sys
from PySide6.QtWidgets import QApplication, QLabel, QInputDialog
from PySide6.QtCore import Qt, QEvent

class CustomInputDialog(QInputDialog):
    def event(self, event):
        # Check if the event type is of interest
        print(event.Type.__name__)
        return super().event(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Create the label
    label = QLabel("Hello World!")
    label.resize(200, 200)
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    label.setWindowTitle("Hello World")
    label.setStyleSheet("background-color: #e0e0e0; color: #333; font-size: 24px; font-family: Arial;")
    label.setAcceptDrops(True)
    label.show()

    # Create the custom input dialog
    input_dialog = CustomInputDialog(label)
    input_dialog.resize(200, 200)
    
    # Show the input dialog
    input_dialog.show()
    
    sys.exit(app.exec())
