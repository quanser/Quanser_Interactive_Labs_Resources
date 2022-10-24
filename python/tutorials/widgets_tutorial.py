"""
Widget Library Example
----------------------

.. note:: Make sure you have Quanser Interactive Labs open before running any of these examples.

.. tip:: If you are struggling to get this example running check out our _Troubleshooting page.

"""
# imports to important libraries
import sys
import math
import time
sys.path.append('../libraries/')
from library_qlabs import QuanserInteractiveLabs
from library_qlabs_free_camera import QLabsFreeCamera
from library_qlabs_widget import QLabsWidget

def widgets(qlabs):
    # initialize the widget class in qlabs
    widget = QLabsWidget(qlabs)
    
    # choose to show shadows on our objects since we aren't going to be spawning a lot of widgets
    widget.widget_spawn_configuration(enableShadow=True)

    # create 10 cubes of a variety of shades of red
    for count in range(10):
        widget.spawn_degrees(widgetType = widget.CUBE, location = [-15.504, 34.584+count*0.01, 1+count*0.6], rotation = [90,0,0], scale = [0.5,0.5,0.5], color = [1,0+count*0.03,0+count*0.02], measuredMass=0, IDTag=0, properties='', waitForConfirmation=True)

    time.sleep(2)

    # create 20 grey metal cans and place them at slightly different spots
    for count in range(20):
        widget.spawn(widgetType = widget.METAL_CAN, location = [-15.504, 32.584, 1+count*0.2], rotation = [0,0,0], scale = [1,1,1], color = [1,1,1], measuredMass=0, IDTag=0, properties='', waitForConfirmation=True)

    time.sleep(1)

    # create 20 plastic bottles of a variety of shades of blue
    for count in range(20):
        widget.spawn_degrees(widgetType = widget.PLASTIC_BOTTLE, location = [-15.504, 32.584, 1+count*0.2], rotation = [90,0,0], scale = [1,1,1], color = [count*0.01 ,count*0.02, 1], measuredMass=0, IDTag=0, properties='', waitForConfirmation=True)

    time.sleep(1)

    # create 10 spheres of a ombre of red to yellow
    for count in range(10):
        widget.spawn_degrees(widgetType = widget.SPHERE, location = [-15.504, 38.584+count*0.01, 1+count*0.6], rotation = [90,0,0], scale = [0.5,0.5,0.5], color = [1,0+ count*0.05,0+ count*0.01], measuredMass=0, IDTag=0, properties='', waitForConfirmation=True)

    time.sleep(5)

    # destroy widgets so that they don't continue to consume resources rolling around
    #widget.destroy_all_spawned_widgets()

def main():

    # creates a server connection with Quanser Interactive Labs and manages 
    # the communications
    qlabs = QuanserInteractiveLabs()

    # initialize our desired variables 
    # note that you can use the coordinate helper to pick locations for your camera.
    loc = [-23.201, 34.875, 3.482]
    rot = [0, 20.023, -2.275]

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