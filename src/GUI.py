from PySide6 import QtCore, QtWidgets, QtGui
import sys
from ClickableGrid import init, mainLoop

class Launcher(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.GridSize = 0
        self.shouldLoad = False
        self.layout = QtWidgets.QGridLayout(self)
        self.launcherScreen()


    def launcherScreen(self):
        self.inputGrid = QtWidgets.QLineEdit()
        self.buttonLaunch = QtWidgets.QPushButton("Launch")
        self.buttonLoad = QtWidgets.QPushButton("Launch Save")
        self.textGrid = QtWidgets.QLabel("Grid Size")

        self.layout.addWidget(self.textGrid, 1, 0)
        self.layout.addWidget(self.inputGrid, 2,0)
        self.layout.addWidget(self.buttonLoad, 4, 2)
        self.layout.addWidget(self.buttonLaunch,4,1)
        self.buttonLaunch.clicked.connect(self.storeValue)
        self.buttonLoad.clicked.connect(self.load)

    def storeValue(self):
        self.GridSize = int(self.inputGrid.text())
        self.X = int(self.GridSize/10)
        self.Y = int(self.GridSize/10)
        print(f"{self.GridSize} {self.X} {self.Y}")
        self.close()
        self.launch()


    def load(self):
        self.GridSize = int(self.inputGrid.text())
        self.X = int(self.GridSize/10)
        self.Y = int(self.GridSize/10)
        self.shouldLoad = True
        print(f"{self.GridSize} {self.X} {self.Y}")
        self.close()
        self.launch()


    def launch(self):
        self.grid = init(self.GridSize,self.GridSize,self.shouldLoad,"./Save")
        mainLoop((self.GridSize,self.GridSize),self.X,self.Y,self.grid)        


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = Launcher()
    widget.show()

    sys.exit(app.exec())