"""
Walls Example
---------------

.. note::

    Make sure you have Quanser Interactive Labs open before running this
    example. This example is designed to be run in the Plane, Warehouse
    or Studio environment.

"""

from qvl.qlabs import QuanserInteractiveLabs
from qvl.free_camera import QLabsFreeCamera 
from qvl.basic_shape import QLabsBasicShape

import time

from qvl.walls import QLabsWalls


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

    # Initialize an instance of a custom camera 
    camera = QLabsFreeCamera(qlabs)
    camera.spawn([2.295, -3.826, 1.504], [-0, 0.213, 1.957])
    camera.possess()

    # Initialize instances of walls 
    wall = QLabsWalls(qlabs)
    
    # Use 'for' loops to spawn a line of walls
    for y in range (5):
        wall.spawn_degrees([-0.5, y*1.05, 0.001])
        
    # Spawn a second line of walls but enable the dynamics
    for y in range (5):
        wall.spawn_degrees([0.5, y*1.05, 0.001])
    
        # Enable dynamics for this set of walls
        wall.set_enable_dynamics(True)


    # Spawn a large sphere to demonstrate which walls are dynamic
    sphere = QLabsBasicShape(qlabs)
    sphere.spawn(location=[0,2,3], scale=[1.5,1.5,1.5], configuration=sphere.SHAPE_SPHERE)
    sphere.set_enable_dynamics(True)
    


    # Closing qlabs
    qlabs.close()
    print('Done!')

if __name__ == "__main__":
    main()