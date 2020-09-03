# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.indicatorButton = QtWidgets.QPushButton(self.centralwidget)
        self.indicatorButton.setObjectName("indicatorButton")
        self.horizontalLayout_3.addWidget(self.indicatorButton)
        self.indicatorBox = QtWidgets.QComboBox(self.centralwidget)
        self.indicatorBox.setObjectName("indicatorBox")
        self.indicatorBox.addItem("")
        self.indicatorBox.addItem("")
        self.indicatorBox.addItem("")
        self.horizontalLayout_3.addWidget(self.indicatorBox)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 888, 383))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.linkRegionsCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.linkRegionsCheckBox.setObjectName("linkRegionsCheckBox")
        self.gridLayout.addWidget(self.linkRegionsCheckBox, 2, 0, 1, 1)
        self.candlestickCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.candlestickCheckBox.setObjectName("candlestickCheckBox")
        self.gridLayout.addWidget(self.candlestickCheckBox, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 908, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.indicatorButton.setText(_translate("MainWindow", "Add Indicator"))
        self.indicatorBox.setItemText(0, _translate("MainWindow", "SMA"))
        self.indicatorBox.setItemText(1, _translate("MainWindow", "RSI"))
        self.indicatorBox.setItemText(2, _translate("MainWindow", "candle"))
        self.linkRegionsCheckBox.setText(_translate("MainWindow", "Link Regions"))
        self.candlestickCheckBox.setText(_translate("MainWindow", "Candlestick"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
