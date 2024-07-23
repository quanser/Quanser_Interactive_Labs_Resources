"""
Road Signage Library Traffic Cones Example
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
from qvl.system import QLabsSystem
from qvl.traffic_cone import QLabsTrafficCone


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
    hSystem.set_title_string('Traffic Cones Tutorial')

    num_destroyed = qlabs.destroy_all_spawned_actors()

    # Switch the camera angle to see where we will be spawning the cones
    camera0 = QLabsFreeCamera(qlabs)
    camera0.spawn([-20.355, 27.374, 2.055], [-0, 0.308, -0.001])
    camera0.possess()

    # creates 3 cones in this qlabs instance
    cone = QLabsTrafficCone(qlabs)
    cone1 = QLabsTrafficCone(qlabs)
    cone2 = QLabsTrafficCone(qlabs)
    cone3 = QLabsTrafficCone(qlabs)
    cone4 = QLabsTrafficCone(qlabs)
    
    # spawns a small traffic cone we just initialized using radians
    cone.spawn(location=[-17, 28, 1.0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    # waits so we can see the output
    time.sleep (1)
    # destroy the cone we just made
    cone.destroy()
    # waits so we can see the output
    time.sleep(1)
    # spawns another small traffic cone we just initialized using radians in the same place
    cone1.spawn_id(actorNumber=1, location=[-17, 28, 1.0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    # spawns a construction pylon using the cone we just initialized using degrees and generating
    # the actorNumber internally
    cone2.spawn_degrees(location=[-15, 28, 1.0], rotation=[0,0,180], scale=[1,1,1], configuration=1, waitForConfirmation=True)
    # spawns a small cone with one color stripe initialized using actor number and a position in degrees
    cone3.spawn_id_degrees(actorNumber=3, location=[-15, 26.5, 1.0], rotation=[0,0,90], scale=[1,1,1], configuration=2, waitForConfirmation=True)
    # spawns a bigger cone with two color stripes using radians and generating the actorNumber internally
    cone4.spawn(location=[-17, 26.5, 1.0], rotation=[0,0,math.pi/4], scale=[1,1,1], configuration=3, waitForConfirmation=True)
    
    # waits so we can see the output
    time.sleep(1.5)

    
    # change the color of the cones (materialSlot 0 is the base color, and 1 is the stripes)
    cone1.set_material_properties(materialSlot=0, color=[0,0,1],metallic=True) # Blue
    # waits so we can see the output
    time.sleep(.5)

    cone2.set_material_properties(materialSlot=0, color=[1,0,0],roughness=1,metallic=False) # Red
    cone2.set_material_properties(materialSlot=1, color=[1,.5,0])
    time.sleep(.5)

    cone3.set_material_properties(materialSlot=0, color=[0,1,1]) # Cyan 
    cone3.set_material_properties(materialSlot=1, color=[0,.3,1],roughness=1,metallic=True)
    time.sleep(.5)

    cone4.set_material_properties(materialSlot=0, color=[1,0,1],roughness=0,metallic=False) # Magenta
    cone4.set_material_properties(materialSlot=1, color=[.3,0,1])
    time.sleep(.5)

    cone1.set_material_properties(materialSlot=0, color=[0,1,0],roughness=0.5,metallic=False) # Green
    cone1.set_material_properties(materialSlot=1, color=[1,.5,0])
    time.sleep(.5)

    cone2.set_material_properties(materialSlot=0, color=[1,1,0],roughness=1,metallic=True) # Yellow
    cone2.set_material_properties(materialSlot=1, color=[0,0,0])
    time.sleep(.5)

    cone3.set_material_properties(materialSlot=0, color=[0.5,0.5,0.5]) # Grey
    cone3.set_material_properties(materialSlot=1, color=[0.6,0.2,0.6],roughness=1,metallic=True)
    time.sleep(.5)
    
    cone4.set_material_properties(materialSlot=0, color=[0.0,0.5,0.5],roughness=0,metallic=False) # Magenta
    cone4.set_material_properties(materialSlot=1, color=[0.5,0.5,0.0])
    time.sleep(.5)

    cone1.destroy()
    time.sleep(0.5)

    cone2.destroy()
    time.sleep(0.5)

    cone3.destroy()
    time.sleep(0.5)

    cone4.destroy()
    time.sleep(0.5)

    # Closing qlabs
    qlabs.close()
    print('Done!')

if __name__ == "__main__":
    main()
