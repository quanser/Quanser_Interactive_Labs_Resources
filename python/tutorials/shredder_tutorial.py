"""
Shredder Library Example
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
from qvl.widget import QLabsWidget
from qvl.shredder import QLabsShredder
from random import randrange

# this function creates a cylindrical widget at desired location,
# color of the widget is randomized.
def createCylinder(cylinder,location):
        #random color between red, green and blue
        color = [[0,1,0], [0,0,1], [1,0,0]]
        position = randrange(3)
        cylinder.spawn(location = location,
               rotation = [0, 0, .5],
               scale = [.05, .05, .05], # decrease the size of the widget
               configuration = cylinder.CYLINDER,  #set widget shape to cylinder
               color = color[position])

def main():

    # creates a server connection with Quanser Interactive Labs and manages the communications
    qlabs = QuanserInteractiveLabs()

    try:
        qlabs.open("localhost")
    except:
        print("Unable to connect to QLabs")
        return
    # create the widget instance
    cylinder = QLabsWidget(qlabs)
    # destroy any spawned actors (this is useful if you are running the same script over and over)
    qlabs.destroy_all_spawned_actors()

    # create a camera in this qlabs instance
    camera = QLabsFreeCamera(qlabs)
    # place the custom camera at a specified location and rotation using radians
    camera.spawn(location=[0.39, -11.2, 1.8], rotation=[0, 0.8, -1.581])
    # to switch our view from our current camera to the new camera we just initialized to
    # be able to view where our people will spawn
    camera.possess()

    ### Shredder
    # Create the shredder instance
    shredder = QLabsShredder(qlabs)
    # Spawn the first shredder, configuration = 2 indicates the color is blue
    shredder.spawn(location=[0, -12, 0], scale=[1,1,1], configuration=2)
    # Spawn the second shredder that is larger, controlled by the scale argument
    shredder.spawn(location=[.5, -12, 0], scale=[1.7,1.7,1.7], configuration=shredder.RED)
    time.sleep(2)
    
    # spawn 20 widgets and drop them into the shredders
    for i in range(20):
        # adding noise to the spawn location of the widgets
        noiseX = randrange(0,1)/20
        noiseY = randrange(0,1)/20
        # spawn one cylindical widget for each shredder
        createCylinder(cylinder,[0+noiseX, -12-noiseY, 1])
        createCylinder(cylinder,[.5-noiseX, -12+noiseY, 1])
        time.sleep(0.7)

    qlabs.close()

if __name__ == "__main__":
    main()