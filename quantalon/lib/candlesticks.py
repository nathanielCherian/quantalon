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
            bar = QtCore.QRectF(i-w, row.open, w*2, row.close-row.open)

            if row.close - row.open < 0:
                p.setBrush(pg.mkBrush('r'))
            else:
                p.setBrush(pg.mkBrush('g'))


            p.drawRect(bar)

        return p 


    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())