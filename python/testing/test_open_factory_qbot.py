import sys
library_path = '../libraries'
sys.path.append(library_path)

from library_qlabs import QuanserInteractiveLabs
from library_qlabs_free_camera import QLabsFreeCamera
from library_qlabs_basic_shape import QLabsBasicShape
from library_qlabs_widget import QLabsWidget
from library_qlabs_qbot2e import QLabsQBot2e
from library_qlabs_system import QLabsSystem


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
    cv2.startWindowThread()

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
    
    
    ### Free Camera    
    hCamera = QLabsFreeCamera(qlabs)
    hCamera.spawn(location=[0.073, -2.743, 0], rotation=[0, 0.339, 2.206])
    #hCamera.possess()


    ### QBOT

    myQBot = QLabsQBot2e(qlabs)
    myQBot.spawn_degrees([0.073, -2.743, 0], [0,0,90])


    ### Shapes
    construct_maze(qlabs)

    
    qlabs.close()
    print("Done!")  
 

main()


