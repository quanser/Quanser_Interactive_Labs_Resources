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

    num_destroyed = qlabs.destroy_all_spawned_actors()

    # create a camera in this qlabs instance
    camera = QLabsFreeCamera(qlabs)

    #place the custom camera at a specified location and rotation using radians
    camera.spawn([-0., 43.807, 8.82], [-0, 0.606, 3.127])

    # to switch our view from our current camera to the new camera we just initialized to
    # be able to view where our people will spawn
    camera.possess()

    # creates an instance of the Animal
    animal1 = QLabsAnimal(qlabs)

    # place the Animal at a specified location and rotation using radians
    # spawn_id allows us to specify the internal number for the actor
    animal1.spawn_id(0, LOCATION_START_P1, ROTATION_P1P2, SCALE, 0, True)

    # creates a second instance of a person
    animal2 = QLabsAnimal(qlabs)

    # place the animal at a specified location and rotation using radians
    # spawn creates the internal number for the actor automatically using
    # the next available actor number
    animal2.spawn(LOCATION_START_P2, ROTATION_P1P2, SCALE, 1, True)

    # creates a third instance of a person
    animal3 = QLabsAnimal(qlabs, True)

    # place the animal at a specified location and rotation using degrees
    # spawn_degrees creates the internal number for the actor automatically using the next
    # available number and takes the inputted rotation as degrees
    animal3.spawn_degrees(LOCATION_START_P3, ROTATION_P3, SCALE, 2, True)

    # move the 3 people created to a new location
    animal1.move_to(LOCATION_END_P1, animal1.GOAT_WALK, True)
    animal2.move_to(LOCATION_END_P2, animal2.SHEEP_RUN, True)
    animal3.move_to(LOCATION_END_P3, animal3.COW_RUN, True)

    # time.sleep to change camera angle 
    time.sleep(8)

    # re position camera
    hCameraAnimals = QLabsFreeCamera(qlabs)
    x = hCameraAnimals.spawn([25.243, 46.069, 1.628], [-0, 0.188, 1.098])
    hCameraAnimals.possess()

    # Spawn a Goat in a specific location 
    hGoat = QLabsAnimal(qlabs)
    hGoat.spawn([26.206, 57, 1], [0,0,0], [1,1,1], hGoat.GOAT, True)
    hGoat.move_to([27.214, 49.286, 0], hGoat.GOAT_RUN, True)
    time.sleep(3)

    # Move the Goat to your desired loaction 
    hGoat.move_to([28.338, 47.826, 0], hGoat.GOAT_WALK, True)
    time.sleep(4)
    hGoat.destroy()

    # Spawn a Sheep in a specific location
    hSheep = QLabsAnimal(qlabs)
    hSheep.spawn([26.206, 57, 1], [0,0,0], [1,1,1], hSheep.SHEEP, True)
    hSheep.move_to([27.214, 49.286, 0], hSheep.SHEEP_RUN, True)
    time.sleep(3)

    # Move the Sheep to your desired loaction 
    hSheep.move_to([28.338, 47.826, 0], hSheep.SHEEP_WALK, True)
    time.sleep(4)
    hSheep.destroy()

    # Spawn a Cow in a specific location
    hCow = QLabsAnimal(qlabs)
    hCow.spawn([26.206, 57, 1], [0,0,0], [1,1,1], hCow.COW, True)
    hCow.move_to([27.214, 49.286, 0], hCow.COW_RUN, True)
    time.sleep(3)

    # Move the Cow to your desired loaction 
    hCow.move_to([28.338, 47.826, 0], hCow.COW_WALK, True)
    time.sleep(6)

    qlabs.close()
    print('Done!')
    
if __name__ == "__main__":
    main()
