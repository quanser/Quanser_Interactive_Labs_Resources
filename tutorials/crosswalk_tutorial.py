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

from qvl.qlabs import QuanserInteractiveLabs
from qvl.free_camera import QLabsFreeCamera
from qvl.crosswalk import QLabsCrosswalk
from qvl.system import QLabsSystem

def main():

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
        

    print("Connected")

    # Use hSystem to set the tutorial title on the qlabs display screen
    hSystem = QLabsSystem(qlabs)
    hSystem.set_title_string('Crosswalk Tutorial')

    num_destroyed = qlabs.destroy_all_spawned_actors()

    # initialize a camera - See Camera Actor Library Reference for more information
    cameraCrosswalk = QLabsFreeCamera(qlabs)
    cameraCrosswalk.spawn([-19.286, 43, 5.5], [-0, 0.239, -0.043])
    cameraCrosswalk.possess()

    # create a crosswalk in this qlabs instance
    crosswalk = QLabsCrosswalk(qlabs)
    crosswalk1 = QLabsCrosswalk(qlabs)
    crosswalk2 = QLabsCrosswalk(qlabs)

    # spawn crosswalk with radians in configuration 0
    time.sleep(0.5)
    crosswalk.spawn_id(0, [-10.788, 45, 0.00], [0, 0, math.pi/2], [1, 1, 1], 0, 1)
    # waits so we can see the output
    time.sleep(1.5)
    # spawn crosswalk with degrees in configuration 1
    crosswalk1.spawn_id_degrees(1, [-6.788, 45, 0.00], [0, 0, 90], [1, 1, 1], 1, 1)
    # waits so we can see the output
    time.sleep(1.5)
    # spawn crosswalk with degrees in configuration 2
    crosswalk2.spawn_id_degrees(2, [-2.8, 45, 0.0], [0, 0, 90], [1, 1, 1], 2, 1)
    time.sleep(1.5)

    crosswalk.destroy()
    time.sleep(1.5)

    crosswalk1.destroy()
    time.sleep(1.5)

    crosswalk2.destroy()

    # Closing qlabs
    qlabs.close()
    print('Done!')

if __name__ == "__main__":
    main()