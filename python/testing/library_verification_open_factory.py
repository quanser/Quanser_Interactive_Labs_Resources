import sys
library_path = '../libraries'
sys.path.append(library_path)

from library_qlabs import QuanserInteractiveLabs
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
    x = "Destroyed {} actors.".format(qlabs.destroy_all_spawned_actors())
    print(x)
    vr.PrintWS(2, x)
    
    ### System
    vr.PrintWSHeader("System")
    hSystem = QLabsSystem(qlabs)
    x = hSystem.set_title_string('QLABS VERIFICATION SCRIPT', waitForConfirmation=True)
    vr.PrintWS(x == True, "Set title string")
    vr.checkFunctionTestList("library_qlabs_system", "../docs/source/System/system_library.rst")

    
    ### Free Camera
    vr.PrintWSHeader("Free Camera")
    print("\n\n---Free Camera---")
    print("Basic spawning")
    hCamera = QLabsFreeCamera(qlabs)
    x = hCamera.spawn_id(actorNumber=0, location=[3.578, 1.766, 1.702], rotation=[0, 0.355, -2.766])
    vr.PrintWS(x == 0, "Spawn sign with radians")
    
    x = hCamera.spawn_id(actorNumber=0, location=[3.578, 1.766, 1.702], rotation=[0, 0.355, -2.766])
    vr.PrintWS(x == 2, "Spawn sign with duplicate ID (return code 2)")
    
    hCamera.spawn_id(actorNumber=1, location=[-23.201, 34.875, 3.482], rotation=[0, 0.349, -0.04])
    x = hCamera.destroy()
    vr.PrintWS(x == 1, "Spawn and destroy existing camera (expect return 1)")
    
    hCamera.actorNumber = 1
    x = hCamera.destroy()
    vr.PrintWS(x == 0, "Destroy camera that doesn't exist (expect return 0)")
    
    loc2 = [3.578, 1.766, 1.702]
    rot2 = [0, 20.023, -2.275]
    x = hCamera.spawn_id_degrees(actorNumber=2, location=loc2, rotation=rot2)
    vr.PrintWS(x == 0, "Spawn sign with degrees")
    
    x, loc, rot, scale = hCamera.get_world_transform()
    vr.PrintWS(abs(np.sum(np.subtract(loc, loc2))) < 0.001 and x == True, "Get world transform")
    
    x = hCamera.ping()
    vr.PrintWS(x == True, "Ping existing sign (expect True)")
    
    hCamera.actorNumber = 3
    x = hCamera.ping()
    vr.PrintWS(x == False, "Ping sign that doesn't exist (expect False)")

    
    print("Cinematic functions")
    
    x, CameraNumber = hCamera.spawn(location=[3.578, 1.766, 1.702], rotation=[0, 0.116, -2.668])
    x = hCamera.possess()

    

    hCamera.set_camera_properties(fieldOfView=40, depthOfField=True, aperature=2.3, focusDistance=0.6)
    
    
    
    for y in range(26):
        x = hCamera.set_camera_properties(fieldOfView=40, depthOfField=True, aperature=2.3, focusDistance=(0.6 + pow(y/25, 3)*23.7))
    
    for y in range(25):
        x = hCamera.set_camera_properties(fieldOfView=40+y*2, depthOfField=True, aperature=2.3, focusDistance=(0.6 + 23.7))
        

    vr.PrintWS(x == True, "Set camera properties")
    
    x = hCamera.set_camera_properties(fieldOfView=90, depthOfField=False, aperature=2.3, focusDistance=10000)
    
    
    print("Transforms")
        
    x = hCamera.set_transform([3.394, -2.712, 1.634], [-0, 0.278, 3.117])
    vr.PrintWS(x == True, "Set transform")
    time.sleep(0.5)
    
    x = hCamera.set_transform_degrees([3.599, -0.051, 1.748], [0, 16.378, 179.184])
    vr.PrintWS(x == True, "Set transform degrees (expect True)")
    time.sleep(0.5)
    
    
    print("Image capture")

    cv2.namedWindow('CameraImageStream', cv2.WINDOW_AUTOSIZE)
    camera_image = cv2.imread('Quanser640x480.jpg')
    cv2.imshow('CameraImageStream', camera_image)
    cv2.waitKey(1)
    
    x = hCamera.set_image_capture_resolution(width=640, height=480)
    vr.PrintWS(x == True, "Set image capture resolution")
    x, camera_image = hCamera.get_image()
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
    
    hCamera.set_image_capture_resolution(width=820, height=410)
    vr.PrintWS(x == True, "Read image 820x410 (expect True)")
    x, camera_image = hCamera.get_image()
    if (x == True):
        cv2.imshow('CameraImageStream2', camera_image)
        cv2.waitKey(1)
    else:
        print("Image decoding failure")    
       
    
    print("Parenting")
       
    loc3 = [0,0,1]
    hBasicShape0 = QLabsBasicShape(qlabs, True)
    x = hBasicShape0.spawn_id(0, loc3, [0,0,0], [0.5,0.5,0.5], configuration=hBasicShape0.SHAPE_CUBE, waitForConfirmation=True)

    hCameraRelative = QLabsFreeCamera(qlabs, True)
    x = hCameraRelative.spawn_id_and_parent_with_relative_transform(10, [0, -3, 0], [0,0,math.pi/2], [1,1,1], 0,  hBasicShape0.classID, 0, 0)
    vr.PrintWS(x == 0, "Spawn and parent with relative transform")
    x = hCameraRelative.possess()
    for y in range(26):
        x = hBasicShape0.set_transform(loc3, [0, 0, y/25*math.pi*2], [0.5,0.5,0.5])
    
    time.sleep(0.5)
    
    hCameraRelative.destroy()
    x = hCameraRelative.spawn_id_and_parent_with_relative_transform_degrees(10, [0, -3, 0], [0,0,90], [1,1,1], 0, hBasicShape0.classID, 0, 0)
    vr.PrintWS(x == 0, "Spawn and parent with relative transform degrees")
    x = hCameraRelative.possess()
    for y in range(26):
        x = hBasicShape0.set_transform(loc3, [0, 0, y/25*math.pi*2], [0.5,0.5,0.5])
    
    
    x, CameraOverviewNum = hCameraRelative.spawn_degrees(location=[0.089, -3.446, 2.184], rotation=[0, 32.993, 89.295])
    vr.PrintWS(x == 0, "Spawn with automatically generated ID ({})".format(CameraOverviewNum))
    

    vr.checkFunctionTestList("library_qlabs_free_camera", "../docs/source/Objects/camera_library.rst", "library_qlabs_actor")
    
    cv2.destroyAllWindows()
    hBasicShape0.destroy()
    
    
    
    ### Basic Shape
    vr.PrintWSHeader("Basic Shape")
    print("\n\n---Basic Shape---")

    hCamera.set_transform_degrees(location=[0.089, -3.446, 2.184], rotation=[0, 32.993, 89.295])
    hCamera.possess()

    

    hBasicShape200 = QLabsBasicShape(qlabs)
    x = hBasicShape200.spawn_id(actorNumber=200, location=[-3.086, 1.986, 0.5], rotation=[0,0,math.pi/4], scale=[0.25,0.25,0.25], configuration=hBasicShape200.SHAPE_CUBE, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn shape with radians")

    x = hBasicShape200.spawn_id(actorNumber=200, location=[-3.086, 1.986, 0.5], rotation=[0,0,math.pi/4], scale=[0.25,0.25,0.25], configuration=hBasicShape200.SHAPE_CUBE, waitForConfirmation=True)
    vr.PrintWS(x == 2, "Spawn with duplicate ID")

    hBasicShape220 = QLabsBasicShape(qlabs)
    x = hBasicShape220.spawn_id_degrees(actorNumber=220, location=[-0.086, 1.986, 0.5], rotation=[0,0,45], scale=[0.25,0.25,0.25], configuration=hBasicShape220.SHAPE_CUBE, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn shape with degrees")

    hBasicShape221 = QLabsBasicShape(qlabs)
    x = hBasicShape221.spawn_id_degrees(actorNumber=221, location=[-1.086, 1.986, 0], rotation=[0,0,45], scale=[0.5,0.5,0.5], configuration=hBasicShape221.SHAPE_CUBE, waitForConfirmation=True)
    x = hBasicShape221.destroy()
    vr.PrintWS(x == 1, "Spawn and destroy existing (expect return 1)")


    hBasicShape221.actorNumber = 221
    x = hBasicShape221.destroy()
    vr.PrintWS(x == 0, "Destroy shape that doesn't exist (expect return 0)")
    
    x = hBasicShape220.ping()
    vr.PrintWS(x == True, "Ping existing shape (expect True)")
    
    hBasicShape221.actorNumber = 221
    x = hBasicShape221.ping()
    vr.PrintWS(x == False, "Ping shape that doesn't exist (expect False)")

    x, loc, rot, scale = hBasicShape200.get_world_transform()
    vr.PrintWS(np.sum(np.subtract(loc, [-3.086, 1.986, 0.5])) < 0.001 and x == True, "Get world transform")
       
    hBasicShape201 = QLabsBasicShape(qlabs)
    x = hBasicShape201.spawn_id_and_parent_with_relative_transform(actorNumber=201, location=[0,2,0], rotation=[0,0,math.pi/4], scale=[1,1,1], configuration=hBasicShape201.SHAPE_CUBE, parentClassID=hBasicShape201.ID_BASIC_SHAPE, parentActorNumber=200, parentComponent=0, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn with parent relative transform (expect 0)")

    hBasicShape202 = QLabsBasicShape(qlabs)
    x = hBasicShape202.spawn_id_and_parent_with_relative_transform_degrees(actorNumber=202, location=[0,-2,0], rotation=[0,0,45], scale=[1,1,1], configuration=hBasicShape202.SHAPE_CUBE, parentClassID=hBasicShape202.ID_BASIC_SHAPE, parentActorNumber=200, parentComponent=0, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn with parent relative transform degrees (expect 0)")


    x = hBasicShape202.set_material_properties(colour=[0,1,0], roughness=0.0, metallic=True, waitForConfirmation=True)
    x = hBasicShape201.set_material_properties(colour=[1,0,0], roughness=0.0, metallic=True, waitForConfirmation=True)
    vr.PrintWS(x == True, "Set material properties (expect True)")

    

    for y in range(26):
        x = hBasicShape201.set_transform(location=[0,2,0], rotation=[0,0,math.pi/4-math.pi/25*y*2], scale=[1,1,1])
        x = hBasicShape202.set_transform_degrees(location=[0,-2,0], rotation=[0,0,45-180/25*y*2], scale=[1,1,1])
        x = hBasicShape200.set_transform(location=[-3.086, 1.986, 0.5], rotation=[0,0,math.pi/4+2*math.pi/50*y*2], scale=[0.25+0.25*y/50,0.25+0.25*y/50,0.25+0.25*y/50])
    
    hBasicShape203 = QLabsBasicShape(qlabs)
    x = hBasicShape203.spawn_id(actorNumber=203, location=[0.928, 2.283, 0.5], rotation=[0,0,0], scale=[0.5,0.5,0.5], configuration=hBasicShape203.SHAPE_SPHERE, waitForConfirmation=True)
    x = hBasicShape203.set_material_properties(colour=[1,1,1], roughness=0.0, metallic=True, waitForConfirmation=True)
    
    
    hBasicShape204 = QLabsBasicShape(qlabs)
    x = hBasicShape204.spawn_id(actorNumber=204, location=[1.928, 2.283, 0.5], rotation=[0,0,0], scale=[0.5,0.5,0.5], configuration=hBasicShape204.SHAPE_SPHERE, waitForConfirmation=True)
    x = hBasicShape204.set_material_properties(colour=[0,0,1], roughness=0.0, metallic=False, waitForConfirmation=True)
    x = hBasicShape204.set_enable_collisions(enableCollisions=False, waitForConfirmation=True)
    vr.PrintWS(x == True, "Enable collisions")


    hBasicShape205 = QLabsBasicShape(qlabs)
    hBasicShape206 = QLabsBasicShape(qlabs)
    hBasicShape207 = QLabsBasicShape(qlabs)
    
    x = hBasicShape205.spawn_id(actorNumber=205, location=[0.928, 2.3, 1], rotation=[0,0,0], scale=[0.3,0.3,0.3], configuration=hBasicShape205.SHAPE_SPHERE, waitForConfirmation=True)
    x = hBasicShape206.spawn_id(actorNumber=206, location=[1.928, 2.3, 1], rotation=[0,0,0], scale=[0.3,0.3,0.3], configuration=hBasicShape206.SHAPE_SPHERE, waitForConfirmation=True)
    x = hBasicShape207.spawn_id(actorNumber=207, location=[2.928, 2.3, 1], rotation=[0,0,0], scale=[0.3,0.3,0.3], configuration=hBasicShape207.SHAPE_SPHERE, waitForConfirmation=True)
    
    x = hBasicShape207.set_physics_properties(mass=1, linearDamping=10, angularDamping=0, enableDynamics=False, waitForConfirmation=True)
    vr.PrintWS(x == True, "Set physics properties")

    x = hBasicShape205.set_enable_dynamics(enableDynamics=True, waitForConfirmation=False)
    x = hBasicShape206.set_enable_dynamics(enableDynamics=True, waitForConfirmation=False)
    x = hBasicShape207.set_enable_dynamics(enableDynamics=True, waitForConfirmation=True)
    vr.PrintWS(x == True, "Enable dynamics")

    x = hBasicShape205.set_enable_dynamics(enableDynamics=True, waitForConfirmation=False)
    
    
    hBasicShapeWall_1 = QLabsBasicShape(qlabs)
    x = hBasicShapeWall_1.spawn_id_box_walls_from_center(actorNumbers=[210, 211, 212, 213, 214], centerLocation=[-1.012, 1.17, -0], yaw=math.pi/4, xSize=1, ySize=1, zHeight=0.25, wallThickness=0.05, floorThickness=0.05, wallColour=[1,0,0], floorColour=[0,0,1], waitForConfirmation=True)
    vr.PrintWS(x == True, "Spawn box walls from center")

    hBasicShapeWall_2 = QLabsBasicShape(qlabs)
    x = hBasicShapeWall_2.spawn_id_box_walls_from_center_degrees(actorNumbers=[270, 271, 272, 273, 274], centerLocation=[1.458, 1.195, -0], yaw=45, xSize=1, ySize=1, zHeight=0.25, wallThickness=0.05, floorThickness=0.05, wallColour=[1,0,0], floorColour=[0,0,1], waitForConfirmation=True)
    vr.PrintWS(x == True, "Spawn box walls from center degrees")

    hBasicShapeWall_3 = QLabsBasicShape(qlabs)
    x = hBasicShapeWall_3.spawn_id_box_walls_from_end_points(actorNumber=280, startLocation=[-0.046, 0.705, 0], endLocation=[0.454, 1.399, -0], height=0.1, thickness=0.1, colour=[0.2,0.2,0.2], waitForConfirmation=True)
    vr.PrintWS(x == True, "Spawn box walls from end points")

    
    hBasicShape = QLabsBasicShape(qlabs)
    x, shapeHandle1 = hBasicShape.spawn(location=[3.041, 1.461, 0.25], rotation=[0,0,math.pi/4], scale=[0.5,0.5,0.5], configuration=hBasicShape.SHAPE_CUBE, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn next")

    x, shapeHandle4 = hBasicShape.spawn_degrees(location=[4.041, 1.461, 0.25], rotation=[0,0,45], scale=[0.5,0.5,0.5], configuration=hBasicShape.SHAPE_CUBE, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn next degrees")
    
    x = hBasicShape.set_material_properties(colour=[1,0,1], roughness=0.0, metallic=True, waitForConfirmation=True)
    vr.checkFunctionTestList("library_qlabs_basic_shape", "../docs/source/Objects/basic_shapes.rst", "library_qlabs_actor")    



    
    ### Widget
    vr.PrintWSHeader("Widget")
    print("\n\n--Widget---")

    x = hCamera.possess()
    hWidget = QLabsWidget(qlabs)
    hWidget.widget_spawn_configuration(enableShadow=True)

    for count in range(10):
        x = hWidget.spawn(hWidget.METAL_CAN, [-1.012, 1.17, 1+count*0.2], [0,0,0], [1,1,1], [1,1,1], measuredMass=0, IDTag=0, properties='', waitForConfirmation=True)

    vr.PrintWS(x == True, "Widget spawn (expect True)")

    time.sleep(1)

    for count in range(10):
        x = hWidget.spawn_degrees(hWidget.METAL_CAN, [1.458, 1.195, 1+count*0.2], [90,0,0], [1,1,1], [1,0,0], measuredMass=0, IDTag=0, properties='', waitForConfirmation=True)

    vr.PrintWS(x == True, "Widget spawn degrees(expect True)")

    time.sleep(1)

    x = hWidget.destroy_all_spawned_widgets()
    vr.PrintWS(x == True, "Widgets destroyed (expect True)")
    hWidget.widget_spawn_configuration(enableShadow=False)
    
    for count in range(10):
        x = hWidget.spawn_degrees(hWidget.SPHERE, [-1.012, 1.17+count*0.01, 1+count*0.3], [90,0,0], [0.25,0.25,0.25], [1,0,0], measuredMass=0, IDTag=0, properties='', waitForConfirmation=True)

    
    hWidget.widget_spawn_configuration(enableShadow=True)

    for count in range(10):
        x = hWidget.spawn_degrees(hWidget.SPHERE, [1.458, 1.195+count*0.01, 1+count*0.3], [90,0,0], [0.25,0.25,0.25], [1,0,0], measuredMass=0, IDTag=0, properties='', waitForConfirmation=True)

    time.sleep(1)
    
    vr.checkFunctionTestList("library_qlabs_widget", "../docs/source/Objects/widgets.rst")  
  
    return
    ### Spline Line
    vr.PrintWSHeader("Spline Line")
    print("\n\n---Spline Line---")

    vr.checkFunctionTestList("library_qlabs_spline_line", "../docs/source/Objects/spline_line.rst", "library_qlabs_actor")  

    x = hCamera.spawn_id(actorNumber=300, location=[-3.097, 2.579, 11.849], rotation=[0, 0.92, 1.536])
    hCamera.possess()
    
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
