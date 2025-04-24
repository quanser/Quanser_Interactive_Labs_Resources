"""
QDrone 2 Library Example
--------------------------
This example will show you how to spawn qdrones, and use the qvl library commands
to control the drone and its related functions.

.. note::

    Make sure you have Quanser Interactive Labs open before running this
    example.  This example is designed to best be run in the open warehouse or plane.

"""

from qvl.qlabs import QuanserInteractiveLabs
from qvl.free_camera import QLabsFreeCamera
from qvl.basic_shape import QLabsBasicShape
from qvl.qdrone2 import QLabsQDrone2

import time
import numpy as np
import cv2
import os

from qvl.system import QLabsSystem



def main():
    os.system('cls')

    #Communications with qlabs

    qlabs = QuanserInteractiveLabs()
    cv2.startWindowThread()

    print("Connecting to QLabs...")
    if (not qlabs.open("localhost")):
        print("Unable to connect to QLabs")
        return    

    print("Connected")

    qlabs.destroy_all_spawned_actors()

    # Use hSystem to set the tutorial title in the upper left of the qlabs window 
    hSystem = QLabsSystem(qlabs)
    hSystem.set_title_string('QDrone Tutorial')


    hCamera = QLabsFreeCamera(qlabs)
    hCamera.spawn_id(actorNumber=1, location=[-1.683, 2.333, 1.787], rotation=[-0, 0.391, -1.541])
    hCamera.possess()

    print("\n---QDrone---")

    #spawning the QDrone. Rotation in radians
    myQDrone = QLabsQDrone2(qlabs)
    myQDrone.spawn_id(actorNumber=0, location=[-2,0,0], rotation=[0,0,np.pi/2], waitForConfirmation=True)
    time.sleep(1)

    myQDrone2 = QLabsQDrone2(qlabs)
    myQDrone2.spawn_degrees(location=[0,0,0], rotation=[0,0,45], waitForConfirmation=True)
    x = myQDrone2.ping()
    print('QDrone 2 ping test:', x)
    time.sleep(2)

    myQDrone2.destroy()
    x = myQDrone2.ping()
    print('QDrone 2 ping test:', x)

    velocities = [.2, .5, .8, -.8, -.5, -.2]
    # setting the velocity of the drone in the z direction to make it go up and down.
    for count in range(6):
        x = myQDrone.set_velocity_and_request_state(motorsEnabled=True, velocity=[0,0, velocities[count]], orientation=[0,0,0])
        time.sleep(1)

    myQDrone.set_velocity_and_request_state_degrees(motorsEnabled=True, velocity=[0,0, 0], orientation=[0,0,90])
    time.sleep(1)
    # this is just here to disable motors, so speed and orientation does not matter.
    myQDrone.set_velocity_and_request_state(motorsEnabled=False, velocity=[0,0, 0], orientation=[0,0,0])
    time.sleep(1)

    # adding a few shapes to the scene for understanding the camera views
    rectangle = QLabsBasicShape(qlabs)
    rectangle.spawn(location=[0,0,0], rotation=[0,0,0], scale=[.2,.2,1], configuration=rectangle.SHAPE_CUBE, waitForConfirmation=True)
    rectangle.set_material_properties(color=[1,0,0])
    time.sleep(.25)
    rectangle2 = QLabsBasicShape(qlabs)
    rectangle2.spawn(location=[-4,-3,0], rotation=[0,0,0], scale=[.2,.2,1], configuration=rectangle.SHAPE_CUBE, waitForConfirmation=True)
    rectangle2.set_material_properties(color=[0,1,0])
    time.sleep(.25)
    cone = QLabsBasicShape(qlabs)
    cone.spawn(location=[-1.4,0,0], rotation=[0,0,0], scale=[.2,.2,1], configuration=rectangle.SHAPE_CONE, waitForConfirmation=True)
    cone.set_material_properties(color=[0,0,1])
    time.sleep(.25)
    rectangle3 = QLabsBasicShape(qlabs)
    rectangle3.spawn(location=[-2,1.5,0], rotation=[0,0,0], scale=[.2,.2,1], configuration=rectangle.SHAPE_CUBE, waitForConfirmation=True)
    time.sleep(1)

    myQDrone.set_transform_and_dynamics(location=[-2,0,1], rotation=[0,0,np.pi/2], enableDynamics=True)
    time.sleep(1.5)

    # cycle through camera views
    
    cameras = [myQDrone.VIEWPOINT_CSI_LEFT, myQDrone.VIEWPOINT_CSI_BACK, myQDrone.VIEWPOINT_CSI_RIGHT, myQDrone.VIEWPOINT_RGB, myQDrone.VIEWPOINT_DEPTH, myQDrone.VIEWPOINT_DOWNWARD, myQDrone.VIEWPOINT_OPTICAL_FLOW, myQDrone.VIEWPOINT_OVERHEAD, myQDrone.VIEWPOINT_TRAILING]
    cameraNames = ['LEFT', 'BACK', 'RIGHT', 'RGB', 'DEPTH', 'DOWNWARD', 'OPTICAL FLOW', 'OVERHEAD', 'TRAILING']
    for count in range(9):
        x = myQDrone.possess(camera=cameras[count])
        hSystem.set_title_string(cameraNames[count])
        time.sleep(1.5)

    hCamera.possess()
    hSystem.set_title_string('QDrone Tutorial')
    # using get world transform to get current location of the drone
    myQDrone.set_transform_and_dynamics(location=[-2,0,1.2], rotation=[0,0,np.pi/2], enableDynamics=True)
    print(myQDrone.get_world_transform())
    time.sleep(1)

    myQDrone.set_transform_and_dynamics(location=[-2,0,0], rotation=[0,0,np.pi/2], enableDynamics=True)
    print(myQDrone.get_world_transform_degrees())
    time.sleep(1)


    # Getting images from the different cameras 
    status, camera_number, camera_image = myQDrone.get_image(camera=myQDrone.CAMERA_CSI_LEFT)
    status, camera_number, camera_image = myQDrone.get_image(camera=myQDrone.CAMERA_CSI_RIGHT)
    status, camera_number, camera_image = myQDrone.get_image(camera=myQDrone.CAMERA_CSI_BACK)
    
    status, camera_number, camera_image = myQDrone.get_image(camera=myQDrone.CAMERA_RGB)
    status, camera_number, camera_image = myQDrone.get_image(camera=myQDrone.CAMERA_DEPTH)
    status, camera_number, camera_image = myQDrone.get_image(camera=myQDrone.CAMERA_DOWNWARD)
    status, camera_number, camera_image = myQDrone.get_image(camera=myQDrone.CAMERA_OPTICAL_FLOW)


    # Closing qlabs
    qlabs.close()
    print("Done!")


main()