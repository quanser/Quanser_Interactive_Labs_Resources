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

def main():

    # creates a server connection with Quanser Interactive Labs and manages 
    # the communications
    qlabs = QuanserInteractiveLabs()

    # initialize our desired variables 
    # note that you can use the coordinate helper to pick locations for your camera.
    loc = [-23.201, 34.875, 3.482]
    rot = [0, 20.023, -2.275]

    # trying to connect to QLabs and open the instance we have created - program will end if this fails
    print("Connecting to QLabs...")
    try:
        qlabs.open("localhost")
    except:
        print("Unable to connect to QLabs")
        return

    # destroy any spawned actors in our QLabs that currently exist
    qlabs.destroy_all_spawned_actors()

    # create a camera in this qlabs instance
    camera = QLabsFreeCamera(qlabs)

    # add a custom camera at a specified location and rotation using degrees
    camera.spawn_degrees(location=loc, rotation=rot)

    # to switch our view from our current camera to the new camera we just initialized
    camera.possess()


    widget = QLabsWidget()
    widget.widget_spawn_configuration(qlabs, enableShadow=True)

    for count in range(20):
        widget.spawn(qlabs, widget.METAL_CAN, [-15.504, 32.584, 1+count*0.2], [0,0,0], [1,1,1], [1,1,1], measuredMass=0, IDTag=0, properties='', waitForConfirmation=True)

    time.sleep(1)

    for count in range(20):
        widget.spawn_degrees(qlabs, widget.METAL_CAN, [-15.504, 32.584, 1+count*0.2], [90,0,0], [1,1,1], [1,0,0], measuredMass=0, IDTag=0, properties='', waitForConfirmation=True)

    time.sleep(1)

    #hQLabsWidget.destroy_all_spawned_widgets(qlabs)
    widget.widget_spawn_configuration(qlabs, enableShadow=False)

    for count in range(15):
        widget.spawn_degrees(qlabs, widget.SPHERE, [-15.504, 32.584+count*0.01, 1+count*0.6], [90,0,0], [0.5,0.5,0.5], [1,0,0], measuredMass=0, IDTag=0, properties='', waitForConfirmation=True)

    time.sleep(1)

    #hQLabsWidget.destroy_all_spawned_widgets(qlabs)
    widget.widget_spawn_configuration(qlabs, enableShadow=True)

    for count in range(10):
        widget.spawn_degrees(qlabs, widget.SPHERE, [-15.504, 32.584+count*0.01, 1+count*0.6], [90,0,0], [0.5,0.5,0.5], [1,0,0], measuredMass=0, IDTag=0, properties='', waitForConfirmation=True)

if __name__ == "__main__":
    main()