# Note use this method to get your qvl libraries to ensure you're using the latest version
# in GitHub. It is inserted first in the list to take precedence over all other libraries
# in your python path.
import sys
sys.path.insert(0, "../")


from qvl.qlabs import QuanserInteractiveLabs
from qvl.free_camera import QLabsFreeCamera
from qvl.qbot_platform import QLabsQBotPlatform
from qvl.spline_line import QLabsSplineLine

from qvl.animal import QLabsAnimal

import sys
import time
import math
import struct
import numpy as np
import cv2
import keyboard


########### Main program #################


def main():

    tank_drive = False

    qlabs = QuanserInteractiveLabs()

    print("Connecting to QLabs...")
    try:
        qlabs.open("localhost")
    except:
        print("Unable to connect to QLabs")
        return

    print("Connected")

    # destroy the previous QBot and respawn it in a starting position

    qlabs.destroy_all_spawned_actors()


    hQBot = QLabsQBotPlatform(qlabs)
    hQBot.spawn_id_degrees(actorNumber=0, location=[0, 0, 2], rotation=[0,0,0], scale=[1,1,1], configuration=0)
    hQBot.possess(hQBot.VIEWPOINT_TRAILING)

    hSpline = QLabsSplineLine(qlabs)
    hSpline.spawn(location=[0.073, -2.743, 0], rotation=[0, 0, 0], scale=[1, 1, 1], configuration=0, waitForConfirmation=True)

    point_list = [[6.49, -3.596, 0, 0.02],
                  [7.007, 0.345, 0, 0.02]]

    hSpline.set_points([1, 0, 1], point_list, alignEndPointTangents=False, waitForConfirmation=True)


    location_x = 0
    location_y = 0
    rotation_z = 0

    speed = 0

    cv2.startWindowThread()
    cv2.namedWindow('image_stream', cv2.WINDOW_AUTOSIZE)
    image_RGBD = cv2.imread('Quanser640x480.jpg')
    cv2.imshow('image_stream', image_RGBD)

    done = False
    counter = 0

    # -------- Main Program Loop -----------
    while not done:


        status, image_RGBD = hQBot.get_image(hQBot.CAMERA_RGB)
        print(status)

        if status == True:

            if (tank_drive):
                image_RGBD = cv2.putText(img = image_RGBD, text = "QA, ED for tank-control driving", org = (0, 30), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 0.5, color = (255, 255, 255), thickness = 1)
            else:
                image_RGBD = cv2.putText(img = image_RGBD, text = "WASD for steering-control driving", org = (0, 30), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 0.5, color = (255, 255, 255), thickness = 1)
            
            image_RGBD = cv2.putText(img = image_RGBD, text = "ESC to exit", org = (0, 45), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 0.5, color = (255, 255, 255), thickness = 1)

            cv2.imshow('image_stream', image_RGBD)
            cv2.waitKey(1)

        if (tank_drive):
            speedScale = 1
            leftWheelSpeed = 0
            rightWheelSpeed = 0

            if (keyboard.is_pressed('Q')):
                leftWheelSpeed = leftWheelSpeed + speedScale

            if (keyboard.is_pressed('A')):
                leftWheelSpeed = leftWheelSpeed - speedScale

            if (keyboard.is_pressed('E')):
                rightWheelSpeed = rightWheelSpeed + speedScale

            if (keyboard.is_pressed('D')):
                rightWheelSpeed = rightWheelSpeed - speedScale

        else:
            speedScale = 1
            leftWheelSpeed = 0
            rightWheelSpeed = 0

            if (keyboard.is_pressed('W')):
                leftWheelSpeed = leftWheelSpeed + speedScale
                rightWheelSpeed = rightWheelSpeed + speedScale

            if (keyboard.is_pressed('S')):
                leftWheelSpeed = leftWheelSpeed - speedScale
                rightWheelSpeed = rightWheelSpeed - speedScale

            if (keyboard.is_pressed('D')):
                leftWheelSpeed = leftWheelSpeed + 0.5*speedScale
                rightWheelSpeed = rightWheelSpeed - 0.5*speedScale

            if (keyboard.is_pressed('A')):
                leftWheelSpeed = leftWheelSpeed - 0.5*speedScale
                rightWheelSpeed = rightWheelSpeed + 0.5*speedScale


        if (keyboard.is_pressed('Esc')):
            done = True

        print('{}, {}'.format(rightWheelSpeed, leftWheelSpeed))

        c = hQBot.command_and_request_state(rightWheelSpeed, leftWheelSpeed)
        if c == False:
            done = True


    cv2.destroyAllWindows()
    qlabs.close()
    print("Done!")

main()