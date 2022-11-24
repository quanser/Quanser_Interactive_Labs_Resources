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
from library_qlabs_reference_frame import QLabsReferenceFrame
from library_qlabs_free_camera import QLabsFreeCamera
from library_qlabs_basic_shape import QLabsBasicShape


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
    

    frame_configuration = 2
    wait_for_confirmation = True

    
    hCamera = QLabsFreeCamera(qlabs)
    hCamera.spawn([-20.851, 33.956, 3.878], [0, 0.313, -0.06])
    hCamera.possess()
    
    time.sleep(2)
    
    hShape = QLabsBasicShape(qlabs)

    hBaseYawJoint = QLabsReferenceFrame(qlabs)
    hBaseYawJoint.spawn_id_degrees(0, [-15.492, 34.512, 0.005], [0,0,0], [1,1,1], frame_configuration, wait_for_confirmation)
    
    hBaseShoulderJoint = QLabsReferenceFrame(qlabs)
    hBaseShoulderJoint.spawn_id_degrees(1, [0,0,0], [0,0,0], [1,1,1], frame_configuration, wait_for_confirmation)
    hBaseShoulderJoint.parent_with_relative_transform(location=[0, 0, 0.5], rotation=[0, 0, 0], scale=[1, 1, 1], parentClassID=hBaseYawJoint.classID, parentActorNumber=hBaseYawJoint.actorNumber, parentComponent=0, waitForConfirmation=False)

    hShape.spawn_id(0, [0,0,0], [0,0,0], [1,1,1], hShape.SHAPE_CUBE, wait_for_confirmation)
    hShape.parent_with_relative_transform(location=[0, 0, 1], rotation=[0, 0, 0], scale=[0.25, 0.25, 2], parentClassID=hBaseShoulderJoint.classID, parentActorNumber=hBaseShoulderJoint.actorNumber, parentComponent=0, waitForConfirmation=False)

    hShape.spawn_id(1, [0,0,0], [0,0,0], [1,1,1], hShape.SHAPE_CYLINDER, wait_for_confirmation)
    hShape.parent_with_relative_transform_degrees(location=[0, 0, 0], rotation=[0, 90, 0], scale=[0.5, 0.5, 0.5], parentClassID=hBaseShoulderJoint.classID, parentActorNumber=hBaseShoulderJoint.actorNumber, parentComponent=0, waitForConfirmation=False)
    

    hBaseElbowJoint = QLabsReferenceFrame(qlabs)
    hBaseElbowJoint.spawn_id_degrees(2, [0,0,0], [0,0,0], [1,1,1], frame_configuration, wait_for_confirmation)
    hBaseElbowJoint.parent_with_relative_transform(location=[0, 0, 2], rotation=[0, 0, 0], scale=[1, 1, 1], parentClassID=hBaseShoulderJoint.classID, parentActorNumber=hBaseShoulderJoint.actorNumber, parentComponent=0, waitForConfirmation=False)

    hShape.spawn_id(2, [0,0,0], [0,0,0], [1,1,1], hShape.SHAPE_CUBE, wait_for_confirmation)
    hShape.parent_with_relative_transform(location=[0, 0, 1], rotation=[0, 0, 0], scale=[0.25, 0.25, 2], parentClassID=hBaseElbowJoint.classID, parentActorNumber=hBaseElbowJoint.actorNumber, parentComponent=0, waitForConfirmation=False)

    hShape.spawn_id(3, [0,0,0], [0,0,0], [1,1,1], hShape.SHAPE_CYLINDER, wait_for_confirmation)
    hShape.parent_with_relative_transform_degrees(location=[0, 0, 0], rotation=[90, 0, 0], scale=[0.5, 0.5, 0.5], parentClassID=hBaseElbowJoint.classID, parentActorNumber=hBaseElbowJoint.actorNumber, parentComponent=0, waitForConfirmation=False)
    

    count_range = 600
    for count in range(count_range):
        hBaseYawJoint.set_transform_degrees([-15.492, 34.512, 0.005], [0,0,count/count_range*180], [1,1,1], False)
        hBaseShoulderJoint.set_transform_degrees([0,0,0.5], [math.sin(count/count_range*20)*30,0,0], [1,1,1], False)
        hBaseElbowJoint.set_transform_degrees([0,0,2], [0,math.sin(count/count_range*20)*60,0], [1,1,1], True)
        

   
test()





