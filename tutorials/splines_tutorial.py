"""
Splines Tutorial
---------------

.. note::

    Make sure you have Quanser Interactive Labs open before running this
    example.  This example is designed to run ONLY in the Plane environment.

"""

# imports to important libraries
import math
import time

from qvl.qlabs import QuanserInteractiveLabs
from qvl.system import QLabsSystem
from qvl.spline_line import QLabsSplineLine
from qvl.free_camera import QLabsFreeCamera


# Clears the screen in Windows

def main():

    print("\n\n------------------------------ Communications --------------------------------\n")

    # Creates a server connection with Quanser Interactive Labs and manages
    # the communications
    qlabs = QuanserInteractiveLabs()

    # Ensure that QLabs is running on your local machine
    print("Connecting to QLabs...")
    if (not qlabs.open("localhost")):
        print("Unable to connect to QLabs")
        return    

    print("Connected")

    # Use hSystem to set the tutorial title in the upper left of the qlabs window 
    hSystem = QLabsSystem(qlabs)
    hSystem.set_title_string('Splines Tutorial')

    # Create top view camera and go to that view
    camera = QLabsFreeCamera(qlabs)
    camera.spawn([5.971, 11.781, 30.704], [0, 1.569, 1.57] )
    camera.possess()

    height = 0
    width = 1
    color = [0,0,0]

    # create splines to create virtual roads of 1m of thickness
    # Using the same initialization of QLabsSplineLine because the 
    # actors will not have to be referenced again. So overwriting them 
    # once they are spawned is not a problem. 

    #  In functions (not spawn) that do not have a height value, height needs
    # to be specified in the spawn function as a Z translation
    splineRoads = QLabsSplineLine(qlabs)
    splineRoads.spawn(location=[10,10,height], scale=[1,1,1], configuration=1)
    splineRoads.rounded_rectangle_from_center(cornerRadius=.5,xWidth=20, yLength=20, lineWidth=width, color=color)

    splineRoads.spawn(location=[0,0,0], scale=[1,1,1], configuration=1)
    splineRoads.set_points(color=color, pointList=[[0,13.8,height,width],[6,16.8,height,width], [11,12,height,width], [15.5, 14.5, height,width], [20, 11, height,width]], alignEndPointTangents=False)

    splineRoads.spawn(location=[14,4.5,height], scale=[1,1,1], configuration=1)
    splineRoads.circle_from_center(radius=3, lineWidth=width, color=color, numSplinePoints=8)

    splineRoads.spawn(location=[0,0,0], scale=[1,1,1], configuration=1)
    splineRoads.set_points(color=color, pointList=[[13.7,13.1,height,width],[14.8,11.8,height,width],[15.5,7.15,height,width]], alignEndPointTangents=False)

    splineRoads.spawn(location=[0,0,0], scale=[1,1,1], configuration=1)
    splineRoads.set_points(color=color, pointList=[[10.987, 4.199,height,width],[9.399, 6.559, height,width],[3.002, 4.034,height,width],[1.112, 3.004, height,width],[-0.045, 4.465, height,width]], alignEndPointTangents=False)
    
    splineRoads.spawn(location=[0,0,0], scale=[1,1,1], configuration=1)
    splineRoads.set_points(color=color, pointList=[[3, 20,height,width],[3, 4, height,width]], alignEndPointTangents=False)

    splineRoads.spawn(location=[0,0,0], scale=[1,1,1], configuration=1)
    splineRoads.set_points(color=color, pointList=[[8.7, 14.2, height,width],[8.7,0,height,width]], alignEndPointTangents=False)

    splineRoads.spawn(location=[20,20,height], scale=[1,1,1], configuration=1)
    splineRoads.arc_from_center(radius=5, startAngle= math.pi, endAngle= 3*math.pi/2, lineWidth=width, color=color)


    # create same splines with color and .1 m of thickness to simulate lines in the road
    # the next lines are a copy of the above one under a different name to differentiate
    # both sets of lines. Height needs to be higher than the road since overlays will 
    # reproduce weirdly in QLabs. 
    height = .02
    width = .1
    color = [1,1,0]

    splineLines = QLabsSplineLine(qlabs)
    splineLines.spawn(location=[10,10,height], scale=[1,1,1], configuration=1)
    splineLines.rounded_rectangle_from_center(cornerRadius=.5,xWidth=20, yLength=20, lineWidth=width, color=color)

    splineLines.spawn(location=[0,0,0], scale=[1,1,1], configuration=1)
    splineLines.set_points(color=color, pointList=[[0,13.8,height,width],[6,16.8,height,width], [11,12,height,width], [15.5, 14.5, height,width], [20, 11, height,width]], alignEndPointTangents=False)

    splineLines.spawn(location=[14,4.5,height], scale=[1,1,1], configuration=1)
    splineLines.circle_from_center(radius=3, lineWidth=width, color=color, numSplinePoints=8)

    splineLines.spawn(location=[0,0,0], scale=[1,1,1], configuration=1)
    splineLines.set_points(color=color, pointList=[[13.7,13.1,height,width],[14.8,11.8,height,width],[15.5,7.15,height,width]], alignEndPointTangents=False)

    splineLines.spawn(location=[0,0,0], scale=[1,1,1], configuration=1)
    splineLines.set_points(color=color, pointList=[[10.987, 4.199,height,width],[9.399, 6.559, height,width],[3.002, 4.034,height,width],[1.112, 3.004, height,width],[-0.045, 4.465, height,width]], alignEndPointTangents=False)
    
    splineLines.spawn(location=[0,0,0], scale=[1,1,1], configuration=1)
    splineLines.set_points(color=color, pointList=[[3, 20,height,width],[3, 4, height,width]], alignEndPointTangents=False)

    splineLines.spawn(location=[0,0,0], scale=[1,1,1], configuration=1)
    splineLines.set_points(color=color, pointList=[[8.7, 14.2, height,width],[8.7,0,height,width]], alignEndPointTangents=False)

    splineLines.spawn(location=[20,20,height], scale=[1,1,1], configuration=1)
    splineLines.arc_from_center(radius=5, startAngle= math.pi, endAngle= 3*math.pi/2, lineWidth=width, color=color)
    
    
    qlabs.close()
    print('Done!')
# -- -- -- -- -- -- -- -- -- -- -- -- --

if __name__ == "__main__":
    main()

