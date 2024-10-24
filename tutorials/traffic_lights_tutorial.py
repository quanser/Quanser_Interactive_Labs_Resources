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

    # Creates a server connection with Quanser Interactive Labs and manages
    # the communications
    qlabs = QuanserInteractiveLabs()

    # Ensure that QLabs is running on your local machine
    print("Connecting to QLabs...")
    if (not qlabs.open("localhost")):
        print("Unable to connect to QLabs")
        return    

    print("Connected")

    num_destroyed = qlabs.destroy_all_spawned_actors()

    # initialize a camera - See Camera Actor Library Reference for more information
    cameraTraffic = QLabsFreeCamera(qlabs)
    cameraTraffic.spawn(location=[0.131, 2.05, 2.047], rotation=[-0, -0.068, 1.201])
    cameraTraffic.possess()

    # initialize three traffic light instances in qlabs
    trafficLight1 = QLabsTrafficLight(qlabs)
    trafficLight2 = QLabsTrafficLight(qlabs)
    trafficLight3 = QLabsTrafficLight(qlabs)

    
    # spawn a traffic light in config 1 - vertical using radians and specifying a specific actorNumber
    trafficLight1.spawn_id(actorNumber=0, location=[5.616, 14.131, 0.215], rotation=[0,0,0], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    trafficLight1.set_color(color=trafficLight1.COLOR_GREEN)
    
    # spawn a second traffic light using degrees in config 1 - vertical and specifying a specific actorNumber
    trafficLight2.spawn_id_degrees(actorNumber=2, location=[-3.078, 14.136, 0.215], rotation=[0,0,180], scale=[1,1,1], configuration=1, waitForConfirmation=True)
    trafficLight2.set_color(color=trafficLight2.COLOR_GREEN)

    # spawn traffic light using degrees in config 2 - horizontal and generating the actorNumber internally
    trafficLight3.spawn_degrees(location=[6.703, 5.6, 0.215], rotation=[0,0,-90], scale=[1,1,1], configuration=2, waitForConfirmation=True)
    trafficLight3.set_color(color=trafficLight3.COLOR_RED)

    # changing the state of the traffic lights from green to red
    time.sleep(2)

    trafficLight1.set_color(color=trafficLight1.COLOR_YELLOW)
    trafficLight2.set_color(color=trafficLight2.COLOR_YELLOW)

    time.sleep(1)

    trafficLight1.set_color(color=trafficLight1.COLOR_RED)
    trafficLight2.set_color(color=trafficLight2.COLOR_RED)

    time.sleep(1)

    trafficLight3.set_color(color=trafficLight3.COLOR_GREEN)


    # Closing qlabs
    qlabs.close()
    print('Done!')

if __name__ == "__main__":
    main()
