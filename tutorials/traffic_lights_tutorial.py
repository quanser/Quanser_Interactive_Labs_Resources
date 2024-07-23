"""
Road Signage Library Traffic Lights Example
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

from qvl.crosswalk import QLabsCrosswalk
from qvl.qlabs import QuanserInteractiveLabs
from qvl.free_camera import QLabsFreeCamera
from qvl.system import QLabsSystem
from qvl.traffic_cone import QLabsTrafficCone
from qvl.traffic_light import QLabsTrafficLight


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

    # Use hSystem to set the tutorial title in the upper left of the qlabs window 
    hSystem = QLabsSystem(qlabs)
    hSystem.set_title_string('Traffic Lights Tutorial')

    num_destroyed = qlabs.destroy_all_spawned_actors()

    # initialize a camera - See Camera Actor Library Reference for more information
    cameraTraffic = QLabsFreeCamera(qlabs)
    cameraTraffic.spawn(location=[0.131, 2.05, 2.047], rotation=[-0, -0.068, 1.201])
    cameraTraffic.possess()

    # initialize three traffic light instances in qlabs
    trafficLight = QLabsTrafficLight(qlabs)
    trafficLight2 = QLabsTrafficLight(qlabs)
    trafficLight3 = QLabsTrafficLight(qlabs)

    # Initialize two crosswalk instances in qlabs
    crosswalk = QLabsCrosswalk(qlabs)
    crosswalk1 = QLabsCrosswalk(qlabs)

    # spawn a traffic light in config 1 - vertical using radians and specifying a specific actorNumber
    trafficLight.spawn_id(actorNumber=0, location=[5.616, 14.131, 0.215], rotation=[0,0,0], scale=[1,1,1], configuration=0, waitForConfirmation=True)

    # spawn a second traffic light using degrees in config 1 - vertical and specifying a specific actorNumber
    trafficLight2.spawn_id_degrees(actorNumber=2, location=[-3.078, 14.136, 0.215], rotation=[0,0,180], scale=[1,1,1], configuration=1, waitForConfirmation=True)

    # spawn traffic light using degrees in config 2 - horizontal and generating the actorNumber internally
    trafficLight3.spawn_degrees(location=[6.703, 5.6, 0.215], rotation=[0,0,-90], scale=[1,1,1], configuration=2, waitForConfirmation=True)

    time.sleep(0.5)

    # Spawn crosswalk with radians in configuration 0
    crosswalk.spawn_id(actorNumber = 0, location= [1.3, 16.7, 0.005], rotation= [0, 0, 0], scale=[1, 1, 1], configuration= 0, waitForConfirmation= 1)

    time.sleep(1)

    # Spawn crosswalk with radians in configuration 1
    crosswalk1.spawn_id(actorNumber = 1, location= [8.5, 10.21, 0.01], rotation= [0, 0, math.pi/2], scale=[1, 1, 1], configuration= 1, waitForConfirmation= 1)

    # changing the state of the traffic lights from green to red
    
    time.sleep(2)

    trafficLight.set_state(state=trafficLight.STATE_YELLOW, waitForConfirmation=True)
    trafficLight2.set_state(state=trafficLight2.STATE_YELLOW, waitForConfirmation=True)

    time.sleep(1)

    trafficLight.set_state(state=trafficLight.STATE_RED, waitForConfirmation=True)
    trafficLight2.set_state(state=trafficLight2.STATE_RED, waitForConfirmation=True)

    time.sleep(1)

    trafficLight3.set_state(state=trafficLight3.STATE_GREEN, waitForConfirmation=True)

    # Destroying a traffic light
    trafficLight.destroy()

    time.sleep(1)

    # Destroy the first crosswalk 
    crosswalk.destroy()

    time.sleep(1)

    # Destroy the first crosswalk 
    crosswalk1.destroy()

    # Closing qlabs
    qlabs.close()
    print('Done!')

if __name__ == "__main__":
    main()
