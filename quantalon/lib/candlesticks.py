import pyqtgraph as pg
from pyqtgraph import QtCore, QtGui


class CandlestickItem(pg.GraphicsObject):

    def __init__(self, ohlc):
        pg.GraphicsObject.__init__(self)
        self.ohlc = ohlc
        self.generatePicture()

    def generatePicture(self):

        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)
        p.setPen(pg.mkPen('w'))
        p = self._generate(p)
        p.end()

    def _generate(self, p):
        
        w = .35

        p.setPen(pg.mkPen(color=(155, 163, 157)))

        #rects = [(QtCore.QRectF(i-w, row.open, w*2, row.close-row.open), row.open-row.close ) for i, row in self.ohlc.iterrows()]

        for i, row in self.ohlc.iterrows():

            p.drawLine(QtCore.QPointF(i, row.low), QtCore.QPointF(i, row.high))
            candlestick_bar = QtCore.QRectF(i-w, row.open, w*2, row.close-row.open)

            if row.close - row.open < 0:
                p.setBrush(pg.mkBrush('r'))
            else:
                p.setBrush(pg.mkBrush('g'))


            p.drawRect(candlestick_bar)



        return p 


    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())


class VolumeItem(pg.GraphicsObject):

    def __init__(self, ohlc):
        pg.GraphicsObject.__init__(self)
        self.ohlc = ohlc
        self.generatePicture()

    def generatePicture(self):

        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)
        p.setPen(pg.mkPen('w'))
        p = self._generate(p)
        p.end()

    def _generate(self, p):
        
        w = .35


        bar_max = self.ohlc['close'].max()
        vol_max = self.ohlc['volume'].max()
        quo = vol_max/bar_max*5


        for i, row in self.ohlc.iterrows():

            volume_bar = QtCore.QRectF(i-w, 0, w*2, row.volume/quo)

            if row.close - row.open < 0:
                p.setBrush(pg.mkBrush('#ffa1a1'))
            else:
                p.setBrush(pg.mkBrush('#a1ffa1'))

            p.drawRect(volume_bar)



        return p 


    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())