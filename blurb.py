        """

        label = QtWidgets.QLabel("Hello World!")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)


        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("click me!")
        self.b1.clicked.connect(self.onclick)
        
        self.graphWidget = pg.PlotWidget()
        #self.setCentralWidget(self.graphWidget)
        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]
        self.graphWidget.plot(hour, temperature)
        """

    def onclick(self):
        print("clicked")

        filename = QtWidgets.QFileDialog.getOpenFileName(
            parent=None,
            caption="open data",
            directory=QtCore.QDir.currentPath(),
            filter='Text (*.csv);;Text (*.csv)'
        )