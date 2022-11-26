import sys
library_path = '../libraries'
sys.path.append(library_path)

from library_qlabs import QuanserInteractiveLabs
from library_qlabs_free_camera import QLabsFreeCamera
from library_qlabs_basic_shape import QLabsBasicShape
from library_qlabs_system import QLabsSystem
from library_qlabs_walls import QLabsWalls
from library_qlabs_flooring import QLabsFlooring
from library_qlabs_qcar import QLabsQCar


import sys
import time
import math
import struct
import numpy as np
import cv2
import xlsxwriter
import os


  
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
    
    
    hSystem = QLabsSystem(qlabs)
    x = hSystem.set_title_string('CUSTOM QCAR EXAMPLE', waitForConfirmation=True)
    
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
    

    ### Free Camera    
    hCamera = QLabsFreeCamera(qlabs)
    hCamera.spawn(location=[2.39, -3.525, 2.547], rotation=[0, 0.762, 2.073])
    #hCamera.possess()



    qlabs.close()
    print("Done!")  
 

main()


