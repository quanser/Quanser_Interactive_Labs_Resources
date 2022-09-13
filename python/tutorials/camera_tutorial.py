"""
Camera Testing Examples
-----------------------

.. note:: Make sure you have Quanser Interactive Labs open before running any of these examples.

.. tip:: If you are struggling to get this example running check out our _Troubleshooting page.

"""
# imports to important libraries we will 
import sys
sys.path.append('../libraries/')

from library_qlabs import QuanserInteractiveLabs
from library_qlabs_common import QLabsCommon
from library_qlabs_free_camera import QLabsFreeCamera

# creates a server connection with Quanser Interactive Labs and manages the communications
qlabs = QuanserInteractiveLabs()

# initialize our variables 
# note that you can use the ..Coordinate Helper to pick locations for your camera.
location = [15, 10, 15]
rotation = [-0, 0.817, 2.159]

# not sure if this is needed
print("Connecting to QLabs...")
qlabs.open("localhost")

QLabsCommon().destroy_all_spawned_actors(qlabs)

# add a custom camera at a specified location and rotation using radians
QLabsFreeCamera().spawn(qlabs, location=location, rotation=rotation)

# to switch our view from our current camera to the new camera we just initialized
QLabsFreeCamera().possess(qlabs, 0)
print("magic")
