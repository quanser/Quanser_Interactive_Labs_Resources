"""
Free Camera Library Example
---------------------------

.. note::

    Make sure you have Quanser Interactive Labs open before running this
    example.  This example is designed to best be run in QCar Cityscape.

"""
# imports to important libraries
import time
import cv2

from qvl.qlabs import QuanserInteractiveLabs
from qvl.free_camera import QLabsFreeCamera
from qvl.system import QLabsSystem

def main():

    # creates a server connection with Quanser Interactive Labs and manages
    # the communications
    qlabs = QuanserInteractiveLabs()
    
    

    # initialize our desired variables
    # note that you can use the coordinate helper to pick locations for your camera.
    loc = [-5.631, -1.467, 2.198]
    rot = [0, -2.386, -20.528]

    # trying to connect to QLabs and open the instance we have created - program will end if this fails
    print("Connecting to QLabs...")
    try:
        qlabs.open("localhost")
    except:
        print("Unable to connect to QLabs")
        return

    # destroy any spawned actors in our QLabs that currently exist
    qlabs.destroy_all_spawned_actors()

    title = QLabsSystem(qlabs)
    title.set_title_string("Camera Tutorial")

    # create a camera in this qlabs instance
    camera = QLabsFreeCamera(qlabs)
    # add a custom camera at a specified location and rotation using degrees
    camera.spawn_degrees(location=loc, rotation=rot)
    # to switch our view from our current camera to the new camera we just initialized
    camera.possess()

    time.sleep(3)

    camera.set_camera_properties(60, 1, 2.0, 1.3)

    [success, location, rotation, scale] = camera.get_world_transform()

    ping = camera.ping()

    # Take a image from the first camera angle 
    if ping:
        camera.set_image_capture_resolution()
        [success, image1] = camera.get_image()
        
        if not success:
            print("Image decoding failure")
        # if success:
        #     cv2.imshow('image1',image1)
        # else:
        #     print("Image decoding failure")
            
        
    time.sleep(2)    

    # Initialize and spawn the second camera angle 
    loc2 = [-33.17276819, 13.50500671, 2.282]
    rot2 = [0, 0.077, 0.564]
    camera2 = QLabsFreeCamera(qlabs)
    x = camera2.spawn_id(2, loc2, rot2)
    camera2.possess()

    time.sleep(2)

    camera.destroy()

    [success, location, rotation, scale] = camera2.get_world_transform()
    camera2.set_camera_properties(40, True, 2.3, 0.6)

    time.sleep(2)

    # Focus the camera 
    for y in range(1, 52):
        camera2.set_camera_properties(40, True, 2.3, (0.6 + ((y / 50) ** 3) * 23.7))

    camera.set_image_capture_resolution()

    # Take image of the second camera angle 
    [success, image2] = camera.get_image()
    print(success)

    time.sleep(2)

    # Initialize and spawn the third camera angle 
    camera3 = QLabsFreeCamera(qlabs)
    loc3 = [-21.456, 31.995, 3.745]
    rot3 = [0, 18.814, 0.326]
    camera3.spawn_degrees(loc3, rot3)
    camera3.possess()

    # Display a image of the first camera angle 
    cv2.imshow('image1',image1)
    cv2.waitKey(0)

    # Closing qlabs
    qlabs.close()
    print('Done!')

if __name__ == "__main__":
    main()
