from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys
import os

import pandas as pd
import numpy as np

from finta import TA

class Ui_MainWindow(object):

    graphs = []

    def setupUi(self, MainWindow):

        #Central Widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Grid Layout
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")


        #Horizontal 2
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.graphWidget = pg.PlotWidget(self.centralwidget)
        self.graphWidget.setBackground('w')
        self.graphWidget.showGrid(x=True, y=True)
        self.graphWidget.addLegend()
        self.graphWidget.enableAutoRange(axis='y')
        self.graphWidget.setMouseEnabled(x=True, y=False)



        self.verticalLayout_2.addWidget(self.graphWidget)

        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        #Horizontal1
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.loadDataButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadDataButton.setObjectName("loadDataButton")
        self.loadDataButton.clicked.connect(self.load_from_file)
        self.horizontalLayout.addWidget(self.loadDataButton)

        self.loadDataLabel = QtWidgets.QLabel(self.centralwidget)
        self.loadDataLabel.setObjectName("loadDataLabel")
        self.horizontalLayout.addWidget(self.loadDataLabel)

        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        #Horizontal 3
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.indicatorConfirmButton = QtWidgets.QPushButton(self.centralwidget)
        self.indicatorConfirmButton.setObjectName("indicatorConfirmButton")
        self.indicatorConfirmButton.clicked.connect(self.load_indicator)
        self.horizontalLayout_3.addWidget(self.indicatorConfirmButton)
        self.indicatorBox = QtWidgets.QComboBox(self.centralwidget)
        self.indicatorBox.setObjectName("indicatorBox")
        self.indicatorBox.addItem("SMA")
        self.indicatorBox.addItem("RSI")
        self.horizontalLayout_3.addWidget(self.indicatorBox)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        #Menu and Status
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 815, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




    def load_from_file(self):
        print("load_from_file")

        filename = QtWidgets.QFileDialog.getOpenFileName(
            parent=None,
            caption="open ohlc data",
            directory=QtCore.QDir.currentPath(),
            filter='Text (*.csv);;Text (*.csv)'
        )

        try:
            self.ohlc = pd.read_csv(filename[0])

            time = [i for i in range(len(self.ohlc ))]
            price = np.array(self.ohlc["Close"])
            #pen = pg.mkPen(color=(255, 0, 0))
            
            self.graphWidget.clear()

            self.plot(time, price, "security", (255, 0, 0))

            self.region = pg.LinearRegionItem()
            self.region.setZValue(10)
            self.region.sigRegionChanged.connect(self.update)

            self.graphWidget.addItem(self.region, ignoreBounds=True)

        except:
            print("failed")



    def load_indicator(self):
        print("load_indicator")

        try:
            self.ohlc = self.ohlc.rename(columns={"Close":"close"})

            selection = self.indicatorBox.currentText()

            transformed_data = getattr(TA, selection)(self.ohlc, period=14)
            transformed_data.dropna(inplace=True)

            time = transformed_data.index
            price = np.array(transformed_data)

            #self.plot(time, price, selection, (0, 255, 0))

            graphWidget2 = pg.PlotWidget(self.centralwidget)
            graphWidget2.setBackground('w')
            graphWidget2.setTitle(selection, color='k', size="15pt")
            graphWidget2.showGrid(x=True, y=True)
            graphWidget2.enableAutoRange(axis='y')
            graphWidget2.setMouseEnabled(x=True, y=False)
            self.verticalLayout_2.addWidget(graphWidget2)
            
            pen=pg.mkPen(color=(0, 255, 0), width=2.5)
            graphWidget2.plot(time, price, name=selection, pen=pen)
            
            self.graphs.append(graphWidget2)
            self.update()

        except:
            print("failed")

    def plot(self, x, y, plotname, color):
        pen=pg.mkPen(color=color)
        self.graphWidget.plot(x, y, name=plotname, pen=pen)
        
    def update(self):
        self.region.setZValue(10)
        minX, maxX = self.region.getRegion()
        print(minX, maxX)

        for graph in self.graphs:
            graph.setXRange(minX, maxX, padding=0)  

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.loadDataButton.setText(_translate("MainWindow", "Load Data"))
        self.loadDataLabel.setText(_translate("MainWindow", "Load data to start"))
        self.indicatorConfirmButton.setText(_translate("MainWindow", "Add Indicator"))