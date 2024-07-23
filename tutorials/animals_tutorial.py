"""
Animal Example
---------------

.. note::

    Make sure you have Quanser Interactive Labs open before running this
    example.  This example is designed to run in the QCar Cityscape.

"""

from qvl import qlabs
from qvl.animal import QLabsAnimal
from qvl.qlabs import QuanserInteractiveLabs
from qvl.free_camera import QLabsFreeCamera 
from qvl.environment_outdoors import QLabsEnvironmentOutdoors
from qvl.system import QLabsSystem

import time
import os
import math


# initialize our variables
# note that you can use the ..Coordinate Helper to pick locations for your actor.
LOCATION_START_P1 = [-6.85, 40.396, 0.005]
ROTATION_P1P2 = [0,0,math.pi/2]
SCALE = [1,1,1]

LOCATION_START_P2 = [-8.53, 40.7, 0.005]
LOCATION_START_P3 = [-11.884, 40.292, 0.005]
ROTATION_P3 = [0,0,90]

LOCATION_END_P1 = [-7.637, 51, 0.005]
LOCATION_END_P2 = [-11.834, 51, 0.005]
LOCATION_END_P3 = [-23.71, 43.245, 0.005]


def main():

    print("\n\n------------- Communications -------------------\n")

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

    # Use hSystem to set the tutorial title on the qlabs display screen
    hSystem = QLabsSystem(qlabs)
    hSystem.set_title_string('Animals Tutorial')

    num_destroyed = qlabs.destroy_all_spawned_actors()

    # create a camera in this qlabs instance
    camera = QLabsFreeCamera(qlabs)

    #place the custom camera at a specified location and rotation using radians
    camera.spawn([-0., 43.807, 8.82], [-0, 0.606, 3.127])

    # to switch our view from our current camera to the new camera we just initialized to
    # be able to view where our animals will spawn
    camera.possess()

    # Animal configurations 
    #
    #   Goat = 0
    #   Sheep = 1
    #   Cow = 2

    # creates an instance of the Animal
    goat = QLabsAnimal(qlabs)

    # place the Animal at a specified location and rotation using radians
    # spawn_id allows us to specify the internal number for the actor
    goat.spawn_id(0, LOCATION_START_P1, ROTATION_P1P2, SCALE, 0, True)

    # creates a second instance of a animal
    sheep = QLabsAnimal(qlabs)

    # place the animal at a specified location and rotation using radians
    # spawn creates the internal number for the actor automatically using
    # the next available actor number
    sheep.spawn(LOCATION_START_P2, ROTATION_P1P2, SCALE, 1, True)

    # creates a third instance of a animal
    cow = QLabsAnimal(qlabs, True)

    # place the animal at a specified location and rotation using degrees
    # spawn_degrees creates the internal number for the actor automatically using the next
    # available number and takes the inputted rotation as degrees
    cow.spawn_degrees(LOCATION_START_P3, ROTATION_P3, SCALE, 2, True)

    # move the 3 people created to a new location
    goat.move_to(LOCATION_END_P1, goat.GOAT_WALK, True)
    sheep.move_to(LOCATION_END_P2, sheep.SHEEP_RUN, True)
    cow.move_to(LOCATION_END_P3, cow.COW_RUN, True)

    # time.sleep to change camera angle 
    time.sleep(7)

    # destroy each animal one by one 
    goat.destroy()
    time.sleep(1)

    sheep.destroy()
    time.sleep(1)

    cow.destroy()
    time.sleep(1)

    # re position camera
    hCameraAnimals = QLabsFreeCamera(qlabs)
    x = hCameraAnimals.spawn([25.243, 46.069, 1.628], [-0, 0.188, 1.098])
    hCameraAnimals.possess()

    # Spawn a Goat and make it run to a specific location  
    hGoat = QLabsAnimal(qlabs)
    hGoat.spawn([26.206, 57, 1], [0,0,0], [1,1,1], hGoat.GOAT, True)
    hGoat.move_to([27.214, 49.286, 0], hGoat.GOAT_RUN, True)
    time.sleep(3)

    # Move the Goat at walking speed to your desired location 
    hGoat.move_to([28.338, 47.826, 0], hGoat.GOAT_WALK, True)
    time.sleep(4)
    hGoat.destroy()

    # Spawn a Sheep and make it run to a specific location
    hSheep = QLabsAnimal(qlabs)
    hSheep.spawn([26.206, 57, 1], [0,0,0], [1,1,1], hSheep.SHEEP, True)
    hSheep.move_to([27.214, 49.286, 0], hSheep.SHEEP_RUN, True)
    time.sleep(3)

    # Move the Sheep at walking speed to your desired location
    hSheep.move_to([28.338, 47.826, 0], hSheep.SHEEP_WALK, True)
    time.sleep(4)
    hSheep.destroy()

    # Spawn a Cow and make it run to a specific location
    hCow = QLabsAnimal(qlabs)
    hCow.spawn([26.206, 57, 1], [0,0,0], [1,1,1], hCow.COW, True)
    hCow.move_to([27.214, 49.286, 0], hCow.COW_RUN, True)
    time.sleep(3)

    # Move the Cow at walking speed to your desired location
    hCow.move_to([28.338, 47.826, 0], hCow.COW_WALK, True)
    time.sleep(6)
    
    # Close qlabs
    qlabs.close()
    print('Done!')

if __name__ == "__main__":
    main()
