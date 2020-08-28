from . import __title__ as title
from . import __version__ as version

from .ui import Ui_MainWindow

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys
import os


class MainWindow(QtWidgets.QMainWindow):

    size = (800, 500)
    title = '%s %s' % (title, version)

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setMinimumSize(*self.size)
        self.setWindowTitle(self.title)
        self.resize(*self.size)

    def contextMenuEvent(self, event):
        print("Context menu event!")
        super(MainWindow, self).contextMenuEvent(event)


def main():

    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec())

    print("test")


if __name__ == '__main__':
    main()