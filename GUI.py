from PySide6 import QtCore, QtWidgets, QtGui
import sys
import random
import GameOfLife


class Launcher(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.button = QtWidgets.QPushButton("Launch")
        self.inputGrid = QtWidgets.QLineEdit()
        self.text = QtWidgets.QLabel("Grid Size")

        self.layout = QtWidgets.QGridLayout(self)
        self.layout.addWidget(self.text, 1, 0)
        self.layout.addWidget(self.inputGrid, 2,0)
        self.layout.addWidget(self.button,4,1)
        self.button.clicked.connect(self.launch)

    def launch(self):
        self.GridSize = int(self.inputGrid.text())
        print(self.GridSize)
        GameOfLife.main(self.GridSize,self.GridSize)
        


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = Launcher()
    widget.show()

    sys.exit(app.exec())