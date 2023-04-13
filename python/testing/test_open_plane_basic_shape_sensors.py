import sys
sys.path.append("../qvl/")

from qvl.qlabs import QuanserInteractiveLabs
from qvl.free_camera import QLabsFreeCamera
from qvl.basic_shape import QLabsBasicShape
from qvl.system import QLabsSystem
from qvl.walls import QLabsWalls
from qvl.flooring import QLabsFlooring
from qvl.qcar import QLabsQCar
from qvl.spline_line import QLabsSplineLine
from qvl.generic_sensor import QLabsGenericSensor



import time
import math
import struct
import numpy as np
import cv2
import xlsxwriter
import os


def sigmoid(t):
    return math.exp(-1*math.exp(-2*((t*2-1))))


def lerp_v1(a, b, t):
    return (a-b)*t + b

def lerp_v3(v1, v2, t):
    return [lerp_v1(v1[0], v2[0], t), lerp_v1(v1[1], v2[1], t),  lerp_v1(v1[2], v2[2], t) ]



def main():
    os.system('cls')

    qlabs = QuanserInteractiveLabs()


    print("Connecting to QLabs...")
    try:
        qlabs.open("localhost")
    except:
        print("Unable to connect to QLabs")
        return

    print("Connected")


    qlabs.destroy_all_spawned_actors()

    ### Free Camera
    hCamera = QLabsFreeCamera(qlabs)
    hCamera.spawn(location=[-5.505, -5.092, 2.618], rotation=[0, 0.287, 0.586])
    #hCamera.possess()

    ### Shapes
    
    hShape1 = QLabsBasicShape(qlabs)
    hShape1.spawn_id(123, location=[0,0,1], rotation=[0,0,0], scale=[1,1,1], configuration=3)
    success, color, roughness, metallic = hShape1.get_material_properties()
    print("Read success: {}, Color: {}, Roughness: {:.2f}, Metallic: {}".format(success, color, roughness, metallic))
    
    success, measuredMass, IDTag, properties, = hShape1.get_custom_properties()
    print("Read success: {}, Measured mass: {:.2f}, ID Tag: {}, Property string: {}".format(success, measuredMass, IDTag, properties))
    
    print("Setting properties...")

    hShape1.set_material_properties(color=[1,0,0], roughness=0.0, metallic=True, waitForConfirmation=True)
    hShape1.set_custom_properties(measuredMass=12.3, IDTag=456, properties="<Prop1>Hello</Prop1><Prop2>World</Prop2>", waitForConfirmation=True)
    
    
    success, color, roughness, metallic = hShape1.get_material_properties()
    print("Read success: {}, Color: {}, Roughness: {:.2f}, Metallic: {}".format(success, color, roughness, metallic))

    success, measuredMass, IDTag, properties, = hShape1.get_custom_properties()
    print("Read success: {}, Measured mass: {:.2f}, ID Tag: {}, Property string: {}".format(success, measuredMass, IDTag, properties))


    ### Beam Actor
    hBeam1 = QLabsGenericSensor(qlabs)
    hBeam1.spawn_degrees(location=[-4,-1,1], rotation=[0,0,0], scale=[1,1,1])
    hBeam1.show_sensor(showBeam=True, showOriginIcon=True, iconScale=0.2, waitForConfirmation=True)
    hBeam1.set_beam_size(startDistance=1, endDistance=5.0, heightOrRadius=0.2, width=0.1, waitForConfirmation=True)

    hShapeTest = QLabsBasicShape(qlabs)

    for i in range(50):
        hBeam1.set_transform_degrees(location=[-4,-1+i/50*2,1], rotation=[0,0,0], scale=[1,1,1])
        success, hit, actorClass, actorNumber, distance = hBeam1.test_beam_hit()

        

        if (hit == True):
            print("Actor class: {}, Actor Number: {}, Distance: {:.3f}".format(actorClass, actorNumber, distance))
            if actorClass == hShapeTest.ID_BASIC_SHAPE:
                hShapeTest.actorNumber = actorNumber
                success, color, roughness, metallic = hShapeTest.get_material_properties()
                print("Read success: {}, Color: {}, Roughness: {:.2f}, Metallic: {}".format(success, color, roughness, metallic))

                success, measuredMass, IDTag, properties, = hShapeTest.get_custom_properties()
                print("Read success: {}, Measured mass: {:.2f}, ID Tag: {}, Property string: {}".format(success, measuredMass, IDTag, properties))
        else:
            print("No hit")
            

        time.sleep(0.05)

    qlabs.close()
    print("Done!")


main()


