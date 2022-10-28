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

    time.sleep(2)
    

    hShape = QLabsBasicShape(qlabs)
    hShape.spawn([-17.224, 35.494, 2], [0,0,0], [0.5,0.5,0.5])
    hShape.set_physics_properties(enableDynamics=True, mass=1.0, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=0.7, frictionCombineMode=hShape.COMBINE_AVERAGE, restitution=0.3, restitutionCombineMode=hShape.COMBINE_AVERAGE, waitForConfirmation=True)

    hShape.spawn([-17.224, 34.494, 2], [0,0,0], [0.5,0.5,0.5])
    hShape.set_physics_properties(enableDynamics=True, mass=1.0, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=0.7, frictionCombineMode=hShape.COMBINE_AVERAGE, restitution=0.95, restitutionCombineMode=hShape.COMBINE_MAX, waitForConfirmation=True)

    hShape.spawn_degrees([-17.224, 32, 0.25], [-15,0,0], [1,4,0.5])

    hShape.spawn([-17.234, 31.175, 2], [0,0,0], [0.5,0.5,0.5])
    hShape.set_physics_properties(enableDynamics=True, mass=1.0, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=0.0, frictionCombineMode=hShape.COMBINE_MIN, restitution=0, restitutionCombineMode=hShape.COMBINE_MAX, waitForConfirmation=True)

    time.sleep(1)

    hShape.spawn([-17.234, 31.175, 2], [0,0,0], [0.5,0.5,0.5])
    hShape.set_physics_properties(enableDynamics=True, mass=1.0, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=0.2, frictionCombineMode=hShape.COMBINE_MIN, restitution=0, restitutionCombineMode=hShape.COMBINE_MAX, waitForConfirmation=True)

    time.sleep(1)

    hShape.spawn([-17.234, 31.175, 2], [0,0,0], [0.5,0.5,0.5])
    hShape.set_physics_properties(enableDynamics=True, mass=1.0, linearDamping=0.01, angularDamping=0.0, staticFriction=0.0, dynamicFriction=1, frictionCombineMode=hShape.COMBINE_MIN, restitution=0, restitutionCombineMode=hShape.COMBINE_MAX, waitForConfirmation=True)


test()





