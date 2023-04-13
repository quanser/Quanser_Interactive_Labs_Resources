import sys
sys.path.append('../')

import os
import numpy as np
import time
import math

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtWidgets

from qvl.qlabs import QuanserInteractiveLabs
from qvl.qcar import QLabsQCar
from qvl.basic_shape import QLabsBasicShape
from qvl.free_camera import QLabsFreeCamera


large_car = False

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

    qlabs.destroy_all_spawned_actors()

    hCamera = QLabsFreeCamera(qlabs)
    hCamera.spawn([53.696, 18.906, 51.107], [0, 0.865, -0.01])
    #hCamera.possess()


    hQCar = QLabsQCar(qlabs)
    
    if (large_car):
        hQCar.spawn_degrees(location=[82.545, 28.056, 0], rotation=[0,0,0], scale=[1,1,1])
    else:
        hQCar.spawn_degrees(location=[82.545, 28.056, 0], rotation=[0,0,0], scale=[0.1,0.1,0.1])
    
    hQCar.possess(hQCar.CAMERA_OVERHEAD)
    #hQCar.possess(hQCar.CAMERA_DEPTH)

    hShape = QLabsBasicShape(qlabs)
    hShape.spawn_id_box_walls_from_end_points(0, [70, 40, 0], [130, 40, 0], height=3, thickness=1, color=[1,0,0], waitForConfirmation=True)
    hShape.spawn_id_box_walls_from_end_points(1, [130, 40, 0], [130, 0, 0], height=3, thickness=1, color=[1,0,0], waitForConfirmation=True)
    hShape.spawn_id_box_walls_from_end_points(2, [70, 0, 0], [130, 0, 0], height=3, thickness=1, color=[1,0,0], waitForConfirmation=True)
    hShape.spawn_id_box_walls_from_end_points(3, [70, 40, 0], [70, 0, 0], height=3, thickness=1, color=[1,0,0], waitForConfirmation=True)
    
    for count in range(5):
        hShape.spawn([96.741+count*5, 26.891, 0], [0,0,0], [1,1,1], 2)
    
    lidarPlot = pg.plot(title="LIDAR")
    squareSize = 50
    lidarPlot.setXRange(-squareSize, squareSize)
    lidarPlot.setYRange(-squareSize, squareSize)
    lidarData = lidarPlot.plot([], [], pen=None, symbol='o', symbolBrush='r', symbolPen=None, symbolSize=2)


    time.sleep(1)

    hQCar.set_velocity_and_request_state(forward=5, turn=0, headlights=False, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)

    for count in range(100):


        success, angle, distance = hQCar.get_lidar(samplePoints=400)
        
        if (success):

            x = np.sin(angle)*distance
            y = np.cos(angle)*distance

            lidarData.setData(x,y)
            QtWidgets.QApplication.instance().processEvents()
        else:
            print("Lidar read failure")

    hQCar.set_velocity_and_request_state(forward=0, turn=0, headlights=False, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)


    qlabs.close()

    print("Done. Hit any key to exit.")
    input()


testLIDAR()





