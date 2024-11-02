import sys
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QApplication, QTableWidget \
    , QTableWidgetItem


# thanks for gpt for color suggestions
colors = [
    ("AliceBlue", QColor(240, 248, 255)),
    ("AntiqueWhite", QColor(250, 235, 215)),
    ("Aqua", QColor(0, 255, 255)),
    ("Aquamarine", QColor(127, 255, 212)),
    ("Azure", QColor(240, 255, 255)),
    ("Beige", QColor(245, 245, 220)),
    ("Bisque", QColor(255, 228, 196)),
    ("Black", QColor(0, 0, 0)),
    ("BlanchedAlmond", QColor(255, 235, 205)),
    ("Blue", QColor(0, 0, 255)),
    ("BlueViolet", QColor(138, 43, 226)),
    ("Brown", QColor(165, 42, 42)),
    ("BurlyWood", QColor(222, 184, 135)),
    ("CadetBlue", QColor(95, 158, 160)),
    ("Chartreuse", QColor(127, 255, 0)),
    ("Chocolate", QColor(210, 105, 30)),
    ("Coral", QColor(255, 127, 80)),
    ("CornflowerBlue", QColor(100, 149, 237)),
    ("Cornsilk", QColor(255, 248, 220)),
    ("Crimson", QColor(220, 20, 60)),
    ("Cyan", QColor(0, 255, 255)),
    ("DarkBlue", QColor(0, 0, 139)),
    ("DarkCyan", QColor(0, 139, 139)),
    ("DarkGoldenrod", QColor(184, 134, 11)),
    ("DarkGray", QColor(169, 169, 169)),
    ("DarkGreen", QColor(0, 100, 0)),
    ("DarkKhaki", QColor(189, 183, 107)),
    ("DarkMagenta", QColor(139, 0, 139)),
    ("DarkOliveGreen", QColor(85, 107, 47)),
    ("DarkOrange", QColor(255, 140, 0)),
    ("DarkOrchid", QColor(153, 50, 204)),
    ("DarkRed", QColor(139, 0, 0)),
    ("DarkSalmon", QColor(233, 150, 122)),
    ("DarkSeaGreen", QColor(143, 188, 143)),
]


# function from hex to rgb
# ref: https://doc.qt.io/qtforpython-6/tutorials/basictutorial/tablewidget.html
def get_rgb_from_hex(code):
    code_hex = code.replace("#", "")
    rgb = tuple(int(code_hex[i:i+2], 16) for i in (0, 2, 4))
    return QColor.fromRgb(rgb[0], rgb[1], rgb[2])


app = QApplication(sys.argv)

table = QTableWidget()
table.resize(500, 300)
table.setWindowTitle("Color Table")
table.setRowCount(len(colors))
table.setColumnCount(2)
table.setHorizontalHeaderLabels(["Color Name", "Color"])

for i, (name, color) in enumerate(colors):
    item = QTableWidgetItem(name)
    table.setItem(i, 0, item)
    table.setColumnWidth(0, 200)

    item = QTableWidgetItem()
    item.setBackground(color)
    table.setItem(i, 1, item)

table.show()

sys.exit(app.exec())