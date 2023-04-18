# Note use this method to get your qvl libraries to ensure you're using the latest version
# in GitHub. It is inserted first in the list to take precendence over all other libraries
# in your python path.
import sys
sys.path.insert(0, "../")


from qvl.qlabs import QuanserInteractiveLabs
from qvl.free_camera import QLabsFreeCamera
from qvl.qbot_platform import QLabsQBotPlatform

import sys
import time
import math
import struct
import numpy as np
import cv2
import keyboard


########### Main program #################


def main():
    qlabs = QuanserInteractiveLabs()

    print("Connecting to QLabs...")
    try:
        qlabs.open("localhost")
    except:
        print("Unable to connect to QLabs")
        return

    print("Connected")

    # destroy the previous QBot and respawn it in a starting position

    hQBot = QLabsQBotPlatform(qlabs)
    hQBot.actorNumber=0
    hQBot.destroy()
    hQBot.spawn_id_degrees(actorNumber=0, location=[0.073, -2.743, 0], rotation=[0,0,90], scale=[1,1,1], configuration=0)
    hQBot.possess(hQBot.VIEWPOINT_TRAILING)

    

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


        status, image_RGBD = hQBot.get_image_rgb()

        if status == True:

            image_RGBD = cv2.putText(img = image_RGBD, text = "QA, ED for tank-control driving", org = (0, 30), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 0.5, color = (255, 255, 255), thickness = 1)
            image_RGBD = cv2.putText(img = image_RGBD, text = "ESC to exit", org = (0, 45), fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 0.5, color = (255, 255, 255), thickness = 1)

            cv2.imshow('image_stream', image_RGBD)
            cv2.waitKey(1)

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