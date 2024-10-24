"""
Road Signage Library Example
----------------------------

.. note::

    Make sure you have Quanser Interactive Labs open before running this
    example.  This example is designed to best be run in QCar Cityscape 
    or Cityscape Lite. This is an example of a typical setup script
    to populate the city with signage for subsequent use in a vehicle
    simulation.

"""

# imports to important libraries
import time
import math

from qvl.qlabs import QuanserInteractiveLabs
from qvl.free_camera import QLabsFreeCamera
from qvl.crosswalk import QLabsCrosswalk
from qvl.roundabout_sign import QLabsRoundaboutSign
from qvl.system import QLabsSystem
from qvl.yield_sign import QLabsYieldSign
from qvl.stop_sign import QLabsStopSign
from qvl.traffic_cone import QLabsTrafficCone
from qvl.traffic_light import QLabsTrafficLight


# specify if you want the signage on the left or right side of the road.
right_hand_driving = True

def main(right_hand_driving):

    # creates a server connection with Quanser Interactive Labs and manages the communications
    qlabs = QuanserInteractiveLabs()

    # trying to connect to QLabs and open the instance we have created - program will end if this fails
    print("Connecting to QLabs...")
    if (not qlabs.open("localhost")):
        print("Unable to connect to QLabs")
        return    

    print("Connected") 

    # destroying any spawned actors in our QLabs that currently exist
    qlabs.destroy_all_spawned_actors()

    # Use hSystem to set the tutorial title on the qlabs display screen
    hSystem = QLabsSystem(qlabs)
    hSystem.set_title_string('Complete Road Signage Tutorial')
    
    spawn_crosswalk(qlabs)
    spawn_signs(qlabs, right_hand_driving)
    spawn_traffic_lights(qlabs, right_hand_driving)
    spawn_cones(qlabs)

    fly_through_animation(qlabs)
    
    # Closing qlabs
    qlabs.close()
    print('Done!')




def spawn_crosswalk(qlabs):
    # Create a crosswalk in this qlabs instance. Since we don't need
    # to access the actors again after creating them, we can use a single
    # class object to spawn all the varieties. We also don't need to use
    # the waitForConfirmation because we don't need to store the actor ID
    # for future reference.

    crosswalk = QLabsCrosswalk(qlabs)

    # spawn crosswalk with radians in config 0
    crosswalk.spawn_degrees(location=[-12.992, -7.407, 0.005], rotation=[0,0,48], scale=[1,1,1], configuration=0, waitForConfirmation=False)
    
    # spawn crosswalk with degrees in config 1
    crosswalk.spawn_degrees(location=[-6.788, 45, 0.00], rotation=[0,0,90], scale=[1,1,1], configuration=1, waitForConfirmation=False)
    
    # spawn crosswalk with degrees in config 2
    crosswalk.spawn_degrees(location=[21.733, 3.347, 0.005], rotation=[0,0,0], scale=[1,1,1], configuration=2, waitForConfirmation=False)

    # spawn the last crosswalk with waitForConfirmation=True to confirm everything is flushed from the send buffers
    crosswalk.spawn_degrees(location=[21.733, 16, 0.005], rotation=[0,0,0], scale=[1,1,1], configuration=2, waitForConfirmation=True)


def spawn_signs(qlabs, right_hand_driving):
    # Like the crosswalks, we don't need to access the actors again after
    # creating them.

    roundabout_sign = QLabsRoundaboutSign(qlabs)
    yield_sign = QLabsYieldSign(qlabs)
    stop_sign = QLabsStopSign(qlabs)

    if (right_hand_driving):
        stop_sign.spawn_degrees([17.561, 17.677, 0.215], [0,0,90])
        stop_sign.spawn_degrees([24.3, 1.772, 0.2], [0,0,-90])
        stop_sign.spawn_degrees([14.746, 6.445, 0.215], [0,0,180])

        roundabout_sign.spawn_degrees([3.551, 40.353, 0.215], [0,0,180])
        roundabout_sign.spawn_degrees([10.938, 28.824, 0.215], [0,0,-135])
        roundabout_sign.spawn_degrees([24.289, 32.591, 0.192], [0,0,-90])

        # spawn the actor with waitForConfirmation=True to confirm everything is flushed from the send buffers
        yield_sign.spawn_degrees(location=[-2.169, -12.594, 0.2], rotation=[0,0,180], waitForConfirmation=True)
    else:
        stop_sign.spawn_degrees([24.333, 17.677, 0.215], [0,0,90])
        stop_sign.spawn_degrees([18.03, 1.772, 0.2], [0,0,-90])
        stop_sign.spawn_degrees([14.746, 13.01, 0.215], [0,0,180])

        roundabout_sign.spawn_degrees([16.647, 28.404, 0.215], [0,0,-45])
        roundabout_sign.spawn_degrees([6.987, 34.293, 0.215], [0,0,-130])
        roundabout_sign.spawn_degrees([9.96, 46.79, 0.2], [0,0,-180])

        # spawn the actor with waitForConfirmation=True to confirm everything is flushed from the send buffers
        yield_sign.spawn_degrees(location=[-21.716, 7.596, 0.2], rotation=[0,0,-90], waitForConfirmation=True)


def spawn_traffic_lights(qlabs, right_hand_driving):
    # In this case, we want to track each traffic light individually so we
    # can subsequently set the color state.  By using spawning with an ID,
    # we'll know exactly which one is which and this will allow us to also
    # reference them in separate programs, and we can also spawn without
    # waiting for confirmation because the object already knows its own ID.


    # initialize four traffic light instances in qlabs
    trafficLight1 = QLabsTrafficLight(qlabs)
    trafficLight2 = QLabsTrafficLight(qlabs)
    trafficLight3 = QLabsTrafficLight(qlabs)
    trafficLight4 = QLabsTrafficLight(qlabs)

    if (right_hand_driving):
        
        trafficLight1.spawn_id_degrees(actorNumber=0, location=[5.889, 16.048, 0.215], rotation=[0,0,0], configuration=0, waitForConfirmation=False)
        trafficLight2.spawn_id_degrees(actorNumber=1, location=[-2.852, 1.65, 0], rotation=[0,0,180], configuration=0, waitForConfirmation=False)
        trafficLight1.set_color(color=trafficLight1.COLOR_GREEN, waitForConfirmation=False)
        trafficLight2.set_color(color=trafficLight2.COLOR_GREEN, waitForConfirmation=False)

        trafficLight3.spawn_id_degrees(actorNumber=3, location=[8.443, 5.378, 0], rotation=[0,0,-90], configuration=0, waitForConfirmation=False)
        trafficLight4.spawn_id_degrees(actorNumber=4, location=[-4.202, 13.984, 0.186], rotation=[0,0,90], configuration=0, waitForConfirmation=False)
        trafficLight3.set_color(color=trafficLight3.COLOR_RED, waitForConfirmation=False)
        trafficLight4.set_color(color=trafficLight4.COLOR_RED, waitForConfirmation=False)  

    else:
        trafficLight1.spawn_id_degrees(actorNumber=0, location=[-2.831, 16.643, 0.186], rotation=[0,0,180], configuration=1, waitForConfirmation=False)
        trafficLight2.spawn_id_degrees(actorNumber=1, location=[5.653, 1.879, 0], rotation=[0,0,0], configuration=1, waitForConfirmation=False)
        trafficLight1.set_color(color=trafficLight1.COLOR_GREEN, waitForConfirmation=False)
        trafficLight2.set_color(color=trafficLight2.COLOR_GREEN, waitForConfirmation=False)

        trafficLight3.spawn_id_degrees(actorNumber=3, location=[8.779, 13.7, 0.215], rotation=[0,0,90], configuration=1, waitForConfirmation=False)
        trafficLight4.spawn_id_degrees(actorNumber=4, location=[-4.714, 4.745, 0], rotation=[0,0,-90], configuration=1, waitForConfirmation=False)
        trafficLight3.set_color(color=trafficLight3.COLOR_RED, waitForConfirmation=False)
        trafficLight4.set_color(color=trafficLight4.COLOR_RED, waitForConfirmation=False)                



def spawn_cones(qlabs):
    
    # We'll assume the cones don't need to be referenced after they're spawned so a
    # single class object will suffice for spawning.
    
    cone = QLabsTrafficCone(qlabs)

    for count in range(10):
        # Since we're going to set the color, we need to wait for QLabs to assign
        # an actor number.  This can be executed more quickly if you spawn by ID
        # instead and manually assign the numbers.
        #
        # Also note that since this are physics objects, it's a good idea to
        # spawn the actors slight above the surface so they can fall into place.
        # If you spawn exactly at ground level, they may "pop" up from the surface.

        cone.spawn(location=[-15.313, 35.374+count*-1.3, 0.25], configuration=1, waitForConfirmation=True)
        cone.set_material_properties(materialSlot=0, color=[0,0,0],roughness=1,metallic=False)
        cone.set_material_properties(materialSlot=1, color=HSVtoRGB([count/10, 1, 1]))        


def HSVtoRGB(hsv):

    H = hsv[0]
    S = hsv[1]
    V = hsv[2]

    kr = (5+H*6) % 6
    kg = (3+H*6) % 6
    kb = (1+H*6) % 6

    r = 1 - max(min(min(kr, 4-kr), 1), 0)
    g = 1 - max(min(min(kg, 4-kg), 1), 0)
    b = 1 - max(min(min(kb, 4-kb), 1), 0)
    
    return [r, g, b]


def fly_through_animation(qlabs):
    # Linearly interpolate through a series of points to fly the camera
    # around the map. For each source and destination, calculate the distance
    # so the step size is an even multiple that is approximately equal to the 
    # desired velocity. 

    # Translation/rotation point pairs
    points = [[[1.5, -12.558, 1.708], [-0, 0.023, 1.405]],
              [[0.721, -0.922, 1.721], [-0, 0.027, 1.255]],
              [[6.082, 7.208, 1.566], [-0, 0.027, -0.309]],
              [[20.732, 3.179, 1.997], [0, 0.049, 1.452]],
              [[26.083, 30.157, 2.459], [0, 0.153, 2.491]],
              [[17.211, 46.775, 11.61], [-0, 0.348, -2.189+2*math.pi]],
              [[-17.739, 38.866, 0.956], [0, 0.142, -1.385+2*math.pi]],
              [[-16.068, 24.53, 0.628], [-0, -0.043, -1.484+2*math.pi]],
              [[-20.302, 1.82, 1.815], [-0, 0.03, -0.872+2*math.pi]],
              [[-3.261, -14.664, 1.597], [-0, -0.038, 0.894+2*math.pi]]]

    speed = 0.3
    filter_translation_weight = 0.1
    filter_rotation_weight = 0.1


    camera = QLabsFreeCamera(qlabs)
    camera.spawn_id(0,points[0][0], points[0][1])
    camera.possess()

    fx = points[0][0][0]
    fy = points[0][0][1]
    fz = points[0][0][2]

    froll  = points[0][1][0]
    fpitch = points[0][1][1]
    fyaw   = points[0][1][2]

    for index in range(len(points) - 1):
        # Calculate the integer number of steps by dividing the distance by speed
        translation_distance = dist(points[index][0], points[index+1][0])
        total_steps = int(round(translation_distance/speed,0))
        

        for step in range(total_steps):
            # Linearly interpolate between each of the target points
            x = interp(points[index][0][0], points[index+1][0][0], step, total_steps)
            y = interp(points[index][0][1], points[index+1][0][1], step, total_steps)
            z = interp(points[index][0][2], points[index+1][0][2], step, total_steps)

            roll  = interp(points[index][1][0], points[index+1][1][0], step, total_steps)
            pitch = interp(points[index][1][1], points[index+1][1][1], step, total_steps)
            yaw   = interp(points[index][1][2], points[index+1][1][2], step, total_steps)

            # Filter the calcuated values to smooth out the camera motion
            fx = fx*(1-filter_translation_weight) + x*filter_translation_weight
            fy = fy*(1-filter_translation_weight) + y*filter_translation_weight
            fz = fz*(1-filter_translation_weight) + z*filter_translation_weight

            froll = froll*(1-filter_translation_weight) + roll*filter_translation_weight
            fpitch = fpitch*(1-filter_translation_weight) + pitch*filter_translation_weight
            fyaw = fyaw*(1-filter_translation_weight) + yaw*filter_translation_weight            


            # To try to make the animation as consistent as possible across different
            # hardware, measure the elapsed time and delay a variable amount to try
            # to maintain 33 fps.

            start_time = time.time()
            camera.set_transform(location=[fx, fy, fz], rotation=[froll, fpitch, fyaw])
            end_time = time.time()
            if (start_time - end_time < 0.03):
                time.sleep(0.03 - (start_time - end_time))

def dist(v1, v2):
    return pow( pow(v1[0]-v2[0], 2) + pow(v1[1]-v2[1], 2) + pow(v1[2]-v2[2], 2), 0.5 )

def interp(start, finish, step, total_steps):
    return (finish-start)/total_steps*step + start

if __name__ == "__main__":
    main(right_hand_driving)
