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
from library_qlabs_basic_shape import QLabsBasicShape
from library_qlabs_free_camera import QLabsFreeCamera

from library_qlabs_utilities import *

setup_only = False

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

    QLabsFreeCamera().spawn(qlabs,0,[53.696, 18.906, 51.107], [0, 0.865, -0.01])
    QLabsFreeCamera().possess(qlabs, 0)

    
    QLabsQCar().spawn_degrees(qlabs, actorNumber=0, location=[82.545, 28.056, 0], rotation=[0,0,0], waitForConfirmation=True)
    #QLabsQCar().possess(qlabs, 0, QLabsQCar().CAMERA_OVERHEAD)
    QLabsBasicShape().spawn_box_walls_from_end_points(qlabs, 0, [70, 40, 0], [130, 40, 0], height=3, thickness=1, colour=[1,0,0], waitForConfirmation=True)
    QLabsBasicShape().spawn_box_walls_from_end_points(qlabs, 1, [130, 40, 0], [130, 0, 0], height=3, thickness=1, colour=[1,0,0], waitForConfirmation=True)
    QLabsBasicShape().spawn_box_walls_from_end_points(qlabs, 2, [70, 0, 0], [130, 0, 0], height=3, thickness=1, colour=[1,0,0], waitForConfirmation=True)    
    QLabsBasicShape().spawn_box_walls_from_end_points(qlabs, 3, [70, 40, 0], [70, 0, 0], height=3, thickness=1, colour=[1,0,0], waitForConfirmation=True)
    
    
    if (setup_only):
        qlabs.close()
        return
    
    lidarPlot = pg.plot(title="LIDAR")   
    squareSize = 50
    lidarPlot.setXRange(-squareSize, squareSize)
    lidarPlot.setYRange(-squareSize, squareSize)
    lidarData = lidarPlot.plot([], [], pen=None, symbol='o', symbolBrush='r', symbolPen=None, symbolSize=2)
    
    
    time.sleep(1)
    
    QLabsQCar().set_velocity_and_request_state(qlabs, actorNumber=0, forward=5, turn=0, headlights=False, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)
    
    for count in range(100):
        
        print("Reading data")
        success, angle, distance = QLabsQCar().get_lidar(qlabs,0,samplePoints=400)
        
        x = np.sin(angle)*distance
        y = np.cos(angle)*distance

        lidarData.setData(x,y)
        QtWidgets.QApplication.instance().processEvents()
        time.sleep(0.01)
    
    QLabsQCar().set_velocity_and_request_state(qlabs, actorNumber=0, forward=0, turn=0, headlights=False, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)
    
    
    qlabs.close()
    
    print("Done. Hit any key to exit.")
    input()


testLIDAR()





