import sys
library_path = '../libraries'
sys.path.append(library_path)

from library_qlabs import QuanserInteractiveLabs
from library_qlabs_free_camera import QLabsFreeCamera
from library_qlabs_basic_shape import QLabsBasicShape
from library_qlabs_widget import QLabsWidget
from library_qlabs_qbot3 import QLabsQBot3
from library_qlabs_system import QLabsSystem
from library_qlabs_spline_line import QLabsSplineLine
from library_qlabs_real_time import QLabsRealTime


import sys
import time
import math
import struct
import numpy as np
import cv2
import xlsxwriter
import os


class simpleAI():

    hQBot3 = None
    actorNumber = -1
    state = 0
    turn_time = 0

    def __init__(self, qlabs, actorNumber, start_location):
        self.hQBot3 = QLabsQBot3(qlabs)
        self.hQBot3.spawn_id_degrees(actorNumber, location=start_location, rotation=[0,0,90], scale=[1,1,1], configuration=0)

    def update(self):
        if (self.state == 0):

            [success, location, forward, up, frontHit, leftHit, rightHit, gyro, heading, encoderLeft, encoderRight] = self.hQBot3.command_and_request_state(rightWheelSpeed = 1, leftWheelSpeed = 1)

            if rightHit or frontHit:
                self.state = 1
                self.turn_time = time.time()
            elif leftHit:
                self.state = 3
                self.turn_time = time.time()

        elif (self.state == 1):

            [success, location, forward, up, frontHit, leftHit, rightHit, gyro, heading, encoderLeft, encoderRight] = self.hQBot3.command_and_request_state(rightWheelSpeed = -1, leftWheelSpeed = -1)

            if time.time() - self.turn_time > 0.5:
                self.state = 2
                self.turn_time = time.time()

        elif (self.state == 2):

            [success, location, forward, up, frontHit, leftHit, rightHit, gyro, heading, encoderLeft, encoderRight] = self.hQBot3.command_and_request_state(rightWheelSpeed = 0.5, leftWheelSpeed = -0.5)

            if time.time() - self.turn_time > 0.5:
                self.state = 0


        elif (self.state == 3):

            [success, location, forward, up, frontHit, leftHit, rightHit, gyro, heading, encoderLeft, encoderRight] = self.hQBot3.command_and_request_state(rightWheelSpeed = -1, leftWheelSpeed = -1)

            if time.time() - self.turn_time > 0.5:
                self.state = 4
                self.turn_time = time.time()

        elif (self.state == 4):
            [success, location, forward, up, frontHit, leftHit, rightHit, gyro, heading, encoderLeft, encoderRight] = self.hQBot3.command_and_request_state(rightWheelSpeed = -0.5, leftWheelSpeed = 0.5)

            if time.time() - self.turn_time > 0.5:
                self.state = 0

    def stop(self):
        [success, location, forward, up, frontHit, leftHit, rightHit, gyro, heading, encoderLeft, encoderRight] = self.hQBot3.command_and_request_state(rightWheelSpeed = 0, leftWheelSpeed = 0)
        
  
def main():
    os.system('cls')
    
    qlabs = QuanserInteractiveLabs()
    

    print("Connecting to QLabs...")
    try:
        qlabs.open("localhost")
    except:
        print("Unable to connect to QLabs")
        return
    
    print("Connected")
    
    # This can be removed if you don't want to remove existing actors.
    qlabs.destroy_all_spawned_actors()
    
    hCamera = QLabsFreeCamera(qlabs)
    hCamera.spawn([4.596, -3.489, 2.375], [0, 0.402, 2.461])
    hCamera.possess()

    time.sleep(2)

    QBotArmy = []

    for count in range(25):
        QBotArmy.append(simpleAI(qlabs, count, [(count % 5) - 2, -math.floor(count/5)+1,0]))

    # Now you can implement any drive routine you want
    start_time = time.time()
    current_time = start_time

    while (current_time - start_time < 200):

        for QBot in QBotArmy:
            QBot.update()

        current_time = time.time()


    for QBot in QBotArmy:
        QBot.stop()
    

    qlabs.close()
    print("Done!")  
 

main()


