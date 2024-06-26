"""
Conveyor Library Example
-------------------------

.. note::

    Make sure you have Quanser Interactive Labs open before running this
    example.  This example is designed to best be run in any of the open
    world environments.

"""

# imports to important libraries
import sys
import math
import time

from qvl.qlabs import QuanserInteractiveLabs
from qvl.free_camera import QLabsFreeCamera
from qvl.system import QLabsSystem
from qvl.widget import QLabsWidget
from qvl.conveyor_curved import QLabsConveyorCurved
from qvl.conveyor_straight import QLabsConveyorStraight

def main():

    # creates a server connection with Quanser Interactive Labs and manages the communications
    qlabs = QuanserInteractiveLabs()

    try:
        qlabs.open("localhost")
    except:
        print("Unable to connect to QLabs")
        return
    
    # Use hSystem to set the tutorial title on the qlabs printlay screen
    hSystem = QLabsSystem(qlabs)
    hSystem.set_title_string('Conveyor Tutorial')
    
    # destroy any spawned actors (this is useful if you are running the same script over and over)
    qlabs.destroy_all_spawned_actors()


    
    cylinder = QLabsWidget(qlabs)
    # create a camera in this qlabs instance
    camera = QLabsFreeCamera(qlabs)
    # place the custom camera at a specified location and rotation using radians
    camera.spawn(location=[0.8, 0.7, 1.3], rotation=[0, 0.8, -1.581])
    # to switch our view from our current camera to the new camera we just initialized to
    # be able to view where our people will spawn
    camera.possess()

    ### Create conveyors
    # The configuration argument is an integer associated with the length of the conveyors
    # For straight conveyor, configuration = 0 corresponds to a length of 0.5. With each 
    # increase in configuration, the lengh is increased by 0.25, up to configuratoin = 20  
    straightConveyor = QLabsConveyorStraight(qlabs)
    straightConveyor.spawn_id_degrees(actorNumber = 0,
                                    location = [0, 0, 0],
                                    rotation = [0, 0, 0],
                                    scale = [1,1,1],
                                    configuration = 5)
    # For curved conveyor, configuration = 0 corresponds to a circular arc of 15 degree. 
    # With each increase in configuration, the arc length is increased by 15 degrees, up to 
    # configuratoin = 24.
    curvedConveyor = QLabsConveyorCurved(qlabs)
    curvedConveyor.spawn_id_degrees(actorNumber = 1,
                                    location = [0.03, -0.5, 0],
                                    rotation = [0, 0, 0],
                                    scale = [1,1,1],
                                    configuration = 6)
    time.sleep(2)

    ### set the speed for each conveyor 
    straightConveyor.set_speed(0.3)
    curvedConveyor.set_speed(0.07)

    time.sleep(2)

    ### drop one cylinder widget on top of the straight convoryer
    cylinder.spawn(location = [1.6, 0, 1],
               rotation = [0, 0, .5],
               scale = [.05, .05, .05],
               configuration = cylinder.CYLINDER)

    time.sleep(1)

    qlabs.close()

if __name__ == "__main__":
    main()