"""
Road Signage Library Example
----------------------------

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
from library_qlabs_crosswalk import QLabsCrosswalk
from library_qlabs_roundabout_sign import QLabsRoundaboutSign
from library_qlabs_yield_sign import QLabsYieldSign
from library_qlabs_stop_sign import QLabsStopSign 
from library_qlabs_traffic_cone import QLabsTrafficCone
from library_qlabs_traffic_light import QLabsTrafficLight

# set any of these flags to False if you don't want to see the output
CROSSWALK_FLAG = True
ROUNDABOUT_FLAG = True
YIELDSIGN_FLAG = True
STOPSIGN_FLAG = True
TRAFFICCONE_FLAG = True
TRAFFICLIGHT_FLAG = True

def crosswalk(qlabs):
    """This method demonstrates some basic commands with the crosswalk class"""
    
    # initialize a camera - See Camera Actor Library Reference for more information
    cameraCrosswalk = QLabsFreeCamera(qlabs)
    cameraCrosswalk.spawn(location=[-25.286, 46.167, 5.333], rotation=[-0, 0.239, -0.043])
    cameraCrosswalk.possess()

    # create a crosswalk in this qlabs instance
    crosswalk = QLabsCrosswalk(qlabs)

    # spawn crosswalk with radians in config
    crosswalk.spawn_id(actorNumber=0, location=[-15.788, 47.5, 0.00], rotation=[0,0,math.pi/2], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    # waits so we can see the output
    time.sleep(1)
    # spawn crosswalk with degrees in config 1
    crosswalk.spawn_id_degrees(actorNumber=1, location=[-11.788, 47.5, 0.00], rotation=[0,0,90], scale=[1,1,1], configuration=1, waitForConfirmation=True)
    # waits so we can see the output
    time.sleep(1)
    # spawn crosswalk with degress in config 2
    crosswalk.spawn_id_degrees(actorNumber=2, location=[-7.8, 47.5, 0.0], rotation=[0,0,90], scale=[1,1,1], configuration=2, waitForConfirmation=True)
    
    # collecting the world transform coordinates of the crosswalk
    x, loc, rot, scale = crosswalk.get_world_transform()
    print( x, loc, rot, scale)
    
    # pinging existing sign - this should return True if we printed it
    crosswalk.ping()
   


def roundabout_sign(qlabs):
    """This method demonstrates some basic commands with the roundabout sign class"""

    # create two roundabouts in this qlabs instance
    roundabout = QLabsRoundaboutSign(qlabs)
    roundabout2 = QLabsRoundaboutSign(qlabs)

    # spawns the sign we just created using radians and specifying the actorNumber
    roundabout.spawn_id(actorNumber=0, location=[-17, 36, 0.0], rotation=[0, 0, math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)    
    # spawns the second sign we just created using degrees and allowing the computer to 
    # generate an actorNumber internally
    roundabout2.spawn_id_degrees(actorNumber=2, location=[-15, 36, 0.0], rotation=[0,0,180], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    
    # collecting the world transform coordinates of the roundabout sign
    x, loc, rot, scale = roundabout2.get_world_transform()
    print( x, loc, rot, scale)

    # pinging existing sign - this should return True if we printed it
    roundabout2.ping()
    # waits so we can see the output
    time.sleep(1)

    # destroying the sign we just created
    roundabout.destroy()


def yield_sign(qlabs):
    """This method demonstrates some basic commands with the yield sign class"""

    # create two yieldsigns in this qlabs instance
    yieldsign = QLabsYieldSign(qlabs)
    yieldsign2 = QLabsYieldSign(qlabs)

    # spawns the sign we just created using radians and specifying the actorNumber
    yieldsign.spawn_id(actorNumber=0, location=[-17, 38, 0.0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    # spawns the second sign we just created using degrees and allowing the computer to 
    # generate an actorNumber internally
    yieldsign2.spawn_degrees(location=[-15, 38, 0.0], rotation=[0,0,180], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    
    # collecting the world transform coordinates of the yield sign
    x, loc, rot, scale = yieldsign2.get_world_transform()
    print( x, loc, rot, scale)
    
    # pinging existing sign - this should return "True" if we printed it
    yieldsign2.ping()
    # waits so we can see the output
    time.sleep(1) 

    # destroying the sign we just created
    yieldsign.destroy()


def stop_sign(qlabs):
    """This method demonstrates some basic commands with the stop sign class"""

    # create two stop signs in this qlabs instance
    stop = QLabsStopSign(qlabs)
    stop2 = QLabsStopSign(qlabs)
    # spawns the sign we just created using radians
    stop.spawn_id(actorNumber=1, location=[-16, 37, 0.0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    # spawns the second sign we just created using degrees and generating the actorNumber internally
    stop2.spawn_degrees(location=[-15, 37, 0.0], rotation=[0,0,180], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    
    # collecting the world transform coordinates of the stop sign
    x, loc, rot, scale = stop2.get_world_transform()
    print(x, loc, rot, scale)
    
    # pinging existing sign - this should return True if we printed it
    stop2.ping()
    # waits so we can see the output
    time.sleep(1)

    # destroying the sign we just created
    stop.destroy()
    

def traffic_cone(qlabs):
    """This method demonstrates some basic commands with the traffic cone class"""

    # creates 3 cones in this qlabs instance
    cone = QLabsTrafficCone(qlabs)
    cone1 = QLabsTrafficCone(qlabs)
    cone2 = QLabsTrafficCone(qlabs)

    # spawns a small traffic cone we just initialized using radians
    cone.spawn(location=[-17, 35, 1.0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    # waits so we can see the output
    time.sleep (1)
    # destroy the cone we just made
    cone.destroy()
    # waits so we can see the output
    time.sleep(1)
    # spawns another small traffic cone we just initialized using radians in the same place
    cone1.spawn_id(actorNumber=1, location=[-17, 35, 1.0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    # spawns a construction pylon using the cone we just initialized using degrees and generating 
    # the actorNumber internally
    cone2.spawn_degrees(location=[-15, 35, 1.0], rotation=[0,0,180], scale=[1,1,1], configuration=1, waitForConfirmation=True)
   
    # collecting the world transform coordinates of the traffic cone
    x, loc, rot, scale = cone2.get_world_transform()
    print(x, loc, rot, scale)
    
    # pinging existing cone - this should return True if we printed it
    cone2.ping()


def traffic_light(qlabs):
    """This method demonstrates some basic commands with the traffic light class"""

    # initialize a camera - See Camera Actor Library Reference for more information
    cameraTraffic = QLabsFreeCamera(qlabs)
    cameraTraffic.spawn(location=[-6.891, 3.568, 2.127], rotation=[0, 0.049, 1.105])
    cameraTraffic.possess()

    # initialize three traffic light instances in qlabs
    trafficLight = QLabsTrafficLight(qlabs)
    trafficLight2 = QLabsTrafficLight(qlabs)
    trafficLight3 = QLabsTrafficLight(qlabs)

    # spawn a traffic light in config 1 - vertical using radians and specifying a specific actorNumber
    trafficLight.spawn_id(actorNumber=0, location=[-0.044, 17.715, 0.215], rotation=[0,0,0], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    # spawn a second traffic light using degrees in config 1 - vertical and specifying a specific actorNumber
    trafficLight2.spawn_id_degrees(actorNumber=2, location=[-8.455, 17.527, 0.215], rotation=[0,0,180], scale=[1,1,1], configuration=1, waitForConfirmation=True)
    # spawn traffic light using degrees in config 2 - horizontal and generating the actorNumber internally
    trafficLight3.spawn_degrees(location=[-0.195, 7.261, 0.215], rotation=[0,0,-90], scale=[1,1,1], configuration=2, waitForConfirmation=True)
    
    # collecting the world transform coordinates of the traffic light
    x, loc, rot, scale = trafficLight2.get_world_transform()
    print(x, loc, rot, scale)
    
    # pinging existing traffic light - this should return True if we printed it
    trafficLight2.ping()
    
    # changing the state of the traffic lights from green to red
    trafficLight.set_state(state=trafficLight.STATE_GREEN, waitForConfirmation=True)
    trafficLight2.set_state(state=trafficLight2.STATE_GREEN, waitForConfirmation=True)
    trafficLight3.set_state(state=trafficLight3.STATE_RED, waitForConfirmation=True)

    time.sleep(2)
    
    trafficLight.set_state(state=trafficLight.STATE_YELLOW, waitForConfirmation=True)
    trafficLight2.set_state(state=trafficLight2.STATE_YELLOW, waitForConfirmation=True)

    time.sleep(1)

    trafficLight.set_state(state=trafficLight.STATE_RED, waitForConfirmation=True)
    trafficLight2.set_state(state=trafficLight2.STATE_RED, waitForConfirmation=True)
    
    time.sleep(1)

    trafficLight3.set_state(state=trafficLight3.STATE_GREEN, waitForConfirmation=True)

    # destroying a traffic light
    trafficLight.destroy()


def main():
    
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

    if CROSSWALK_FLAG == True:
        crosswalk(qlabs)
        time.sleep(2)

    # switch the camera angle from whatever it was previous to be able to see where we will be 
    # spawning the rest of the objects - see Camera Actor Library Reference for more information
    if ROUNDABOUT_FLAG or YIELDSIGN_FLAG or STOPSIGN_FLAG or TRAFFICCONE_FLAG:
        camera0 = QLabsFreeCamera(qlabs)
        camera0.spawn(location=[-23.106, 37.257, 3.482], rotation=[0, 0.349, -0.04])
        camera0.possess()

        if ROUNDABOUT_FLAG:
            roundabout_sign(qlabs)
            time.sleep(1)
        
        if YIELDSIGN_FLAG:
            yield_sign(qlabs)
            time.sleep(1)
        
        if STOPSIGN_FLAG:
            stop_sign(qlabs)
            time.sleep(1)
        
        if TRAFFICCONE_FLAG:
            traffic_cone(qlabs)
            time.sleep(1)
    
    if TRAFFICLIGHT_FLAG:
        traffic_light(qlabs)


if __name__ == "__main__":
    main()









