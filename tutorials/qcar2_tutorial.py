"""
QCar 2 Library Example
----------------------
This example will show you how to spawn cars, and use the qvl library commands
to control the car and its related functions.

.. note::

    Make sure you have Quanser Interactive Labs open before running this
    example.  This example is designed to best be run in QCar Cityscape.

"""

from qvl.qlabs import QuanserInteractiveLabs
from qvl.free_camera import QLabsFreeCamera
from qvl.basic_shape import QLabsBasicShape
from qvl.qcar2 import QLabsQCar2
from qvl.environment_outdoors import QLabsEnvironmentOutdoors

import time
import math
import numpy as np
import cv2
import os

import pyqtgraph as pg
from pyqtgraph.Qt import QtWidgets

from qvl.system import QLabsSystem



def main():
    os.system('cls')

    #Communications with qlabs

    qlabs = QuanserInteractiveLabs()
    cv2.startWindowThread()

    print("Connecting to QLabs...")
    try:
        qlabs.open("localhost")
    except:
        print("Unable to connect to QLabs")
        return

    print("Connected")

    qlabs.destroy_all_spawned_actors()

    # Use hSystem to set the tutorial title in the upper left of the qlabs window 
    hSystem = QLabsSystem(qlabs)
    hSystem.set_title_string('QCar Tutorial')

    ### QCar

    hCameraQCars = QLabsFreeCamera(qlabs)
    hCameraQCars.spawn_id(actorNumber=1, location=[-15.075, 26.703, 6.074], rotation=[0, 0.564, -1.586])
    hCameraQCars.possess()

    print("\n\n---QCar---")

    #spawning the QCar with radians
    hQCar0 = QLabsQCar(qlabs)
    hQCar0.spawn_id(actorNumber=0, location=[-8.700, 14.643, 0.005], rotation=[0,0,math.pi/2], waitForConfirmation=True)

    #Spawn and destroy the existing QCar
    hQCar1 = QLabsQCar2(qlabs)
    hQCar1.spawn_id(actorNumber=1, location=[-15.075, 26.703, 6.074], rotation=[0,0,math.pi/2], waitForConfirmation=True)
    hQCar1.destroy()

    #spawn a QCar with degrees
    hQCar2 = QLabsQCar(qlabs)
    x = hQCar2.spawn_id_degrees(actorNumber=2, location=[-11.048, 14.643, 0.005], rotation=[0,0,90], waitForConfirmation=True)

    #pinging the QCar
    hQCar2.ping()

    time.sleep(0.5)

    # Set the velocity and direction of the QCar in radians while also turning on the headlights and right turn signal
    hQCar2.set_velocity_and_request_state(forward=1, turn = -math.pi/6, headlights=True, leftTurnSignal=False, rightTurnSignal=True, brakeSignal=False, reverseSignal=False)
    time.sleep(1)
    # Set the velocity to 0 and direction of the QCar in radians while keeping the headlights on and right turn signal on
    hQCar2.set_velocity_and_request_state(forward=0.0, turn = -math.pi/6, headlights=True, leftTurnSignal=False, rightTurnSignal=True, brakeSignal=False, reverseSignal=False)
    # Set the velocity to 1 and direction of the QCar in degrees while keeping the headlights on and turning on the left turn signal
    hQCar2.set_velocity_and_request_state_degrees(forward=1, turn = 30, headlights=True, leftTurnSignal=True, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)
    time.sleep(1)
    # Set the velocity to 0 and direction of the QCar in degrees while keeping the headlights on and left turn signal on
    success, location, rotation, frontHit, rearHit = hQCar2.set_velocity_and_request_state_degrees(forward=0.0, turn = 30, headlights=True, leftTurnSignal=True, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)

    # Possess another QCar
    x = hQCar2.possess()

    time.sleep(0.1)
    # Set the velocity to 1 of the QCar in radians while keeping the headlights, brakeSignal and reverseSignal on
    hQCar2.set_velocity_and_request_state(forward=1, turn = 0, headlights=True, leftTurnSignal=True, rightTurnSignal=True, brakeSignal=True, reverseSignal=True)
    time.sleep(1)
    # Set the velocity to 0 while keeping the headlights, brakeSignal and reverseSignal on and turning on the left turn signal and right turn signal
    hQCar2.set_velocity_and_request_state(forward=0.0, turn = 0, headlights=True, leftTurnSignal=True, rightTurnSignal=True, brakeSignal=True, reverseSignal=True)

    # Turn all the lights off
    hQCar2.set_velocity_and_request_state(forward=0, turn = 0, headlights=False, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)

    # Car bumper test
    hCameraQCars.possess()
    # Change the camera view to see the bumper test
    hCameraQCars.set_transform(location=[-17.045, 32.589, 6.042], rotation=[0, 0.594, -1.568])

    # Spawn some shapes for our bumper test
    hCubeQCarBlocks = QLabsBasicShape(qlabs)
    hCubeQCarBlocks .spawn_id(100, [-11.919, 26.289, 0.5], [0,0,0], [1,1,1], configuration=hCubeQCarBlocks.SHAPE_CUBE, waitForConfirmation=True)
    hCubeQCarBlocks .spawn_id(101, [-19.919, 26.289, 0.5], [0,0,0], [1,1,1], configuration=hCubeQCarBlocks.SHAPE_CUBE, waitForConfirmation=True)

    # Create another QCar
    hQCar3 = QLabsQCar(qlabs)
    hQCar3.spawn_id(actorNumber=3, location=[-13.424, 26.299, 0.005], rotation=[0,0,math.pi])

    # Have the QCar drive forward to hit the front block
    for count in range(10):
        x, location, rotation, frontHit, rearHit  = hQCar3.set_velocity_and_request_state(forward=2, turn = 0, headlights=False, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)
        time.sleep(0.25)

    # Put the QCar in ghost mode
    hQCar3.ghost_mode()

    # Have the QCar drive backwards to hit the back bumper
    for count in range(10):
        x, location, rotation, frontHit, rearHit  = hQCar3.set_velocity_and_request_state(forward=-2, turn = 0, headlights=False, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)
        time.sleep(0.25)

    # Change the color of ghost mode to red
    hQCar3.ghost_mode(enable=True, color=[1,0,0])
    time.sleep(0.50)

    # Set the velocity to 0 and turn all lights off
    hQCar3.set_velocity_and_request_state(forward=0, turn = 0, headlights=False, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)

    # Set the location of the QCar and request the state of the car.  If x== True and frontHit==True then the front bumper hit the block correctly.
    x, location, rotation, forward_vector, up_vector, frontHit, rearHit = hQCar3.set_transform_and_request_state(location=[-16.1, 26.299, 0.005], rotation=[0,0,math.pi-0.01], enableDynamics=True, headlights=False, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)
    time.sleep(0.50)

    # Getting and saving the world transform of the QCar in Quanser Interactive Labs
    x, loc, rot, scale = hQCar3.get_world_transform()

    # Set the location of the QCar and request the state of the car.  If x== True and rearHit==True then the back bumper hit the block correctly.
    x, location, rotation, forward_vector, up_vector, frontHit, rearHit = hQCar3.set_transform_and_request_state_degrees(location=[-13.1, 26.299, 0.005], rotation=[0,0,179], enableDynamics=True, headlights=False, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)
    time.sleep(0.50)

    #Turning off ghost mode for the QCar
    hQCar3.ghost_mode(enable=False, color=[1,0,0])

    # Possessing the overhead camera on the QCar
    hQCar2.possess(hQCar2.CAMERA_OVERHEAD)
    time.sleep(0.5)
    
    # Possessing the trailing camera on the QCar
    hQCar2.possess(hQCar2.CAMERA_TRAILING)
    time.sleep(0.5)
    
    #Possessing the front CSI camera on the QCar
    hQCar2.possess(hQCar2.CAMERA_CSI_FRONT)
    time.sleep(0.5)

    # Possessing the right CSI camera on the QCar
    hQCar2.possess(hQCar2.CAMERA_CSI_RIGHT)
    time.sleep(0.5)

    # Possessing the back CSI camera on the QCar
    hQCar2.possess(hQCar2.CAMERA_CSI_BACK)
    time.sleep(0.5)

    # Possessing the left CSI camera on the QCar
    hQCar2.possess(hQCar2.CAMERA_CSI_LEFT)
    time.sleep(0.5)

    # Possessing the front RealSense RGB camera on the QCar
    hQCar2.possess(hQCar2.CAMERA_RGB)
    time.sleep(0.5)

    # Possessing the RealSense depth camera on the QCar
    hQCar2.possess(hQCar2.CAMERA_DEPTH)
    time.sleep(0.5)

    # Getting images from the different cameras 
    x, camera_image = hQCar2.get_image(camera=hQCar2.CAMERA_CSI_FRONT)
    x, camera_image = hQCar2.get_image(camera=hQCar2.CAMERA_CSI_RIGHT)
    x, camera_image = hQCar2.get_image(camera=hQCar2.CAMERA_CSI_BACK)
    x, camera_image = hQCar2.get_image(camera=hQCar2.CAMERA_CSI_LEFT)
    x, camera_image = hQCar2.get_image(camera=hQCar2.CAMERA_RGB)
    x, camera_image = hQCar2.get_image(camera=hQCar2.CAMERA_DEPTH)


    #LIDAR

    hQCar3.possess(hQCar3.CAMERA_OVERHEAD)

    # Creating a plot to plot the LIDAR data 
    lidarPlot = pg.plot(title="LIDAR")
    squareSize = 100
    lidarPlot.setXRange(-squareSize, squareSize)
    lidarPlot.setYRange(-squareSize, squareSize)
    lidarData = lidarPlot.plot([], [], pen=None, symbol='o', symbolBrush='r', symbolPen=None, symbolSize=2)

    time.sleep(1)

    print("Reading from LIDAR... if QLabs crashes or output isn't great, make sure FPS > 100")
    
    # Have the QCar drive forward to hit the front block to show the live lidar.
    # Speed can be changed by increasing or decreasing the value in the first
    # parameter "forward"
    hQCar3.set_velocity_and_request_state(1, 0, False, False, False, False, False)
    lidar_rate = 0.05

    # Obtaining and plotting lidar data for 0.2s
    for count in range(25): 
        
        success, angle, distance = hQCar3.get_lidar(samplePoints=400)

        x = np.sin(angle)*distance
        y = np.cos(angle)*distance
    
        lidarData.setData(x,y)
        QtWidgets.QApplication.instance().processEvents()
        time.sleep(lidar_rate) #lidar_rate is set at the top of this example


    time.sleep(5)

    # Closing qlabs
    qlabs.close()
    print("Done!")


main()