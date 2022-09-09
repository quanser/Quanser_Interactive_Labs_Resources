import sys
library_path = '../libraries'
sys.path.append(library_path)

from library_qlabs import QuanserInteractiveLabs
from library_qlabs_common import QLabsCommon
from library_qlabs_yield_sign import QLabsYieldSign
from library_qlabs_stop_sign import QLabsStopSign
from library_qlabs_roundabout_sign import QLabsRoundaboutSign
from library_qlabs_traffic_cone import QLabsTrafficCone
from library_qlabs_crosswalk import QLabsCrosswalk
from library_qlabs_free_camera import QLabsFreeCamera
from library_qlabs_basic_shape import QLabsBasicShape
from library_qlabs_qcar import QLabsQCar
from library_qlabs_environment_outdoors import QLabsEnvironmentOutdoors
from library_qlabs_system import QLabsSystem
from library_qlabs_person import QLabsPerson
from library_qlabs_utilities import *
from library_qlabs_spline_line import QLabsSplineLine
from library_qlabs_real_time import QLabsRealTime
from library_qlabs_widget import QLabsWidget



import sys
import time
import math
import struct
import numpy as np
import cv2
import xlsxwriter
import os

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtWidgets

####################################################
require_user_input = False
lidar_rate = 0.1


####################################################


ignore_list = ['library_qlabs_autoclave', \
               'library_qlabs_bottle_table', \
               'library_qlabs_conveyor_curved', \
               'library_qlabs_conveyor_straight', \
               'library_qlabs_delivery_tube', \
               'library_qlabs_qarm', \
               'library_qlabs_qbot', \
               'library_qlabs_qbot2e', \
               'library_qlabs_qbot_hopper', \
               'library_qlabs_shredder', \
               'library_qlabs_srv02', \
               'library_qlabs_weigh_scale', \
               'library_qlabs_image_utilities']

                
def checkFunctionTestList(library_name):

    PrintWS(2, "")
    PrintWS(2, "Function check")
    all_functions_tested = True;
    f_validation_code = open( os.path.dirname(os.path.realpath(__file__)) + '\library_verification.py', 'r')
    validation_code = f_validation_code.read()
    f_validation_code.close()
    
    print("\nChecking function usage...")
    f_library = open(library_path + '/' + library_name + '.py', 'r')
    library_data = f_library.readlines();    
    f_library.close();
    
    class_name = ""
    
    for line in library_data:
        if "class" in line:
            if line[0] == "c":
                if ":" in line:
                    class_name = line[6:len(line)-2]
                    print("Class name: {}".format(class_name))
    
    for line in library_data:
        if "def " in line:
            function_name = line.lstrip()
            function_name = function_name[4:function_name.find('(')]
            
            if (function_name[0] != "_"):
                if (function_name != "__init__"):
                    function_name = class_name + "()." + function_name
                    if not(function_name in validation_code):
                        print("*** {} not tested".format(function_name))
                        all_functions_tested = False
                        PrintWS(0, function_name)
                    else:
                        PrintWS(1, function_name)

                    
                    
    
    
    if (all_functions_tested == True):
        print("All functions tested")
                
def checkValidationLibraryList():
    #load this file for self checking
    f_validation_code = open( os.path.dirname(os.path.realpath(__file__)) + '\library_verification.py', 'r')
    validation_code = f_validation_code.read()
    f_validation_code.close()
    
    for f in os.listdir(library_path):
        if os.path.isfile(os.path.join(library_path, f)):
            filename, file_extension = os.path.splitext(f)
            if (file_extension == ".py"):
                if not(filename in ignore_list):
                    if not(filename in validation_code):
                        print("*** {} not loaded in verification".format(filename))
                        PrintWS(0, filename)
                    else:
                        PrintWS(1, filename)
                        

def PrintWSHeader(text):
    global row
    if row > 0:
        row = row + 2
    ws.write(row, 0, text, header_text)
    row = row + 2
    
def PrintWS(status, text):
    global row
    
    if (status == 1):
        ws.write(row, 0, "", status_good)
    elif (status == 0):
        ws.write(row, 0, "", status_bad)
        
    ws.write(row, 1, text)
    row = row + 1
  

  
def main():
    os.system('cls')
    
    print("----------------- Checking that all libraries are being tested -------------------\n")
    PrintWSHeader("Library Test List")
    checkValidationLibraryList()  

    
    print("\n\n------------------------------ Communications --------------------------------\n")
    
    PrintWSHeader("Communications")
    qlabs = QuanserInteractiveLabs()
    cv2.startWindowThread()

    print("Connecting to QLabs...")
    try:
        qlabs.open("localhost")
    except:
        print("Unable to connect to QLabs")
        PrintWS(0, "Connection success")
        return
    
    print("Connected")
    PrintWS(1, "Connection success")
    

    print("\n\n------------------------- Testing Individual Libraries ---------------------------\n")
    
    
    ### Common
    PrintWSHeader("Common")
    x = "Destroyed {} actors.".format(QLabsCommon().destroy_all_spawned_actors(qlabs))
    print(x)
    PrintWS(2, x)
    
    ### System
    PrintWSHeader("System")
    x = QLabsSystem().set_title_string(qlabs, 'QLABS VERIFICATION SCRIPT', waitForConfirmation=True)
    PrintWS(x == True, "Set title string")
    checkFunctionTestList("library_qlabs_system")
    
    ### Free Camera
    PrintWSHeader("Free Camera")
    print("\n\n---Free Camera---")
    
    x = QLabsFreeCamera().spawn(qlabs, actorNumber=0, location=[-11.154, 42.544, 8.43], rotation=[0, 1.204, 1.548])
    PrintWS(x == 0, "Spawn sign with radians")
    
    x = QLabsFreeCamera().spawn(qlabs, actorNumber=0, location=[-11.154, 42.544, 8.43], rotation=[0, 1.204, 1.548])
    PrintWS(x == 2, "Spawn sign with duplicate ID (return code 2)")
    
    QLabsFreeCamera().spawn(qlabs, actorNumber=1, location=[-23.201, 34.875, 3.482], rotation=[0, 0.349, -0.04])
    x = QLabsFreeCamera().destroy(qlabs, actorNumber=1)
    PrintWS(x == 1, "Spawn and destroy existing sign (expect return 1)")
    
    x = QLabsFreeCamera().destroy(qlabs, actorNumber=10)
    PrintWS(x == 0, "Destroy sign that doesn't exist (expect return 0)")
    
    loc2 = [-23.201, 34.875, 3.482]
    rot2 = [0, 20.023, -2.275]
    x = QLabsFreeCamera().spawn_degrees(qlabs, actorNumber=2, location=loc2, rotation=rot2)
    PrintWS(x == 0, "Spawn sign with degrees")
    
    x, loc, rot, scale = QLabsFreeCamera().get_world_transform(qlabs, 2)
    PrintWS(abs(np.sum(np.subtract(loc, loc2))) < 0.001 and x == True, "Get world transform")
    
    x = QLabsFreeCamera().ping(qlabs, 2)
    PrintWS(x == True, "Ping existing sign (expect True)")
    
    x = QLabsFreeCamera().ping(qlabs, 3)
    PrintWS(x == False, "Ping sign that doesn't exist (expect False)")
    
    '''
    QLabsFreeCamera().spawn(qlabs, actorNumber=3, location=[-34.03, 23.433, 5.328], rotation=[0, 0.261, 0.683])
    QLabsFreeCamera().set_camera_properties(qlabs, actorNumber=3, fieldOfView=40, depthOfField=True, aperature=2.3, focusDistance=0.6)
    x = QLabsFreeCamera().possess(qlabs, 3)
    
    for y in range(51):
        x = QLabsFreeCamera().set_camera_properties(qlabs, actorNumber=3, fieldOfView=40, depthOfField=True, aperature=2.3, focusDistance=(0.6 + pow(y/50, 3)*23.7))
    PrintWS(x == True, "Set camera properties")
    '''
    
    x = QLabsFreeCamera().possess(qlabs, 2)
    PrintWS(x == True, "Possess camera 2")
    
    '''
        
    for y in range(26):
        x = QLabsFreeCamera().set_transform(qlabs, 2, loc2, np.add(np.array(rot2)/180*math.pi, [0, 0, y/25*math.pi*2]))
    PrintWS(x == True, "Set transform")
    
    for y in range(26):
        x = QLabsFreeCamera().set_transform_degrees(qlabs, 2, loc2, np.add(rot2, [0, 0, y/25*360]))
    PrintWS(x == True, "Set transform degrees (expect True)")
    
    
    cv2.namedWindow('CameraImageStream', cv2.WINDOW_AUTOSIZE)
    camera_image = cv2.imread('Quanser640x480.jpg')
    cv2.imshow('CameraImageStream', camera_image)
    cv2.waitKey(1)
    
    x = QLabsFreeCamera().set_image_capture_resolution(qlabs, actorNumber=2, width=640, height=480)
    PrintWS(x == True, "Set image capture resolution")
    x, camera_image = QLabsFreeCamera().get_image(qlabs, actorNumber=2)
    PrintWS(x == True, "Read image 640x480")
    if (x == True):
        cv2.imshow('CameraImageStream', camera_image)
        cv2.waitKey(1)
        
    else:
        print("Image decoding failure")
        
    cv2.namedWindow('CameraImageStream2', cv2.WINDOW_AUTOSIZE)
    camera_image = cv2.imread('Quanser820x410.jpg')
    cv2.imshow('CameraImageStream2', camera_image)
    cv2.waitKey(1)
    
    QLabsFreeCamera().set_image_capture_resolution(qlabs, actorNumber=2, width=820, height=410)
    PrintWS(x == True, "Read image 820x410 (expect True)")
    x, camera_image = QLabsFreeCamera().get_image(qlabs, actorNumber=2)
    if (x == True):
        cv2.imshow('CameraImageStream2', camera_image)
        cv2.waitKey(1)
    else:
        print("Image decoding failure")    
       
       
    loc3 = [5.252, 20.852, 9.461]
    QLabsBasicShape().spawn(qlabs, 0, loc3, [0,0,0], [1,1,1], configuration=QLabsBasicShape().SHAPE_CUBE, waitForConfirmation=True)
    x = QLabsFreeCamera().spawn_and_parent_with_relative_transform(qlabs, 5, [0, -10, 0], [0,0,math.pi/2], QLabsBasicShape().ID_BASIC_SHAPE, 0, 0)
    PrintWS(x == 0, "Spawn and parent with relative transform")
    x = QLabsFreeCamera().possess(qlabs, 5)
    for y in range(26):
        x = QLabsBasicShape().set_transform(qlabs, 0, loc3, [0, 0, y/25*math.pi*2], [1,1,1])
    
    time.sleep(0.5)
    
    QLabsFreeCamera().destroy(qlabs, actorNumber=5)
    x = QLabsFreeCamera().spawn_and_parent_with_relative_transform_degrees(qlabs, 5, [0, -10, 0], [0,0,90], QLabsBasicShape().ID_BASIC_SHAPE, 0, 0)
    PrintWS(x == 0, "Spawn and parent with relative transform degrees")
    x = QLabsFreeCamera().possess(qlabs, 5)
    for y in range(26):
        x = QLabsBasicShape().set_transform(qlabs, 0, loc3, [0, 0, y/25*math.pi*2], [1,1,1])
    
    checkFunctionTestList("library_qlabs_free_camera")
    '''
    cv2.destroyAllWindows()
    x = QLabsFreeCamera().possess(qlabs, 2)
    
    '''
    ### Yield Sign    
    PrintWSHeader("Yield Sign")
    print("\n\n---Yield Sign---")
    
    x = QLabsYieldSign().spawn(qlabs, actorNumber=0, location=[-17, 38, 0.0], rotation=[0,0,math.pi], scale=[1,1,1], waitForConfirmation=True)
    PrintWS(x == 0, "Spawn sign with radians")
    
    x = QLabsYieldSign().spawn(qlabs, actorNumber=0, location=[-17, 38, 0.0], rotation=[0,0,math.pi], scale=[1,1,1], waitForConfirmation=True)
    PrintWS(x == 2, "Spawn sign with duplicate ID (return code 2)")
    
    QLabsYieldSign().spawn(qlabs, actorNumber=1, location=[-16, 38, 0.0], rotation=[0,0,math.pi], scale=[1,1,1], waitForConfirmation=True)
    x = QLabsYieldSign().destroy(qlabs, actorNumber=1)
    PrintWS(x == 1, "Spawn and destroy existing sign (expect return 1)")
    
    x = QLabsYieldSign().destroy(qlabs, actorNumber=10)
    PrintWS(x == 0, "Destroy sign that doesn't exist (expect return 0)")
    
    x = QLabsYieldSign().spawn_degrees(qlabs, actorNumber=2, location=[-15, 38, 0.0], rotation=[0,0,180], scale=[1,1,1], waitForConfirmation=True)
    PrintWS(x == 0, "Spawn sign with degrees")
    
    x, loc, rot, scale = QLabsYieldSign().get_world_transform(qlabs, 2)
    PrintWS(np.array_equal(loc, [-15, 38, 0.0]) and x == True, "Get world transform")
    
    x = QLabsYieldSign().ping(qlabs, 2)
    PrintWS(x == True, "Ping existing sign (expect True)")
    
    x = QLabsYieldSign().ping(qlabs, 3)
    PrintWS(x == False, "Ping sign that doesn't exist (expect False)")
    
    
    checkFunctionTestList("library_qlabs_yield_sign")
    

    ### Stop Sign    
    PrintWSHeader("Stop Sign")
    print("\n\n---Stop Sign---")
    
    x = QLabsStopSign().spawn(qlabs, actorNumber=0, location=[-17, 37, 0.0], rotation=[0,0,math.pi], scale=[1,1,1], waitForConfirmation=True)
    PrintWS(x == 0, "Spawn sign with radians")
    
    x = QLabsStopSign().spawn(qlabs, actorNumber=0, location=[-17, 37, 0.0], rotation=[0,0,math.pi], scale=[1,1,1], waitForConfirmation=True)
    PrintWS(x == 2, "Spawn sign with duplicate ID (return code 2)")
    
    QLabsStopSign().spawn(qlabs, actorNumber=1, location=[-16, 37, 0.0], rotation=[0,0,math.pi], scale=[1,1,1], waitForConfirmation=True)
    x = QLabsStopSign().destroy(qlabs, actorNumber=1)
    PrintWS(x == 1, "Spawn and destroy existing sign (expect return 1)")
    
    x = QLabsStopSign().destroy(qlabs, actorNumber=10)
    PrintWS(x == 0, "Destroy sign that doesn't exist (expect return 0)")
    1
    x = QLabsStopSign().spawn_degrees(qlabs, actorNumber=2, location=[-15, 37, 0.0], rotation=[0,0,180], scale=[1,1,1], waitForConfirmation=True)
    PrintWS(x == 0, "Spawn sign with degrees")
    
    x, loc, rot, scale = QLabsStopSign().get_world_transform(qlabs, 2)
    PrintWS(np.array_equal(loc, [-15, 37, 0.0]) and x == True, "Get world transform")
    
    
    x = QLabsStopSign().ping(qlabs, 2)
    PrintWS(x == True, "Ping existing sign (expect True)")
    
    x = QLabsStopSign().ping(qlabs, 3)
    PrintWS(x == False, "Ping sign that doesn't exist (expect False)")    
    
    checkFunctionTestList("library_qlabs_stop_sign")    
    
    
    ### Roundabout Sign    
    PrintWSHeader("Roundabout Sign")
    print("\n\n---Roundabout Sign---")
    
    x = QLabsRoundaboutSign().spawn(qlabs, actorNumber=0, location=[-17, 36, 0.0], rotation=[0,0,math.pi], scale=[1,1,1], waitForConfirmation=True)
    PrintWS(x == 0, "Spawn sign with radians")
    
    x = QLabsRoundaboutSign().spawn(qlabs, actorNumber=0, location=[-17, 36, 0.0], rotation=[0,0,math.pi], scale=[1,1,1], waitForConfirmation=True)
    PrintWS(x == 2, "Spawn sign with duplicate ID (return code 2)")
    
    QLabsRoundaboutSign().spawn(qlabs, actorNumber=1, location=[-16, 36, 0.0], rotation=[0,0,math.pi], scale=[1,1,1], waitForConfirmation=True)
    x = QLabsRoundaboutSign().destroy(qlabs, actorNumber=1)
    PrintWS(x == 1, "Spawn and destroy existing sign (expect return 1)")
    
    x = QLabsRoundaboutSign().destroy(qlabs, actorNumber=10)
    PrintWS(x == 0, "Destroy sign that doesn't exist (expect return 0)")
    
    x = QLabsRoundaboutSign().spawn_degrees(qlabs, actorNumber=2, location=[-15, 36, 0.0], rotation=[0,0,180], scale=[1,1,1], waitForConfirmation=True)
    PrintWS(x == 0, "Spawn sign with degrees")
    
    x, loc, rot, scale = QLabsRoundaboutSign().get_world_transform(qlabs, 2)
    PrintWS(np.array_equal(loc, [-15, 36, 0.0]) and x == True, "Get world transform")
    
    
    x = QLabsRoundaboutSign().ping(qlabs, 2)
    PrintWS(x == True, "Ping existing sign (expect True)")
    
    x = QLabsRoundaboutSign().ping(qlabs, 3)
    PrintWS(x == False, "Ping sign that doesn't exist (expect False)")      
    
    checkFunctionTestList("library_qlabs_roundabout_sign")    
    
    
    ### Traffic Cone
    PrintWSHeader("Traffic Cone")
    print("\n\n---Traffic Cone---")
    
    x = QLabsTrafficCone().spawn(qlabs, actorNumber=0, location=[-17, 35, 1.0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    PrintWS(x == 0, "Spawn cone with radians")
    
    x = QLabsTrafficCone().spawn(qlabs, actorNumber=0, location=[-17, 35, 1.0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    PrintWS(x == 2, "Spawn cone with duplicate ID (return code 2)")
    
    QLabsTrafficCone().spawn(qlabs, actorNumber=1, location=[-16, 35, 1.0], rotation=[0,0,math.pi], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    x = QLabsTrafficCone().destroy(qlabs, actorNumber=1)
    PrintWS(x == 1, "Spawn and destroy existing cone (expect return 1)")
    
    x = QLabsTrafficCone().destroy(qlabs, actorNumber=10)
    PrintWS(x == 0, "Destroy cone that doesn't exist (expect return 0)")
    
    x = QLabsTrafficCone().spawn_degrees(qlabs, actorNumber=2, location=[-15, 35, 1.0], rotation=[0,0,180], scale=[1,1,1], configuration=1, waitForConfirmation=True)
    PrintWS(x == 0, "Spawn cone with degrees in config 1")
    
    x, loc, rot, scale = QLabsTrafficCone().get_world_transform(qlabs, 2)
    PrintWS(x == True, "Get world transform")
    
    
    x = QLabsTrafficCone().ping(qlabs, 2)
    PrintWS(x == True, "Ping existing cone (expect True)")
    
    x = QLabsTrafficCone().ping(qlabs, 3)
    PrintWS(x == False, "Ping cone that doesn't exist (expect False)")      
    
    checkFunctionTestList("library_qlabs_traffic_cone")   
    
    ### Change view points
    
    time.sleep(0.5)
    QLabsFreeCamera().possess(qlabs, 0)
    print("Possess camera 0")
    
    ### Crosswalk
    PrintWSHeader("Crosswalk")
    print("\n\n---Crosswalk---")
    
    x = QLabsCrosswalk().spawn(qlabs, actorNumber=0, location=[-15.788, 47.5, 0.00], rotation=[0,0,math.pi/2], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    PrintWS(x == 0, "Spawn crosswalk with radians")
    
    x = QLabsCrosswalk().spawn(qlabs, actorNumber=0, location=[-11.788, 47.5, 0.00], rotation=[0,0,math.pi/2], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    PrintWS(x == 2, "Spawn crosswalk with duplicate ID (return code 2)")
    
    QLabsCrosswalk().spawn(qlabs, actorNumber=1, location=[-11.788, 47.5, 0.00], rotation=[0,0,math.pi/2], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    x = QLabsCrosswalk().destroy(qlabs, actorNumber=1)
    PrintWS(x == 1, "Spawn and destroy existing crosswalk (expect return 1)")
    
    x = QLabsCrosswalk().destroy(qlabs, actorNumber=10)
    PrintWS(x == 0, "Destroy crosswalk that doesn't exist (expect return 0)")
    
    x = QLabsCrosswalk().spawn_degrees(qlabs, actorNumber=2, location=[-11.788, 47.5, 0.00], rotation=[0,0,90], scale=[1,1,1], configuration=1, waitForConfirmation=True)
    PrintWS(x == 0, "Spawn crosswalk with degrees in config 1")
    
    x = QLabsCrosswalk().spawn_degrees(qlabs, actorNumber=3, location=[-7.8, 47.5, 0.0], rotation=[0,0,90], scale=[1,1,1], configuration=2, waitForConfirmation=True)
    PrintWS(x == 0, "Spawn crosswalk with degrees in config 2")
    
    
    x, loc, rot, scale = QLabsCrosswalk().get_world_transform(qlabs, 3)
    PrintWS(abs(np.sum(np.subtract(loc, [-7.8, 47.5, 0.0]))) < 0.001 and x == True, "Get world transform")
    
    
    x = QLabsCrosswalk().ping(qlabs, 2)
    PrintWS(x == True, "Ping existing crosswalk (expect True)")
    
    x = QLabsCrosswalk().ping(qlabs, 4)
    PrintWS(x == False, "Ping crosswalk that doesn't exist (expect False)")      
    
    checkFunctionTestList("library_qlabs_crosswalk")   
    
    ### People
    PrintWSHeader("People")
    print("\n\n---People---")
    
    QLabsPerson().spawn(qlabs, actorNumber=0, location=[-7.637, 43.756, 0.005], rotation=[0,0,math.pi/2], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    QLabsPerson().spawn(qlabs, actorNumber=1, location=[-11.834, 43.642, 0.005], rotation=[0,0,math.pi/2], scale=[1,1,1], configuration=1, waitForConfirmation=True)
    QLabsPerson().spawn_degrees(qlabs, actorNumber=2, location=[-15.903, 43.802, 0.005], rotation=[0,0,90], scale=[1,1,1], configuration=2, waitForConfirmation=True)
    
    QLabsPerson().move_to(qlabs, actorNumber=0, location=[-7.637, 51, 0.005], speed=QLabsPerson().WALK, waitForConfirmation=True)
    QLabsPerson().move_to(qlabs, actorNumber=1, location=[-11.834, 51, 0.005], speed=QLabsPerson().JOG, waitForConfirmation=True)
    QLabsPerson().move_to(qlabs, actorNumber=2, location=[-15.903, 51, 0.005], speed=QLabsPerson().RUN, waitForConfirmation=True)
    
    time.sleep(3)

    x, pos, rot = QLabsPerson().get_world_transform(qlabs, 2)
    PrintWS(x == True, "Got world transform ({}), ({})".format(pos, rot))      
    
    x, pos, rot = QLabsPerson().get_world_transform_degrees(qlabs, 2)
    PrintWS(x == True, "Got world transform degrees ({}), ({})".format(pos, rot))      
    
    x = QLabsPerson().ping(qlabs, 2)
    PrintWS(x == True, "Ping person 3 (expect True)")      
    
    x = QLabsPerson().destroy(qlabs, 2)
    PrintWS(x == 1, "Person 3 destroyed (expect 1)")      

    x = QLabsPerson().ping(qlabs, 2)
    PrintWS(x == False, "Ping person 3 (expect False)")    
    
    time.sleep(1)
    
    


    checkFunctionTestList("library_qlabs_person")   
    
    ### QCar
    
    QLabsFreeCamera().spawn(qlabs, actorNumber=33, location=[-15.075, 26.703, 6.074], rotation=[0, 0.564, -1.586])
    QLabsFreeCamera().possess(qlabs, 33)
    
    PrintWSHeader("QCar")
    print("\n\n---QCar---")
    
    x = QLabsQCar().spawn(qlabs, actorNumber=0, location=[-14.386, 17.445, 0.005], rotation=[0,0,math.pi/2], waitForConfirmation=True)
    PrintWS(x == 0, "Spawn QCar with radians")
    
    x = QLabsQCar().spawn(qlabs, actorNumber=0, location=[-14.386, 17.445, 0.005], rotation=[0,0,math.pi/2], waitForConfirmation=True)
    PrintWS(x == 2, "Spawn QCar with duplicate ID (return code 2)")
    
    QLabsQCar().spawn(qlabs, actorNumber=1, location=[-17.1, 17.445, 0.005], rotation=[0,0,math.pi/2], waitForConfirmation=True)
    x = QLabsQCar().destroy(qlabs, actorNumber=1)
    PrintWS(x == 1, "Spawn and destroy existing QCar (expect return 1)")
    
    x = QLabsQCar().destroy(qlabs, actorNumber=10)
    PrintWS(x == 0, "Destroy QCar that doesn't exist (expect return 0)")
    
    x = QLabsQCar().spawn_degrees(qlabs, actorNumber=2, location=[-11.6, 17.445, 0.005], rotation=[0,0,90], waitForConfirmation=True)
    PrintWS(x == 0, "Spawn QCar with degrees")
    
    
    # lights
    for env_time in range(60):
        QLabsEnvironmentOutdoors().set_time_of_day(qlabs, 12+env_time/10*2)
    
    time.sleep(0.5)
    
    QLabsQCar().set_velocity_and_request_state(qlabs, actorNumber=2, forward=1, turn = -math.pi/6, headlights=True, leftTurnSignal=False, rightTurnSignal=True, brakeSignal=False, reverseSignal=False)
    time.sleep(1)
    QLabsQCar().set_velocity_and_request_state(qlabs, actorNumber=2, forward=0.0, turn = -math.pi/6, headlights=True, leftTurnSignal=False, rightTurnSignal=True, brakeSignal=False, reverseSignal=False)
    if require_user_input == True:
        x = input("Moving forward towards the right of the screen, headlights on? (Enter yes, anything else no):")
    else:
        x = ""
    PrintWS(x == "", "Headlights")
    PrintWS(x == "", "Set velocity")
    
    QLabsQCar().set_velocity_and_request_state_degrees(qlabs, actorNumber=2, forward=1, turn = 30, headlights=True, leftTurnSignal=True, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)
    time.sleep(1)
    success, location, rotation, frontHit, rearHit = QLabsQCar().set_velocity_and_request_state_degrees(qlabs, actorNumber=2, forward=0.0, turn = 30, headlights=True, leftTurnSignal=True, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)
    print(rotation)
    if require_user_input == True:
        x = input("Moving forward towards the left of the screen? Enter yes, anything else no):")
    else:
        x = ""
    PrintWS(x == "", "Set velocity degrees")
    

    x = QLabsQCar().possess(qlabs, 2)
        
    time.sleep(0.1)
    QLabsQCar().set_velocity_and_request_state(qlabs, actorNumber=2, forward=1, turn = 0, headlights=True, leftTurnSignal=True, rightTurnSignal=True, brakeSignal=True, reverseSignal=True)
    time.sleep(1)
    QLabsQCar().set_velocity_and_request_state(qlabs, actorNumber=2, forward=0.0, turn = 0, headlights=True, leftTurnSignal=True, rightTurnSignal=True, brakeSignal=True, reverseSignal=True)
    
    if require_user_input == True:
        x = input("Brake lights on and casting red glow? (Enter yes, anything else no):")
    else:
        x = ""
    PrintWS(x == "", "Brake lights")
    
    
    QLabsQCar().set_velocity_and_request_state(qlabs, actorNumber=2, forward=0, turn = 0, headlights=False, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)
    
    for env_time in range(60):
        QLabsEnvironmentOutdoors().set_time_of_day(qlabs, env_time/10*2)
    
    
    #bumper test
    print("Testing bumper response...")
    QLabsFreeCamera().possess(qlabs, 33)
    QLabsFreeCamera().set_transform(qlabs, actorNumber=33, location=[-17.045, 32.589, 6.042], rotation=[0, 0.594, -1.568])
    QLabsBasicShape().spawn(qlabs, 100, [-11.919, 26.289, 0.5], [0,0,0], [1,1,1], configuration=QLabsBasicShape().SHAPE_CUBE, waitForConfirmation=True)
    QLabsBasicShape().spawn(qlabs, 101, [-19.919, 26.289, 0.5], [0,0,0], [1,1,1], configuration=QLabsBasicShape().SHAPE_CUBE, waitForConfirmation=True)
    QLabsQCar().spawn(qlabs, actorNumber=3, location=[-13.424, 26.299, 0.005], rotation=[0,0,math.pi])
    
    for count in range(10):
        x, location, rotation, frontHit, rearHit  = QLabsQCar().set_velocity_and_request_state(qlabs, actorNumber=3, forward=2, turn = 0, headlights=False, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)

        time.sleep(0.25)

    PrintWS(x == True and frontHit == True, "Front bumper hit")
    x = QLabsQCar().ghost_mode(qlabs, actorNumber=3)
    PrintWS(x == True, "Ghost Mode")
    

    for count in range(10):
        x, location, rotation, frontHit, rearHit  = QLabsQCar().set_velocity_and_request_state(qlabs, actorNumber=3, forward=-2, turn = 0, headlights=False, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)

        time.sleep(0.25)
        
    QLabsQCar().ghost_mode(qlabs, actorNumber=3, enable=True, colour=[1,0,0])

    PrintWS(x == True and rearHit == True, "Rear bumper hit")
    QLabsQCar().set_velocity_and_request_state(qlabs, actorNumber=3, forward=0, turn = 0, headlights=False, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)
    

    
    x, location, rotation, forward_vector, up_vector, frontHit, rearHit = QLabsQCar().set_transform_and_request_state(qlabs, actorNumber=3, location=[-16.1, 26.299, 0.005], rotation=[0,0,math.pi-0.01], enableDynamics=True, headlights=False, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)
    PrintWS(x == True and frontHit == True, "Front bumper hit with transform")
    
    x, loc, rot = QLabsQCar().get_world_transform(qlabs, 3)
    PrintWS(abs(np.sum(np.subtract(loc, [-16.1, 26.299, 0.005]))) < 0.01 and abs(np.sum(np.subtract(rot, [0,0,math.pi-0.01]))) < 0.01 and x == True, "Get world transform")
    
    
    x, location, rotation, forward_vector, up_vector, frontHit, rearHit = QLabsQCar().set_transform_and_request_state_degrees(qlabs, actorNumber=3, location=[-13.1, 26.299, 0.005], rotation=[0,0,179], enableDynamics=True, headlights=False, leftTurnSignal=False, rightTurnSignal=False, brakeSignal=False, reverseSignal=False)
    PrintWS(x == True and rearHit == True, "Rear bumper hit with transform")

    x, loc, rot = QLabsQCar().get_world_transform_degrees(qlabs, 3)
    PrintWS(abs(np.sum(np.subtract(loc, [-13.1, 26.299, 0.005]))) < 0.01 and abs(np.sum(np.subtract(rot, [0,0,179]))) < 0.01 and x == True, "Get world transform degrees")
    
    QLabsQCar().ghost_mode(qlabs, actorNumber=3, enable=False, colour=[1,0,0])

    
    #camera tests
    print("\nQCar camera tests...")
    QLabsQCar().possess(qlabs, 2, QLabsQCar().CAMERA_OVERHEAD)
    if require_user_input == True:
        x = input("Overhead camera? (Enter yes, anything else no):")
    else:
        x = ""
        time.sleep(0.5)
    PrintWS(x == "", "Possess overhead camera")

    QLabsQCar().possess(qlabs, 2, QLabsQCar().CAMERA_TRAILING)
    if require_user_input == True:
        x = input("Trailing camera? (Enter yes, anything else no):")
    else:
        x = ""
        time.sleep(0.5)
    PrintWS(x == "", "Possess trailing camera")
    
    QLabsQCar().possess(qlabs, 2, QLabsQCar().CAMERA_CSI_FRONT)
    if require_user_input == True:
        x = input("Front camera? (Enter yes, anything else no):")
    else:
        x = ""
        time.sleep(0.5)
    PrintWS(x == "", "Possess front camera")

    QLabsQCar().possess(qlabs, 2, QLabsQCar().CAMERA_CSI_RIGHT)
    if require_user_input == True:
        x = input("Right camera? (Enter yes, anything else no):")
    else:
        x = ""
        time.sleep(0.5)
    PrintWS(x == "", "Possess right camera")

    QLabsQCar().possess(qlabs, 2, QLabsQCar().CAMERA_CSI_BACK)
    if require_user_input == True:
        x = input("Back camera? (Enter yes, anything else no):")
    else:
        x = ""
        time.sleep(0.5)
    PrintWS(x == "", "Possess back camera")

    QLabsQCar().possess(qlabs, 2, QLabsQCar().CAMERA_CSI_LEFT)
    if require_user_input == True:
        x = input("Left camera? (Enter yes, anything else no):")
    else:
        x = ""
        time.sleep(0.5)
    PrintWS(x == "", "Possess left camera")

    QLabsQCar().possess(qlabs, 2, QLabsQCar().CAMERA_RGB)
    if require_user_input == True:
        x = input("Real Sense RGB camera? (Enter yes, anything else no):")
    else:
        x = ""
        time.sleep(0.5)
    PrintWS(x == "", "Possess Real Sense RGB camera")

    QLabsQCar().possess(qlabs, 2, QLabsQCar().CAMERA_DEPTH)
    if require_user_input == True:
        x = input("Real Sense Depth camera? (Enter yes, anything else no):")
    else:
        x = ""
        time.sleep(0.5)
    PrintWS(x == "", "Possess Real Sense Depth camera")
    
    cv2.namedWindow('QCarImageStream', cv2.WINDOW_AUTOSIZE)
    camera_image = cv2.imread('Quanser640x480.jpg')
    cv2.imshow('QCarImageStream', camera_image)
    cv2.waitKey(1)
    
    
    x, camera_image = QLabsQCar().get_image(qlabs, actorNumber=2, camera=QLabsQCar().CAMERA_CSI_FRONT)
    if (x == True):
        cv2.imshow('QCarImageStream', camera_image)
        cv2.waitKey(1)
    else:
        print("Image decoding failure") 

    PrintWS(x == True, "Image read CSI Front")
    cv2.waitKey(1000)

    x, camera_image = QLabsQCar().get_image(qlabs, actorNumber=2, camera=QLabsQCar().CAMERA_CSI_RIGHT)
    if (x == True):
        cv2.imshow('QCarImageStream', camera_image)
        cv2.waitKey(1)
    else:
        print("Image decoding failure") 

    PrintWS(x == True, "Image read CSI Right")
    cv2.waitKey(1000)

    x, camera_image = QLabsQCar().get_image(qlabs, actorNumber=2, camera=QLabsQCar().CAMERA_CSI_BACK)
    if (x == True):
        cv2.imshow('QCarImageStream', camera_image)
        cv2.waitKey(1)
    else:
        print("Image decoding failure") 

    PrintWS(x == True, "Image read CSI Back")
    cv2.waitKey(1000)

    x, camera_image = QLabsQCar().get_image(qlabs, actorNumber=2, camera=QLabsQCar().CAMERA_CSI_LEFT)
    if (x == True):
        cv2.imshow('QCarImageStream', camera_image)
        cv2.waitKey(1)
    else:
        print("Image decoding failure") 

    PrintWS(x == True, "Image read CSI Left")
    cv2.waitKey(1000)

    x, camera_image = QLabsQCar().get_image(qlabs, actorNumber=2, camera=QLabsQCar().CAMERA_RGB)
    if (x == True):
        cv2.imshow('QCarImageStream', camera_image)
        cv2.waitKey(1)
    else:
        print("Image decoding failure") 

    PrintWS(x == True, "Image read Real Sense RGB")
    cv2.waitKey(1000)

    x, camera_image = QLabsQCar().get_image(qlabs, actorNumber=2, camera=QLabsQCar().CAMERA_DEPTH)
    if (x == True):
        cv2.imshow('QCarImageStream', camera_image)
        cv2.waitKey(1)
    else:
        print("Image decoding failure") 

    PrintWS(x == True, "Image read Real Sense Depth")
    cv2.waitKey(1000)


    #ping
    print("Testing ping response...")
    x = QLabsQCar().ping(qlabs, 2)
    PrintWS(x == True, "Ping existing QCar (expect True)")
    
    x = QLabsQCar().ping(qlabs, 123)
    PrintWS(x == False, "Ping QCar that doesn't exist (expect False)")    
    
    
    #LIDAR

    QLabsQCar().possess(qlabs, 3, QLabsQCar().CAMERA_OVERHEAD)

    lidarPlot = pg.plot(title="LIDAR")   
    squareSize = 100
    lidarPlot.setXRange(-squareSize, squareSize)
    lidarPlot.setYRange(-squareSize, squareSize)
    lidarData = lidarPlot.plot([], [], pen=None, symbol='o', symbolBrush='r', symbolPen=None, symbolSize=2)
    
    
    time.sleep(1)
    
    print("Reading from LIDAR... if QLabs crashes, make sure FPS > 100 or fix the crash bug!")
    
    
    for count in range(20):
        
        success, angle, distance = QLabsQCar().get_lidar(qlabs,0,samplePoints=400)
        
        x = np.sin(angle)*distance
        y = np.cos(angle)*distance

        lidarData.setData(x,y)
        QtWidgets.QApplication.instance().processEvents()
        time.sleep(lidar_rate)

    PrintWS(True, "LIDAR didn't crash QLabs!")
    PrintWS(lidar_rate == 0.01, "Passed LIDAR test with 100Hz (lidar_rate = 0.01 expected)")

    time.sleep(2)
    
    checkFunctionTestList("library_qlabs_qcar")    
    '''
    ### Basic Shape
    PrintWSHeader("Basic Shape")
    print("\n\n---Basic Shape---")


    x = QLabsBasicShape().spawn(qlabs, actorNumber=200, location=[-18.852, 36.977, 0.5], rotation=[0,0,math.pi/4], scale=[0.5,0.5,0.5], configuration=QLabsBasicShape().SHAPE_CUBE, waitForConfirmation=True)
    PrintWS(x == 0, "Spawn sign with radians")

    x = QLabsBasicShape().spawn(qlabs, actorNumber=200, location=[-19.852, 36.977, 0.5], rotation=[0,0,math.pi/4], scale=[0.5,0.5,0.5], configuration=QLabsBasicShape().SHAPE_CUBE, waitForConfirmation=True)
    PrintWS(x == 2, "Spawn with duplicate ID")


    x = QLabsBasicShape().spawn_degrees(qlabs, actorNumber=220, location=[-18.832, 34.147, 0.5], rotation=[0,0,45], scale=[0.5,0.5,0.5], configuration=QLabsBasicShape().SHAPE_CUBE, waitForConfirmation=True)
    PrintWS(x == 0, "Spawn sign with degrees")

    x = QLabsBasicShape().spawn_degrees(qlabs, actorNumber=221, location=[-18.832, 35.147, 0.5], rotation=[0,0,45], scale=[0.5,0.5,0.5], configuration=QLabsBasicShape().SHAPE_CUBE, waitForConfirmation=True)
    x = QLabsBasicShape().destroy(qlabs, 221)
    PrintWS(x == 1, "Spawn and destroy existing (expect return 1)")

    x = QLabsBasicShape().destroy(qlabs, 222)
    PrintWS(x == 0, "Destroy shape that doesn't exist (expect return 0)")
    
    x = QLabsBasicShape().ping(qlabs, 220)
    PrintWS(x == True, "Ping existing sign (expect True)")
    
    x = QLabsBasicShape().ping(qlabs, 221)
    PrintWS(x == False, "Ping sign that doesn't exist (expect False)")

    x, loc, rot, scale = QLabsBasicShape().get_world_transform(qlabs, 200)
    PrintWS(np.sum(np.subtract(loc, [-18.852, 36.977, 0.5])) < 0.001 and x == True, "Get world transform")
       
    x = QLabsBasicShape().spawn_and_parent_with_relative_transform(qlabs, actorNumber=201, location=[0,2,0], rotation=[0,0,math.pi/4], scale=[1,1,1], configuration=QLabsBasicShape().SHAPE_CUBE, parentClass=QLabsBasicShape().ID_BASIC_SHAPE, parentActorNumber=200, parentComponent=0, waitForConfirmation=True)
    PrintWS(x == 0, "Spawn with parent relative transform (expect 0)")

    x = QLabsBasicShape().spawn_and_parent_with_relative_transform_degrees(qlabs, actorNumber=202, location=[0,-2,0], rotation=[0,0,45], scale=[1,1,1], configuration=QLabsBasicShape().SHAPE_CUBE, parentClass=QLabsBasicShape().ID_BASIC_SHAPE, parentActorNumber=200, parentComponent=0, waitForConfirmation=True)
    PrintWS(x == 0, "Spawn with parent relative transform degrees (expect 0)")


    x = QLabsBasicShape().set_material_properties(qlabs, actorNumber=202, colour=[0,1,0], roughness=0.0, metallic=True, waitForConfirmation=True)
    x = QLabsBasicShape().set_material_properties(qlabs, actorNumber=201, colour=[1,0,0], roughness=0.0, metallic=True, waitForConfirmation=True)
    PrintWS(x == True, "Set material properties (expect True)")

    
    for y in range(51):
        x = QLabsBasicShape().set_transform(qlabs, actorNumber=201, location=[0,2,0], rotation=[0,0,math.pi/4-math.pi/25*y], scale=[1,1,1])
        x = QLabsBasicShape().set_transform_degrees(qlabs, actorNumber=202, location=[0,-2,0], rotation=[0,0,45-180/25*y], scale=[1,1,1])
        x = QLabsBasicShape().set_transform(qlabs, actorNumber=200, location=[-18.852, 36.977, 0.5], rotation=[0,0,math.pi/4+2*math.pi/50*y], scale=[0.5+0.5*y/50,0.5+0.5*y/50,0.5+0.5*y/50])
    

    x = QLabsBasicShape().spawn(qlabs, actorNumber=203, location=[-18.75, 32.5, 0.25], rotation=[0,0,0], scale=[0.5,0.5,0.5], configuration=QLabsBasicShape().SHAPE_SPHERE, waitForConfirmation=True)
    x = QLabsBasicShape().set_material_properties(qlabs, actorNumber=203, colour=[0,1,0], roughness=0.0, metallic=False, waitForConfirmation=True)
    

    x = QLabsBasicShape().spawn(qlabs, actorNumber=204, location=[-18.75, 31.5, 0.25], rotation=[0,0,0], scale=[0.5,0.5,0.5], configuration=QLabsBasicShape().SHAPE_SPHERE, waitForConfirmation=True)
    x = QLabsBasicShape().set_material_properties(qlabs, actorNumber=204, colour=[0,0,1], roughness=0.0, metallic=False, waitForConfirmation=True)
    x = QLabsBasicShape().set_enable_collisions(qlabs, actorNumber=204, enableCollisions=False, waitForConfirmation=True)
    PrintWS(x == True, "Enable collisions")

    x = QLabsBasicShape().spawn(qlabs, actorNumber=205, location=[-18.6, 32.5, 2], rotation=[0,0,0], scale=[0.6,0.6,0.6], configuration=QLabsBasicShape().SHAPE_SPHERE, waitForConfirmation=True)
    x = QLabsBasicShape().spawn(qlabs, actorNumber=206, location=[-18.6, 31.5, 2], rotation=[0,0,0], scale=[0.6,0.6,0.6], configuration=QLabsBasicShape().SHAPE_SPHERE, waitForConfirmation=True)
    x = QLabsBasicShape().spawn(qlabs, actorNumber=207, location=[-18.6, 30.5, 2], rotation=[0,0,0], scale=[0.6,0.6,0.6], configuration=QLabsBasicShape().SHAPE_SPHERE, waitForConfirmation=True)
    
    x = QLabsBasicShape().set_physics_properties(qlabs, actorNumber=207, mass=1, linearDamping=10, angularDamping=0, enableDynamics=False, waitForConfirmation=True)
    PrintWS(x == True, "Set physics properties")

    x = QLabsBasicShape().set_enable_dynamics(qlabs, actorNumber=205, enableDynamics=True, waitForConfirmation=False)
    x = QLabsBasicShape().set_enable_dynamics(qlabs, actorNumber=206, enableDynamics=True, waitForConfirmation=False)
    x = QLabsBasicShape().set_enable_dynamics(qlabs, actorNumber=207, enableDynamics=True, waitForConfirmation=True)
    PrintWS(x == True, "Enable dynamics")

    x = QLabsBasicShape().set_enable_dynamics(qlabs, actorNumber=205, enableDynamics=True, waitForConfirmation=False)
    
    
    x = QLabsBasicShape().spawn_box_walls_from_center(qlabs, actorNumbers=[210, 211, 212, 213, 214], centerLocation=[-15.103, 32.404, 0.005], yaw=math.pi/4, xSize=2, ySize=2, zHeight=0.5, wallThickness=0.1, floorThickness=0.1, wallColour=[1,0,0], floorColour=[0,0,1], waitForConfirmation=True)

    checkFunctionTestList("library_qlabs_basic_shape")    



    

    ### Widget
    PrintWSHeader("Widget")
    print("\n\n--Widget---")

    x = QLabsFreeCamera().possess(qlabs, 2)
    QLabsWidget().widget_spawn_configuration(qlabs, enableShadow=True)

    for count in range(20):
        x = QLabsWidget().spawn(qlabs, QLabsWidget().METAL_CAN, [-15.504, 32.584, 1+count*0.2], [0,0,0], [1,1,1], [1,1,1], measuredMass=0, IDTag=0, properties='', waitForConfirmation=True)

    PrintWS(x == True, "Widget spawn (expect True)")

    time.sleep(1)

    for count in range(20):
        x = QLabsWidget().spawn_degrees(qlabs, QLabsWidget().METAL_CAN, [-15.504, 32.584, 1+count*0.2], [90,0,0], [1,1,1], [1,0,0], measuredMass=0, IDTag=0, properties='', waitForConfirmation=True)

    PrintWS(x == True, "Widget spawn degrees(expect True)")

    time.sleep(1)

    x = QLabsWidget().destroy_all_spawned_widgets(qlabs)
    PrintWS(x == True, "Widgets destroyed (expect True)")
    QLabsWidget().widget_spawn_configuration(qlabs, enableShadow=False)
    
    for count in range(10):
        x = QLabsWidget().spawn_degrees(qlabs, QLabsWidget().SPHERE, [-15.504, 32.584+count*0.01, 1+count*0.6], [90,0,0], [0.5,0.5,0.5], [1,0,0], measuredMass=0, IDTag=0, properties='', waitForConfirmation=True)

    time.sleep(1)

    QLabsWidget().destroy_all_spawned_widgets(qlabs)
    QLabsWidget().widget_spawn_configuration(qlabs, enableShadow=True)

    for count in range(10):
        x = QLabsWidget().spawn_degrees(qlabs, QLabsWidget().SPHERE, [-15.504, 32.584+count*0.01, 1+count*0.6], [90,0,0], [0.5,0.5,0.5], [1,0,0], measuredMass=0, IDTag=0, properties='', waitForConfirmation=True)

    
    
    checkFunctionTestList("library_qlabs_widget")  

    ### Image Utilities
    PrintWSHeader("Image Utilities")
    print("\n\n---Image Utilities---")

    checkFunctionTestList("library_qlabs_image_utilities")    

    ### Utilities
    PrintWSHeader("Utilities")
    print("\n\n---Utilities---")

    checkFunctionTestList("library_qlabs_utilities")  
    
    ### Real-Time
    PrintWSHeader("Real-Time")
    print("\n\n---Real-Time---")

    checkFunctionTestList("library_qlabs_real_time")    

    ### Spline Line
    PrintWSHeader("Spline Line")
    print("\n\n---Spline Line---")

    checkFunctionTestList("library_qlabs_spline_line")  
    


    print("\n\n------------------------------ Communications --------------------------------\n")
    
    qlabs.close()
    cv2.destroyAllWindows()
    print("Done!")  
 

wb_file = 'QLabs Validation Report.xlsx'
wb = xlsxwriter.Workbook(wb_file)
ws = wb.add_worksheet()
row = 0
header_text = wb.add_format({'bold': True, 'font_size': 18})
status_good = wb.add_format({'bg_color':'green'})
status_bad = wb.add_format({'bg_color':'red'})



main()

ws.set_column(0,0,2.5)
ws.set_column(1,1,40)

try:
    wb.close()
    os.startfile(wb_file)
except:
    print("\n\n*** Couldn't write the Excel file.")