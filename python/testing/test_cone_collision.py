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
from library_qlabs_basic_shape import QLabsBasicShape
from library_qlabs_free_camera import QLabsFreeCamera
from library_qlabs_traffic_cone import QLabsTrafficCone



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
    
    qlabs.destroy_all_spawned_actors()

    hCamera = QLabsFreeCamera(qlabs)
    hCamera.spawn([-20.851, 33.956, 1.211], [0, 0.112, -0.06])
    hCamera.possess()

    hCone = QLabsTrafficCone(qlabs)

    for count in range(8):
        hCone.spawn_degrees([-16.042, 36.951-count*1, count*0.2 + 0.5], [0,45,0], [1,1,1], 1)


testLIDAR()





