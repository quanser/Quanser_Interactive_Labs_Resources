"""
Road Signage Library Example
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

from qvl.qlabs import QuanserInteractiveLabs
from qvl.free_camera import QLabsFreeCamera
from qvl.roundabout_sign import QLabsRoundaboutSign
from qvl.system import QLabsSystem
from qvl.yield_sign import QLabsYieldSign
from qvl.stop_sign import QLabsStopSign

# Clears the screen in Windows

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

    # Use hSystem to set the tutorial title in the upper left of the qlabs window 
    hSystem = QLabsSystem(qlabs)
    hSystem.set_title_string('Road Signage Tutorial')

    num_destroyed = qlabs.destroy_all_spawned_actors()

    # Switch the camera angle to see where we will be spawning the signs
    camera0 = QLabsFreeCamera(qlabs)
    camera0.spawn([-20.14, 29.472, 2.071], [0, 0.203, -0.024])
    camera0.possess()


    # Create two roundabouts in this qlabs instance
    roundabout = QLabsRoundaboutSign(qlabs)
    roundabout2 = QLabsRoundaboutSign(qlabs)

    # Spawn the sign using radians and specifying the actorNumber
    roundabout.spawn_id(0, [-17, 29, 0.0], [0, 0, math.pi], [1, 1, 1], 0, 1)
    # Spawn the second sign using degrees and allowing the computer to
    # generate an actorNumber internally
    roundabout2.spawn_id_degrees(2, [-15, 29, 0.0], [0, 0, 180], [1, 1, 1], 0, 1)

    # Wait to see the output
    time.sleep(1.5)

    # Destroying the sign we just created
    roundabout.destroy()
    time.sleep(1.5)

    # Create two yield signs in this qlabs instance
    yieldsign = QLabsYieldSign(qlabs)
    yieldsign2 = QLabsYieldSign(qlabs)

    # Spawn the sign using radians and specifying the actorNumber
    yieldsign.spawn_id(0, [-17, 31, 0.0], [0, 0, math.pi], [1, 1, 1], 0, 1)
    # Spawn the second sign using degrees and allowing the computer to
    # generate an actorNumber internally
    yieldsign2.spawn_degrees([-15, 31, 0.0], [0, 0, 180], [1, 1, 1], 0, 1)

    # Wait to see the output
    time.sleep(1.5)

    # Destroying the sign we just created
    yieldsign.destroy()
    time.sleep(1.5)

    # Create two stop signs in this qlabs instance
    stop = QLabsStopSign(qlabs)
    stop2 = QLabsStopSign(qlabs)

    # Spawn the sign using radians
    stop.spawn_id(1, [-16, 30, 0.0], [0, 0, math.pi], [1, 1, 1], 0, 1)
    # Spawn the second sign using degrees and allowing the computer to
    # generate an actorNumber internally
    stop2.spawn_degrees([-15, 30, 0.0], [0, 0, 180], [1, 1, 1], 0, 1)

    # Wait to see the output
    time.sleep(1.5)

    # Destroying the sign we just created
    stop.destroy()
    time.sleep(1.5)

    # Destroy the signs one by one
    roundabout2.destroy()
    time.sleep(1)

    stop2.destroy()
    time.sleep(1)

    yieldsign2.destroy()
    time.sleep(1)

    # Closing qlabs
    qlabs.close()
    print('Done!')


if __name__ == "__main__":
    main()
