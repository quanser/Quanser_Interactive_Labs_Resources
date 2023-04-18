import sys
sys.path.append('../')

import os
import numpy as np
import time
import math

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtWidgets

from qvl.qlabs import QuanserInteractiveLabs
from qvl.qcar import QLabsQCar
from qvl.free_camera import QLabsFreeCamera
from qvl.real_time import QLabsRealTime
from qvl.basic_shape import QLabsBasicShape
from qvl.system import QLabsSystem
from qvl.walls import QLabsWalls
from qvl.flooring import QLabsFlooring
from qvl.stop_sign import QLabsStopSign
from qvl.traffic_light import QLabsTrafficLight
from qvl.yield_sign import QLabsYieldSign
from qvl.traffic_cone import QLabsTrafficCone
from qvl.roundabout_sign import QLabsRoundaboutSign
from qvl.person import QLabsPerson

default_rtModel = os.path.normpath(
    os.path.join(
        os.path.dirname(__file__),
        '../../spawn_models/QCar_Workspace_studio'
    )
)

hQCar = None

def setup(
        qlabs, 
        initialPosition=[1.75, -0.626, 0.01],
        initialOrientation=[0, 0, 0],
        carScale=[0.1, 0.1, 0.1],
        rtModel=default_rtModel
    ):



    # Delete any previous QCar instances and stop any running spawn models
    qlabs.destroy_all_spawned_actors()
    #QLabsRealTime().terminate_all_real_time_models()

    #Set Camera
    camera = QLabsFreeCamera(qlabs)
    camera.spawn_degrees(location=[3.304, -3.255, 1.434], rotation= [0, 18.777, 130.312])
    camera.possess()

    #Set the Workspace Title
    hSystem = QLabsSystem(qlabs)
    x = hSystem.set_title_string('QCar Lidar Mapping Demo', waitForConfirmation=True)

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
    
    #spawn traffic lights + stop signs
    stop = QLabsStopSign(qlabs)
    stop.spawn(location=[0.248, -2.761, 0.01], rotation=[0,0,math.pi], scale=[0.1,0.1,0.1], configuration=0, waitForConfirmation=True)
    
    roundabout = QLabsRoundaboutSign(qlabs)
    roundabout.spawn(location=[-0.998, 0.621, 0.01], rotation=[0,0,-math.pi/3], scale=[0.1,0.1,0.1], configuration=0, waitForConfirmation=True)

    cone = QLabsTrafficCone(qlabs)
    for x in range(6):
        cone.spawn(location=[-0.482-2*x*0.1, -2.104, 0.01], rotation=[0,0,math.pi], scale=[0.1,0.1,0.1], configuration=1, waitForConfirmation=True)
    
    yieldsign = QLabsYieldSign(qlabs)
    yieldsign.spawn(location=[3.137, -0.263, 0.01], rotation=[0,0,-math.pi/2], scale=[0.1,0.1,0.1], configuration=0, waitForConfirmation=True)


    QLabsTrafficLight(qlabs).spawn(location=[0.4, -0.13, 0.01], rotation=[0,0,math.pi/2], scale=[0.1,0.1,0.1], configuration=0, waitForConfirmation=True)
    QLabsTrafficLight(qlabs).spawn(location=[1.449, -0.872, 0.01], rotation=[0,0,-math.pi/2], scale=[0.1,0.1,0.1], configuration=0, waitForConfirmation=True)
    QLabsTrafficLight(qlabs).spawn(location=[1.449, -0.13, 0.01], rotation=[0,0, 0*math.pi], scale=[0.1,0.1,0.1], configuration=0, waitForConfirmation=True)
    QLabsTrafficLight(qlabs).spawn(location=[0.4, -0.872, 0.01], rotation=[0,0,-math.pi], scale=[0.1,0.1,0.1], configuration=0, waitForConfirmation=True)
    
    # people
    person = QLabsPerson(qlabs)
    
    person.spawn_degrees(location=[-2.109, 2.748, 0.1],rotation=[0,0,-45], scale=[1,1,1], configuration=8, waitForConfirmation=True)
    person.spawn_degrees(location=[-1.76, 2.891, 0.1],rotation=[0,0,-110], scale=[1,1,1], configuration=7, waitForConfirmation=True)
    person.spawn_degrees(location=[1.79, 2.83, 0.1],rotation=[0,0,-110], scale=[1,1,1], configuration=11, waitForConfirmation=True)
    person.spawn_degrees(location=[2.579, 3.007, 0.1],rotation=[0,0,-110], scale=[1,1,1], configuration=9, waitForConfirmation=True)
    person.spawn_degrees(location=[-3.752, -2.505, 0.1],rotation=[0,0,0], scale=[1,1,1], configuration=9, waitForConfirmation=True)
    person.spawn_degrees(location=[4.44, -1.161, 0.1],rotation=[0,0,-190], scale=[1,1,1], configuration=9, waitForConfirmation=True)
    person.spawn_degrees(location=[4.39, -1.888, 0.1],rotation=[0,0,-210], scale=[1,1,1], configuration=7, waitForConfirmation=True)
    
    person.spawn_degrees(location=[5.387, 2.32, 0.1],rotation=[0,0,-110], scale=[1,1,1], configuration=10, waitForConfirmation=True)
    person.spawn_degrees(location=[5.496, 1.84, 0.1],rotation=[0,0,110], scale=[1,1,1], configuration=7, waitForConfirmation=True)
    
    person.spawn_degrees(location=[-3.48, 2.343, 0.1],rotation=[0,0,-45], scale=[1,1,1], configuration=11, waitForConfirmation=True)
    person.spawn_degrees(location=[-3.817, 1.654, 0.1],rotation=[0,0,20], scale=[1,1,1], configuration=10, waitForConfirmation=True)
    person.spawn_degrees(location=[-4.462, 2.337, 0.1],rotation=[0,0,-10], scale=[1,1,1], configuration=7, waitForConfirmation=True)
    
    person.spawn_degrees(location=[2.569, -5.416, 0.1],rotation=[0,0,180], scale=[1,1,1], configuration=10, waitForConfirmation=True)
    person.spawn_degrees(location=[1.808, -5.36, 0.1],rotation=[0,0,360], scale=[1,1,1], configuration=7, waitForConfirmation=True)
    
    # Spawn a QCar at the given initial pose
    hqcar = QLabsQCar(qlabs)
    hqcar.spawn_id(
        actorNumber=0,
        location=[x for x in initialPosition],
        rotation=initialOrientation,
        scale=carScale,
        waitForConfirmation=True
    )

    # Create a new camera view and attach it to the QCar
    hqcar.possess()

    x_min = -30
    x_max = 20
    y_min = 7
    y_max = 50
    y_mid = (y_max - y_min) / 2
    hBasicShape = QLabsBasicShape(qlabs)

    # Parking Lot Box
    hBasicShape.spawn_id_box_walls_from_end_points(
        actorNumber=0,
        startLocation=[-1.474, -1.2, 0.01],
        endLocation=[-0.64, -1.2, 0.01],
        height=0.5,
        thickness=0.50,
        color=[1,0,0],
        waitForConfirmation=False
    )

    # L
    
    hBasicShape.spawn_id_box_walls_from_end_points(
        actorNumber=2,
        startLocation=[1.5, 0, 0.01],
        endLocation=[1.5, 1.0, 0.01],
        height=0.5,
        thickness=0.10,
        color=[1,0,0],
        waitForConfirmation=False
    )
    hBasicShape.spawn_id_box_walls_from_end_points(
        actorNumber=3,
        startLocation=[2.0, 0.05, 0.01],
        endLocation=[1.5, 0.05, 0.01],
        height=0.5,
        thickness=0.10,
        color=[1,0,0],
        waitForConfirmation=False
    )
    
    # Cylinder
    hBasicShape.spawn_id_degrees(
        actorNumber=4,
        location=[-1.880, 0.889, 0.01],
        rotation=[0,0,45],
        scale=[0.25, 0.25, 0.75],
        configuration=hBasicShape.SHAPE_CYLINDER,

        waitForConfirmation=True
    )
        

    # Start spawn model
    #QLabsRealTime().start_real_time_model(rtModel)
    
    print("Closing QLabs connection")

    return hqcar
    

def testLIDAR(qlabs, hQCar):

    
    lidarPlot = pg.plot(title="LIDAR")
    squareSize = 10
    lidarPlot.setXRange(-squareSize, squareSize)
    lidarPlot.setYRange(-squareSize, squareSize)
    lidarData = lidarPlot.plot([], [], pen=None, symbol='o', symbolBrush='r', symbolPen=None, symbolSize=2)


    time.sleep(1)

    hQCar.set_velocity_and_request_state(forward=0.5, turn=0, headlights=False, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)

    for count in range(1000):


        success, angle, distance = hQCar.get_lidar(samplePoints=400)
        
        if (success):
       

            x = np.sin(angle)*distance
            y = np.cos(angle)*distance

            lidarData.setData(x,y)
            QtWidgets.QApplication.instance().processEvents()
        else:
            print("Lidar read failure")

    hQCar.set_velocity_and_request_state(forward=0, turn=0, headlights=False, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)



    print("Done. Hit any key to exit.")
    input()


# Try to connect to Qlabs
os.system('cls')
qlabs = QuanserInteractiveLabs()
print("Connecting to QLabs for setup...")
try:
    qlabs.open("localhost")
    print("Connected to QLabs")
    
except:
    print("Unable to connect to QLabs")
    quit()

hQCar = setup(qlabs)
testLIDAR(qlabs, hQCar)


print("Closing QLabs connection")
qlabs.close()




