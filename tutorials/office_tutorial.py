"""
Road Signage Library Crosswalk Example
----------------------------

.. note::

    Make sure you have Quanser Interactive Labs open before running this
    example.  This example is designed to best be run in QCar Cityscape 
    or Cityscape Lite.

"""

# imports to important libraries
import sys
import math
import time

import cv2

from qvl.qlabs import QuanserInteractiveLabs
from qvl.free_camera import QLabsFreeCamera
from qvl.crosswalk import QLabsCrosswalk
from qvl.system import QLabsSystem
from qvl.desk import QLabsDesk
from qvl.chair import QLabsChair
from qvl.computer import QLabsComputer
from qvl.computer_monitor import QLabsComputerMonitor
from qvl.computer_keyboard import QLabsComputerKeyboard

from qvl.computer_mouse import QLabsComputerMouse



def main():

    print("\n\n------------------------------ Communications --------------------------------\n")

    # Creates a server connection with Quanser Interactive Labs and manages
    # the communications
    qlabs = QuanserInteractiveLabs()

    # Ensure that QLabs is running on your local machine
    print("Connecting to QLabs...")
    if (not qlabs.open("localhost")):
        print("Unable to connect to QLabs")
        return    

    print("Connected")

    # Use hSystem to set the tutorial title on the qlabs display screen
    hSystem = QLabsSystem(qlabs)
    hSystem.set_title_string('Office Objects Tutorial')

    num_destroyed = qlabs.destroy_all_spawned_actors()

    # initialize a camera - See Camera Actor Library Reference for more information
    camera = QLabsFreeCamera(qlabs)
    camera.spawn([-0.936, -2.518, 1.973], [0, 0.541, 1.158])
    camera.possess()

    desk = QLabsDesk(qlabs)
    desk.spawn([-0.5, -0.5, 0.00], [0, 0, 0], [1, 1, 1], 0, 1)
    time.sleep(0.2)

    chair = QLabsChair(qlabs)
    chair.spawn([-0.6, -1, 0.00], [0, 0, 0], [1, 1, 1], 0, 1)
    time.sleep(0.2)

    computer = QLabsComputer(qlabs)
    computer.spawn([-0.0, -0.45, 0.752], [0, 0, 0], [1, 1, 1], 0, 1)
    time.sleep(0.2)

    monitor = QLabsComputerMonitor(qlabs)
    monitor.spawn([-0.6, -0.32, 0.752], [0, 0, 0], [1, 1, 1], 0, 1)
    time.sleep(0.2)

    keyboard = QLabsComputerKeyboard(qlabs)
    keyboard.spawn([-0.606, -0.603, 0.752], [0, 0, 0], [1, 1, 1], 0, 1)

    mouse = QLabsComputerMouse(qlabs)
    mouse.spawn([-0.25, -0.607, 0.752], [0, 0, 0], [1, 1, 1], 0, 1)

    time.sleep(0.2)

    # the second desk will be spawned with all objects relative to it, 
    # so if the desk location or rotation moves, everything moves with it
    desk2 = QLabsDesk(qlabs)
    desk2.spawn_id(1,[1, -0.5, 0.00], [0, 0, 0], [1, 1, 1], 0, 1)
    time.sleep(0.2)

    chair2 = QLabsChair(qlabs)
    chair2.spawn_id_and_parent_with_relative_transform(1, 
                                                       [0, -.5, 0.00], 
                                                       [0, 0, 0], 
                                                       [1, 1, 1], 
                                                       0, 
                                                       desk2.classID, 
                                                       desk2.actorNumber, 
                                                       0,  
                                                       1)
    time.sleep(0.2)

    computer2 = QLabsComputer(qlabs)
    computer2.spawn_id_and_parent_with_relative_transform(1, 
                                                       [0.52, 0.05, 0.752], 
                                                       [0, 0, 0], 
                                                       [1, 1, 1], 
                                                       0, 
                                                       desk2.classID, 
                                                       desk2.actorNumber, 
                                                       0,  
                                                       1)
    time.sleep(0.2)
    
    monitor2 = QLabsComputerMonitor(qlabs)
    monitor2.spawn_id_and_parent_with_relative_transform(1, 
                                                       [-0.05, 0.15, 0.752], 
                                                       [0, 0, 0], 
                                                       [1, 1, 1], 
                                                       0, 
                                                       desk2.classID, 
                                                       desk2.actorNumber, 
                                                       0,  
                                                       1)
    time.sleep(0.2)
    
    keyboard2 = QLabsComputerKeyboard(qlabs)
    keyboard2.spawn_id_and_parent_with_relative_transform(1, 
                                                       [-0.13, -0.165, 0.752], 
                                                       [0, 0, 0], 
                                                       [1, 1, 1], 
                                                       0, 
                                                       desk2.classID, 
                                                       desk2.actorNumber, 
                                                       0,  
                                                       1)
    
    mouse2 = QLabsComputerMouse(qlabs)
    mouse2.spawn_id_and_parent_with_relative_transform(1, 
                                                       [.275, -0.165, 0.752], 
                                                       [0, 0, 0], 
                                                       [1, 1, 1], 
                                                       0, 
                                                       desk2.classID, 
                                                       desk2.actorNumber, 
                                                       0,  
                                                       1)
    time.sleep(0.2)
    


    # Closing qlabs
    qlabs.close()
    print('Done!')

if __name__ == "__main__":
    main()