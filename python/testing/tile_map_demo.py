from lib2to3 import refactor
import sys
import os

sys.path.append('../libraries/')

from library_qlabs import QuanserInteractiveLabs
from library_qlabs_free_camera import QLabsFreeCamera
from library_tile import TileMap


def testMapGeneration():
    os.system('cls')
    qlabs = QuanserInteractiveLabs()
    print("Connecting to QLabs...")
    try:
        qlabs.open("localhost")
        
        print("Connected to QLabs")
    except:
        print("Unable to connect to QLabs")
        return    
    
    qlabs.destroy_all_spawned_actors()

    hcamera = QLabsFreeCamera(qlabs)
    hcamera.spawn([0.864, -3.48, 2.599], [0, 0.675, 1.81])
    hcamera.possess()

    m = TileMap(qlabs,[0,0,0],0)
    m.add_tile(0,0,0,0)

    m.add_tile(0,1,0,1)
    m.add_tile(-1,0,1,1)
    m.add_tile(1,0,-1,1)
    m.add_tile(0,-1,2,1)

    m.add_tile(-1,1,-1,2)
    m.add_tile(1,1,2,2)
    m.add_tile(-1,-1,0,2)
    m.add_tile(1,-1,1,2)

    qlabs.close()
    
testMapGeneration()
