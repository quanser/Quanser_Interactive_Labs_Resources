"""
Multiagent Example
----------------------------

.. note::
    Make sure you have the teaching or research resources from the Quanser website 
    downloaded. It will not find the necessary files if you do not have them.

    Make sure to only try to spawn robots your Quanser Interactive Labs license
    allows for. It will not spawn robots you do not have access to. 

    Make sure you have Quanser Interactive Labs open before running this
    example.  This example is designed to best be run in any of the Open World environments.

"""

#imports to necessary libraries
import time
import numpy as np
from qvl.multi_agent import MultiAgent, readRobots
from qvl.qlabs import QuanserInteractiveLabs
from qvl.free_camera import QLabsFreeCamera
from qvl.basic_shape import QLabsBasicShape
import sys

qlabs = QuanserInteractiveLabs()
    
print("Connecting to QLabs...")
if (not qlabs.open("localhost")):
    print("Unable to connect to QLabs") 
    sys.exit()  

print("Connected")  

qlabs.destroy_all_spawned_actors()

# create a camera in this qlabs instance
camera = QLabsFreeCamera(qlabs)
camera.spawn_degrees(location=[0.063, 1.9, 0.603], rotation=[0, 9.186, -83.687])
# to switch our view to the new camera we just initialized
camera.possess()

# add shapes in the space
rectangle2 = QLabsBasicShape(qlabs)
rectangle2.spawn(location=[-1,-.8,0], rotation=[0,0,0], scale=[.2,.2,1], configuration=QLabsBasicShape.SHAPE_CUBE, waitForConfirmation=True)
rectangle2.set_material_properties(color=[0,1,0])
time.sleep(1)
cone = QLabsBasicShape(qlabs)
cone.spawn(location=[0.7,-.4,0], rotation=[0,0,0], scale=[.2,.2,1], configuration=QLabsBasicShape.SHAPE_CONE, waitForConfirmation=True)
cone.set_material_properties(color=[0,0,1])
time.sleep(.5)

qlabs.close()

print("Disconnected from camera and object spawn") 

time.sleep(1)

# Initialize an empty list (not a dictionary, because dictionaries are key-value pairs)
myRobots = []

# Adding a new robot to the list
# comment out robots that you may not be licensed for

#QCar 2 needs to be spawned at a smaller scale since it is made to work in
# cityscape where it is made to spawn the size of a real car. 
# as a 1/10th car, spawning at 0.1 scale will make it the size of the real
# QCar 2
myRobots.append({
    "RobotType": "QCar2", 
    "Location": [-.5, 0, 0], 
    "Rotation": [0, 0, 90], 
    "Scale": .1,
    "ActorNumber" : 5 # set actor number to 5
})


myRobots.append({
    "RobotType": "QD2", 
    "Location": [1, 0.5, 0], 
    "Rotation": [0, 0, 90], 
    "Scale": 1
})
 
myRobots.append({
    "RobotType": "QBP", 
    "Location": [.15, -.3, -0], 
    "Rotation": [0, 0, 90], 
})

# only need to call this once, and it will spawn and initialize all necessary
# RT files to start talking to the Robots.
mySpawns = MultiAgent(myRobots)

# list of QLabs objects that were spawned
actors = mySpawns.robotActors

print(actors)
print(actors[0].actorNumber)
print(actors[0].classID)

# this is how to still use the actor functions with the spawns
# setting the color of the LED strip on the QCar 2 to purple
# these functions are directly from qvl.qcar2
actors[0].set_led_strip_uniform(color=[1,0,1])

# robotsDict should be the same as the output of readRobots(). 
# Use readRobots when reading the JSON file from a different python file.
actorsDict = mySpawns.robotsDict
print(actorsDict)

robotsDir = readRobots()
print(robotsDir)

# this would be used when initializing a QCar 2 using HIL to find the assigned port.
print(robotsDir["QC2_5"]["hilPort"]) 

mySpawns.qlabs.close()



