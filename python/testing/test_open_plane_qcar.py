from qvl.qlabs import QuanserInteractiveLabs
from qvl.free_camera import QLabsFreeCamera
from qvl.basic_shape import QLabsBasicShape
from qvl.system import QLabsSystem
from qvl.walls import QLabsWalls
from qvl.flooring import QLabsFlooring
from qvl.qcar import QLabsQCar
from qvl.spline_line import QLabsSplineLine


import sys
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

    ### Flooring
    hFloor = QLabsFlooring(qlabs)
    hFloor.spawn([0.199, -0.491, 0.005])

    ### Walls
    hWall = QLabsWalls(qlabs)

    for x in range(4):
        hWall.spawn(location=[-3.072, -2.096+x*1.1, 0.5], rotation=[0, 0, 0])
        hWall.set_enable_dynamics(True)
        hWall.spawn(location=[3.4, -2.096+x*1.1, 0.5], rotation=[0, 0, 0])
        hWall.set_enable_dynamics(True)

    for y in range(5):
        hWall.spawn_degrees(location=[2.52-y*1.1, -3.062, 0.5], rotation=[0, 0, 90])
        hWall.set_enable_dynamics(True)
        hWall.spawn_degrees(location=[2.52-y*1.1, 2.0, 0.5], rotation=[0, 0, 90])
        hWall.set_enable_dynamics(True)

    hWall.spawn_degrees(location=[2.975, 1.564, 0.5], rotation=[0, 0, 45])
    hWall.set_enable_dynamics(True)

    hWall.spawn_degrees(location=[2.843, -2.46, 0.5], rotation=[0, 0, -45])
    hWall.set_enable_dynamics(True)

    hQCar = QLabsQCar(qlabs)
    hQCar.spawn_id_degrees(0, location=[1.75, -0.626, 0.01], rotation=[0,0,0], scale=[0.1,0.1,0.1])





    steps = 100

    for count in range(steps):
        t = count/steps
        hCamera.set_transform(lerp_v3( [-7.169, 1.386, 3.227], [-5.505, -5.092, 2.618], sigmoid(t)), lerp_v3( [0, 0.331, 0.272], [0, 0.287, 0.586], sigmoid(t)) )
        time.sleep(0.01)

    ### Road

    hSpline = QLabsSplineLine(qlabs)

    hSpline.spawn()

    y = 6
    x_start = -3.1
    x_end = 300
    road_width = 7
    line_width = 0.2
    dash_length = 1

    hSpline.set_points([0.01,0.01,0.01], [[x_start,y,0.01, road_width], [x_end,y,0.01,road_width]], False, False)

    hSpline.spawn()
    hSpline.set_points([1,1,1], [[x_start,y-road_width/2+line_width*1.5,0.02, line_width], [x_end,y-road_width/2+line_width*1.5,0.02,line_width]], False, False)

    hSpline.spawn()
    hSpline.set_points([1,1,1], [[x_start,y+road_width/2-line_width*1.5,0.02, line_width], [x_end,y+road_width/2-line_width*1.5,0.02,line_width]], False, False)

    dash_count = int((x_end-x_start)/(dash_length*2))
    print(dash_count)


    hQCar2 = QLabsQCar(qlabs)
    hQCar2.spawn_id_degrees(1, location=[x_start+1, y-road_width/4, 0.01], rotation=[0,0,0], scale=[1,1,1])


    for count in range(dash_count):
        hSpline.spawn()
        hSpline.set_points([0.8,0.8,0], [[x_start+dash_length*2*count,y,0.02, line_width], [x_start+dash_length*2*count+dash_length,y,0.02,line_width]], False, False)




    qlabs.close()
    print("Done!")


main()


