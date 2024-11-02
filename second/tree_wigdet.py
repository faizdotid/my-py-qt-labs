import sys
from PySide6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem
from PySide6.QtCore import Qt
app = QApplication(sys.argv)

data = {
    "Fruits": ["Apple", "Banana", "Cherry", "Date"],
    "Vegetables": ["Carrot", "Broccoli", "Cabbage", "Onion"],
    "Grains": ["Barley", "Corn", "Oats", "Rice"],
    "Meats": ["Beef", "Chicken", "Lamb", "Pork"],
}

tree = QTreeWidget()
tree.setWindowTitle("Tree Widget")
tree.resize(400, 300)
tree.setColumnCount(2)

tree.setHeaderLabels(["Category", "Items"])

for key, values in data.items():
    parent = QTreeWidgetItem(tree, [key])
    for value in values:
        child = QTreeWidgetItem(parent, [value])

tree.show()

sys.exit(app.exec())