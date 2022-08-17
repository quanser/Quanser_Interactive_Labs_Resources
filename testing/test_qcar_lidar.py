import sys
import os

library_path = '../libraries'
sys.path.append(library_path)

import numpy as np
import time
import math

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtWidgets

from library_qlabs import QuanserInteractiveLabs
from library_qlabs_common import QLabsCommon
from library_qlabs_qcar import QLabsQCar


def testLIDAR():
    os.system('cls')
    qlabs = QuanserInteractiveLabs()
    print("Connecting to QLabs...")
    try:
        qlabs.open("localhost")
        print("Connected to QLabs")
    except:
        print("Unable to connect to QLabs")
        return    
    
    QLabsCommon().destroy_all_spawned_actors(qlabs)
    
    QLabsQCar().spawn(qlabs, actorNumber=0, location=[-9.568, 34.572, 0.005], rotation=[0,0,0], waitForConfirmation=True)
    QLabsQCar().possess(qlabs, 0, QLabsQCar().CAMERA_OVERHEAD)
    
        
    lidarPlot = pg.plot(title="LIDAR")   
    #lidarPlot.setXRange(-0, 2*math.pi)
    #lidarPlot.setYRange(-0, 100)
    lidarData = lidarPlot.plot([], [], pen=None, symbol='o', symbolBrush='r', symbolPen=None, symbolSize=3)
    
    for count in range(1):
        x = np.random.normal(size=1000)
        y = np.random.normal(size=1000)
        
        print("Reading data")
        success, angle, distance = QLabsQCar().get_lidar(qlabs,0)
        
        
        
        x = np.sin(angle)*distance
        y = np.cos(angle)*distance
     
        
        print("Angle: {}, {}, {}, Dist: {}, {}, {}".format(angle[0], angle[1], angle[2], distance[0], distance[1], distance[2]))
        print("x: {}, y: {}".format(len(x), len(y)))

        lidarData.setData(angle,distance)
        QtWidgets.QApplication.instance().processEvents()
        time.sleep(1)
    
    time.sleep(5)
    
    qlabs.close()


testLIDAR()





