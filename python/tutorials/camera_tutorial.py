"""
Free Camera Library Example
---------------------------

.. note::

    Make sure you have Quanser Interactive Labs open before running this
    example.  This example is designed to best be run in QCar Cityscape.

"""
# imports to important libraries
import sys
import time

from qvl.qlabs import QuanserInteractiveLabs
from qvl.free_camera import QLabsFreeCamera


def main():

    # creates a server connection with Quanser Interactive Labs and manages
    # the communications
    qlabs = QuanserInteractiveLabs()
    qlabs.destroy_all_spawned_actors()

    # initialize our desired variables
    # note that you can use the coordinate helper to pick locations for your camera.
    location = [-5.631, -1.467, 2.198] #-53.022, -7.491, 14.475 -58.881, -11.077, 14.475
    rotation = [0, -2.386, -20.528]

    # not sure if this is needed
    print("Connecting to QLabs...")
    qlabs.open("localhost")

    # destroy any spawned actors in the world
    qlabs.destroy_all_spawned_actors()

    # create a camera in this qlabs instance
    camera = QLabsFreeCamera(qlabs)

    # add a custom camera at a specified location and rotation using radians
    camera.spawn_degrees(location=location, rotation=rotation)

    # to switch our view from our current camera to the new camera we just initialized
    camera.possess()

    #time wait to demonstrate the difference between the default camera settings
    # and after we've set the camera properties
    time.sleep(3)

    # set the properties of our camera to customize it - this is not required
    # default camera is set to a FOV: 90 degrees with DOF disabled
    # (which disables aperature and focal distance)
    camera.set_camera_properties(fieldOfView=60, depthOfField=True, aperature=2.0,
                                focusDistance=1.3)

    # collect the current world transform information from the actor camera (should be
    # the same as the one we set).
    x, loc, rot, scale = camera.get_world_transform()
    print(x, loc, rot, scale)

    # ping the existing camera -- we will expect this to return "True", since the camera
    # does indeed exist.
    camera.ping()

    # set the image resolution height and width - here we are just setting them to be
    # the default 640x480
    camera.set_image_capture_resolution()

    # request an image from the camera
    camera.get_image()

    qlabs.close()

if __name__ == "__main__":
    main()
