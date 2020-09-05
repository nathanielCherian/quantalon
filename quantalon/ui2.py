from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys
import os

import pandas as pd
import numpy as np

from finta import TA

from .screen import Ui_MainWindow
from .lib.candlesticks import CandlestickItem, VolumeItem
from .lib.indicators import IndicatorFunctions

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
            self.ohlc.rename(columns={"Close":"close", "Open":"open", "Low":"low", "High":"high", "Volume":"volume"}, inplace=True)

            gw = self.create_plot()

            self.plot(gw, [i for i in range(len(self.ohlc))], np.array(self.ohlc['close']), "security")

            self.line_graph = gw

            item = CandlestickItem(self.ohlc)
            itemv = VolumeItem(self.ohlc)

            self.candlestick_items = (item, itemv)

            # Data must be loaded before check box becomes active
            self.linkRegionsCheckBox.toggled.connect(self.link_regions_checkbox)
            self.candlestickCheckBox.toggled.connect(self.candlestick_checkbox)

            self.indicatorFunctions = IndicatorFunctions(self.create_plot, self.plot, self.ohlc)

        except Exception as e:
            self.ohlc = None
            print(e)


    def create_plot(self, append=True, crosshair=True):
        graphWidget = pg.PlotWidget(self.centralwidget)
        graphWidget.setMinimumHeight(180)
        graphWidget.setBackground('w')
        graphWidget.showGrid(x=True, y=True)
        #graphWidget.enableAutoRange(axis='y')
        graphWidget.setMouseEnabled(x=True, y=False)
        
        graphWidget.setLimits(xMin=0, xMax=len(self.ohlc)+5)


        if crosshair:
            vLine = pg.InfiniteLine(angle=90, movable=False)
            hLine = pg.InfiniteLine(angle=0, movable=False)
            graphWidget.addItem(vLine, ignoreBounds=True)
            graphWidget.addItem(hLine, ignoreBounds=True)

        if append:
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

        try:
            
            selection = self.indicatorBox.currentText()
            
            """transformed_data = getattr(TA, selection)(self.ohlc)
            transformed_data.dropna(inplace=True)

            time = transformed_data.index
            price = np.array(transformed_data)

            gw = self.create_plot()
            self.plot(gw, time, price, selection, pen=pg.mkPen(color=(108, 189, 128)), width=3.0)"""

            gw = self.indicatorFunctions.indicator_method(selection)

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


    def candlestick_checkbox(self):
        print("candlestick_checkbox ", self.candlestickCheckBox.isChecked())

        try:
            print(self.graphs[0]==self.line_graph)
            if self.candlestickCheckBox.isChecked():

                self.graphs[0].clear()
                self.graphs[0].addItem(self.candlestick_items[0])
                self.graphs[0].addItem(self.candlestick_items[1])

            else:
                self.graphs[0].clear()
                self.plot(self.graphs[0], [i for i in range(len(self.ohlc))], np.array(self.ohlc['close']), "security")

        except Exception as e:
            print(e)