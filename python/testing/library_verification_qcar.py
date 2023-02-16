from qvl.qlabs import QuanserInteractiveLabs
from qvl.yield_sign import QLabsYieldSign
from qvl.stop_sign import QLabsStopSign
from qvl.roundabout_sign import QLabsRoundaboutSign
from qvl.traffic_cone import QLabsTrafficCone
from qvl.crosswalk import QLabsCrosswalk
from qvl.free_camera import QLabsFreeCamera
from qvl.basic_shape import QLabsBasicShape
from qvl.qcar import QLabsQCar
from qvl.environment_outdoors import QLabsEnvironmentOutdoors
from qvl.system import QLabsSystem
from qvl.person import QLabsPerson
from qvl.spline_line import QLabsSplineLine
from qvl.real_time import QLabsRealTime
from qvl.widget import QLabsWidget
from qvl.traffic_light import QLabsTrafficLight
from qvl.animal import QLabsAnimal

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
lidar_rate = 0.01
library_path = 'C:/Users/MKTUSER/Documents/Repos/virtual_qcar_libraries_dev/python/qvl'


####################################################


ignore_list = ['autoclave', \
               'bottle_table', \
               'conveyor_curved', \
               'conveyor_straight', \
               'delivery_tube', \
               'qarm', \
               'qbot', \
               'qbot2e', \
               'qbot3', \
               'qbot_hopper', \
               'shredder', \
               'srv02', \
               'weigh_scale', \
               'qube_servo_2',\
               'actor',\
               'image_utilities']




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


    ### QLabs
    vr.PrintWSHeader("Common")
    x = "Destroyed {} actors.".format(qlabs.destroy_all_spawned_actors())
    print(x)
    vr.PrintWS(2, x)

    ### System
    """
    vr.PrintWSHeader("System")
    hSystem = QLabsSystem(qlabs)
    x = hSystem.set_title_string('QLABS VERIFICATION SCRIPT', waitForConfirmation=True)
    vr.PrintWS(x == True, "Set title string")
    vr.checkFunctionTestList("system", "../docs/source/System/system_library.rst")
    """
    ### Free Camera

    vr.PrintWSHeader("Free Camera")
    print("\n\n---Free Camera---")

    hCamera0 = QLabsFreeCamera(qlabs)
    x = hCamera0.spawn_id(actorNumber=0, location=[-8.248, 39.575, 8.538], rotation=[0, 1.209, 1.559])
    vr.PrintWS(x == 0, "Spawn camera with radians")


    print('Attempt to spawn duplicate.')
    hCamera0Duplicate = QLabsFreeCamera(qlabs, True)
    x = hCamera0Duplicate.spawn_id(actorNumber=0, location=[-13.74076819, 36.68400671, 8.43], rotation=[0, 1.204, 1.548])
    vr.PrintWS(x == 2, "Spawn camera with duplicate ID (return code 2)")

    hCamera1 = QLabsFreeCamera(qlabs)
    hCamera1.spawn_id(actorNumber=1, location=[-25.78776819, 29.01500671, 3.482], rotation=[0, 0.349, -0.04])
    x = hCamera1.destroy()
    vr.PrintWS(x == 1, "Spawn and destroy existing camera (expect return 1)")

    hCamera10 = QLabsFreeCamera(qlabs)
    hCamera10.actorNumber = 10
    x = hCamera10.destroy()
    vr.PrintWS(x == 0, "Destroy camera that doesn't exist (expect return 0)")

    loc2 = [-21.456, 31.995, 3.745]
    rot2 = [0, 18.814, 0.326]
    hCamera2 = QLabsFreeCamera(qlabs)
    x = hCamera2.spawn_id_degrees(actorNumber=2, location=loc2, rotation=rot2)
    vr.PrintWS(x == 0, "Spawn camera with degrees")

    x, loc, rot, scale = hCamera2.get_world_transform()
    vr.PrintWS(abs(np.sum(np.subtract(loc, loc2))) < 0.001 and x == True, "Get world transform")

    x = hCamera2.ping()
    vr.PrintWS(x == True, "Ping existing camera (expect True)")

    x = hCamera10.ping()
    vr.PrintWS(x == False, "Ping camera that doesn't exist (expect False)")

    hCamera3 = QLabsFreeCamera(qlabs)
    hCamera3.spawn_id(actorNumber=3, location=[-33.17276819, 13.50500671, 2.282], rotation=[0, 0.077, 0.564])
    hCamera3.set_camera_properties(fieldOfView=40, depthOfField=True, aperature=2.3, focusDistance=0.6)
    x = hCamera3.possess()


    for y in range(51):
        x = hCamera3.set_camera_properties(fieldOfView=40, depthOfField=True, aperature=2.3, focusDistance=(0.6 + pow(y/50, 3)*23.7))
    vr.PrintWS(x == True, "Set camera properties")

    x = hCamera2.possess()
    vr.PrintWS(x == True, "Possess camera 2")


    for y in range(26):
        x = hCamera2.set_transform(loc2, np.add(np.array(rot2)/180*math.pi, [0, 0, y/25*math.pi*2]))
    vr.PrintWS(x == True, "Set transform")

    for y in range(26):
        x = hCamera2.set_transform_degrees(loc2, np.add(rot2, [0, 0, y/25*360]))
    vr.PrintWS(x == True, "Set transform degrees (expect True)")


    cv2.namedWindow('CameraImageStream', cv2.WINDOW_AUTOSIZE)
    camera_image = cv2.imread('Quanser640x480.jpg')
    cv2.imshow('CameraImageStream', camera_image)
    cv2.waitKey(1)

    #FIX

    x = hCamera2.set_image_capture_resolution(width=640, height=480)
    vr.PrintWS(x == True, "Set image capture resolution")
    x, camera_image = hCamera2.get_image()
    vr.PrintWS(x == True, "Read image 640x480")
    if (x == True):
        cv2.imshow('CameraImageStream', camera_image)
        cv2.waitKey(1)

    else:
        print("Image decoding failure")

    print('Image streaming.')
    cv2.namedWindow('CameraImageStream2', cv2.WINDOW_AUTOSIZE)
    camera_image = cv2.imread('Quanser820x410.jpg')
    cv2.imshow('CameraImageStream2', camera_image)
    cv2.waitKey(1)

    #FIX

    hCamera2.set_image_capture_resolution(width=820, height=410)
    vr.PrintWS(x == True, "Read image 820x410 (expect True)")
    x, camera_image = hCamera2.get_image()
    if (x == True):
        cv2.imshow('CameraImageStream2', camera_image)
        cv2.waitKey(1)
    else:
        print("Image decoding failure")

    print('Testing parenting.')
    loc3 = [5.252, 20.852, 9.461]
    hCubeCameraHook = QLabsBasicShape(qlabs, True)
    x = hCubeCameraHook.spawn_id(1000, loc3, [0,0,0], [1,1,1], configuration=hCubeCameraHook.SHAPE_CUBE, waitForConfirmation=True)

    hCamera5Child = QLabsFreeCamera(qlabs, True)
    x = hCamera5Child.spawn_id_and_parent_with_relative_transform(5, [0, -10, 0], [0,0,math.pi/2], [1,1,1], 0, hCubeCameraHook.ID_BASIC_SHAPE, hCubeCameraHook.actorNumber, 0)
    vr.PrintWS(x == 0, "Spawn and parent with relative transform")
    x = hCamera5Child.possess()
    for y in range(26):
        x = hCubeCameraHook.set_transform(loc3, [0, 0, y/25*math.pi*2], [1,1,1])

    time.sleep(0.5)

    hCamera5Child.destroy()
    x = hCamera5Child.spawn_id_and_parent_with_relative_transform_degrees(5, [0, -10, 0], [0,0,90], [1,1,1], 0, hCubeCameraHook.ID_BASIC_SHAPE, hCubeCameraHook.actorNumber, 0)
    vr.PrintWS(x == 0, "Spawn and parent with relative transform degrees")
    x = hCamera5Child.possess()
    for y in range(26):
        x = hCubeCameraHook.set_transform(loc3, [0, 0, y/25*math.pi*2], [1,1,1])

    hCameraSpawnAutogen1 = QLabsFreeCamera(qlabs)
    x, CameraSpawn1Num = hCameraSpawnAutogen1.spawn(location=[-11.154, 42.544, 8.43], rotation=[0, 1.204, 1.548])
    vr.PrintWS(x == 0, "Spawn with automatically generated ID ({})".format(CameraSpawn1Num))

    hCameraSpawnAutogen2 = QLabsFreeCamera(qlabs)
    x, CameraSpawn2Num = hCameraSpawnAutogen2.spawn_degrees(location=[-11.154, 42.544, 8.43], rotation=[0, 0, 0])
    vr.PrintWS(x == 0, "Spawn with automatically generated ID ({})".format(CameraSpawn2Num))


    vr.checkFunctionTestList("free_camera", "../docs/source/Objects/camera_library.rst", "actor")

    cv2.destroyAllWindows()
    x = hCamera2.possess()


    ### Yield Sign


    vr.PrintWSHeader("Yield Sign")
    print("\n\n---Yield Sign---")

    hYield0 = QLabsYieldSign(qlabs)
    x = hYield0.spawn_id(actorNumber=0, location=[-17, 32.5, 0.0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn sign with radians")

    x = hYield0.spawn_id(actorNumber=0, location=[-17, 32.5, 0.0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    vr.PrintWS(x == 2, "Spawn sign with duplicate ID (return code 2)")

    hYield1 = QLabsYieldSign(qlabs)
    hYield1.spawn_id(actorNumber=1, location=[-16, 32.5, 0.0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    x = hYield1.destroy()
    vr.PrintWS(x == 1, "Spawn and destroy existing sign (expect return 1)")

    hYield1.actorNumber=1
    x = hYield1.destroy()
    vr.PrintWS(x == 0, "Destroy sign that doesn't exist (expect return 0)")

    hYield2 = QLabsYieldSign(qlabs)
    x = hYield2.spawn_id_degrees(actorNumber=2, location=[-15, 32.5, 0.0], rotation=[0,0,180], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn sign with degrees")

    x, loc, rot, scale = hYield2.get_world_transform()
    vr.PrintWS(np.array_equal(loc, [-15, 32.5, 0.0]) and x == True, "Get world transform")

    x = hYield2.ping()
    vr.PrintWS(x == True, "Ping existing sign (expect True)")

    hYield1.actorNumber=1
    x = hYield1.ping()
    vr.PrintWS(x == False, "Ping sign that doesn't exist (expect False)")


    vr.checkFunctionTestList("yield_sign", "../docs/source/Objects/road_signage.rst", "actor")

    ### Stop Sign

    vr.PrintWSHeader("Stop Sign")
    print("\n\n---Stop Sign---")

    hStop0 = QLabsStopSign(qlabs)
    x = hStop0.spawn_id(actorNumber=0, location=[-17, 33.5, 0.0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn sign with radians")

    x = hStop0.spawn_id(actorNumber=0, location=[-17, 33.5, 0.0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    vr.PrintWS(x == 2, "Spawn sign with duplicate ID (return code 2)")

    hStop1 = QLabsStopSign(qlabs)
    hStop1.spawn_id(actorNumber=1, location=[-16, 33.5, 0.0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    x = hStop1.destroy()
    vr.PrintWS(x == 1, "Spawn and destroy existing sign (expect return 1)")

    hStop1.actorNumber=1
    x = hStop1.destroy()
    vr.PrintWS(x == 0, "Destroy sign that doesn't exist (expect return 0)")

    hStop2 = QLabsStopSign(qlabs)
    x = hStop2.spawn_id_degrees(actorNumber=2, location=[-15, 33.5, 0.0], rotation=[0,0,180], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn sign with degrees")

    x, loc, rot, scale = hStop2.get_world_transform()
    vr.PrintWS(np.array_equal(loc, [-15, 33.5, 0.0]) and x == True, "Get world transform")


    x = hStop2.ping()
    vr.PrintWS(x == True, "Ping existing sign (expect True)")

    hStop1.actorNumber=1
    x = hStop1.ping()
    vr.PrintWS(x == False, "Ping sign that doesn't exist (expect False)")

    vr.checkFunctionTestList("stop_sign", "../docs/source/Objects/road_signage.rst", "actor")


    ### Roundabout Sign


    vr.PrintWSHeader("Roundabout Sign")
    print("\n\n---Roundabout Sign---")

    hRoundabout0 = QLabsRoundaboutSign(qlabs)
    x = hRoundabout0.spawn_id(actorNumber=0, location=[-17, 31.5, 0.0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn sign with radians")

    x = hRoundabout0.spawn_id(actorNumber=0, location=[-17, 31.5, 0.0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    vr.PrintWS(x == 2, "Spawn sign with duplicate ID (return code 2)")

    hRoundabout1 = QLabsRoundaboutSign(qlabs)
    hRoundabout1.spawn_id(actorNumber=1, location=[-16, 31.5, 0.0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    x = hRoundabout1.destroy()
    vr.PrintWS(x == 1, "Spawn and destroy existing sign (expect return 1)")

    hRoundabout1.actorNumber = 1
    x = hRoundabout1.destroy()
    vr.PrintWS(x == 0, "Destroy sign that doesn't exist (expect return 0)")

    hRoundabout2 = QLabsRoundaboutSign(qlabs)
    x = hRoundabout2.spawn_id_degrees(actorNumber=2, location=[-15, 31.5, 0.0], rotation=[0,0,180], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn sign with degrees")

    x, loc, rot, scale = hRoundabout2.get_world_transform()
    vr.PrintWS(np.array_equal(loc, [-15, 31.5, 0.0]) and x == True, "Get world transform")


    x = hRoundabout2.ping()
    vr.PrintWS(x == True, "Ping existing sign (expect True)")

    hRoundabout1.actorNumber = 1
    x = hRoundabout1.ping()
    vr.PrintWS(x == False, "Ping sign that doesn't exist (expect False)")

    vr.checkFunctionTestList("roundabout_sign", "../docs/source/Objects/road_signage.rst", "actor")

    ### Traffic Cone

    vr.PrintWSHeader("Traffic Cone")
    print("\n\n---Traffic Cone---")

    hCone0 = QLabsTrafficCone(qlabs)
    x = hCone0.spawn_id(actorNumber=0, location=[-17, 30.5, 1.0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn cone with radians")

    x = hCone0.spawn_id(actorNumber=0, location=[-17, 30.5, 1.0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    vr.PrintWS(x == 2, "Spawn cone with duplicate ID (return code 2)")

    hCone1 = QLabsTrafficCone(qlabs)
    hCone1.spawn_id(actorNumber=1, location=[-16, 30.5, 1.0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    x = hCone1.destroy()
    vr.PrintWS(x == 1, "Spawn and destroy existing cone (expect return 1)")

    hCone1.actorNumber = 1
    x = hCone1.destroy()
    vr.PrintWS(x == 0, "Destroy cone that doesn't exist (expect return 0)")

    hCone2 = QLabsTrafficCone(qlabs)
    x = hCone2.spawn_id_degrees(actorNumber=2, location=[-15, 30.5, 1.0], rotation=[0,0,180], scale=[1,1,1], configuration=1, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn cone with degrees in config 1")

    x, loc, rot, scale = hCone2.get_world_transform()
    vr.PrintWS(x == True, "Get world transform")


    x = hCone2.ping()
    vr.PrintWS(x == True, "Ping existing cone (expect True)")

    hCone1.actorNumber = 1
    x = hCone1.ping()
    vr.PrintWS(x == False, "Ping cone that doesn't exist (expect False)")

    vr.checkFunctionTestList("traffic_cone", "../docs/source/Objects/road_signage.rst", "actor")



    ### Change view points

    time.sleep(0.5)
    hCamera0.possess()
    print("Possess camera 0")

    ### Crosswalk


    vr.PrintWSHeader("Crosswalk")
    print("\n\n---Crosswalk---")

    hCrosswalk = QLabsCrosswalk(qlabs)
    x = hCrosswalk.spawn_id(actorNumber=0, location=[-10.5, 45, 0.00], rotation=[0,0,math.pi/2], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn crosswalk with radians")

    x = hCrosswalk.spawn_id(actorNumber=0, location=[-7.5, 45, 0.00], rotation=[0,0,math.pi/2], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    vr.PrintWS(x == 2, "Spawn crosswalk with duplicate ID (return code 2)")

    hCrosswalk.spawn_id(actorNumber=1, location=[-7.5, 45, 0.00], rotation=[0,0,math.pi/2], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    x = hCrosswalk.destroy()
    vr.PrintWS(x == 1, "Spawn and destroy existing crosswalk (expect return 1)")

    hCrosswalk.actorNumber = 10
    x = hCrosswalk.destroy()
    vr.PrintWS(x == 0, "Destroy crosswalk that doesn't exist (expect return 0)")

    x = hCrosswalk.spawn_id_degrees(actorNumber=2, location=[-7.5, 45, 0.00], rotation=[0,0,90], scale=[1,1,1], configuration=1, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn crosswalk with degrees in config 1")

    x = hCrosswalk.spawn_id_degrees(actorNumber=3, location=[-4.5, 45, 0.00], rotation=[0,0,90], scale=[1,1,1], configuration=2, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn crosswalk with degrees in config 2")


    x, loc, rot, scale = hCrosswalk.get_world_transform()
    vr.PrintWS(abs(np.sum(np.subtract(loc, [-7.8, 47.5, 0.0]))) < 0.001 and x == True, "Get world transform")

    hCrosswalk.actorNumber = 2
    x = hCrosswalk.ping()
    vr.PrintWS(x == True, "Ping existing crosswalk (expect True)")

    hCrosswalk.actorNumber = 4
    x = hCrosswalk.ping()
    vr.PrintWS(x == False, "Ping crosswalk that doesn't exist (expect False)")

    vr.checkFunctionTestList("crosswalk", "../docs/source/Objects/road_signage.rst", "actor")


    ### People


    vr.PrintWSHeader("People")
    print("\n\n---People---")

    hPersonRight = QLabsPerson(qlabs)
    hPersonRight.spawn_id(actorNumber=0, location=[-4.5, 41, 0.005], rotation=[0,0,math.pi/2], scale=[1,1,1], configuration=0, waitForConfirmation=True)

    hPersonMiddle = QLabsPerson(qlabs)
    hPersonMiddle.spawn_id(actorNumber=1, location=[-7.5, 41, 0.005], rotation=[0,0,math.pi/2], scale=[1,1,1], configuration=1, waitForConfirmation=True)

    hPersonLeft = QLabsPerson(qlabs, True)
    hPersonLeft.spawn_id_degrees(actorNumber=2, location=[-10.5, 41, 0.005], rotation=[0,0,90], scale=[1,1,1], configuration=2, waitForConfirmation=True)

    hPersonRight.move_to(location=[-4.5, 48, 0.005], speed=hPersonRight.WALK, waitForConfirmation=True)
    hPersonMiddle.move_to(location=[-7.5, 48, 0.005], speed=hPersonMiddle.JOG, waitForConfirmation=True)
    hPersonLeft.move_to(location=[-10.5, 48, 0.005], speed=hPersonLeft.RUN, waitForConfirmation=True)

    time.sleep(3)

    x, pos, rot, scale = hPersonLeft.get_world_transform()
    vr.PrintWS(x == True, "Got world transform ({}), ({}), ({})".format(pos, rot, scale))

    x, pos, rot, scale = hPersonLeft.get_world_transform_degrees()
    vr.PrintWS(x == True, "Got world transform degrees ({}), ({}), ({})".format(pos, rot, scale))

    x = hPersonLeft.ping()
    vr.PrintWS(x == True, "Ping person left (expect True)")

    x = hPersonLeft.destroy()
    vr.PrintWS(x == 1, "Person left destroyed (expect 1)")

    hPersonLeft.actorNumber = 2
    x = hPersonLeft.ping()
    vr.PrintWS(x == False, "Ping person left after manual assignment of actor number (expect False)")


    time.sleep(1)




    vr.checkFunctionTestList("person", "../docs/source/Objects/person_library.rst", "character", "actor")


    ### QCar


    hCameraQCars = QLabsFreeCamera(qlabs)
    hCameraQCars.spawn_id(actorNumber=33, location=[-15.075, 26.703, 6.074], rotation=[0, 0.564, -1.586])
    hCameraQCars.possess()

    vr.PrintWSHeader("QCar")
    print("\n\n---QCar---")

    hQCar0 = QLabsQCar(qlabs)
    x = hQCar0.spawn_id(actorNumber=0, location=[-8.700, 14.643, 0.005], rotation=[0,0,math.pi/2], waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn QCar with radians")

    hQCar0Duplicate = QLabsQCar(qlabs, True)
    x = hQCar0Duplicate.spawn_id(actorNumber=0, location=[-14.386, 17.445, 0.005], rotation=[0,0,math.pi/2], waitForConfirmation=True)
    vr.PrintWS(x == 2, "Spawn QCar with duplicate ID (return code 2)")

    hQCar1 = QLabsQCar(qlabs)
    hQCar1.spawn_id(actorNumber=1, location=[-15.075, 26.703, 6.074], rotation=[0,0,math.pi/2], waitForConfirmation=True)
    x = hQCar1.destroy()
    vr.PrintWS(x == 1, "Spawn and destroy existing QCar (expect return 1)")

    hQCar1.actorNumber = 10
    x = hQCar1.destroy()
    vr.PrintWS(x == 0, "Destroy QCar that doesn't exist (expect return 0)")

    hQCar2 = QLabsQCar(qlabs)
    x = hQCar2.spawn_id_degrees(actorNumber=2, location=[-11.048, 14.643, 0.005], rotation=[0,0,90], waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn QCar with degrees")


    # lights
    hEnvironmentOutdoors = QLabsEnvironmentOutdoors(qlabs)
    for env_time in range(60):
        hEnvironmentOutdoors.set_time_of_day(12+env_time/10*2)

    time.sleep(0.5)

    hQCar2.set_velocity_and_request_state(forward=1, turn = -math.pi/6, headlights=True, leftTurnSignal=False, rightTurnSignal=True, brakeSignal=False, reverseSignal=False)
    time.sleep(1)
    hQCar2.set_velocity_and_request_state(forward=0.0, turn = -math.pi/6, headlights=True, leftTurnSignal=False, rightTurnSignal=True, brakeSignal=False, reverseSignal=False)
    if require_user_input == True:
        x = input("Moving forward towards the right of the screen, headlights on? (Enter yes, anything else no):")
    else:
        x = ""
    vr.PrintWS(x == "", "Headlights")
    vr.PrintWS(x == "", "Set velocity")

    hQCar2.set_velocity_and_request_state_degrees(forward=1, turn = 30, headlights=True, leftTurnSignal=True, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)
    time.sleep(1)
    success, location, rotation, frontHit, rearHit = hQCar2.set_velocity_and_request_state_degrees(forward=0.0, turn = 30, headlights=True, leftTurnSignal=True, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)
    print(rotation)
    if require_user_input == True:
        x = input("Moving forward towards the left of the screen? Enter yes, anything else no):")
    else:
        x = ""
    vr.PrintWS(x == "", "Set velocity degrees")


    x = hQCar2.possess()

    time.sleep(0.1)
    hQCar2.set_velocity_and_request_state(forward=1, turn = 0, headlights=True, leftTurnSignal=True, rightTurnSignal=True, brakeSignal=True, reverseSignal=True)
    time.sleep(1)
    hQCar2.set_velocity_and_request_state(forward=0.0, turn = 0, headlights=True, leftTurnSignal=True, rightTurnSignal=True, brakeSignal=True, reverseSignal=True)

    if require_user_input == True:
        x = input("Brake lights on and casting red glow? (Enter yes, anything else no):")
    else:
        x = ""
    vr.PrintWS(x == "", "Brake lights")


    hQCar2.set_velocity_and_request_state(forward=0, turn = 0, headlights=False, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)

    for env_time in range(60):
        hEnvironmentOutdoors.set_time_of_day(env_time/10*2)


    #bumper test
    print("Testing bumper response...")
    hCameraQCars.possess()
    hCameraQCars.set_transform(location=[-17.045, 32.589, 6.042], rotation=[0, 0.594, -1.568])

    hCubeQCarBlocks = QLabsBasicShape(qlabs)
    hCubeQCarBlocks .spawn_id(100, [-11.919, 26.289, 0.5], [0,0,0], [1,1,1], configuration=hCubeQCarBlocks.SHAPE_CUBE, waitForConfirmation=True)
    hCubeQCarBlocks .spawn_id(101, [-19.919, 26.289, 0.5], [0,0,0], [1,1,1], configuration=hCubeQCarBlocks.SHAPE_CUBE, waitForConfirmation=True)

    hQCar3 = QLabsQCar(qlabs)
    hQCar3.spawn_id(actorNumber=3, location=[-13.424, 26.299, 0.005], rotation=[0,0,math.pi])

    for count in range(10):
        x, location, rotation, frontHit, rearHit  = hQCar3.set_velocity_and_request_state(forward=2, turn = 0, headlights=False, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)

        time.sleep(0.25)

    vr.PrintWS(x == True and frontHit == True, "Front bumper hit")
    x = hQCar3.ghost_mode()
    vr.PrintWS(x == True, "Ghost Mode")


    for count in range(10):
        x, location, rotation, frontHit, rearHit  = hQCar3.set_velocity_and_request_state(forward=-2, turn = 0, headlights=False, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)

        time.sleep(0.25)

    hQCar3.ghost_mode(enable=True, color=[1,0,0])

    vr.PrintWS(x == True and rearHit == True, "Rear bumper hit")
    hQCar3.set_velocity_and_request_state(forward=0, turn = 0, headlights=False, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)

    x, location, rotation, forward_vector, up_vector, frontHit, rearHit = hQCar3.set_transform_and_request_state(location=[-16.1, 26.299, 0.005], rotation=[0,0,math.pi-0.01], enableDynamics=True, headlights=False, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)
    vr.PrintWS(x == True and frontHit == True, "Front bumper hit with transform")

    x, loc, rot, scale = hQCar3.get_world_transform()
    vr.PrintWS(abs(np.sum(np.subtract(loc, [-16.1, 26.299, 0.005]))) < 0.01 and abs(np.sum(np.subtract(rot, [0,0,math.pi-0.01]))) < 0.01 and x == True, "Get world transform")


    x, location, rotation, forward_vector, up_vector, frontHit, rearHit = hQCar3.set_transform_and_request_state_degrees(location=[-13.1, 26.299, 0.005], rotation=[0,0,179], enableDynamics=True, headlights=False, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)
    vr.PrintWS(x == True and rearHit == True, "Rear bumper hit with transform")

    x, loc, rot, scales = hQCar3.get_world_transform_degrees()
    vr.PrintWS(abs(np.sum(np.subtract(loc, [-13.1, 26.299, 0.005]))) < 0.01 and abs(np.sum(np.subtract(rot, [0,0,179]))) < 0.01 and x == True, "Get world transform degrees")

    hQCar3.ghost_mode(enable=False, color=[1,0,0])


    #camera tests
    print("\nQCar camera tests...")
    hQCar2.possess(hQCar2.CAMERA_OVERHEAD)
    if require_user_input == True:
        x = input("Overhead camera? (Enter yes, anything else no):")
    else:
        x = ""
        time.sleep(0.5)
    vr.PrintWS(x == "", "Possess overhead camera")

    hQCar2.possess(hQCar2.CAMERA_TRAILING)
    if require_user_input == True:
        x = input("Trailing camera? (Enter yes, anything else no):")
    else:
        x = ""
        time.sleep(0.5)
    vr.PrintWS(x == "", "Possess trailing camera")

    hQCar2.possess(hQCar2.CAMERA_CSI_FRONT)
    if require_user_input == True:
        x = input("Front camera? (Enter yes, anything else no):")
    else:
        x = ""
        time.sleep(0.5)
    vr.PrintWS(x == "", "Possess front camera")

    hQCar2.possess(hQCar2.CAMERA_CSI_RIGHT)
    if require_user_input == True:
        x = input("Right camera? (Enter yes, anything else no):")
    else:
        x = ""
        time.sleep(0.5)
    vr.PrintWS(x == "", "Possess right camera")

    hQCar2.possess(hQCar2.CAMERA_CSI_BACK)
    if require_user_input == True:
        x = input("Back camera? (Enter yes, anything else no):")
    else:
        x = ""
        time.sleep(0.5)
    vr.PrintWS(x == "", "Possess back camera")

    hQCar2.possess(hQCar2.CAMERA_CSI_LEFT)
    if require_user_input == True:
        x = input("Left camera? (Enter yes, anything else no):")
    else:
        x = ""
        time.sleep(0.5)
    vr.PrintWS(x == "", "Possess left camera")

    hQCar2.possess(hQCar2.CAMERA_RGB)
    if require_user_input == True:
        x = input("Real Sense RGB camera? (Enter yes, anything else no):")
    else:
        x = ""
        time.sleep(0.5)
    vr.PrintWS(x == "", "Possess Real Sense RGB camera")

    hQCar2.possess(hQCar2.CAMERA_DEPTH)
    if require_user_input == True:
        x = input("Real Sense Depth camera? (Enter yes, anything else no):")
    else:
        x = ""
        time.sleep(0.5)
    vr.PrintWS(x == "", "Possess Real Sense Depth camera")

    cv2.namedWindow('QCarImageStream', cv2.WINDOW_AUTOSIZE)
    camera_image = cv2.imread('Quanser640x480.jpg')
    cv2.imshow('QCarImageStream', camera_image)
    cv2.waitKey(1)


    x, camera_image = hQCar2.get_image(camera=hQCar2.CAMERA_CSI_FRONT)
    if (x == True):
        cv2.imshow('QCarImageStream', camera_image)
        cv2.waitKey(1)
    else:
        print("Image decoding failure")

    vr.PrintWS(x == True, "Image read CSI Front")
    cv2.waitKey(1000)

    x, camera_image = hQCar2.get_image(camera=hQCar2.CAMERA_CSI_RIGHT)
    if (x == True):
        cv2.imshow('QCarImageStream', camera_image)
        cv2.waitKey(1)
    else:
        print("Image decoding failure")

    vr.PrintWS(x == True, "Image read CSI Right")
    cv2.waitKey(1000)

    x, camera_image = hQCar2.get_image(camera=hQCar2.CAMERA_CSI_BACK)
    if (x == True):
        cv2.imshow('QCarImageStream', camera_image)
        cv2.waitKey(1)
    else:
        print("Image decoding failure")

    vr.PrintWS(x == True, "Image read CSI Back")
    cv2.waitKey(1000)

    x, camera_image = hQCar2.get_image(camera=hQCar2.CAMERA_CSI_LEFT)
    if (x == True):
        cv2.imshow('QCarImageStream', camera_image)
        cv2.waitKey(1)
    else:
        print("Image decoding failure")

    vr.PrintWS(x == True, "Image read CSI Left")
    cv2.waitKey(1000)

    x, camera_image = hQCar2.get_image(camera=hQCar2.CAMERA_RGB)
    if (x == True):
        cv2.imshow('QCarImageStream', camera_image)
        cv2.waitKey(1)
    else:
        print("Image decoding failure")

    vr.PrintWS(x == True, "Image read Real Sense RGB")
    cv2.waitKey(1000)

    x, camera_image = hQCar2.get_image(camera=hQCar2.CAMERA_DEPTH)
    if (x == True):
        cv2.imshow('QCarImageStream', camera_image)
        cv2.waitKey(1)
    else:
        print("Image decoding failure")

    vr.PrintWS(x == True, "Image read Real Sense Depth")
    cv2.waitKey(1000)


    #ping
    print("Testing ping response...")
    x = hQCar2.ping()
    vr.PrintWS(x == True, "Ping existing QCar (expect True)")

    x = hQCar1.ping()
    vr.PrintWS(x == False, "Ping QCar that doesn't exist (expect False)")


    #LIDAR

    hQCar3.possess(hQCar3.CAMERA_OVERHEAD)

    lidarPlot = pg.plot(title="LIDAR")
    squareSize = 100
    lidarPlot.setXRange(-squareSize, squareSize)
    lidarPlot.setYRange(-squareSize, squareSize)
    lidarData = lidarPlot.plot([], [], pen=None, symbol='o', symbolBrush='r', symbolPen=None, symbolSize=2)


    time.sleep(1)

    print("Reading from LIDAR... if QLabs crashes, make sure FPS > 100 or fix the crash bug!")


    for count in range(20):

        success, angle, distance = hQCar3.get_lidar(samplePoints=400)

        x = np.sin(angle)*distance
        y = np.cos(angle)*distance

        lidarData.setData(x,y)
        QtWidgets.QApplication.instance().processEvents()
        time.sleep(lidar_rate)

    vr.PrintWS(True, "LIDAR didn't crash QLabs!")
    vr.PrintWS(lidar_rate == 0.01, "Passed LIDAR test with 100Hz (lidar_rate = 0.01 expected)")

    time.sleep(1)

    vr.checkFunctionTestList("qcar", "../docs/source/Objects/car_library.rst", "actor")


    ### Basic Shape


    vr.PrintWSHeader("Basic Shape")
    print("\n\n---Basic Shape---")

    x = hCamera2.possess()

    hCube200 = QLabsBasicShape(qlabs)
    x = hCube200.spawn_id(actorNumber=200, location=[-4.852, 36.977, 0.5], rotation=[0,0,math.pi/4], scale=[0.5,0.5,0.5], configuration=hCube200.SHAPE_CUBE, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn sign with radians")



    hCube200Duplicate = QLabsBasicShape(qlabs)
    x = hCube200Duplicate.spawn_id(actorNumber=200, location=[-5.852, 36.977, 0.5], rotation=[0,0,math.pi/4], scale=[0.5,0.5,0.5], configuration=hCube200Duplicate.SHAPE_CUBE, waitForConfirmation=True)
    vr.PrintWS(x == 2, "Spawn with duplicate ID")

    hCube220 = QLabsBasicShape(qlabs)
    x = hCube220.spawn_id_degrees(actorNumber=220, location=[-4.832, 34.147, 0.5], rotation=[0,0,45], scale=[0.5,0.5,0.5], configuration=hCube220.SHAPE_CUBE, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn sign with degrees")

    hCube221 = QLabsBasicShape(qlabs, True)
    x = hCube221.spawn_id_degrees(actorNumber=221, location=[-4.832, 35.147, 0.5], rotation=[0,0,45], scale=[0.5,0.5,0.5], configuration=hCube221.SHAPE_CUBE, waitForConfirmation=True)
    x = hCube221.destroy()
    print("Num actors destroyed: {}".format(x))
    vr.PrintWS(x == 1, "Spawn and destroy existing (expect return 1)")


    hCube221.actorNumber = 221
    x = hCube221.destroy()
    print("Num actors destroyed: {}".format(x))
    vr.PrintWS(x == 0, "Destroy shape that doesn't exist (expect return 0)")


    x = hCube220.ping()
    vr.PrintWS(x == True, "Ping existing sign (expect True)")

    hCube221.actorNumber = 221
    x = hCube221.ping()
    vr.PrintWS(x == False, "Ping sign that doesn't exist (expect False)")

    x, loc, rot, scale = hCube200.get_world_transform()
    vr.PrintWS(np.sum(np.subtract(loc, [-4.852, 36.977, 0.5])) < 0.001 and x == True, "Get world transform")

    hCube201 = QLabsBasicShape(qlabs, True)
    x = hCube201.spawn_id_and_parent_with_relative_transform(actorNumber=201, location=[0,2,0], rotation=[0,0,math.pi/4], scale=[1,1,1], configuration=hCube201.SHAPE_CUBE, parentClassID=hCube200.ID_BASIC_SHAPE, parentActorNumber=hCube200.actorNumber, parentComponent=0, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn with parent relative transform (expect 0)")

    hCube202 = QLabsBasicShape(qlabs, True)
    x = hCube202.spawn_id_and_parent_with_relative_transform_degrees(actorNumber=202, location=[0,-2,0], rotation=[0,0,45], scale=[1,1,1], configuration=hCube202.SHAPE_CUBE, parentClassID=hCube200.ID_BASIC_SHAPE, parentActorNumber=hCube200.actorNumber, parentComponent=0, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn with parent relative transform degrees (expect 0)")


    x = hCube202.set_material_properties(color=[0,1,0], roughness=0.0, metallic=True, waitForConfirmation=True)
    x = hCube201.set_material_properties(color=[1,0,0], roughness=0.0, metallic=True, waitForConfirmation=True)
    vr.PrintWS(x == True, "Set material properties (expect True)")

    for y in range(51):
        x = hCube201.set_transform(location=[0,2,0], rotation=[0,0,math.pi/4-math.pi/25*y], scale=[1,1,1], waitForConfirmation=False)
        x = hCube202.set_transform_degrees(location=[0,-2,0], rotation=[0,0,45-180/25*y], scale=[1,1,1], waitForConfirmation=False)
        x = hCube200.set_transform(location=[-4.852, 36.977, 0.5], rotation=[0,0,math.pi/4+2*math.pi/50*y], scale=[0.5+0.5*y/50,0.5+0.5*y/50,0.5+0.5*y/50])


    # parenting without spawn
    hCube301 = QLabsBasicShape(qlabs)
    hCube301.spawn(location=[-4.93, 36.985, 1.5], rotation=[0,0,0], scale=[0.2,0.2,0.2], configuration=hCube301.SHAPE_CUBE, waitForConfirmation=True)

    hCube302 = QLabsBasicShape(qlabs)
    hCube302.spawn(location=[-4.93, 35.985, 1.5], rotation=[0,0,0], scale=[0.5,0.5,0.5], configuration=hCube302.SHAPE_CUBE, waitForConfirmation=True)

    for y in range(37):
        x = hCube301.set_transform_degrees(location=[-4.93, 36.985, 1.5], rotation=[0,0,y*10], scale=[0.2,0.2,0.2], waitForConfirmation=True)

    x = hCube302.parent_with_relative_transform(location=[0,1.2/0.2,0], rotation=[0,0,0], scale=[0.5,0.5,0.5], parentClassID=hCube301.classID, parentActorNumber=hCube301.actorNumber, parentComponent=0, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Parent with relative transform")
    time.sleep(0.5)

    for y in range(37):
        x = hCube301.set_transform_degrees(location=[-4.93, 36.985, 1.5], rotation=[0,0,y*10], scale=[0.2,0.2,0.2], waitForConfirmation=True)

    x = hCube302.parent_break()
    vr.PrintWS(x == 0, "Parent break")

    for y in range(37):
        x = hCube301.set_transform_degrees(location=[-4.93, 36.985, 1.5], rotation=[0,0,y*10], scale=[0.2,0.2,0.2], waitForConfirmation=True)

    x = hCube302.parent_with_current_world_transform(parentClassID=hCube301.classID, parentActorNumber=hCube301.actorNumber, parentComponent=0, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Parent with current world transform")
    time.sleep(0.5)

    for y in range(37):
        x = hCube301.set_transform_degrees(location=[-4.93, 36.985, 1.5], rotation=[0,0,y*10], scale=[0.2,0.2,0.2], waitForConfirmation=True)

    x = hCube302.parent_break()
    x = hCube302.parent_with_relative_transform_degrees(location=[0,1.2/0.2,0], rotation=[0,0,0], scale=[0.5,0.5,0.5], parentClassID=hCube301.classID, parentActorNumber=hCube301.actorNumber, parentComponent=0, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Parent with relative transform degrees")
    time.sleep(0.5)

    for y in range(37):
        x = hCube301.set_transform_degrees(location=[-4.93, 36.985, 1.5], rotation=[0,0,y*10], scale=[0.2,0.2,0.2], waitForConfirmation=True)


    #collisions

    hSphere203 = QLabsBasicShape(qlabs)
    x = hSphere203.spawn_id(actorNumber=203, location=[-4.75, 32.5, 0.25], rotation=[0,0,0], scale=[0.5,0.5,0.5], configuration=hSphere203.SHAPE_SPHERE, waitForConfirmation=True)
    x = hSphere203.set_material_properties(color=[0,1,0], roughness=0.0, metallic=False, waitForConfirmation=True)

    hSphere204 = QLabsBasicShape(qlabs)
    x = hSphere204.spawn_id(actorNumber=204, location=[-4.75, 31.5, 0.25], rotation=[0,0,0], scale=[0.5,0.5,0.5], configuration=hSphere204.SHAPE_SPHERE, waitForConfirmation=True)
    x = hSphere204.set_material_properties(color=[0,0,1], roughness=0.0, metallic=False, waitForConfirmation=True)
    x = hSphere204.set_enable_collisions(enableCollisions=False, waitForConfirmation=True)
    vr.PrintWS(x == True, "Enable collisions")

    hSphere205 = QLabsBasicShape(qlabs)
    hSphere206 = QLabsBasicShape(qlabs)
    hSphere207 = QLabsBasicShape(qlabs)

    x = hSphere205.spawn_id(actorNumber=205, location=[-4.6, 32.5, 2], rotation=[0,0,0], scale=[0.6,0.6,0.6], configuration=hSphere205.SHAPE_SPHERE, waitForConfirmation=True)
    x = hSphere206.spawn_id(actorNumber=206, location=[-4.6, 31.5, 2], rotation=[0,0,0], scale=[0.6,0.6,0.6], configuration=hSphere206.SHAPE_SPHERE, waitForConfirmation=True)
    x = hSphere207.spawn_id(actorNumber=207, location=[-4.6, 30.5, 2], rotation=[0,0,0], scale=[0.6,0.6,0.6], configuration=hSphere207.SHAPE_SPHERE, waitForConfirmation=True)

    x = hSphere207.set_physics_properties(enableDynamics=False, mass=1, linearDamping=10, angularDamping=0)
    vr.PrintWS(x == True, "Set physics properties")

    x = hSphere205.set_enable_dynamics(enableDynamics=True, waitForConfirmation=False)
    x = hSphere206.set_enable_dynamics(enableDynamics=True, waitForConfirmation=False)
    x = hSphere207.set_enable_dynamics(enableDynamics=True, waitForConfirmation=True)
    vr.PrintWS(x == True, "Enable dynamics")

    x = hSphere205.set_enable_dynamics(enableDynamics=True, waitForConfirmation=False)

    hBoxSpawn = QLabsBasicShape(qlabs)
    x = hBoxSpawn.spawn_id_box_walls_from_center(actorNumbers=[210, 211, 212, 213, 214], centerLocation=[-1.103, 32.404, 0.005], yaw=math.pi/4, xSize=2, ySize=2, zHeight=0.5, wallThickness=0.1, floorThickness=0.1, wallColor=[1,0,0], floorColor=[0,0,1], waitForConfirmation=True)
    vr.PrintWS(x == True, "Spawn box walls from center")

    x = hBoxSpawn.spawn_id_box_walls_from_center_degrees(actorNumbers=[270, 271, 272, 273, 274], centerLocation=[0.35, 30.4, 0.005], yaw=45, xSize=2, ySize=2, zHeight=0.5, wallThickness=0.1, floorThickness=0.1, wallColor=[1,0,0], floorColor=[0,0,1], waitForConfirmation=True)
    vr.PrintWS(x == True, "Spawn box walls from center degrees")

    x = hBoxSpawn.spawn_id_box_walls_from_end_points(actorNumber=280, startLocation=[-3.232, 31.439, 0.01], endLocation=[-1.403, 29.383, 0.01], height=0.1, thickness=0.1, color=[0.2,0.2,0.2], waitForConfirmation=True)
    vr.PrintWS(x == True, "Spawn box walls from end points")

    x, shapeHandle1 = hBoxSpawn.spawn(location=[-5.632, 34.162, 0.25], rotation=[0,0,math.pi/4], scale=[0.5,0.5,0.5], configuration=hBoxSpawn.SHAPE_CUBE, waitForConfirmation=True)
    x, shapeHandle2 = hBoxSpawn.spawn(location=[-5.632, 33.162, 0.25], rotation=[0,0,math.pi/4], scale=[0.5,0.5,0.5], configuration=hBoxSpawn.SHAPE_CUBE, waitForConfirmation=True)
    x, shapeHandle3 = hBoxSpawn.spawn(location=[-5.632, 32.162, 0.25], rotation=[0,0,math.pi/4], scale=[0.5,0.5,0.5], configuration=hBoxSpawn.SHAPE_CUBE, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn next")

    x, shapeHandle4 = hBoxSpawn.spawn_degrees(location=[-5.632, 31.162, 0.25], rotation=[0,0,45], scale=[0.5,0.5,0.5], configuration=hBoxSpawn.SHAPE_CUBE, waitForConfirmation=True)
    x, shapeHandle5 = hBoxSpawn.spawn_degrees(location=[-5.632, 30.162, 0.25], rotation=[0,0,45], scale=[0.5,0.5,0.5], configuration=hBoxSpawn.SHAPE_CUBE, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn next degrees")

    hBoxSpawn.actorNumber = shapeHandle2
    x = hBoxSpawn.set_material_properties(color=[1,0,1], roughness=0.0, metallic=True, waitForConfirmation=True)
    vr.checkFunctionTestList("basic_shape", "../docs/source/Objects/basic_shapes.rst", "actor")


    ### Widget

    vr.PrintWSHeader("Widget")
    print("\n\n--Widget---")

    x = hCamera2.possess()
    hQLabsWidget = QLabsWidget(qlabs)
    hQLabsWidget.widget_spawn_shadow(enableShadow=True)

    for count in range(20):
        x = hQLabsWidget.spawn([-0.974, 32.404, 1+count*0.2], [0,0,0], [1,1,1], hQLabsWidget.METAL_CAN, [1,1,1], measuredMass=0, IDTag=0, properties='', waitForConfirmation=True)

    vr.PrintWS(x == True, "Widget spawn (expect True)")

    time.sleep(1)

    for count in range(20):
        x = hQLabsWidget.spawn_degrees([-0.974, 32.404, 1+count*0.2], [90,0,0], [1,1,1], hQLabsWidget.METAL_CAN, [1,0,0], measuredMass=0, IDTag=0, properties='', waitForConfirmation=True)

    vr.PrintWS(x == True, "Widget spawn degrees(expect True)")

    time.sleep(1)

    x = hQLabsWidget.destroy_all_spawned_widgets()
    vr.PrintWS(x == True, "Widgets destroyed (expect True)")
    hQLabsWidget.widget_spawn_shadow(enableShadow=False)

    for count in range(10):
        x = hQLabsWidget.spawn_degrees([-0.974, 32.404+count*0.01, 1+count*0.6], [90,0,0], [0.5,0.5,0.5], hQLabsWidget.SPHERE, [1,0,0], measuredMass=0, IDTag=0, properties='', waitForConfirmation=True)

    time.sleep(1)

    hQLabsWidget.destroy_all_spawned_widgets()
    hQLabsWidget.widget_spawn_shadow(enableShadow=True)

    for count in range(10):
        x = hQLabsWidget.spawn_degrees([-0.974, 32.404+count*0.01, 1+count*0.6], [90,0,0], [0.5,0.5,0.5], hQLabsWidget.SPHERE, [1,0,0], measuredMass=0, IDTag=0, properties='', waitForConfirmation=True)



    vr.checkFunctionTestList("widget", "../docs/source/Objects/widgets.rst")



    ### Traffic Light

    vr.PrintWSHeader("Traffic Light")
    print("\n\n---Traffic Light---")


    hCameraTraffic = QLabsFreeCamera(qlabs)
    x = hCameraTraffic.spawn(location=[-6.891, 3.568, 2.127], rotation=[0, 0.049, 1.105])
    hCameraTraffic.possess()

    hTrafficLight0 = QLabsTrafficLight(qlabs)
    x = hTrafficLight0.spawn_id(actorNumber=0, location=[6, 14.328, 0.215], rotation=[0,0,0], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn traffic light with radians")

    x = hTrafficLight0.spawn_id(actorNumber=0, location=[6, 14.328, 0.215], rotation=[0,0,0], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    vr.PrintWS(x == 2, "Spawn traffic light with duplicate ID (return code 2)")

    hTrafficLight1 = QLabsTrafficLight(qlabs)
    hTrafficLight1.spawn_id(actorNumber=1, location=[-2.44, 15, 0.215], rotation=[0,0,0], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    x = hTrafficLight1.destroy()
    vr.PrintWS(x == 1, "Spawn and destroy existing light (expect return 1)")

    hTrafficLight1.actorNumber = 1
    x = hTrafficLight1.destroy()
    vr.PrintWS(x == 0, "Destroy traffic light that doesn't exist (expect return 0)")

    hTrafficLight2 = QLabsTrafficLight(qlabs)
    x = hTrafficLight2.spawn_id_degrees(actorNumber=2, location=[-2.44, 15, 0.215], rotation=[0,0,180], scale=[1,1,1], configuration=1, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn traffic light with degrees in config 1")

    hTrafficLight3 = QLabsTrafficLight(qlabs)
    [x, assignedActorNum] = hTrafficLight3.spawn_degrees(location=[6.686, 5.802, 0.215], rotation=[0,0,-90], scale=[1,1,1], configuration=2, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn traffic light with degrees in config 2")


    x, loc, rot, scale = hTrafficLight2.get_world_transform()
    vr.PrintWS(x == True, "Get world transform")


    x = hTrafficLight2.ping()
    vr.PrintWS(x == True, "Ping existing traffic light (expect True)")

    hTrafficLight1.actorNumber = 1
    x = hTrafficLight1.ping()
    vr.PrintWS(x == False, "Ping traffic light that doesn't exist (expect False)")

    hTrafficLight0.set_state(state=hTrafficLight0.STATE_GREEN, waitForConfirmation=True)
    hTrafficLight2.set_state(state=hTrafficLight2.STATE_GREEN, waitForConfirmation=True)
    hTrafficLight3.set_state(state=hTrafficLight3.STATE_GREEN, waitForConfirmation=True)

    time.sleep(0.5)

    hTrafficLight0.set_state(state=hTrafficLight0.STATE_YELLOW, waitForConfirmation=True)
    hTrafficLight2.set_state(state=hTrafficLight2.STATE_YELLOW, waitForConfirmation=True)
    hTrafficLight3.set_state(state=hTrafficLight3.STATE_YELLOW, waitForConfirmation=True)

    time.sleep(0.5)

    hTrafficLight0.set_state(state=hTrafficLight0.STATE_RED, waitForConfirmation=True)
    hTrafficLight2.set_state(state=hTrafficLight2.STATE_RED, waitForConfirmation=True)
    hTrafficLight3.set_state(state=hTrafficLight3.STATE_RED, waitForConfirmation=True)

    time.sleep(0.5)

    x = hTrafficLight0.destroy_all_actors_of_class()
    vr.PrintWS(x == 3, "Delete all actors of class (expect 3), received {}".format(x))

    vr.checkFunctionTestList("traffic_light", "../docs/source/Objects/road_signage.rst", "actor")


    ### Spline Line
    vr.PrintWSHeader("Spline Line")
    print("\n\n---Spline Line---")

    hCameraSplines = QLabsFreeCamera(qlabs)
    x = hCameraSplines.spawn(location=[-3.097, 2.579, 11.849], rotation=[0, 0.912, 1.141])
    hCameraSplines.possess()

    hSpline2 = QLabsSplineLine(qlabs)

    lineWidth = 0.125
    splineZ = 0.015
    points = [[-6.184, 9.595, splineZ,lineWidth],
              [-4.081, 9.856, splineZ, lineWidth],
              [-1.998, 10.178, splineZ, lineWidth],
              [-0.461, 11.024, splineZ, lineWidth],
              [0.168, 11.721, splineZ, lineWidth],
              [0.742, 13.048, splineZ, lineWidth],
              [0.991, 14.059, splineZ, lineWidth],
              [1.276, 15.72, splineZ, lineWidth],
              [1.363, 17.125, splineZ, lineWidth]]

    color_selection=[[0.5,0,0], [0.5,0,0.5], [0,0.5,0], [0,0,0.5]]

    for counter in range(4):
        x = hSpline2.spawn(location=[0,0-counter*0.75,0+counter*0.001], rotation=[0,0,0], scale=[1,1,1], configuration=counter, waitForConfirmation=True)
        x = hSpline2.set_points(color=color_selection[counter], pointList=points, alignEndPointTangents=False, waitForConfirmation=True)
        vr.PrintWS(x == True, "Spawn configuration {}: {}".format(counter, x))

    time.sleep(0.5)
    x = hSpline2.destroy_all_actors_of_class()
    vr.PrintWS(x == 4, "Destroy all actors of class (expect 4): {}".format(x))

    hSpline2.spawn_id(actorNumber=0, location=[0,0,0], rotation=[0,0,0], scale=[1,1,1], configuration=counter, waitForConfirmation=True)
    hSpline2.set_points(color=color_selection[0], pointList=points, alignEndPointTangents=False, waitForConfirmation=True)
    time.sleep(0.5)

    x = hSpline2.destroy()
    vr.PrintWS(x == 1, "Destroy actor (expect 1): {}".format(x))

    hSpline2.spawn_id_degrees(actorNumber=1, location=[0,0,0], rotation=[0,0,0], scale=[1,1,1], configuration=counter, waitForConfirmation=True)
    hSpline2.set_points(color=color_selection[0], pointList=points, alignEndPointTangents=False, waitForConfirmation=True)
    x = hSpline2.ping()
    vr.PrintWS(x == True, "Ping (expect True): {}".format(x))

    hSpline2.destroy()
    hSpline2.actorNumber = 1
    x = hSpline2.ping()
    vr.PrintWS(x == False, "Ping actor that doesn't exist (expect False): {}".format(x))


    hSpline3 = QLabsSplineLine(qlabs)
    hSpline3.spawn([1.741, 8.757, 0.005], [0,0,0],[1,1,1],1)
    x = hSpline3.circle_from_center(radius=1, lineWidth=0.1, color=[1,0,1], numSplinePoints=8)
    vr.PrintWS(x == True, "Circle from center (expect True): {}".format(x))

    hSpline4 = QLabsSplineLine(qlabs)
    hSpline4.spawn([4.467, 10.579, 0.005], [0,0,0],[1,1,1],1)
    hSpline4.arc_from_center(radius=1, startAngle=0, endAngle=math.pi/2, lineWidth=0.1, color=[1,0,0], numSplinePoints=8)
    vr.PrintWS(x == True, "Arc from center (expect True): {}".format(x))

    hSpline5 = QLabsSplineLine(qlabs)
    hSpline5.spawn([5.045, 11.205, 0.005], [0,0,0],[1,1,1],1)
    hSpline5.arc_from_center_degrees(radius=1, startAngle=0, endAngle=90, lineWidth=0.1, color=[1,0,0], numSplinePoints=8)
    vr.PrintWS(x == True, "Arc from center degrees (expect True): {}".format(x))

    hSpline6 = QLabsSplineLine(qlabs)
    hSpline6.spawn([3.118, 8.109, 0.005], [0,0,0],[1,1,1],1)
    hSpline6.rounded_rectangle_from_center(cornerRadius=0.5, xWidth=2, yLength=4, lineWidth=0.1, color=[1,1,0])
    vr.PrintWS(x == True, "Rounded rectangle (expect True): {}".format(x))


    vr.checkFunctionTestList("spline_line", "../docs/source/Objects/splines.rst", "actor")


    ### Animals
    vr.PrintWSHeader("Animals")
    print("\n\n---Animals---")

    hCameraAnimals = QLabsFreeCamera(qlabs)
    x = hCameraAnimals.spawn(location=[25.802, 47.9, 0.484], rotation=[-0, -0.195, 1.009])
    hCameraAnimals.possess()

    hGoat = QLabsAnimal(qlabs)
    hGoat.spawn(location=[26.206, 57, 1], rotation=[0,0,0], scale=[1,1,1], configuration=hGoat.GOAT, waitForConfirmation=True)
    hGoat.move_to(location=[27.214, 49.286, 0], speed=hGoat.GOAT_RUN, waitForConfirmation=True)

    time.sleep(3)
    hGoat.move_to(location=[28.338, 47.826, 0], speed=hGoat.GOAT_WALK, waitForConfirmation=True)
    time.sleep(6)
    hGoat.destroy()


    hSheep = QLabsAnimal(qlabs)
    hSheep.spawn(location=[26.206, 57, 1], rotation=[0,0,0], scale=[1,1,1], configuration=hSheep.SHEEP, waitForConfirmation=True)
    hSheep.move_to(location=[27.214, 49.286, 0], speed=hSheep.SHEEP_RUN, waitForConfirmation=True)
    time.sleep(3)
    hSheep.move_to(location=[28.338, 47.826, 0], speed=hSheep.SHEEP_WALK, waitForConfirmation=True)
    time.sleep(6)
    hSheep.destroy()


    hCow = QLabsAnimal(qlabs)
    hCow.spawn(location=[26.206, 57, 1], rotation=[0,0,0], scale=[1,1,1], configuration=hCow.COW, waitForConfirmation=True)
    hCow.move_to(location=[27.214, 49.286, 0], speed=hCow.COW_RUN, waitForConfirmation=True)
    time.sleep(3)
    hCow.move_to(location=[28.338, 47.826, 0], speed=hCow.COW_WALK, waitForConfirmation=True)
    time.sleep(6)



    vr.checkFunctionTestList("animal", "../docs/source/Objects/animal_library.rst", "character", "actor")



    ### Outdoor Environment
    vr.PrintWSHeader("Outdoor Environment")
    print("\n\n---Outdoor Environment---")

    hEnvironmentOutdoors2 = QLabsEnvironmentOutdoors(qlabs)
    hEnvironmentOutdoors2.set_outdoor_lighting(0)

    hCameraWeather = QLabsFreeCamera(qlabs)
    x = hCameraWeather.spawn(location=[0.075, -8.696, 1.576], rotation=[0, -0.141, 1.908])
    hCameraWeather.possess()

    time.sleep(2.5)
    hSystem = QLabsSystem(qlabs)

    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.CLEAR_SKIES)
    hSystem.set_title_string('Clear skies')
    time.sleep(2.5)

    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.PARTLY_CLOUDY)
    hSystem.set_title_string('Partly cloudy')
    time.sleep(2.5)

    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.CLOUDY)
    hSystem.set_title_string('Cloudy')
    time.sleep(2.5)

    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.OVERCAST)
    hEnvironmentOutdoors2.set_outdoor_lighting(1)
    hSystem.set_title_string('Overcast')
    time.sleep(2.5)

    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.FOGGY)
    hSystem.set_title_string('Foggy')
    time.sleep(2.5)

    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.LIGHT_RAIN)
    hEnvironmentOutdoors2.set_outdoor_lighting(0)
    hSystem.set_title_string('Light rain')
    time.sleep(2.5)

    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.RAIN)
    hEnvironmentOutdoors2.set_outdoor_lighting(1)
    hSystem.set_title_string('Rain')
    time.sleep(2.5)

    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.THUNDERSTORM)
    hSystem.set_title_string('Thunderstorm')
    time.sleep(2.5)

    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.LIGHT_SNOW)
    hEnvironmentOutdoors2.set_outdoor_lighting(0)
    hSystem.set_title_string('Light snow')
    time.sleep(2.5)

    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.SNOW)
    hEnvironmentOutdoors2.set_outdoor_lighting(1)
    hSystem.set_title_string('Snow')
    time.sleep(2.5)

    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.BLIZZARD)
    hSystem.set_title_string('Blizzard')
    time.sleep(2.5)

    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.PARTLY_CLOUDY)
    hEnvironmentOutdoors2.set_outdoor_lighting(0)
    hSystem.set_title_string('QLABS VERIFICATION SCRIPT')

    ### Real-Time
    vr.PrintWSHeader("Real-Time")
    print("\n\n---Real-Time---")

    vr.checkFunctionTestList("real_time", "../docs/source/System/real_time_library.rst")



    print("\n\n------------------------------ Communications --------------------------------\n")

    qlabs.close()
    cv2.destroyAllWindows()
    print("Done!")


vr = verificationReport('QCar Validation Report.xlsx', 'library_verification_qcar.py', library_path)
vr.ignore_list = ignore_list
#vr.verbose = True


main()

vr.WriteFileBuffer()
