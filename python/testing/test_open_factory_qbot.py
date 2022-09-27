import sys
library_path = '../libraries'
sys.path.append(library_path)

from library_qlabs import QuanserInteractiveLabs
from library_qlabs_free_camera import QLabsFreeCamera
from library_qlabs_basic_shape import QLabsBasicShape
from library_qlabs_widget import QLabsWidget
from library_qlabs_qbot3 import QLabsQBot3
from library_qlabs_system import QLabsSystem
from library_qlabs_spline_line import QLabsSplineLine
from library_qlabs_real_time import QLabsRealTime


import sys
import time
import math
import struct
import numpy as np
import cv2
import xlsxwriter
import os


basic_shape_id_count = 0

def draw_wall_on_grid(qlabs, start_xy, end_xy):
    global basic_shape_id_count
    height = 0.3
    thickness= 0.05

    origin = [-2.5, -3]
    cell_size = 0.75
    colour = [0.8, 0, 0]

    wall = QLabsBasicShape(qlabs)
    wall.spawn_id_box_walls_from_end_points(basic_shape_id_count, [origin[0]+start_xy[0]*cell_size, origin[1]+start_xy[1]*cell_size, 0], [origin[0]+end_xy[0]*cell_size, origin[1]+end_xy[1]*cell_size, 0], height, thickness, colour, waitForConfirmation=False)
    basic_shape_id_count = basic_shape_id_count + 1


def construct_maze(qlabs):
    draw_wall_on_grid(qlabs, [0,0], [3,0])
    draw_wall_on_grid(qlabs, [1,0], [1,1])
    draw_wall_on_grid(qlabs, [3,0], [3,1])
    draw_wall_on_grid(qlabs, [3,1], [2,1])
    draw_wall_on_grid(qlabs, [2,1], [2,2])
    draw_wall_on_grid(qlabs, [2,2], [1,2])
    

    draw_wall_on_grid(qlabs, [0,0], [0,7])
    draw_wall_on_grid(qlabs, [0,7], [3,7])
    draw_wall_on_grid(qlabs, [3,7], [3,5])
    draw_wall_on_grid(qlabs, [3,5], [5,5])
    draw_wall_on_grid(qlabs, [5,5], [5,6])
    draw_wall_on_grid(qlabs, [5,6], [4,6])
    draw_wall_on_grid(qlabs, [4,7], [7,7])
    draw_wall_on_grid(qlabs, [0,5], [1,5])
    draw_wall_on_grid(qlabs, [1,5], [1,6])
    draw_wall_on_grid(qlabs, [1,6], [2,6])

    
    draw_wall_on_grid(qlabs, [6,7], [6,6])
    draw_wall_on_grid(qlabs, [7,7], [7,0])
    draw_wall_on_grid(qlabs, [7,5], [6,5])
    draw_wall_on_grid(qlabs, [7,5], [6,5])
    
    draw_wall_on_grid(qlabs, [7,2], [5,2])
    draw_wall_on_grid(qlabs, [5,2], [5,4])
    draw_wall_on_grid(qlabs, [5,4], [6,4])
    draw_wall_on_grid(qlabs, [6,4], [6,3])
    draw_wall_on_grid(qlabs, [6,2], [6,1])
    
    draw_wall_on_grid(qlabs, [7,0], [4,0])
    draw_wall_on_grid(qlabs, [5,0], [5,1])
    draw_wall_on_grid(qlabs, [4,0], [4,2])
    draw_wall_on_grid(qlabs, [4,2], [3,2])
    draw_wall_on_grid(qlabs, [3,2], [3,3])
    draw_wall_on_grid(qlabs, [3,3], [1,3])
    draw_wall_on_grid(qlabs, [1,3], [1,4])
    draw_wall_on_grid(qlabs, [1,4], [4,4])
    draw_wall_on_grid(qlabs, [4,4], [4,3])
    draw_wall_on_grid(qlabs, [2,4], [2,5])

  
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
    
    
    hSystem = QLabsSystem()
    x = hSystem.set_title_string(qlabs, 'CUSTOM QBOT EXAMPLE', waitForConfirmation=True)
    
    
    ### Shapes
    construct_maze(qlabs)
    
    hSpline = QLabsSplineLine(qlabs)
    
    lineWidth = 0.04

    points = [[0.112, -2.996, 0,lineWidth],
              [0.017, -1.907, 0, lineWidth],
              [-0.602, -1.801, 0, lineWidth],
              [-0.656, -1.13, 0, lineWidth],
              [-2.087, -1.012, 0, lineWidth],
              [-2.093, 0.34, 0, lineWidth],
              [-1.317, 0.403, 0,lineWidth],
              [-1.44, 1.077, 0, lineWidth],
              [-0.638, 1.114, 0,lineWidth],
              [-0.613, 0.343, -0, lineWidth],
              [1.473, 0.328, 0, lineWidth],
              [1.428, 1.904, 0, lineWidth],
              [0.087, 1.905, 0, lineWidth],
              [0.074, 2.606, 0, lineWidth]]
    
    hSpline.spawn(location=[0,0,0], rotation=[0,0,0], scale=[1,1,1], configuration=1)
    hSpline.set_points(colour=[0,0.2,0], pointList=points, alignEndPointTangents=False, waitForConfirmation=True)

    lineWidth = 0.04

    points = [[3.395, -3.46, 0,lineWidth],
              [5.274, -0.389, 0, lineWidth],
              [5.31, 3.181, 0, lineWidth],
              [3.726, 4.718, -0, lineWidth],
              [-3.624, 4.453, 0, lineWidth],
              [-5.678, 2.738, 0, lineWidth],
              [-5.458, -4.044, -0, lineWidth],
              [-3.72, -5.601, 0, lineWidth],
              [1.233, -5.814, 0, lineWidth],
              [3.395, -3.46, 0,lineWidth]]
    
    #spawning a new actor internally sets a new ID
    hSpline.spawn(location=[0,0,0], rotation=[0,0,0], scale=[1,1,1], configuration=1)
    hSpline.set_points(colour=[0.2,0,0], pointList=points, alignEndPointTangents=True, waitForConfirmation=True)
    
    ### QBOT

    myQBot = QLabsQBot3(qlabs)
    myQBot.spawn_id_degrees(actorNumber=0, location=[-0.347, -5.97, -0], rotation=[0,0,0], scale=[1,1,1], configuration=0)
    myQBot.possess(myQBot.VIEWPOINT_TRAILING)
    
    rt = QLabsRealTime()
    rt.terminate_all_real_time_models()
    time.sleep(1)
    rt.start_real_time_model(modelName="../../rtmodels/QBot3/QBot3_Spawn", actorNumber=0, QLabsHostName='localhost', additionalArguments="")

    ### Free Camera    
    hCamera = QLabsFreeCamera(qlabs)
    hCamera.spawn(location=[2.39, -3.525, 2.547], rotation=[0, 0.762, 2.073])
    #hCamera.possess()



    qlabs.close()
    print("Done!")  
 

main()


