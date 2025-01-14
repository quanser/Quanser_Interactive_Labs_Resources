"""
Person Library Example
----------------------

.. note::

    Make sure you have Quanser Interactive Labs open before running this
    example.  This example is designed to best be run in QCar Cityscape.

"""

# imports to important libraries
import sys
import math
import time

from qvl.qlabs import QuanserInteractiveLabs
from qvl.free_camera import QLabsFreeCamera
from qvl.person import QLabsPerson
from qvl.system import QLabsSystem

def main():

    # initialize our variables
    # note that you can use the ..Coordinate Helper to pick locations for your actor.
    LOCATION_START_P1 = [-6.8, 40.7, 0.005]
    LOCATION_START_P2 = [-8.5, 40.7, 0.005]
    LOCATION_START_P3 = [-11.9, 40.7,0.005]

    ROTATION_P1P2 = [0,0,math.pi/2]
    SCALE = [1,1,1]
    ROTATION_P3 = [0,0,90]

    LOCATION_END_P1 = [-7.6, 51, 0.005]
    LOCATION_END_P2 = [-11.0, 48, 0.005]
    LOCATION_END_P3 = [-23.7, 43, 0.005]

    # creates a server connection with Quanser Interactive Labs and manages the communications
    qlabs = QuanserInteractiveLabs()

    print("Connecting to QLabs...")
    if (not qlabs.open("localhost")):
        print("Unable to connect to QLabs")
        return    

    print("Connected")

    # Use hSystem to set the tutorial title in the upper left of the qlabs window 
    hSystem = QLabsSystem(qlabs)
    hSystem.set_title_string('People Tutorial')

    # destroy any spawned actors (this is useful if you are running the same script over and over)
    qlabs.destroy_all_spawned_actors()

    # create a camera in this qlabs instance
    camera = QLabsFreeCamera(qlabs)
    # place the custom camera at a specified location and rotation using radians
    camera.spawn(location=[-2.061, 43.916, 4.348], rotation=[0, 0.383, -3.097])
    # to switch our view from our current camera to the new camera we just initialized to
    # be able to view where our people will spawn
    
    camera.possess()

    # creates an instance of the person
    person1 = QLabsPerson(qlabs)
    # place the person at a specified location and rotation using radians
    # spawn_id allows us to specify the internal number for the actor
    person1.spawn_id(actorNumber=0, location=LOCATION_START_P1, rotation=ROTATION_P1P2, scale=SCALE, configuration=6, waitForConfirmation=True)

    # creates a second instance of a person
    person2 = QLabsPerson(qlabs)
    # place the person at a specified location and rotation using radians
    # spawn creates the internal number for the actor automatically using
    # the next available actor number
    person2.spawn(location=LOCATION_START_P2, rotation=ROTATION_P1P2, scale=SCALE, configuration=7, waitForConfirmation=True)

    # creates a third instance of a person
    person3 = QLabsPerson(qlabs, True)
    # place the person at a specified location and rotation using degrees
    # spawn_degrees creates the internal number for the actor automatically using the next
    # available number and takes the inputted rotation as degrees
    person3.spawn_degrees(location=LOCATION_START_P3, rotation=ROTATION_P3, scale=SCALE, configuration=8, waitForConfirmation=True)

    # move the 3 people created to a new location
    person1.move_to(location=LOCATION_END_P1, speed=person1.WALK, waitForConfirmation=True)
    person2.move_to(location=LOCATION_END_P2, speed=person2.JOG, waitForConfirmation=True)
    person3.move_to(location=LOCATION_END_P3, speed=person3.RUN, waitForConfirmation=True)

    time.sleep(3)
    qlabs.close()

if __name__ == "__main__":
    main()