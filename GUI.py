from PySide6 import QtCore, QtWidgets, QtGui
import sys
import random
from ClickableGrid import init, mainLoop

class Launcher(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.GridSize = 0
        self.layout = QtWidgets.QGridLayout(self)
        self.launcherScreen()


    def launcherScreen(self):
        self.inputGrid = QtWidgets.QLineEdit()
        self.button = QtWidgets.QPushButton("Launch")
        self.text = QtWidgets.QLabel("Grid Size")
        self.layout.addWidget(self.text, 1, 0)
        self.layout.addWidget(self.inputGrid, 2,0)
        self.layout.addWidget(self.button,4,1)
        self.button.clicked.connect(self.storeValue)

    def storeValue(self):
        self.GridSize = int(self.inputGrid.text())
        self.X = int(self.GridSize/10)
        self.Y = int(self.GridSize/10)
        print(f"{self.GridSize} {self.X} {self.Y}")
        self.close()
        self.launch()

    def launch(self):
        self.grid = init(self.GridSize,self.GridSize)
        mainLoop((self.GridSize,self.GridSize),self.X,self.Y,self.grid)        


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = Launcher()
    widget.show()

    sys.exit(app.exec())