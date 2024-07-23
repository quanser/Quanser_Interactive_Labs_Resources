"""
QCar Floor Mats Example
---------------

.. note::

    Make sure you have Quanser Interactive Labs open before running this
    example. This example is designed to be run in any of the open world 
    environments.

"""

from qvl.qcar_flooring import QLabsQCarFlooring
from qvl.qlabs import QuanserInteractiveLabs
from qvl.free_camera import QLabsFreeCamera 
from qvl.system import QLabsSystem

import time
import os
import math

from qvl.walls import QLabsWalls


def main():

    # Clears the screen in Windows
    os.system('cls')

    print("\n\n------------------------------ Communications --------------------------------\n")

    # Creates a server connection with Quanser Interactive Labs and manages
    # the communications
    qlabs = QuanserInteractiveLabs()

    # Ensure that QLabs is running on your local machine
    print("Connecting to QLabs...")
    try:
        qlabs.open("localhost")
    except:
        print("Unable to connect to QLabs")
        return

    print("Connected")

    hSystem = QLabsSystem(qlabs)
    hSystem.set_title_string('QCar Floor Mats Tutorial')

    num_destroyed = qlabs.destroy_all_spawned_actors()

    # Initialize an instance of a camera 
    camera = QLabsFreeCamera(qlabs)

    # Set the spawn of the camera in a specific location 
    camera.spawn([4.945, -3.006, 1.482], [0, 0.201, 2.644], [1, 1, 1], 0, 1)

    # Spawn the camera
    camera.possess()

    # set locational parameters 
    x_offset = 0.13
    y_offset = 0

    # Initialize an instance of each configuration of floor mat 
    floor = QLabsQCarFlooring(qlabs)
    floor1 = QLabsQCarFlooring(qlabs)

    time.sleep(0.5)

    # Spawn the first configuration floor mat
    floor.spawn_degrees([x_offset, y_offset, 0.001], [0, 0, -90], [1, 1, 1], 0, 1)

    # Initialize instances of walls 
    wall = QLabsWalls(qlabs)
    


    # Use 'for' loops to spawn walls on the perimeter of the floor mat and wait for walls to spawn
    for y in range (5):
        wall.spawn_degrees([-2.4 + x_offset, (-y*1.0)+2.55 + y_offset, 0.001], [0, 0, 0], [1, 1, 1], 0, 1)
        #make walls harder to knock down
        wall.set_enable_dynamics(False)
    time.sleep(1)

    for x in range (4):
        wall.spawn_degrees([-1.9 + x + x_offset, 3.05 + y_offset, 0.001], [0, 0, 90], [1, 1, 1], 0, 1)
        wall.set_enable_dynamics(False)

    time.sleep(1)
    wall.spawn_degrees([2.174, 2.686, 0.001], [0, 0, 45], [1, 1, 1], 0, 1)
    wall.set_enable_dynamics(False)

    time.sleep(1)

    for y in range (4):
        wall.spawn_degrees([2.4 + x_offset, (-y*1.0)+1.68 + y_offset, 0.001], [0, 0, 0], [1, 1, 1,], 0, 1)
        wall.set_enable_dynamics(False)

    time.sleep(1)

    wall.spawn_degrees([2.334, -2.456, 0.001], [0, 0, -22], [1, 1, 1], 0, 1)
    wall.set_enable_dynamics(False)

    time.sleep(1)

    for x in range (3):
        wall.spawn_degrees([-0.56 + x + x_offset, -3.05 + y_offset, 0.001], [0, 0, 90], [1, 1, 1], 0, 1)
        wall.set_enable_dynamics(False)

    time.sleep(1)

    wall.spawn_degrees([-2.03 + x_offset, -2.275 + y_offset, 0.001], [0, 0, 48], [1, 1, 1], 0, 1)
    wall.set_enable_dynamics(False)
    wall.spawn_degrees([-1.575 + x_offset, -2.7 + y_offset, 0.001], [0, 0, 48], [1, 1, 1], 0, 1)
    wall.set_enable_dynamics(False)

    time.sleep(2)

    # Destroy all of the walls
    wall.destroy_all_actors_of_class()

    time.sleep(1)

    # Destroy the first configuration floor mat
    floor.destroy()

    # Spawn the second configuration floor mat
    floor1.spawn_degrees([0, 0, 0.001], [0, 0, -90], [1, 1, 1], 1, 1)

    time.sleep(1)

    # Spawn the walls around the second floor mat

    wall.spawn_degrees([2.217, -0.819, 0.001], [0, 0, -22], [1, 1, 1], 0, 1)
    wall.set_enable_dynamics(False)

    time.sleep(1)

    for x in range (3):
        wall.spawn_degrees([-0.6 + x + x_offset, -1.3, 0.001], [0, 0, 90], [1, 1, 1], 0, 1)
        wall.set_enable_dynamics(False)

    time.sleep(1)

    wall.spawn_degrees([-2.06 + x_offset, -0.6, 0.001], [0, 0, 48], [1, 1, 1], 0, 1)
    wall.set_enable_dynamics(False)
    wall.spawn_degrees([-1.5 + x_offset, -1.1, 0.001], [0, 0, 48], [1, 1, 1], 0, 1)
    wall.set_enable_dynamics(False)

    time.sleep(1)

    wall.spawn_degrees([-2.3, 0.28, 0.001], [0, 0, 0], [1, 1, 1], 0, 1)
    wall.set_enable_dynamics(False)
    wall.spawn_degrees([-2.3, 0.8, 0.001], [0, 0, 0], [1, 1, 1], 0, 1)
    wall.set_enable_dynamics(False)

    time.sleep(1)

    for x in range (5):
        wall.spawn_degrees([-1.9 + x + x_offset, 1.32 , 0.001], [0, 0, 90], [1, 1, 1], 0, 1)
        wall.set_enable_dynamics(False)

    time.sleep(1)

    wall.spawn_degrees([2.4, 0.22, 0.001], [0, 0, 0], [1, 1, 1], 0, 1)
    wall.set_enable_dynamics(False)
    wall.spawn_degrees([2.4, 0.8, 0.001], [0, 0, 0], [1, 1, 1], 0, 1)
    wall.set_enable_dynamics(False)

    time.sleep(2)

    # Destroy all of the walls
    wall.destroy_all_actors_of_class()

    time.sleep(2)

    # Destroy the second configuration of floor mat                                                                                                                                                                         
    floor1.destroy()

    # Closing qlabs
    qlabs.close()
    print('Done!')

if __name__ == "__main__":
    main()