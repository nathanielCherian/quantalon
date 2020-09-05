from pyqtgraph import PlotWidget, plot
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg


class CustomPlotWidget(PlotWidget):

    def __init__(self, *args, **kwargs):
        PlotWidget.__init__(self)
        self.scene().sigMouseClicked.connect(self.mouseClickEvent)
        self.setMenuEnabled(False)
        self.menu = None
        self.menu = self.getContextMenus()

    def mouseClickEvent(self, ev):
        print("mouseclickedevent")
        if ev.button() == QtCore.Qt.RightButton:
            if self.raiseContextMenu(ev):
                ev.accept()


    def raiseContextMenu(self, ev):
        print("raisecontectmenue")
        
        pos = ev.screenPos()
        self.menu.popup(QtCore.QPoint(pos.x(), pos.y()))
        return True


    def getContextMenus(self, event=None):
        if self.menu is None:
            print("getcontextmenu")
            self.menu = QtGui.QMenu()
            self.menu.setTitle(" options..")
            remove = QtGui.QAction("Remove", self.menu)
            remove.triggered.connect(self.remove_graph)
            self.menu.addAction(remove)
            self.menu.remove = remove

        return self.menu

    def remove_graph(self):
        print("remove_graph")
        self.clear()
        self.update()