import numpy as np
from finta import TA
import pyqtgraph as pg


"""
Different indicators require different methods of plotting
for example rsi can have lines at 70 and 30
"""

class IndicatorFunctions:

    def __init__(self, create_func, plot_func, ohlc):
        self.create_func = create_func
        self.plot_func = plot_func
        self.ohlc = ohlc

        self.funcs = {
            "SMA": self.standard_function,
            "RSI": lambda indicator, **kwargs: self.RSI_lines(self.standard_function(indicator, **kwargs))
        }

    def indicator_method(self, indicator, **kwargs):
        
        self.func = self.funcs[indicator](indicator)


    def standard_function(self, indicator, **kwargs):
        transformed_data = getattr(TA, indicator)(self.ohlc)
        transformed_data.dropna(inplace=True)

        time = transformed_data.index
        price = np.array(transformed_data)

        gw = self.create_func()
        self.plot_func(gw, time, price, indicator, pen=pg.mkPen(color=(108, 189, 128)), width=3.0)

        return gw

    def RSI_lines(self, gw):
        gw.addLine(x=None, y=70, pen=pg.mkPen('b', width=1))
        gw.addLine(x=None, y=30, pen=pg.mkPen('b', width=1))


