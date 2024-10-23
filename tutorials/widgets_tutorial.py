"""
Widget Library Example
----------------------

.. note::

    Make sure you have Quanser Interactive Labs open before running this
    example.  This example is designed to best be run in Cityscape.

"""
# imports to important libraries
import sys
import math
import time

from qvl.qlabs import QuanserInteractiveLabs
from qvl.free_camera import QLabsFreeCamera
from qvl.system import QLabsSystem
from qvl.widget import QLabsWidget

def create_widgets(qlabs):

    # Use hSystem to set the tutorial title in the upper left of the qlabs window 
    hSystem = QLabsSystem(qlabs)
    hSystem.set_title_string('Widgets Tutorial')

    # Create the widget class object in qlabs
    widget = QLabsWidget(qlabs)

    # Hide the shadowns on our first stack of objects. This is a global state that is preserved
    # for all new widgets spawned. Shadows are expensive and can be disabled if spawning a 
    # large number of widgets (thousands).
    widget.widget_spawn_shadow(enableShadow=False)

    # Create 10 cubes of a variety of shades of red
    for count in range(10):
        widget.spawn_degrees(location = [-11.000, 30.000+count*0.01, 1+count*0.6], rotation = [90,0,0], scale = [0.5,0.5,0.5], configuration = widget.CUBE, color = [1,0+count*0.03,0+count*0.02], measuredMass=0, IDTag=0, properties='', waitForConfirmation=True)
    
    # Re-enable shadows for widgets
    widget.widget_spawn_shadow(enableShadow=True)
    
    # Create 20 grey metal cans and place them at slightly different spots
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

    
def main():
    # Initialize our desired variables
    # Note that you can use the coordinate helper to pick locations for your camera.
    loc = [-18.783, 30.023, 2.757]
    rot = [0, 8.932, -2.312]

    # Creates a server connection with Quanser Interactive Labs and manages the communications
    qlabs = QuanserInteractiveLabs()

    print("Connecting to QLabs...")
    if (not qlabs.open("localhost")):
        print("Unable to connect to QLabs")
        return    

    print("Connected")

    # Destroying any spawned actors in our QLabs that currently exist
    qlabs.destroy_all_spawned_actors()

    # Create a camera in this qlabs instance
    camera = QLabsFreeCamera(qlabs)

    # Add a custom camera at a specified location and rotation using degrees
    camera.spawn_degrees(location=loc, rotation=rot)

    # To switch our view from our current camera to the new camera we just initialized
    camera.possess()

    # Run the code for using widgets
    create_widgets(qlabs)

    # Close qlabs
    qlabs.close()
    print('Done!')

if __name__ == "__main__":
    main()