import yaml
from dar import *
import datetime as dt
import threading
import schedule
interval = 15



import numpy as np
from pyqtgraph.Qt import QtGui, QtCore
from PyQt5 import QtWidgets, uic
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg




#RR   = Respiratory rate [respirations/minute]
#IT   = Inspiratoin time [seconds]
#PEEP = Positive ending exhalatory pressure [mbar]
#MIP  = Maximum inspiratory pressure [mbar]
#O2   = Oxigen percentage  [%]
RR, IT, PEEP, MIP, O2 = lee('config.yaml')







### START QtApp #####
app = QtGui.QApplication([])            # you MUST do this once (initialize things)
win = pg.GraphicsWindow() # creates a window
p1 = win.addPlot(title="Presión",row=1,col=1)  # creates empty space for the plot in the window
p2 = win.addPlot(title="Volumen",row=2,col=1)  # creates empty space for the plot in the window
p3 = win.addPlot(title="O2",     row=3,col=1)  # creates empty space for the plot in the window




curve1, curve2, curve3, x1, x2, x3, windowWidth, ptr  = init_graph(p1,p2,p3)
# curve = p.plot()                        # create an empty "plot" (a curve to plot)
# windowWidth = 100                       # width of the window displaying the curve





schedule.every(0.1).seconds.do(update_graph,curve1,curve2, curve3, ptr, x1, x2, x3)


i = 0
while True:
    

    schedule.run_pending()

### END QtApp ####
pg.QtGui.QApplication.exec_() # you MUST put this at the end
##################








guarda_config(RR,IT, PEEP,MIP, O2)
