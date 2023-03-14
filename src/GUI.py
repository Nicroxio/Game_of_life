from PySide6 import QtCore, QtWidgets, QtGui
import sys
from ClickableGrid import init, mainLoop


class Launcher(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.GridSize = 0
        self.saveLocation = "./Save"
        self.shouldLoad = False
        self.layout = QtWidgets.QGridLayout(self)
        self.launcherScreen()

    def launcherScreen(self):
        self.inputGrid = QtWidgets.QLineEdit()
        self.inputSaveName = QtWidgets.QLineEdit()
        self.buttonLaunch = QtWidgets.QPushButton("Launch")
        self.buttonLoad = QtWidgets.QPushButton("Launch Save")
        self.textGrid = QtWidgets.QLabel("Grid Size")
        self.textSaveName = QtWidgets.QLabel("Save Name")

        self.layout.addWidget(self.textGrid, 1, 0)
        self.layout.addWidget(self.inputGrid, 2, 0)
        self.layout.addWidget(self.textSaveName, 3, 0)
        self.layout.addWidget(self.inputSaveName, 4, 0)
        self.layout.addWidget(self.buttonLoad, 5, 2)
        self.layout.addWidget(self.buttonLaunch, 5, 1)
        self.buttonLaunch.clicked.connect(self.storeValue)
        self.buttonLaunch.clicked.connect(self.run)
        self.buttonLoad.clicked.connect(self.storeValue)
        self.buttonLoad.clicked.connect(self.load)

    def storeValue(self):
        self.GridSize = int(self.inputGrid.text())
        self.saveLocation = str(self.inputSaveName.text())
        self.X = int(self.GridSize/10)
        self.Y = int(self.GridSize/10)
        print(f"{self.GridSize} {self.X} {self.Y} {self.saveLocation}")

    def load(self):
        self.shouldLoad = True
        self.close()
        self.launch()

    def run(self):
        self.close()
        self.launch()

    def launch(self):
        self.grid = init(self.GridSize, self.GridSize,
                         self.shouldLoad, self.saveLocation)
        mainLoop((self.GridSize, self.GridSize), self.X,
                 self.Y, self.grid, self.saveLocation)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = Launcher()
    widget.show()

    sys.exit(app.exec())
