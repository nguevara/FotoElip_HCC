from PyQt5 import QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib

matplotlib.use('QT5Agg')


        
class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)   # Inherit from QWidget

        self.vbl = QtWidgets.QVBoxLayout()
        
        
    def make_plot(self,plot):
        try:
            self.vbl.removeWidget(self.vbl.canvas)
            self.vbl.removeItem(self.vbl.canvas)
            self.vbl.removeWidget(self.vbl.toolbar)
            self.vbl.removeItem(self.vbl.toolbar)
            del(self.vbl.canvas,self.vbl.toolbar )
        except AttributeError:
            pass
        
        self.canvas = Canvas(plot)   # Create canvas object
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding,
                                       QtWidgets.QSizePolicy.Expanding)
        Canvas.updateGeometry(self)
        self.toolbar = NavigationToolbar(self.canvas, self) # toolbar
        
                 # Set box for plotting
        self.vbl.addWidget(self.toolbar)
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)
            
