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
from library_qlabs_widget import QLabsWidget
from library_qlabs_free_camera import QLabsFreeCamera


setup_only = False

def test():
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


    hWidget = QLabsWidget(qlabs)
    hWidget.spawn_degrees(configuration=0, location=[-17.313, 34.009, 1], rotation=[0,0,0], scale=[0.5,0.5,0.5], color=[1,0,0], measuredMass=0, IDTag=0, properties="", waitForConfirmation=True)
    hWidget.spawn_degrees(configuration=1, location=[-17.313, 33.009, 1], rotation=[0,0,0], scale=[0.5,0.5,0.5], color=[1,0,0], measuredMass=0, IDTag=0, properties="", waitForConfirmation=True)
    hWidget.spawn_degrees(configuration=2, location=[-17.313, 32.009, 1], rotation=[0,0,0], scale=[0.5,0.5,0.5], color=[1,0,0], measuredMass=0, IDTag=0, properties="", waitForConfirmation=True)
    hWidget.spawn_degrees(configuration=3, location=[-17.313, 31.009, 1], rotation=[0,0,0], scale=[0.5,0.5,0.5], color=[1,0,0], measuredMass=0, IDTag=0, properties="", waitForConfirmation=True)
    hWidget.spawn_degrees(configuration=4, location=[-17.313, 30.009, 1], rotation=[0,0,0], scale=[0.5,0.5,0.5], color=[1,0,0], measuredMass=0, IDTag=0, properties="", waitForConfirmation=True)
    hWidget.spawn_degrees(configuration=5, location=[-17.313, 29.009, 1], rotation=[0,0,0], scale=[0.5,0.5,0.5], color=[1,0,0], measuredMass=0, IDTag=0, properties="", waitForConfirmation=True)

test()





