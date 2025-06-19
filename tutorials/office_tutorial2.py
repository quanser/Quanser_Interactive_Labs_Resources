"""
Office Objects2 Library Example
---------------------------------

.. note::

    This example spawns desks with a chair, computer, monitor, mouse and keyboard, 
    using a function to simplify creating multiple desks set up the same way. 
    
    Make sure you have Quanser Interactive Labs open before running this
    example.  This example is designed to best be run in the Warehouse, Plane or 
    Studio environment.

"""

# imports to important libraries
import time
import math

from qvl.qlabs import QuanserInteractiveLabs
from qvl.free_camera import QLabsFreeCamera
from qvl.system import QLabsSystem
from qvl.desk import QLabsDesk
from qvl.chair import QLabsChair
from qvl.computer import QLabsComputer
from qvl.computer_monitor import QLabsComputerMonitor
from qvl.computer_keyboard import QLabsComputerKeyboard

from qvl.computer_mouse import QLabsComputerMouse



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

    # Use hSystem to set the tutorial title on the qlabs display screen
    hSystem = QLabsSystem(qlabs)
    hSystem.set_title_string('Office Objects Tutorial')

    num_destroyed = qlabs.destroy_all_spawned_actors()

    # initialize a camera - See Camera Actor Library Reference for more information
    camera = QLabsFreeCamera(qlabs)
    camera.spawn([-0.936, -2.518, 1.973], [0, 0.541, 1.158])
    camera.possess()

    # make sure the second argument: actorNumber, is different for each of the times the function is called

    setupDesk(qlabs, 0, location = [1, -1.5, 0], rotation = [0, 0, math.pi/2])
    time.sleep(1)

    setupDesk(qlabs, 1, location = [0, 1.5, 0], rotation = [0, 0, 0])
    time.sleep(1)

    setupDesk(qlabs, 2, location = [-1, 0, 0], rotation = [0, 0, -math.pi/2])
    time.sleep(1)

    setupDesk(qlabs, 3, location = [-1, -1.5, 0], rotation = [0, 0, 0])
    time.sleep(1)
    


    # Closing qlabs
    qlabs.close()
    print('Done!')

def setupDesk(qlabs, actorNumber, location = [0, 0, 0], rotation = [0, 0, 0]):
    desk = QLabsDesk(qlabs)
    desk.spawn_id(actorNumber,location, rotation, [1, 1, 1], 0, 1)
    time.sleep(0.2)

    chair2 = QLabsChair(qlabs)
    chair2.spawn_id_and_parent_with_relative_transform(actorNumber, 
                                                       [0, -.5, 0.00], 
                                                       [0, 0, 0], 
                                                       [1, 1, 1], 
                                                       0, 
                                                       desk.classID, 
                                                       desk.actorNumber, 
                                                       0,  
                                                       1)
    time.sleep(0.2)

    computer2 = QLabsComputer(qlabs)
    computer2.spawn_id_and_parent_with_relative_transform(actorNumber, 
                                                       [0.52, 0.05, 0.752], 
                                                       [0, 0, 0], 
                                                       [1, 1, 1], 
                                                       0, 
                                                       desk.classID, 
                                                       desk.actorNumber, 
                                                       0,  
                                                       1)
    time.sleep(0.2)
    
    monitor2 = QLabsComputerMonitor(qlabs)
    monitor2.spawn_id_and_parent_with_relative_transform(actorNumber, 
                                                       [-0.05, 0.15, 0.752], 
                                                       [0, 0, 0], 
                                                       [1, 1, 1], 
                                                       0, 
                                                       desk.classID, 
                                                       desk.actorNumber, 
                                                       0,  
                                                       1)
    time.sleep(0.2)
    
    keyboard2 = QLabsComputerKeyboard(qlabs)
    keyboard2.spawn_id_and_parent_with_relative_transform(actorNumber, 
                                                       [-0.13, -0.165, 0.752], 
                                                       [0, 0, 0], 
                                                       [1, 1, 1], 
                                                       0, 
                                                       desk.classID, 
                                                       desk.actorNumber, 
                                                       0,  
                                                       1)
    
    mouse2 = QLabsComputerMouse(qlabs)
    mouse2.spawn_id_and_parent_with_relative_transform(actorNumber, 
                                                       [.275, -0.165, 0.752], 
                                                       [0, 0, 0], 
                                                       [1, 1, 1], 
                                                       0, 
                                                       desk.classID, 
                                                       desk.actorNumber, 
                                                       0,  
                                                       1)
    time.sleep(0.2)

if __name__ == "__main__":
    main()