
import yaml
from random import gauss
import numpy as np


import numpy as np
from pyqtgraph.Qt import QtGui, QtCore
from PyQt5 import QtWidgets, uic
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg






def lee(archivo):
    with open(archivo) as f:
        variables            = yaml.load(f, Loader=yaml.FullLoader)
    Respiratory_rate         = variables['Respiratory_rate']
    Inspiratory_time         = variables['Inspiratory_time']
    PEEP                     = variables['PEEP']
    Max_inspiratory_pressure = variables['Max_inspiratory_pressure']
    FiO2                     = variables['FiO2']
    return Respiratory_rate,Inspiratory_time, PEEP, Max_inspiratory_pressure, FiO2



def guarda_config(Respiratory_rate,Inspiratory_time, PEEP,Max_inspiratory_pressure, FiO2):
    datos = {"Respiratory_rate":Respiratory_rate,"Inspiratory_time":Inspiratory_time,"PEEP":PEEP,"Max_inspiratory_pressure":Max_inspiratory_pressure,"FiO2":FiO2}
    with open('config.yaml','w') as file:
        yaml.dump(datos,file)

def read_pressure_volume_02():
    return gauss(40,10), gauss(100,10), gauss(80,5)

#lenin define funcion para leer presion
def lee_presion():
    presion,_,_ = read_pressure_volume_02()
    return presion

def init_graph(p1,p2,p3):

    curve1 = p1.plot()                        # create an empty "plot" (a curve to plot)
    curve2 = p2.plot()                        # create an empty "plot" (a curve to plot)
    curve3 = p3.plot()                        # create an empty "plot" (a curve to plot)
    # curve = p.plot()                        # create an empty "plot" (a curve to plot)
    windowWidth = 300                       # width of the window displaying the curve
    x1 = np.linspace(0,0,windowWidth)          # create array that will contain the relevant time series
    x2 = np.linspace(0,0,windowWidth)          # create array that will contain the relevant time series
    x3 = np.linspace(0,0,windowWidth)          # create array that will contain the relevant time series

    ptr = -windowWidth                      # set first x position

    return curve1,curve2, curve3, x1, x2,x3, windowWidth,ptr

def update_graph(curve1,curve2,curve3, ptr, x1,x2,x3):
    # global curve, ptr, Xm

    x1[:-1] = x1[1:]                      # shift data in the temporal mean 1 sample left
    x2[:-1] = x2[1:]                      # shift data in the temporal mean 1 sample left
    x3[:-1] = x3[1:]                      # shift data in the temporal mean 1 sample left

    P = lee_presion()               # read line (single value) from the serial port
    x1[-1] = P                 # vector containing the instantaneous values
    x2[-1] = 0                 # vector containing the instantaneous values
    x3[-1] = 0                 # vector containing the instantaneous values

    ptr += 1
                                  # update x position for displaying the curve
    curve1.setData(x1,symbol='o',symbolPen=None)                      # update x position for displaying the curve
    curve1.setPos(ptr,0)                   # set x position in the graph to 0
    curve2.setData(x2)                      # update x position for displaying the curve
    curve2.setPos(ptr,0)                   # set x position in the graph to 0
    curve3.setData(x3)                      # update x position for displaying the curve
    curve3.setPos(ptr,0)                   # set x position in the graph to 0


    QtGui.QApplication.processEvents()    # you MUST process the plot now
