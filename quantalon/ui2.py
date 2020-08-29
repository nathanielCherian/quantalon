from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys
import os

import pandas as pd
import numpy as np

from finta import TA

from .test import Ui_MainWindow
from .lib.candlesticks import CandlestickItem

class CustomWindow(Ui_MainWindow):

    graphs = []

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        
        #Menu Bar
        self.actionOpen.triggered.connect(self.open_file)

        #Indicator Button
        self.indicatorButton.clicked.connect(self.add_TA)


    def open_file(self):
        print("open_file")

        filename = QtWidgets.QFileDialog.getOpenFileName(
                    parent=None,
                    caption="open ohlc data",
                    directory=QtCore.QDir.currentPath(),
                    filter='Text (*.csv);;Text (*.csv)'
                )

        try:
            self.ohlc = pd.read_csv(filename[0])
            self.ohlc.rename(columns={"Close":"close", "Open":"open", "Low":"low", "High":"high"}, inplace=True)

            gw = self.create_plot()

            self.plot(gw, [i for i in range(len(self.ohlc))], np.array(self.ohlc['close']), "security")



            # Data must be loaded before check box becomes active
            self.linkRegionsCheckBox.toggled.connect(self.link_regions_checkbox)

        except Exception as e:
            self.ohlc = None
            print(e)


    def create_plot(self):
        graphWidget = pg.PlotWidget(self.centralwidget)
        graphWidget.setBackground('w')
        graphWidget.showGrid(x=True, y=True)
        #graphWidget.enableAutoRange(axis='y')
        graphWidget.setMouseEnabled(x=True, y=False)
        
        graphWidget.setLimits(xMin=0, xMax=len(self.ohlc)+5)

        #graphWidget.sigRangeChanged.connect(lambda x, y: self.region_updated(x, y, graphWidget))

        self.verticalLayout_3.addWidget(graphWidget)
        self.graphs.append(graphWidget)

        return graphWidget
        
    def region_updated(self):
        self.region.setZValue(10)
        minX, maxX = self.region.getRegion()

        for g in self.graphs[1:]:
            g.setXRange(minX, maxX, padding=0)


    def plot(self, widget, x, y, plotname, pen=pg.mkPen(color=(155, 163, 157)), width=2.5):

        widget.plot(x, y, name=plotname, pen=pen)


    def add_TA(self):
        print("add_TA")

        if self.indicatorBox.currentText() == "candle":
            item = CandlestickItem(self.ohlc)
            gw = self.create_plot()
            gw.addItem(item)
            



        try:
            
            selection = self.indicatorBox.currentText()
            transformed_data = getattr(TA, selection)(self.ohlc)
            transformed_data.dropna(inplace=True)

            time = transformed_data.index
            price = np.array(transformed_data)

            gw = self.create_plot()
            self.plot(gw, time, price, selection, pen=pg.mkPen(color=(108, 189, 128)), width=3.0)

        except Exception as e:
            print(e)

        return


    def link_regions_checkbox(self):
        print("link_regions ", self.linkRegionsCheckBox.isChecked())

        try:
            if self.linkRegionsCheckBox.isChecked():

                self.region = pg.LinearRegionItem(bounds=(0, len(self.ohlc)))
                self.region.setZValue(10)
                self.region.setRegion((0, len(self.ohlc)))
                self.region.sigRegionChanged.connect(self.region_updated)

                self.graphs[0].addItem(self.region, ignoreBounds=True)

            else:
                self.graphs[0].removeItem(self.region)

        except Exception as e:
            print(e)