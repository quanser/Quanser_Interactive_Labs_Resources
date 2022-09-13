import sys
library_path = '../libraries'
sys.path.append(library_path)

from library_qlabs import QuanserInteractiveLabs
from library_qlabs_common import QLabsCommon
from library_qlabs_yield_sign import QLabsYieldSign
from library_qlabs_stop_sign import QLabsStopSign
from library_qlabs_roundabout_sign import QLabsRoundaboutSign
from library_qlabs_traffic_cone import QLabsTrafficCone
from library_qlabs_crosswalk import QLabsCrosswalk
from library_qlabs_free_camera import QLabsFreeCamera
from library_qlabs_basic_shape import QLabsBasicShape
from library_qlabs_qcar import QLabsQCar
from library_qlabs_environment_outdoors import QLabsEnvironmentOutdoors
from library_qlabs_system import QLabsSystem
from library_qlabs_person import QLabsPerson
from library_qlabs_spline_line import QLabsSplineLine
from library_qlabs_real_time import QLabsRealTime
from library_qlabs_widget import QLabsWidget

from library_verification_report import verificationReport



import sys
import time
import math
import struct
import numpy as np
import cv2
import xlsxwriter
import os

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtWidgets

####################################################
require_user_input = False
lidar_rate = 0.1


####################################################


ignore_list = ['library_qlabs_yield_sign',\
               'library_qlabs_stop_sign',\
               'library_qlabs_roundabout_sign',\
               'library_qlabs_crosswalk',\
               'library_qlabs_qcar',\
               'library_qlabs_person',\
               'library_qlabs_environment_outdoors']

 

  
def main():
    os.system('cls')
    
    print("----------------- Checking that all libraries are being tested -------------------\n")
    vr.PrintWSHeader("Library Test List")
    vr.checkValidationLibraryList()  

    
    print("\n\n------------------------------ Communications --------------------------------\n")
    
    vr.PrintWSHeader("Communications")
    qlabs = QuanserInteractiveLabs()
    cv2.startWindowThread()

    print("Connecting to QLabs...")
    try:
        qlabs.open("localhost")
    except:
        print("Unable to connect to QLabs")
        vr.PrintWS(0, "Connection success")
        return
    
    print("Connected")
    vr.PrintWS(1, "Connection success")
    

    print("\n\n------------------------- Testing Individual Libraries ---------------------------\n")
    
    
    ### Common
    vr.PrintWSHeader("Common")
    x = "Destroyed {} actors.".format(QLabsCommon().destroy_all_spawned_actors(qlabs))
    print(x)
    vr.PrintWS(2, x)
    
    ### System
    vr.PrintWSHeader("System")
    x = QLabsSystem().set_title_string(qlabs, 'QLABS VERIFICATION SCRIPT', waitForConfirmation=True)
    vr.PrintWS(x == True, "Set title string")
    vr.checkFunctionTestList("library_qlabs_system", "../docs/source/System/system_library.rst")

    
    ### Free Camera
    vr.PrintWSHeader("Free Camera")
    print("\n\n---Free Camera---")
    print("Basic spawning")
    x = QLabsFreeCamera().spawn_id(qlabs, actorNumber=0, location=[3.578, 1.766, 1.702], rotation=[0, 0.355, -2.766])
    vr.PrintWS(x == 0, "Spawn sign with radians")
    
    x = QLabsFreeCamera().spawn_id(qlabs, actorNumber=0, location=[3.578, 1.766, 1.702], rotation=[0, 0.355, -2.766])
    vr.PrintWS(x == 2, "Spawn sign with duplicate ID (return code 2)")
    
    QLabsFreeCamera().spawn_id(qlabs, actorNumber=1, location=[-23.201, 34.875, 3.482], rotation=[0, 0.349, -0.04])
    x = QLabsFreeCamera().destroy(qlabs, actorNumber=1)
    vr.PrintWS(x == 1, "Spawn and destroy existing camera (expect return 1)")
    
    x = QLabsFreeCamera().destroy(qlabs, actorNumber=10)
    vr.PrintWS(x == 0, "Destroy camera that doesn't exist (expect return 0)")
    
    loc2 = [3.578, 1.766, 1.702]
    rot2 = [0, 20.023, -2.275]
    x = QLabsFreeCamera().spawn_id_degrees(qlabs, actorNumber=2, location=loc2, rotation=rot2)
    vr.PrintWS(x == 0, "Spawn sign with degrees")
    
    x, loc, rot, scale = QLabsFreeCamera().get_world_transform(qlabs, 2)
    vr.PrintWS(abs(np.sum(np.subtract(loc, loc2))) < 0.001 and x == True, "Get world transform")
    
    x = QLabsFreeCamera().ping(qlabs, 2)
    vr.PrintWS(x == True, "Ping existing sign (expect True)")
    
    x = QLabsFreeCamera().ping(qlabs, 3)
    vr.PrintWS(x == False, "Ping sign that doesn't exist (expect False)")

    
    print("Cinematic functions")
    
    x, hCamera = QLabsFreeCamera().spawn(qlabs, location=[3.578, 1.766, 1.702], rotation=[0, 0.116, -2.668])
    x = QLabsFreeCamera().possess(qlabs, hCamera)

    

    QLabsFreeCamera().set_camera_properties(qlabs, actorNumber=hCamera, fieldOfView=40, depthOfField=True, aperature=2.3, focusDistance=0.6)
    
    
    
    for y in range(26):
        x = QLabsFreeCamera().set_camera_properties(qlabs, actorNumber=hCamera, fieldOfView=40, depthOfField=True, aperature=2.3, focusDistance=(0.6 + pow(y/25, 3)*23.7))
    
    for y in range(25):
        x = QLabsFreeCamera().set_camera_properties(qlabs, actorNumber=hCamera, fieldOfView=40+y*2, depthOfField=True, aperature=2.3, focusDistance=(0.6 + 23.7))
        

    vr.PrintWS(x == True, "Set camera properties")
    
    x = QLabsFreeCamera().set_camera_properties(qlabs, actorNumber=hCamera, fieldOfView=90, depthOfField=False, aperature=2.3, focusDistance=10000)
    
    
    print("Transforms")
        
    x = QLabsFreeCamera().set_transform(qlabs, hCamera, [3.394, -2.712, 1.634], [-0, 0.278, 3.117])
    vr.PrintWS(x == True, "Set transform")
    time.sleep(0.5)
    
    x = QLabsFreeCamera().set_transform_degrees(qlabs, hCamera, [3.599, -0.051, 1.748], [0, 16.378, 179.184])
    vr.PrintWS(x == True, "Set transform degrees (expect True)")
    time.sleep(0.5)
    
    
    print("Image capture")

    cv2.namedWindow('CameraImageStream', cv2.WINDOW_AUTOSIZE)
    camera_image = cv2.imread('Quanser640x480.jpg')
    cv2.imshow('CameraImageStream', camera_image)
    cv2.waitKey(1)
    
    x = QLabsFreeCamera().set_image_capture_resolution(qlabs, actorNumber=hCamera, width=640, height=480)
    vr.PrintWS(x == True, "Set image capture resolution")
    x, camera_image = QLabsFreeCamera().get_image(qlabs, actorNumber=hCamera)
    vr.PrintWS(x == True, "Read image 640x480")
    if (x == True):
        cv2.imshow('CameraImageStream', camera_image)
        cv2.waitKey(1)
        
    else:
        print("Image decoding failure")
        
    cv2.namedWindow('CameraImageStream2', cv2.WINDOW_AUTOSIZE)
    camera_image = cv2.imread('Quanser820x410.jpg')
    cv2.imshow('CameraImageStream2', camera_image)
    cv2.waitKey(1)
    
    QLabsFreeCamera().set_image_capture_resolution(qlabs, actorNumber=hCamera, width=820, height=410)
    vr.PrintWS(x == True, "Read image 820x410 (expect True)")
    x, camera_image = QLabsFreeCamera().get_image(qlabs, actorNumber=hCamera)
    if (x == True):
        cv2.imshow('CameraImageStream2', camera_image)
        cv2.waitKey(1)
    else:
        print("Image decoding failure")    
       

    print("Parenting")
       
    loc3 = [0,0,1]
    QLabsBasicShape().spawn_id(qlabs, 0, loc3, [0,0,0], [0.5,0.5,0.5], configuration=QLabsBasicShape().SHAPE_CUBE, waitForConfirmation=True)
    x = QLabsFreeCamera().spawn_id_and_parent_with_relative_transform(qlabs, 10, [0, -3, 0], [0,0,math.pi/2], QLabsBasicShape().ID_BASIC_SHAPE, 0, 0)
    vr.PrintWS(x == 0, "Spawn and parent with relative transform")
    x = QLabsFreeCamera().possess(qlabs, 10)
    for y in range(26):
        x = QLabsBasicShape().set_transform(qlabs, 0, loc3, [0, 0, y/25*math.pi*2], [0.5,0.5,0.5])
    
    time.sleep(0.5)
    
    QLabsFreeCamera().destroy(qlabs, actorNumber=10)
    x = QLabsFreeCamera().spawn_id_and_parent_with_relative_transform_degrees(qlabs, 10, [0, -3, 0], [0,0,90], QLabsBasicShape().ID_BASIC_SHAPE, 0, 0)
    vr.PrintWS(x == 0, "Spawn and parent with relative transform degrees")
    x = QLabsFreeCamera().possess(qlabs, 10)
    for y in range(26):
        x = QLabsBasicShape().set_transform(qlabs, 0, loc3, [0, 0, y/25*math.pi*2], [0.5,0.5,0.5])
    
    
    x, hCameraOverview = QLabsFreeCamera().spawn_degrees(qlabs, location=[0.089, -3.446, 2.184], rotation=[0, 32.993, 89.295])
    vr.PrintWS(x == 0, "Spawn with automatically generated ID ({})".format(hCameraOverview))
    

    vr.checkFunctionTestList("library_qlabs_free_camera", "../docs/source/Objects/camera_library.rst")
    
    cv2.destroyAllWindows()
    QLabsBasicShape().destroy(qlabs, 0)
    
    
    
    
    ### Basic Shape
    vr.PrintWSHeader("Basic Shape")
    print("\n\n---Basic Shape---")

    QLabsFreeCamera().set_transform_degrees(qlabs, hCamera, location=[0.089, -3.446, 2.184], rotation=[0, 32.993, 89.295])
    QLabsFreeCamera().possess(qlabs, hCamera)

    

    x = QLabsBasicShape().spawn_id(qlabs, actorNumber=200, location=[-3.086, 1.986, 0.5], rotation=[0,0,math.pi/4], scale=[0.25,0.25,0.25], configuration=QLabsBasicShape().SHAPE_CUBE, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn shape with radians")

    x = QLabsBasicShape().spawn_id(qlabs, actorNumber=200, location=[-3.086, 1.986, 0.5], rotation=[0,0,math.pi/4], scale=[0.25,0.25,0.25], configuration=QLabsBasicShape().SHAPE_CUBE, waitForConfirmation=True)
    vr.PrintWS(x == 2, "Spawn with duplicate ID")


    x = QLabsBasicShape().spawn_id_degrees(qlabs, actorNumber=220, location=[-0.086, 1.986, 0.5], rotation=[0,0,45], scale=[0.25,0.25,0.25], configuration=QLabsBasicShape().SHAPE_CUBE, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn shape with degrees")

    x = QLabsBasicShape().spawn_id_degrees(qlabs, actorNumber=221, location=[-1.086, 1.986, 0], rotation=[0,0,45], scale=[0.5,0.5,0.5], configuration=QLabsBasicShape().SHAPE_CUBE, waitForConfirmation=True)
    x = QLabsBasicShape().destroy(qlabs, 221)
    vr.PrintWS(x == 1, "Spawn and destroy existing (expect return 1)")

    x = QLabsBasicShape().destroy(qlabs, 222)
    vr.PrintWS(x == 0, "Destroy shape that doesn't exist (expect return 0)")
    
    x = QLabsBasicShape().ping(qlabs, 220)
    vr.PrintWS(x == True, "Ping existing shape (expect True)")
    
    x = QLabsBasicShape().ping(qlabs, 221)
    vr.PrintWS(x == False, "Ping shape that doesn't exist (expect False)")

    x, loc, rot, scale = QLabsBasicShape().get_world_transform(qlabs, 200)
    vr.PrintWS(np.sum(np.subtract(loc, [-3.086, 1.986, 0.5])) < 0.001 and x == True, "Get world transform")
       
    x = QLabsBasicShape().spawn_id_and_parent_with_relative_transform(qlabs, actorNumber=201, location=[0,2,0], rotation=[0,0,math.pi/4], scale=[1,1,1], configuration=QLabsBasicShape().SHAPE_CUBE, parentClass=QLabsBasicShape().ID_BASIC_SHAPE, parentActorNumber=200, parentComponent=0, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn with parent relative transform (expect 0)")

    x = QLabsBasicShape().spawn_id_and_parent_with_relative_transform_degrees(qlabs, actorNumber=202, location=[0,-2,0], rotation=[0,0,45], scale=[1,1,1], configuration=QLabsBasicShape().SHAPE_CUBE, parentClass=QLabsBasicShape().ID_BASIC_SHAPE, parentActorNumber=200, parentComponent=0, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn with parent relative transform degrees (expect 0)")


    x = QLabsBasicShape().set_material_properties(qlabs, actorNumber=202, colour=[0,1,0], roughness=0.0, metallic=True, waitForConfirmation=True)
    x = QLabsBasicShape().set_material_properties(qlabs, actorNumber=201, colour=[1,0,0], roughness=0.0, metallic=True, waitForConfirmation=True)
    vr.PrintWS(x == True, "Set material properties (expect True)")

    

    for y in range(26):
        x = QLabsBasicShape().set_transform(qlabs, actorNumber=201, location=[0,2,0], rotation=[0,0,math.pi/4-math.pi/25*y*2], scale=[1,1,1])
        x = QLabsBasicShape().set_transform_degrees(qlabs, actorNumber=202, location=[0,-2,0], rotation=[0,0,45-180/25*y*2], scale=[1,1,1])
        x = QLabsBasicShape().set_transform(qlabs, actorNumber=200, location=[-3.086, 1.986, 0.5], rotation=[0,0,math.pi/4+2*math.pi/50*y*2], scale=[0.25+0.25*y/50,0.25+0.25*y/50,0.25+0.25*y/50])
    
    x = QLabsBasicShape().spawn_id(qlabs, actorNumber=203, location=[0.928, 2.283, 0.5], rotation=[0,0,0], scale=[0.5,0.5,0.5], configuration=QLabsBasicShape().SHAPE_SPHERE, waitForConfirmation=True)
    x = QLabsBasicShape().set_material_properties(qlabs, actorNumber=203, colour=[1,1,1], roughness=0.0, metallic=True, waitForConfirmation=True)
    
    
    
    x = QLabsBasicShape().spawn_id(qlabs, actorNumber=204, location=[1.928, 2.283, 0.5], rotation=[0,0,0], scale=[0.5,0.5,0.5], configuration=QLabsBasicShape().SHAPE_SPHERE, waitForConfirmation=True)
    x = QLabsBasicShape().set_material_properties(qlabs, actorNumber=204, colour=[0,0,1], roughness=0.0, metallic=False, waitForConfirmation=True)
    x = QLabsBasicShape().set_enable_collisions(qlabs, actorNumber=204, enableCollisions=False, waitForConfirmation=True)
    vr.PrintWS(x == True, "Enable collisions")

    x = QLabsBasicShape().spawn_id(qlabs, actorNumber=205, location=[0.928, 2.3, 1], rotation=[0,0,0], scale=[0.3,0.3,0.3], configuration=QLabsBasicShape().SHAPE_SPHERE, waitForConfirmation=True)
    x = QLabsBasicShape().spawn_id(qlabs, actorNumber=206, location=[1.928, 2.3, 1], rotation=[0,0,0], scale=[0.3,0.3,0.3], configuration=QLabsBasicShape().SHAPE_SPHERE, waitForConfirmation=True)
    x = QLabsBasicShape().spawn_id(qlabs, actorNumber=207, location=[2.928, 2.3, 1], rotation=[0,0,0], scale=[0.3,0.3,0.3], configuration=QLabsBasicShape().SHAPE_SPHERE, waitForConfirmation=True)
    
    x = QLabsBasicShape().set_physics_properties(qlabs, actorNumber=207, mass=1, linearDamping=10, angularDamping=0, enableDynamics=False, waitForConfirmation=True)
    vr.PrintWS(x == True, "Set physics properties")

    x = QLabsBasicShape().set_enable_dynamics(qlabs, actorNumber=205, enableDynamics=True, waitForConfirmation=False)
    x = QLabsBasicShape().set_enable_dynamics(qlabs, actorNumber=206, enableDynamics=True, waitForConfirmation=False)
    x = QLabsBasicShape().set_enable_dynamics(qlabs, actorNumber=207, enableDynamics=True, waitForConfirmation=True)
    vr.PrintWS(x == True, "Enable dynamics")

    x = QLabsBasicShape().set_enable_dynamics(qlabs, actorNumber=205, enableDynamics=True, waitForConfirmation=False)
    
    
    x = QLabsBasicShape().spawn_id_box_walls_from_center(qlabs, actorNumbers=[210, 211, 212, 213, 214], centerLocation=[-1.012, 1.17, -0], yaw=math.pi/4, xSize=1, ySize=1, zHeight=0.25, wallThickness=0.05, floorThickness=0.05, wallColour=[1,0,0], floorColour=[0,0,1], waitForConfirmation=True)
    vr.PrintWS(x == True, "Spawn box walls from center")

    x = QLabsBasicShape().spawn_id_box_walls_from_center_degrees(qlabs, actorNumbers=[270, 271, 272, 273, 274], centerLocation=[1.458, 1.195, -0], yaw=45, xSize=1, ySize=1, zHeight=0.25, wallThickness=0.05, floorThickness=0.05, wallColour=[1,0,0], floorColour=[0,0,1], waitForConfirmation=True)
    vr.PrintWS(x == True, "Spawn box walls from center degrees")

    x = QLabsBasicShape().spawn_id_box_walls_from_end_points(qlabs, actorNumber=280, startLocation=[-0.046, 0.705, 0], endLocation=[0.454, 1.399, -0], height=0.1, thickness=0.1, colour=[0.2,0.2,0.2], waitForConfirmation=True)
    vr.PrintWS(x == True, "Spawn box walls from end points")

    
    x, shapeHandle1 = QLabsBasicShape().spawn(qlabs, location=[3.041, 1.461, 0.25], rotation=[0,0,math.pi/4], scale=[0.5,0.5,0.5], configuration=QLabsBasicShape().SHAPE_CUBE, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn next")

    x, shapeHandle4 = QLabsBasicShape().spawn_degrees(qlabs, location=[4.041, 1.461, 0.25], rotation=[0,0,45], scale=[0.5,0.5,0.5], configuration=QLabsBasicShape().SHAPE_CUBE, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn next degrees")
    
    x = QLabsBasicShape().set_material_properties(qlabs, actorNumber=shapeHandle1, colour=[1,0,1], roughness=0.0, metallic=True, waitForConfirmation=True)
    vr.checkFunctionTestList("library_qlabs_basic_shape", "../docs/source/Objects/basic_shapes.rst")    



    
    ### Widget
    vr.PrintWSHeader("Widget")
    print("\n\n--Widget---")

    x = QLabsFreeCamera().possess(qlabs, hCamera)
    QLabsWidget().widget_spawn_configuration(qlabs, enableShadow=True)

    for count in range(10):
        x = QLabsWidget().spawn(qlabs, QLabsWidget().METAL_CAN, [-1.012, 1.17, 1+count*0.2], [0,0,0], [1,1,1], [1,1,1], measuredMass=0, IDTag=0, properties='', waitForConfirmation=True)

    vr.PrintWS(x == True, "Widget spawn (expect True)")

    time.sleep(1)

    for count in range(10):
        x = QLabsWidget().spawn_degrees(qlabs, QLabsWidget().METAL_CAN, [1.458, 1.195, 1+count*0.2], [90,0,0], [1,1,1], [1,0,0], measuredMass=0, IDTag=0, properties='', waitForConfirmation=True)

    vr.PrintWS(x == True, "Widget spawn degrees(expect True)")

    time.sleep(1)

    x = QLabsWidget().destroy_all_spawned_widgets(qlabs)
    vr.PrintWS(x == True, "Widgets destroyed (expect True)")
    QLabsWidget().widget_spawn_configuration(qlabs, enableShadow=False)
    
    for count in range(10):
        x = QLabsWidget().spawn_degrees(qlabs, QLabsWidget().SPHERE, [-1.012, 1.17+count*0.01, 1+count*0.3], [90,0,0], [0.25,0.25,0.25], [1,0,0], measuredMass=0, IDTag=0, properties='', waitForConfirmation=True)

    
    QLabsWidget().widget_spawn_configuration(qlabs, enableShadow=True)

    for count in range(10):
        x = QLabsWidget().spawn_degrees(qlabs, QLabsWidget().SPHERE, [1.458, 1.195+count*0.01, 1+count*0.3], [90,0,0], [0.25,0.25,0.25], [1,0,0], measuredMass=0, IDTag=0, properties='', waitForConfirmation=True)

    time.sleep(1)
    
    vr.checkFunctionTestList("library_qlabs_widget", "../docs/source/Objects/widgets.rst")  
  
    return
    ### Spline Line
    vr.PrintWSHeader("Spline Line")
    print("\n\n---Spline Line---")

    vr.checkFunctionTestList("library_qlabs_spline_line", "../docs/source/Objects/spline_line.rst")  

    x = QLabsFreeCamera().spawn_id(qlabs, actorNumber=300, location=[-3.097, 2.579, 11.849], rotation=[0, 0.92, 1.536])
    QLabsFreeCamera().possess(qlabs, 300)
    
    ### Real-Time
    vr.PrintWSHeader("Real-Time")
    print("\n\n---Real-Time---")

    vr.checkFunctionTestList("library_qlabs_real_time", "../docs/source/System/real_time_library.rst")    
    
    


    print("\n\n------------------------------ Communications --------------------------------\n")
    
    qlabs.close()
    cv2.destroyAllWindows()
    print("Done!")  
 

vr = verificationReport('Open Factory Validation Report.xlsx', 'library_verification_open_factory.py', library_path)
vr.ignore_list = ignore_list



main()

vr.WriteFileBuffer()
