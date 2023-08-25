import sys
sys.path.insert(0, "../")

from qvl.qlabs import QuanserInteractiveLabs

from qvl.qbot import QLabsQbot
from qvl.qbot2e import QLabsQBot2e
from qvl.qbot3 import QLabsQBot3
from qvl.qbot_platform import QLabsQBotPlatform
from qvl.walls import QLabsWalls
from qvl.reference_frame import QLabsReferenceFrame
from qvl.shredder import QLabsShredder
from qvl.delivery_tube import QLabsDeliveryTube, QLabsDeliveryTubeBottles
from qvl.qarm import QLabsQArm
from qvl.conveyor_curved import QLabsConveyorCurved
from qvl.conveyor_straight import QLabsConveyorStraight
from qvl.qbot_platform_flooring import QLabsQBotPlatformFlooring
from qvl.free_camera import QLabsFreeCamera
from qvl.basic_shape import QLabsBasicShape
from qvl.widget import QLabsWidget

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

##########################################

library_path = '.../qvl'

##########################################

ignore_list = ['autoclave', \
               'bottle_table', \
               'qbot_hopper', \
               'srv02', \
               'weigh_scale', \
               'qube_servo_2',\
               'actor',\
               'yield_sign',\
               'stop_sign',\
               'roundabout_sign',\
               'traffic_cone',\
               'crosswalk',\
               'basic_shape',\
               'qcar',\
               'environment_outdoors',\
               'person',\
               'spline_line',\
               'widget',\
               'traffic_light',\
               'image_utilities']

def main():
    os.system('cls')

    print("----------------- Checking that all libraries are being tested -------------------\n")
    vr.PrintWSHeader("Library Test List")
    #vr.checkValidationLibraryList()

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

    print("\n\n------------------------------ Testing Libraries --------------------------------\n")

    ### QLabs
    vr.PrintWSHeader("Common")
    x = "Destroyed {} actors.".format(qlabs.destroy_all_spawned_actors())
    print(x)
    vr.PrintWS(2, x)

    #'''
    print("\n\n------------------------------ Free Camera --------------------------------\n")

    vr.PrintWSHeader("Free Camera")
    print("\n\n---Free Camera---")

    hCamera0 = QLabsFreeCamera(qlabs)
    x = hCamera0.spawn_id(actorNumber=0, location=[0, 0, 8.538], rotation=[0, 1.209, 1.559])
    vr.PrintWS(x == 0, "Spawn camera with radians")


    print('Attempt to spawn duplicate.')
    hCamera0Duplicate = QLabsFreeCamera(qlabs, True)
    x = hCamera0Duplicate.spawn_id(actorNumber=0, location=[0, 0, 8.43], rotation=[0, 1.204, 1.548])
    vr.PrintWS(x == 2, "Spawn camera with duplicate ID (return code 2)")

    hCamera1 = QLabsFreeCamera(qlabs)
    hCamera1.spawn_id(actorNumber=1, location=[0, 0, 3.482], rotation=[0, 0.349, -0.04])
    x = hCamera1.destroy()
    vr.PrintWS(x == 1, "Spawn and destroy existing camera (expect return 1)")

    hCamera10 = QLabsFreeCamera(qlabs)
    hCamera10.actorNumber = 10
    x = hCamera10.destroy()
    vr.PrintWS(x == 0, "Destroy camera that doesn't exist (expect return 0)")

    loc2 = [0, 0, 3.745]
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
    hCamera3.spawn_id(actorNumber=3, location=[0, 0, 2.282], rotation=[0, 0.077, 0.564])
    hCamera3.set_camera_properties(fieldOfView=40, depthOfField=True, aperture=2.3, focusDistance=0.6)
    x = hCamera3.possess()


    for y in range(51):
        x = hCamera3.set_camera_properties(fieldOfView=40, depthOfField=True, aperture=2.3, focusDistance=(0.6 + pow(y/50, 3)*23.7))
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
    loc3 = [0, 0, 2]
    hCubeCameraHook = QLabsBasicShape(qlabs, True)
    x = hCubeCameraHook.spawn_id(1000, loc3, [0,0,0], [1,1,1], configuration=hCubeCameraHook.SHAPE_CUBE, waitForConfirmation=True)

    hCamera5Child = QLabsFreeCamera(qlabs, True)
    x = hCamera5Child.spawn_id_and_parent_with_relative_transform(5, [0, 0, 0], [0,0,math.pi/2], [1,1,1], 0, hCubeCameraHook.ID_BASIC_SHAPE, hCubeCameraHook.actorNumber, 0)
    vr.PrintWS(x == 0, "Spawn and parent with relative transform")
    x = hCamera5Child.possess()
    for y in range(26):
        x = hCubeCameraHook.set_transform(loc3, [0, 0, y/25*math.pi*2], [1,1,1])

    time.sleep(0.5)

    hCamera5Child.destroy()
    x = hCamera5Child.spawn_id_and_parent_with_relative_transform_degrees(5, [0, 0, 0], [0,0,90], [1,1,1], 0, hCubeCameraHook.ID_BASIC_SHAPE, hCubeCameraHook.actorNumber, 0)
    vr.PrintWS(x == 0, "Spawn and parent with relative transform degrees")
    x = hCamera5Child.possess()
    for y in range(26):
        x = hCubeCameraHook.set_transform(loc3, [0, 0, y/25*math.pi*2], [1,1,1])

    hCameraSpawnAutogen1 = QLabsFreeCamera(qlabs)
    x, CameraSpawn1Num = hCameraSpawnAutogen1.spawn(location=[0, 0, 8.43], rotation=[0, 1.204, 1.548])
    vr.PrintWS(x == 0, "Spawn with automatically generated ID ({})".format(CameraSpawn1Num))

    hCameraSpawnAutogen2 = QLabsFreeCamera(qlabs)
    x, CameraSpawn2Num = hCameraSpawnAutogen2.spawn_degrees(location=[0, 0, 8.43], rotation=[0, 0, 0])
    vr.PrintWS(x == 0, "Spawn with automatically generated ID ({})".format(CameraSpawn2Num))


    #vr.checkFunctionTestList("free_camera", "../docs/source/Objects/camera_library.rst", "actor")

    cv2.destroyAllWindows()
    x = hCamera2.possess()


    print("\n\n------------------------------ Qbot --------------------------------\n")
    vr.PrintWSHeader("Qbot")

    hQbotCamera = QLabsFreeCamera(qlabs, True)
    hQbotCamera.spawn_id_degrees(actorNumber=8, location=[-3.5, 2, 2], rotation=[0, 40, -90])
    x = hQbotCamera.possess()

    """
    hQbot0 = QLabsQbot(qlabs)
    x = hQbot0.spawn_id(actorNumber = 0, location=[-3, 0, 0], rotation=[0, 0, math.pi], scale=[1, 1, 1], configuration=0, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn qbot with radians")

    x = hQbot0.spawn_id(actorNumber=0, location=[-3.5, 0, 0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    vr.PrintWS(x == 2, "Spawn qbot with duplicate ID (return code 2)")

    hQbot1 = QLabsQbot(qlabs)
    hQbot1.spawn_id(actorNumber=1, location=[-3.5, 0, 0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    x = hQbot1.destroy()
    vr.PrintWS(x == 1, "Spawn and destroy existing qbot (expect return 1)")

    hQbot1.actorNumber=1
    x = hQbot1.destroy()
    vr.PrintWS(x == 0, "Destroy qbot that doesn't exist (expect return 0)")

    hQbot2 = QLabsQbot(qlabs)
    x = hQbot2.spawn_id_degrees(actorNumber=2, location=[-4, 0, 0], rotation=[0,0,180], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn qbot with degrees")

    x, loc, rot, scale = hQbot2.get_world_transform()
    vr.PrintWS(np.array_equal(loc, [-4, 0, 0]) and x == True, "Get world transform")
    print(hQbot2.get_world_transform())

    x = hQbot2.ping()
    vr.PrintWS(x == True, "Ping existing qbot (expect True)")

    hQbot1.actorNumber=1
    x = hQbot1.ping()
    vr.PrintWS(x == False, "Ping qbot that doesn't exist (expect False)")
    """

    time.sleep(0.5)


    print("\n\n------------------------------ Qbot2e --------------------------------\n")
    vr.PrintWSHeader("Qbot2e")

    hQbot2eCamera = QLabsFreeCamera(qlabs, True)
    hQbot2eCamera.spawn_id_degrees(actorNumber=9, location=[-5.5, 2, 2], rotation=[0, 40, -90])
    x = hQbot2eCamera.possess()

    hQbot2e0 = QLabsQBot2e(qlabs)
    x = hQbot2e0.spawn_id(actorNumber = 0, location=[-5, 0, 0], rotation=[0, 0, math.pi], scale=[1, 1, 1], configuration=0, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn qbot with radians")

    x = hQbot2e0.spawn_id(actorNumber=0, location=[-5.5, 0, 0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    vr.PrintWS(x == 2, "Spawn qbot with duplicate ID (return code 2)")

    hQbot2e1 = QLabsQBot2e(qlabs)
    hQbot2e1.spawn_id(actorNumber=1, location=[-5.5, 0, 0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    x = hQbot2e1.destroy()
    vr.PrintWS(x == 1, "Spawn and destroy existing qbot (expect return 1)")

    hQbot2e1.actorNumber=1
    x = hQbot2e1.destroy()
    vr.PrintWS(x == 0, "Destroy qbot that doesn't exist (expect return 0)")

    hQbot2e2 = QLabsQBot2e(qlabs)
    x = hQbot2e2.spawn_id_degrees(actorNumber=2, location=[-6, 0, 0], rotation=[0,0,180], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn qbot with degrees")

    x, loc, rot, scale = hQbot2e2.get_world_transform()
    vr.PrintWS(abs(np.sum(np.subtract(loc, [-6, 0, 0]))) < 0.001 and x == True, "Get world transform")
    print(hQbot2e2.get_world_transform())

    x = hQbot2e2.ping()
    vr.PrintWS(x == True, "Ping existing qbot (expect True)")

    hQbot2e1.actorNumber=1
    x = hQbot2e1.ping()
    vr.PrintWS(x == False, "Ping qbot that doesn't exist (expect False)")

    hQbot2e0.command_and_request_state(rightWheelSpeed = 1, leftWheelSpeed = 1)
    time.sleep(1)


    print("\n\n------------------------------ Qbot3 --------------------------------\n")
    vr.PrintWSHeader("Qbot3")

    hQbot3Camera = QLabsFreeCamera(qlabs, True)
    hQbot3Camera.spawn_id_degrees(actorNumber=10, location=[-7.5, 2, 2], rotation=[0, 40, -90])
    x = hQbot3Camera.possess()

    hQbot3_0 = QLabsQBot3(qlabs)
    x = hQbot3_0.spawn_id(actorNumber = 0, location=[-7, 0, 0], rotation=[0, 0, math.pi], scale=[1, 1, 1], configuration=0, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn qbot with radians")

    x = hQbot3_0.spawn_id(actorNumber=0, location=[-7.5, 0, 0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    vr.PrintWS(x == 2, "Spawn qbot with duplicate ID (return code 2)")

    hQbot3_1 = QLabsQBot3(qlabs)
    hQbot3_1.spawn_id(actorNumber=1, location=[-7.5, 0, 0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    x = hQbot3_1.destroy()
    vr.PrintWS(x == 1, "Spawn and destroy existing qbot (expect return 1)")

    hQbot3_1.actorNumber=1
    x = hQbot3_1.destroy()
    vr.PrintWS(x == 0, "Destroy qbot that doesn't exist (expect return 0)")

    hQbot3_2 = QLabsQBot3(qlabs)
    x = hQbot3_2.spawn_id_degrees(actorNumber=2, location=[-8, 0, 0], rotation=[0,0,180], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn qbot with degrees")

    x, loc, rot, scale = hQbot3_2.get_world_transform()
    vr.PrintWS(abs(np.sum(np.subtract(loc, [-8, 0, 0]))) < 0.001 and x == True, "Get world transform")
    print(hQbot3_2.get_world_transform())

    x = hQbot3_2.ping()
    vr.PrintWS(x == True, "Ping existing qbot (expect True)")

    hQbot3_1.actorNumber=1
    x = hQbot3_1.ping()
    vr.PrintWS(x == False, "Ping qbot that doesn't exist (expect False)")

    hQbot3_0.command_and_request_state(rightWheelSpeed = 1, leftWheelSpeed = 1)
    time.sleep(1)


    print("\n\n------------------------------ QBot Platform --------------------------------\n")
    vr.PrintWSHeader("QBot Platform")

    hQbotPFCamera = QLabsFreeCamera(qlabs, True)
    hQbotPFCamera.spawn_id_degrees(actorNumber=11, location=[-9.5, 2, 2], rotation=[0, 40, -90])
    x = hQbotPFCamera.possess()

    hQbotPF0 = QLabsQBotPlatform(qlabs)
    x = hQbotPF0.spawn_id(actorNumber = 0, location=[-9, 0, 0], rotation=[0, 0, math.pi], scale=[1, 1, 1], configuration=0, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn qbot with radians")

    x = hQbotPF0.spawn_id(actorNumber=0, location=[-9.5, 0, 0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    vr.PrintWS(x == 2, "Spawn qbot with duplicate ID (return code 2)")

    hQbotPF1 = QLabsQBotPlatform(qlabs)
    hQbotPF1.spawn_id(actorNumber=1, location=[-9.5, 0, 0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    x = hQbotPF1.destroy()
    vr.PrintWS(x == 1, "Spawn and destroy existing qbot (expect return 1)")

    hQbotPF1.actorNumber=1
    x = hQbotPF1.destroy()
    vr.PrintWS(x == 0, "Destroy qbot that doesn't exist (expect return 0)")

    hQbotPF2 = QLabsQBotPlatform(qlabs)
    x = hQbotPF2.spawn_id_degrees(actorNumber=2, location=[-10, 0, 0], rotation=[0,0,180], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn qbot with degrees")

    x, loc, rot, scale = hQbotPF2.get_world_transform()
    vr.PrintWS(abs(np.sum(np.subtract(loc, [-10, 0, 0]))) < 0.001 and x == True, "Get world transform")
    print(hQbotPF2.get_world_transform())

    x = hQbotPF2.ping()
    vr.PrintWS(x == True, "Ping existing qbot (expect True)")

    hQbotPF1.actorNumber=1
    x = hQbotPF1.ping()
    vr.PrintWS(x == False, "Ping qbot that doesn't exist (expect False)")

    hQbotPF0.command_and_request_state(rightWheelSpeed = 1, leftWheelSpeed = 1)
    time.sleep(1)


    print("\n\n------------------------------ Walls --------------------------------\n")
    vr.PrintWSHeader("Walls")

    wallCamera = QLabsFreeCamera(qlabs, True)
    wallCamera.spawn_id_degrees(actorNumber=12, location=[-9.5, 2, 2], rotation=[0, 40, -90])
    x = wallCamera.possess()

    hWall0 = QLabsWalls(qlabs)
    x = hWall0.spawn_id(actorNumber = 0, location=[-9, 0, 0], rotation=[0, 0, math.pi], scale=[1, 1, 1], configuration=0, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn wall with radians")

    x = hWall0.spawn_id(actorNumber=0, location=[-9.5, 0, 0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    vr.PrintWS(x == 2, "Spawn wall with duplicate ID (return code 2)")

    hWall1 = QLabsWalls(qlabs)
    hWall1.spawn_id(actorNumber=1, location=[-9.5, 0, 0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    x = hWall1.destroy()
    vr.PrintWS(x == 1, "Spawn and destroy existing wall (expect return 1)")

    hWall1.actorNumber=1
    x = hWall1.destroy()
    vr.PrintWS(x == 0, "Destroy wall that doesn't exist (expect return 0)")

    hWall2 = QLabsWalls(qlabs)
    x = hWall2.spawn_id_degrees(actorNumber=2, location=[-10, 0, 0], rotation=[0,0,180], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn wall with degrees")

    x, loc, rot, scale = hWall2.get_world_transform()
    vr.PrintWS(abs(np.sum(np.subtract(loc, [-10, 0, 0]))) < 0.001 and x == True, "Get world transform")
    print(hWall2.get_world_transform())

    x = hWall2.ping()
    vr.PrintWS(x == True, "Ping existing wall (expect True)")

    hWall1.actorNumber=1
    x = hWall1.ping()
    vr.PrintWS(x == False, "Ping wall that doesn't exist (expect False)")

    hWall2.set_enable_dynamics(enableDynamics = True)
    print("Wall dynamics enabled")

    time.sleep(5)

    hWall2.set_transform_degrees(location=[-10, 3, 0], rotation=[0, 0, 0], scale=[1,1,1])

    print("\n\n------------------------------ Reference Frame --------------------------------\n")
    vr.PrintWSHeader("Reference Frame")

    frameCamera = QLabsFreeCamera(qlabs, True)
    frameCamera.spawn_id_degrees(actorNumber=13, location=[-12, 2, 2], rotation=[0, 40, -90])
    x = frameCamera.possess()

    hFrame0 = QLabsReferenceFrame(qlabs)
    x = hFrame0.spawn_id(actorNumber = 0, location = [-12, 2, 0], rotation = [0, 0, 0], scale = [1, 1, 1], configuration=0, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn invisible frame with radians")
    
    hFrame1 = QLabsReferenceFrame(qlabs)
    x = hFrame1.spawn_id(actorNumber = 1, location = [-12, 0, 0], rotation = [0, 0, 0], scale = [1, 1, 1], configuration=1, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn frame with radians")

    hFrame2 = QLabsReferenceFrame(qlabs)
    x = hFrame2.spawn_id(actorNumber = 2, location = [-12, -2, 0], rotation = [0, 0, 0], scale = [1, 1, 1], configuration=2, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn second frame with radians")

    x = hFrame0.spawn_id(actorNumber=0, location=[-12, 2, 0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    vr.PrintWS(x == 2, "Spawn frame with duplicate ID (return code 2)")

    hFrame3 = QLabsReferenceFrame(qlabs)
    hFrame3.spawn_id(actorNumber=3, location=[-13, 0, 0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    x = hFrame3.destroy()
    vr.PrintWS(x == 1, "Spawn and destroy existing frame (expect return 1)")

    hFrame1.actorNumber=4
    x = hFrame1.destroy()
    vr.PrintWS(x == 0, "Destroy frame that doesn't exist (expect return 0)")

    hFrame4 = QLabsReferenceFrame(qlabs)
    hFrame4.spawn_id_degrees(actorNumber = 5, location = [-13, 0, 0], rotation = [0,0,0], scale = [1,1,1], configuration=1)
    vr.PrintWS(x == 0, "Spawn frame with degrees")

    x, loc, rot, scale = hFrame0.get_world_transform()
    vr.PrintWS(abs(np.sum(np.subtract(loc, [-12, 2, 0]))) < 0.001 and x == True, "Get world transform")
    print(hFrame0.get_world_transform())

    # Custom functions:

    time.sleep(1)
    hFrame4.set_transform_degrees(location = [-13, -2, 0], rotation = [0,0,0], scale = [1,4,1])

    time.sleep(0.5)

    hFrame4.set_icon_scale(scale = [2,2,2])


    print("\n\n------------------------------ Shredder --------------------------------\n")
    vr.PrintWSHeader("Shredder")

    shredderCamera = QLabsFreeCamera(qlabs, True)
    shredderCamera.spawn_id_degrees(actorNumber=14, location=[4, 2, 2], rotation=[0, 40, -90])
    x = shredderCamera.possess()

    hShredder0 = QLabsShredder(qlabs)
    x = hShredder0.spawn_id(actorNumber = 0, location = [3, 0, 0], rotation = [0, 0, 0], scale = [1,1,1], configuration=0)
    vr.PrintWS(x == 0, "Spawn shredder in configuration 0 with radians")

    hShredder1 = QLabsShredder(qlabs)
    x = hShredder1.spawn_id(actorNumber = 1, location = [4, 0, 0], rotation = [0, 0, 0], scale = [3,3,3], configuration=1)
    vr.PrintWS(x == 0, "Spawn shredder in configuration 1 with radians")

    hShredder2 = QLabsShredder(qlabs)
    x = hShredder2.spawn_id(actorNumber = 2, location = [5, 0, 0], rotation = [0, 0, 0], scale = [2,2,2], configuration=2)
    vr.PrintWS(x == 0, "Spawn shredder in configuration 2 with radians")

    hShredder3 = QLabsShredder(qlabs)
    x = hShredder3.spawn_id(actorNumber = 3, location = [6, 0, 0], rotation = [0, 0, 0], scale = [2,0.5,0.5], configuration=3)
    vr.PrintWS(x == 0, "Spawn shredder in configuration 3 with radians")

    hShredder4 = QLabsShredder(qlabs)
    hShredder4.spawn_id(actorNumber=4, location=[6, 0, 0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    x = hShredder4.destroy()
    vr.PrintWS(x == 1, "Spawn and destroy existing shredder (expect return 1)")

    hShredder1.actorNumber=5
    x = hShredder1.destroy()
    vr.PrintWS(x == 0, "Destroy shredder that doesn't exist (expect return 0)")

    hShredder5 = QLabsShredder(qlabs)
    hShredder5.spawn_id_degrees(actorNumber = 6, location = [3, -2, 0], rotation = [0,0,0], scale = [10,10,10], configuration=2)
    vr.PrintWS(x == 0, "Spawn shredder with degrees")

    x, loc, rot, scale = hShredder5.get_world_transform()
    vr.PrintWS(abs(np.sum(np.subtract(loc, [3, -2, 0]))) < 0.001 and x == True, "Get world transform")
    print(hShredder5.get_world_transform())

    for i in range(0, 50):
        sacrificialCube = QLabsWidget(qlabs)
        sacrificialCube.spawn_degrees(location = [3, -2, 4], rotation = [0,0,0], scale = [1,1,1], configuration = 4, color=[0,1,1])

    for i in range(0, 500):
        sacrificialCube = QLabsWidget(qlabs)
        sacrificialCube.spawn_degrees(location = [3, -2, 4+(i*0.1)], rotation = [0,0,0], scale = [1,1,1], configuration = 4, color=[0,1,1])

    time.sleep(0.2)

    # Shredder currently has NO internal functions for setting transform


    print("\n\n------------------------------ Delivery Tube --------------------------------\n")
    vr.PrintWSHeader("Delivery Tube")

    tubeCamera = QLabsFreeCamera(qlabs, True)
    tubeCamera.spawn_id_degrees(actorNumber=15, location=[8, 1.5, 2.5], rotation=[0, 10, -90])
    x = tubeCamera.possess()

    hTube0 = QLabsDeliveryTube(qlabs)
    x = hTube0.spawn_id(actorNumber = 0, location = [7, 0, 0], scale = [1,1,1])
    vr.PrintWS(x == 0, "Spawn delivery tube with radians")
    hTube0.set_height(height = 2)

    hTube1 = QLabsDeliveryTubeBottles(qlabs)
    x = hTube1.spawn_id(actorNumber = 0, location = [8, 0, 2], scale = [1,1,1])
    vr.PrintWS(x == 0, "Spawn delivery tube bottles with radians")
    hTube1.set_height(height = 2)

    hTube2 = QLabsDeliveryTube(qlabs)
    x = hTube2.spawn_id_degrees(actorNumber = 1, location = [9, 0, 0], scale = [1,1,1])
    vr.PrintWS(x == 0, "Spawn delivery tube with degrees")
    hTube2.set_height(height = 2)

    #Custom Funcitons

    hTube0.spawn_block(blockType = hTube0.BLOCK_CUBE, mass = 10, yawRotation = 0, color = [1,0,0])

    hTube1.spawn_container(metallic = False, color = [1,0,0], mass = 10, height = 0.1, diameter = 0.65, roughness = 0.65)

    hTube2.spawn_block(blockType = hTube2.BLOCK_GEOSPHERE, mass = 10, yawRotation = 0, color = [1,0,0])

    time.sleep(2)


    print("\n\n------------------------------ QArm --------------------------------\n")
    vr.PrintWSHeader("QArm")

    qArmCamera = QLabsFreeCamera(qlabs, True)
    qArmCamera.spawn_id_degrees(actorNumber=16, location=[12, 2, 2], rotation=[0, 40, -90])
    x = qArmCamera.possess()

    hQArm0 = QLabsQArm(qlabs)
    x = hQArm0.spawn_id(actorNumber = 0, location = [11, 0, 0], rotation = [0, 0, 0], scale = [1,1,1], configuration=0)
    vr.PrintWS(x == 0, "Spawn QArm with radians")

    x = hQArm0.spawn_id(actorNumber=0, location=[11, 0, 0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    vr.PrintWS(x == 2, "Spawn QArm with duplicate ID (return code 2)")

    hQArm1 = QLabsQArm(qlabs)
    hQArm1.spawn_id(actorNumber=1, location=[12, 0, 0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    x = hQArm1.destroy()
    vr.PrintWS(x == 1, "Spawn and destroy existing QArm (expect return 1)")

    hQArm1.actorNumber=2
    x = hQArm1.destroy()
    vr.PrintWS(x == 0, "Destroy QArm that doesn't exist (expect return 0)")

    hQArm3 = QLabsQArm(qlabs)
    x = hQArm3.spawn_id_degrees(actorNumber=3, location=[12, 0, 0], rotation=[0,0,180], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    vr.PrintWS(x == 0, "Spawn QArm with degrees")

    x, loc, rot, scale = hQArm3.get_world_transform()
    vr.PrintWS(abs(np.sum(np.subtract(loc, [12, 0, 0]))) < 0.001 and x == True, "Get world transform")
    print(hQArm3.get_world_transform())

    x = hQArm3.ping()
    vr.PrintWS(x == True, "Ping existing QArm (expect True)")

    hWall1.actorNumber=4
    x = hWall1.ping()
    vr.PrintWS(x == False, "Ping QArm that doesn't exist (expect False)")


    print("\n\n------------------------------ Conveyor Curved --------------------------------\n")
    vr.PrintWSHeader("Conveyor Curved")

    conveyorCurvedCam = QLabsFreeCamera(qlabs, True)
    conveyorCurvedCam.spawn_id_degrees(actorNumber=17, location=[16, 2, 2], rotation=[0, 40, -90])
    x = conveyorCurvedCam.possess()

    hBeltCurve0 = QLabsConveyorCurved(qlabs)
    x = hBeltCurve0.spawn_id(actorNumber=0, location = [15, 0, 0], rotation = [0, 0, 0], scale = [1,1,1])
    vr.PrintWS(x == 0, "Spawn conveyor with radians")

    conveyorPoint = QLabsReferenceFrame(qlabs)
    conveyorPoint.spawn_id(actorNumber = 20, location = [16, 0, 0], rotation = [0,0,0], scale = [1,1,1], configuration = 0)
    
    for i in range (0, 12):
        hBeltCurve1 = QLabsConveyorCurved(qlabs)
        hBeltCurve1.spawn_id_and_parent_with_relative_transform_degrees(actorNumber = 1+i, location = [0,0,0], rotation = [0,0,i*30], scale = [2,2,2], configuration=0, parentClassID = conveyorPoint.classID, parentActorNumber = 20, parentComponent=0)
        hBeltCurve1.set_speed(7)
        
        x, loc, rot, scale = hBeltCurve1.get_world_transform()
        
        print("Conveyor Spawned")

    hCubeTube = QLabsDeliveryTubeBottles(qlabs)
    hCubeTube.spawn(location = [loc[0]-1, loc[1]+0.2, loc[2]+1], rotation = [0,0,0], scale = [1,1,1])
    hCubeTube.set_height(height = 10)

    for i in range (0, 5):
        hCubeTube.spawn_container(metallic = False, color = [0,1,0], mass = 10, height = 0.1, diameter = 0.65, roughness = 0.65)
        time.sleep(0.5)
    

    # Single section conveyor

    conveyorCurvedCam2 = QLabsFreeCamera(qlabs, True)
    conveyorCurvedCam2.spawn_id_degrees(actorNumber=18, location=[19, 2, 2], rotation=[0, 40, -90])
    x = conveyorCurvedCam2.possess()

    hBeltCurve2 = QLabsConveyorCurved(qlabs)
    x = hBeltCurve2.spawn_id_degrees(actorNumber = 20, location = [19, 0, 0], rotation = [0,0,0], scale = [1,1,1], configuration = 12)
    vr.PrintWS(x == 0, "Spawn Q-belt with degrees and 12 sections (configurations)")



    print("\n\n------------------------------ Conveyor Straight --------------------------------\n")
    vr.PrintWSHeader("Conveyor Straight")

    conveyorStraightCam = QLabsFreeCamera(qlabs, True)
    conveyorStraightCam.spawn_id_degrees(actorNumber=19, location=[21, 2.5, 2], rotation=[0, 40, -90])
    x = conveyorStraightCam.possess()

    hBeltS0 = QLabsConveyorStraight(qlabs)
    x = hBeltS0.spawn_id(actorNumber=0, location = [22, 0, 0], rotation = [0, 0, 0], scale = [1,1,1])
    vr.PrintWS(x == 0, "Spawn conveyor with radians")

    hBeltS1 = QLabsConveyorStraight(qlabs)
    x = hBeltS1.spawn_id_degrees(actorNumber=1, location = [20, 0, 0], rotation = [0, 0, 0], scale = [2,2,2])
    vr.PrintWS(x == 0, "Spawn conveyor with degrees & at a larger scale")

    time.sleep(0.5)
    hBeltS1.set_speed(0.1)

    time.sleep(2)
    hBeltS1.set_speed(0.5)

    conveyorLength = 3

    hBeltS2 = QLabsConveyorStraight(qlabs)
    x = hBeltS2.spawn_id_degrees(actorNumber=2, location = [20, 1, 0], rotation = [0, 0, 0], scale = [2,2,2], configuration = conveyorLength)
    vr.PrintWS(x == 0, "Spawn conveyor with degrees & with multipule sections")

    hCubeTube1 = QLabsDeliveryTubeBottles(qlabs)
    hCubeTube1.spawn(location = [conveyorLength + 19.3, 1, 0.5], rotation = [0,0,0], scale = [1,1,1])
    hCubeTube1.set_height(height = 10)

    #Spawn bottles on conveyor at different speeds

    time.sleep(0.5)
    hBeltS2.set_speed(0.5)
    for i in range (0, 4):
        hCubeTube1.spawn_container(metallic = False, color = [1,0.5,0], mass = 10, height = 0.1, diameter = 0.65, roughness = 0.65)
        print("Bottle Spawned")
        time.sleep(0.5)

    time.sleep(0.5)
    hBeltS2.set_speed(1)
    for i in range (0, 4):
        hCubeTube1.spawn_container(metallic = False, color = [1,0.5,0], mass = 10, height = 0.1, diameter = 0.65, roughness = 0.65)
        print("Bottle Spawned")
        time.sleep(0.5)

    time.sleep(0.5)
    hBeltS2.set_speed(2)
    for i in range (0, 4):
        hCubeTube1.spawn_container(metallic = False, color = [1,0.5,0], mass = 10, height = 0.1, diameter = 0.65, roughness = 0.65)
        print("Bottle Spawned")
        time.sleep(0.5)

    time.sleep(0.5)
    hBeltS2.set_speed(10)
    for i in range (0, 4):
        hCubeTube1.spawn_container(metallic = False, color = [1,0.5,0], mass = 10, height = 0.1, diameter = 0.65, roughness = 0.65)
        print("Bottle Spawned")
        time.sleep(0.5)

    time.sleep(0.5)
    hBeltS2.set_speed(100)
    for i in range (0, 4):
        hCubeTube1.spawn_container(metallic = False, color = [1,0.5,0], mass = 10, height = 0.1, diameter = 0.65, roughness = 0.65)
        print("Bottle Spawned")
        time.sleep(0.5)

    print("\n\n------------------------------ Both Conveyors --------------------------------\n")

    conveyorCurvedCam2.possess()

    hBeltBoth0 = QLabsConveyorStraight(qlabs)
    hBeltBoth0.spawn_id_degrees(actorNumber = 3, location = [18.5,0,0], rotation = [0,0,-90], scale = [1,1,1], configuration = 10)

    hBeltBoth1 = QLabsConveyorStraight(qlabs)
    hBeltBoth1.spawn_id_degrees(actorNumber = 4, location = [19.5,0,0], rotation = [0,0,-90], scale = [1,1,1], configuration = 10)

    hBeltBoth2 = QLabsConveyorCurved(qlabs)
    x = hBeltBoth2.spawn_id_degrees(actorNumber = 21, location = [19, -3, 0], rotation = [0,0,-180], scale = [1,1,1], configuration = 12)

    def loopSpeed(QBspeed=0):
        hBeltBoth0.set_speed(QBspeed*-1)
        hBeltBoth1.set_speed(QBspeed)
        hBeltBoth2.set_speed(QBspeed)
        hBeltCurve2.set_speed(QBspeed)
    def spawnBottleBC(quantity = 4):
        for i in range (0, quantity):
            hCubeTube2.spawn_container(metallic = False, color = [1,0,1], mass = 10, height = 0.1, diameter = 0.65, roughness = 0.65)
            print("Bottle Spawned")
            time.sleep(0.5)

    hCubeTube2 = QLabsDeliveryTubeBottles(qlabs)
    hCubeTube2.spawn(location = [19, 0.5, 0.5], rotation = [0,0,0], scale = [1,1,1])
    hCubeTube2.set_height(height = 10)

    time.sleep(0.5)
    loopSpeed(0.1)
    spawnBottleBC()

    time.sleep(1)
    loopSpeed(0.5)
    spawnBottleBC()

    time.sleep(0.5)
    loopSpeed(1)
    spawnBottleBC()

    time.sleep(2)
    loopSpeed(2)
    spawnBottleBC()

    time.sleep(0.5)
    loopSpeed(-1)
    spawnBottleBC()

    time.sleep(2)
    

    print("\n\n------------------------------ Flooring --------------------------------\n")
    vr.PrintWSHeader("Flooring")

    floorCam0 = QLabsFreeCamera(qlabs, True)
    floorCam0.spawn_id_degrees(actorNumber=20, location=[19, 7, 2], rotation=[0, 40, -90])
    x = floorCam0.possess()

    hFloor0 = QLabsQBotPlatformFlooring(qlabs)
    x = hFloor0.spawn_id(actorNumber = 0, location = [19, 5, 0], rotation = [0,0,0], scale = [1,1,1], configuration = 0)
    vr.PrintWS(x == 0, "Spawn floor in configuration 0 with radians")

    time.sleep(0.2)

    floorCam1 = QLabsFreeCamera(qlabs, True)
    floorCam1.spawn_id_degrees(actorNumber=21, location=[14, 7, 2], rotation=[0, 40, -90])
    x = floorCam1.possess()

    #hFloor0 = QLabsQBotPlatformFlooring(qlabs)
    #x = hFloor0.spawn_id_degrees(actorNumber = 1, location = [14, 5, 0], rotation = [0,0,0], scale = [1,1,1], configuration = 1)
    #vr.PrintWS(x == 0, "Spawn floor in configuration 1 with degrees")

    floorCam2 = QLabsFreeCamera(qlabs, True)
    floorCam2.spawn_id_degrees(actorNumber=22, location=[10, 7, 2], rotation=[0, 40, -90])
    x = floorCam2.possess()


    #Modular flooring
    x = hFloor0.spawn_id_degrees(actorNumber = 2, location = [10, 5, 0], rotation = [0,0,0], scale = [1,1,1], configuration = 2)
    vr.PrintWS(x == 0, "Spawn floor in configuration 2 with degrees")

    x = hFloor0.spawn_id_degrees(actorNumber = 3, location = [10, 6.2, 0], rotation = [0,0,0], scale = [1,1,1], configuration = 3)
    vr.PrintWS(x == 0, "Spawn floor in configuration 3 with degrees")

    x = hFloor0.spawn_id_degrees(actorNumber = 4, location = [10, 3.8, 0], rotation = [0,0,0], scale = [1,1,1], configuration = 4)
    vr.PrintWS(x == 0, "Spawn floor in configuration 4 with degrees")

    x = hFloor0.spawn_id_degrees(actorNumber = 5, location = [11.2, 5, 0], rotation = [0,0,0], scale = [1,1,1], configuration = 5)
    vr.PrintWS(x == 0, "Spawn floor in configuration 5 with degrees")

    x = hFloor0.spawn_id_degrees(actorNumber = 6, location = [12.4, 5, 0], rotation = [0,0,0], scale = [1,1,1], configuration = 6)
    vr.PrintWS(x == 0, "Spawn floor in configuration 6 with degrees")

    x = hFloor0.spawn_id_degrees(actorNumber = 7, location = [8.8, 5, 0], rotation = [0,0,0], scale = [1,1,1], configuration = 7)
    vr.PrintWS(x == 0, "Spawn floor in configuration 7 with degrees")

 
vr = verificationReport('QBot Validation Report.xlsx', 'library_verification_qbot.py', library_path)
vr.ignore_list = ignore_list

main()

vr.WriteFileBuffer()