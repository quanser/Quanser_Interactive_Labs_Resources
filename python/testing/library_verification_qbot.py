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
from qvl.delivery_tube import QLabsDeliveryTube
from qvl.qarm import QLabsQArm
from qvl.conveyor_curved import QLabsConveyorCurved
from qvl.flooring import QLabsFlooring
from qvl.conveyor_straight import QLabsConveyorStraight
from qvl.free_camera import QLabsFreeCamera
from qvl.basic_shape import QLabsBasicShape

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
    vr.PrintWS(np.array_equal(loc, [-6, 0, 0]) and x == True, "Get world transform")
    print(hQbot2e2.get_world_transform())

    x = hQbot2e2.ping()
    vr.PrintWS(x == True, "Ping existing qbot (expect True)")

    hQbot2e1.actorNumber=1
    x = hQbot2e1.ping()
    vr.PrintWS(x == False, "Ping qbot that doesn't exist (expect False)")

    hQbot2e1.command_and_request_state(qlabs, actorNumber = 0, rightWheelSpeed = 1, leftWheelSpeed = 1)
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
    vr.PrintWS(np.array_equal(loc, [-8, 0, 0]) and x == True, "Get world transform")
    print(hQbot3_2.get_world_transform())

    x = hQbot3_2.ping()
    vr.PrintWS(x == True, "Ping existing qbot (expect True)")

    hQbot3_1.actorNumber=1
    x = hQbot3_1.ping()
    vr.PrintWS(x == False, "Ping qbot that doesn't exist (expect False)")

    hQbot3_0.command_and_request_state(rightWheelSpeed = 1, leftWheelSpeed = 1)
    time.sleep(1)


    print("\n\n------------------------------ QLabsQBotPlatform --------------------------------\n")
    vr.PrintWSHeader("QLabsQBotPlatform")

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

    x, loc, rot, scale = hQbot3_2.get_world_transform()
    vr.PrintWS(np.array_equal(loc, [-10, 0, 0]) and x == True, "Get world transform")
    print(hQbotPF2.get_world_transform())

    x = hQbotPF2.ping()
    vr.PrintWS(x == True, "Ping existing qbot (expect True)")

    hQbotPF1.actorNumber=1
    x = hQbotPF1.ping()
    vr.PrintWS(x == False, "Ping qbot that doesn't exist (expect False)")

    hQbotPF0.command_and_request_state(rightWheelSpeed = 1, leftWheelSpeed = 1)
    time.sleep(1)



vr = verificationReport('QBot Validation Report.xlsx', 'library_verification_qbot.py', library_path)
vr.ignore_list = ignore_list

main()

vr.WriteFileBuffer()