"""
Widget Library Example
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
from qvl.widget import QLabsWidget

def widgets(qlabs):

    # initialize the widget class in qlabs
    widget = QLabsWidget(qlabs)

    # choose to show shadows on our objects since we aren't going to be spawning a lot of widgets
    widget.widget_spawn_shadow(enableShadow=True)

    # create 10 cubes of a variety of shades of red
    for count in range(10):
        widget.spawn_degrees(location = [-11.000, 30.000+count*0.01, 1+count*0.6], rotation = [90,0,0], scale = [0.5,0.5,0.5], configuration = widget.CUBE, color = [1,0+count*0.03,0+count*0.02], measuredMass=0, IDTag=0, properties='', waitForConfirmation=True)

    time.sleep(2)

    # create 20 grey metal cans and place them at slightly different spots
    for count in range(20):
        widget.spawn(location = [-11.000, 29.000, 1+count*0.2], rotation = [0,0,0], scale = [1,1,1], configuration = widget.METAL_CAN, color = [1,1,1], measuredMass=0, IDTag=0, properties='', waitForConfirmation=True)

    time.sleep(1)

    # create 20 plastic bottles of a variety of shades of blue
    for count in range(20):
        widget.spawn_degrees(location = [-11.000, 29.000, 1+count*0.2], rotation = [90,0,0], scale = [1,1,1], configuration = widget.PLASTIC_BOTTLE, color = [count*0.01 ,count*0.02, 1], measuredMass=0, IDTag=0, properties='', waitForConfirmation=True)

    time.sleep(1)

    # create 10 spheres of a ombre of red to yellow
    for count in range(10):
        widget.spawn_degrees(location = [-11.000, 31.000+count*0.01, 1+count*0.6], rotation = [90,0,0], scale = [0.5,0.5,0.5], configuration = widget.SPHERE, color = [1,0+ count*0.05,0+ count*0.01], measuredMass=1000, IDTag=0, properties='', waitForConfirmation=True)

    time.sleep(5)

    # destroy widgets so that they don't continue to consume resources rolling around
    #widget.destroy_all_spawned_widgets()

def main():

    # creates a server connection with Quanser Interactive Labs and manages
    # the communications
    qlabs = QuanserInteractiveLabs()

    # initialize our desired variables
    # note that you can use the coordinate helper to pick locations for your camera.
    loc = [-18.783, 30.023, 2.757]
    rot = [0, 8.932, -2.312]

    # creates a server connection with Quanser Interactive Labs and manages the communications
    qlabs = QuanserInteractiveLabs()

    print("Connecting to QLabs...")
    # trying to connect to QLabs and open the instance we have created - program will end if this fails
    try:
        qlabs.open("localhost")
    except:
        print("Unable to connect to QLabs")
        return

    # destroying any spawned actors in our QLabs that currently exist
    qlabs.destroy_all_spawned_actors()

    # create a camera in this qlabs instance
    camera = QLabsFreeCamera(qlabs)

    # add a custom camera at a specified location and rotation using degrees
    camera.spawn_degrees(location=loc, rotation=rot)

    # to switch our view from our current camera to the new camera we just initialized
    camera.possess()

    # run the code for using widgets
    widgets(qlabs)

    # close our connection to qlabs
    qlabs.close()

if __name__ == "__main__":
    main()