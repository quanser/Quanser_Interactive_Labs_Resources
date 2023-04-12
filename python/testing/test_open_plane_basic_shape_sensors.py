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
    hCamera.possess()

    ### Shapes
    
    hShape1 = QLabsBasicShape(qlabs)
    hShape1.spawn(location=[0,0,1], rotation=[0,0,0], scale=[1,1,1], configuration=3)
    success, color, roughness, metallic = hShape1.get_material_properties()
    print("Read success: {}, Color: {}, Roughness: {:.2f}, Metallic: {}".format(success, color, roughness, metallic))

    hShape1.set_material_properties(color=[1,0,0], roughness=0.0, metallic=True, waitForConfirmation=True)
    success, color, roughness, metallic = hShape1.get_material_properties()
    print("Read success: {}, Color: {}, Roughness: {:.2f}, Metallic: {}".format(success, color, roughness, metallic))


    qlabs.close()
    print("Done!")


main()


