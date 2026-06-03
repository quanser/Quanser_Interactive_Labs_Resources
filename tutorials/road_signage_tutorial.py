"""
Road Signage Library Example
----------------------------

.. note::

    This example will spawn one of each sign near the origin of the map.

"""

# imports to important libraries
import sys
import math
import time

from qvl.qlabs import QuanserInteractiveLabs
from qvl.yield_sign import QLabsYieldSign
from qvl.stop_sign import QLabsStopSign
from qvl.roundabout_sign import QLabsRoundaboutSign
from qvl.crossing_sign import QLabsCrossingSign
from qvl.obstacle_sign import QLabsObstacleSign
from qvl.turn_sign import QLabsTurnSign
from qvl.speed_sign import QLabsSpeedSign


def main():
   
    qlabs = QuanserInteractiveLabs()

    print("Connecting to QLabs...")
    if (not qlabs.open("localhost")):
        print("Unable to connect to QLabs")
        return    


    print("Connected")
    
    qlabs.destroy_all_spawned_actors()

    ### Stop Sign

    hSign = QLabsStopSign(qlabs)
    hSign.spawn_degrees(location=[0, 0, 0], rotation=[0,0,180], configuration=0)
    hSign.spawn_degrees(location=[2, 0, 0], rotation=[0,0,180], configuration=1)


    ### Yield Sign

    hSign = QLabsYieldSign(qlabs)
    hSign.spawn_degrees(location=[0, 1, 0], rotation=[0,0,180], configuration=0)
    hSign.spawn_degrees(location=[2, 1, 0], rotation=[0,0,180], configuration=1)    


    ### Roundabout Sign

    hSign = QLabsRoundaboutSign(qlabs)
    hSign.spawn_degrees(location=[0, 2, 0], rotation=[0,0,180], configuration=0)
    hSign.spawn_degrees(location=[2, 2, 0], rotation=[0,0,180], configuration=1)    
    hSign.spawn_degrees(location=[4, 2, 0], rotation=[0,0,180], configuration=2)    


    ### Crossing Sign

    hSign = QLabsCrossingSign(qlabs)
    hSign.spawn_degrees(location=[0, 3, 0], rotation=[0,0,180], configuration=0)
    hSign.spawn_degrees(location=[2, 3, 0], rotation=[0,0,180], configuration=1)    
    hSign.spawn_degrees(location=[4, 3, 0], rotation=[0,0,180], configuration=2) 


    ### Obstacle Sign

    hSign = QLabsObstacleSign(qlabs)
    hSign.spawn_degrees(location=[0, 4, 0], rotation=[0,0,180], configuration=0)
    hSign.spawn_degrees(location=[2, 4, 0], rotation=[0,0,180], configuration=1)    
    hSign.spawn_degrees(location=[4, 4, 0], rotation=[0,0,180], configuration=2)     


    ### Turn Sign

    hSign = QLabsTurnSign(qlabs)
    hSign.spawn_degrees(location=[0, 5, 0], rotation=[0,0,180], configuration=0)
    hSign.spawn_degrees(location=[2, 5, 0], rotation=[0,0,180], configuration=1)    
    hSign.spawn_degrees(location=[4, 5, 0], rotation=[0,0,180], configuration=2)        
    hSign.spawn_degrees(location=[6, 5, 0], rotation=[0,0,180], configuration=3)        
    hSign.spawn_degrees(location=[8, 5, 0], rotation=[0,0,180], configuration=4)
    hSign.spawn_degrees(location=[10, 5, 0], rotation=[0,0,180], configuration=5)    
    hSign.spawn_degrees(location=[12, 5, 0], rotation=[0,0,180], configuration=6)        
    hSign.spawn_degrees(location=[14, 5, 0], rotation=[0,0,180], configuration=7)      


    ### Speed Sign
      
    hSign = QLabsSpeedSign(qlabs)
    
    for count in range(12):
        hSign.spawn_degrees(location=[2*count, 6, 0], rotation=[0,0,180], configuration=0)
        hSign.set_speed((count+1)*10)
    
    qlabs.close()
    print("Done!")


if __name__ == "__main__":
    main()
