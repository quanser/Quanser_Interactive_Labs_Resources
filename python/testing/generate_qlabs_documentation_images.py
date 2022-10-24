import sys
library_path = '../libraries'
sys.path.append(library_path)

from library_qlabs import QuanserInteractiveLabs
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
from library_qlabs_spline_line import QLabsSplineLine
from library_qlabs_real_time import QLabsRealTime
from library_qlabs_widget import QLabsWidget
from library_qlabs_traffic_light import QLabsTrafficLight
from library_qlabs_animal import QLabsAnimal

from library_verification_report import verificationReport



import sys
import subprocess
import time
import math
import struct
import numpy as np
import cv2
import xlsxwriter
import os
import random

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
               'library_qlabs_qube_servo_2',\
               'library_qlabs_actor',\
               'library_qlabs_image_utilities']

 
def openImage(path):
    imageViewerFromCommandLine = {'linux':'xdg-open',
                                  'win32':'explorer',
                                  'darwin':'open'}[sys.platform]
    subprocess.Popen([imageViewerFromCommandLine, path])

def get_color_and_mask(camera_name, crop_range, hsv_min=[0,0,0], hsv_max=[255,255,255], dialate_size = 3, showDebugImages = False):
    
    
    x = camera_name.set_image_capture_resolution(width=4096, height=2000)
    x, img = camera_name.get_image()
    if (x == True):
        if showDebugImages:
            cv2.namedWindow('RawImage', cv2.WINDOW_AUTOSIZE)
            cv2.imshow('RawImage', resize_image(img, 0.25))
            cv2.waitKey(1)
        pass
        
    else:
        print("Image decoding failure")
        return
    
    img = img[crop_range[0]:crop_range[1], crop_range[2]:crop_range[3]]
    
    if showDebugImages:
        cv2.namedWindow('ProcessedImage', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('ProcessedImage', resize_image(img, 0.25))
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Threshold the HSV image 
    mask = cv2.inRange(hsv, hsv_min, hsv_max)
    
    # Dialate the mask to get a bit of overlap
    kernel = np.ones((dialate_size,dialate_size),np.uint8)
    mask = cv2.dilate(mask, kernel)

    # The blur to round the edges
    mask = cv2.GaussianBlur(mask, (5,5), 0)
    mask = cv2.GaussianBlur(mask, (5,5), 0)
    
    # And sharpen again
    kernelSharp = np.array([[1, 4, 6, 4, 1], [4, 16, 24, 16, 4], [6, 24, -476, 24, 6], [4, 16, 24, 16, 4], [1, 4, 6, 4, 1]])/-256
    mask = cv2.filter2D(mask, -1, kernelSharp)
    mask = cv2.filter2D(mask, -1, kernelSharp)
    
    if showDebugImages:
        cv2.namedWindow('MaskImage', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('MaskImage', resize_image(mask, 0.25))
        cv2.waitKey()
    
   
    
    return img, mask

    
    
def save_masked_image(file_path, color_image, mask_image, scale=1.0, previewImages=False):
   
    c_red, c_green, c_blue = cv2.split(color_image)
    
    img_a = cv2.merge((c_red, c_green, c_blue, 255-mask_image))
    
    resized = resize_image(img_a, scale)
    
    cv2.imwrite(file_path, resized)  
    
    if (previewImages):
        full_path = os.path.abspath(file_path)
        openImage(full_path)
    
def resize_image(img, scale):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dim = (width, height)
    
    
    return cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    

def save_image(file_path, color_image, scale=1.0, previewImages=False):


    resized = resize_image(color_image, scale)
    
    cv2.imwrite(file_path, resized)    
    
    if (previewImages):
        full_path = os.path.abspath(file_path)
        openImage(full_path)


def gammaCorrection(img, gamma):
    ## [changing-contrast-brightness-gamma-correction]
    lookUpTable = np.empty((1,256), np.uint8)
    for i in range(256):
        lookUpTable[0,i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)

    return cv2.LUT(img, lookUpTable)
    

    
def main(previewImages = False):
    os.system('cls')
    
    
    print("\n\n------------------------------ Communications --------------------------------\n")
    
    qlabs = QuanserInteractiveLabs()
    cv2.startWindowThread()

    print("Connecting to QLabs...")
    try:
        qlabs.open("localhost")
    except:
        print("Unable to connect to QLabs")
        return
    
    print("Connected")
    
    

    print("\n\n------------------------- Setup ---------------------------\n")
    
    
    ### QLabs
    print("Destroyed {} actors.".format(qlabs.destroy_all_spawned_actors()))
        
    
    ### System

    hSystem = QLabsSystem(qlabs)
    x = hSystem.set_title_string('', waitForConfirmation=True)
    
    
    hCamera = QLabsFreeCamera(qlabs)
    x = hCamera.spawn(location=[91.179, 66.456, 1.786], rotation=[0, 0.096, -1.581])
    hCamera.possess()

    hCamera2 = QLabsFreeCamera(qlabs)
    x = hCamera2.spawn(location=[91.234, 71.06, 2.359], rotation=[0, 0.043, -1.58])
    
    
    #backdrop
    
    loc = [90, 50, 0]
    hCube1 = QLabsBasicShape(qlabs)
    hCube1.spawn_degrees(location=loc, rotation=[0, 0, 0], scale=[150, 60, 1], configuration=0)
    hCube1.set_material_properties([0,1,0], 1)
    
    hCube2 = QLabsBasicShape(qlabs)
    hCube2.spawn_degrees(location=[loc[0], loc[1]-15, 0], rotation=[45, 0, 0], scale=[150, 1, 150], configuration=0)
    hCube2.set_material_properties([0,1,0], 1)
    
    hEnvironmentOutdoors = QLabsEnvironmentOutdoors(qlabs)
    hEnvironmentOutdoors.set_time_of_day(13) #1:00pm
    
    print("\n\n------------------------- Generating Images ---------------------------\n")

    """
    ### People
    print("People\n")

    hPerson = QLabsPerson(qlabs)
    
    for count in range(6):
        hPerson.spawn(location=[95.5 - count*0.8, 60, 0.5], rotation=[0,0,math.pi/2], scale=[1,1,1], configuration=count, waitForConfirmation=True)

    for count in range(6):
        hPerson.spawn(location=[95 - (count+6)*0.8, 60, 0.7], rotation=[0,0,math.pi/2], scale=[1,1,1], configuration=count+6, waitForConfirmation=True)


    time.sleep(0.5)

    hsv_min = np.array([50,100,150])
    hsv_max = np.array([90,255,255])
    color_image, mask_image = get_color_and_mask(hCamera, [300, 1700, 300, 3900], hsv_min, hsv_max, 3)
    color_image = gammaCorrection(color_image, 0.8)
    
    # Change cubes to white to avoid the green splash that shows up on the actors and save just the color image
    hCube1.set_material_properties([1,1,1], 1)
    hCube2.set_material_properties([1,1,1], 1)
    color_image, temp = get_color_and_mask(hCamera, [300, 1700, 300, 3900], hsv_min, hsv_max, 3)
    color_image = gammaCorrection(color_image, 0.8)
    
    save_masked_image('../docs/source/pictures/people.png', color_image, mask_image, 0.4, previewImages)

    hCube1.set_material_properties([0,1,0], 1)
    hCube2.set_material_properties([0,1,0], 1)
    

    hPerson.destroy_all_actors_of_class()
    
    
    ### Cones
    print("Cones\n")

    hCone = QLabsTrafficCone(qlabs)
    
    for count in range(2):
        hCone.spawn(location=[91.562 - count, 63, 0.5], rotation=[0,0,math.pi/2], scale=[1,1,1], configuration=count, waitForConfirmation=True)

    time.sleep(0.5)

    hsv_min = np.array([50,100,50])
    hsv_max = np.array([90,255,255])
    color_image, mask_image = get_color_and_mask(hCamera, [800, 1800, 1400, 3000], hsv_min, hsv_max, showDebugImages=False)
    color_image = gammaCorrection(color_image, 0.6)
    
    
    save_masked_image('../docs/source/pictures/trafficCones.png', color_image, mask_image, 0.6, previewImages)
    hCone.destroy_all_actors_of_class()


    ### yield_sign
    
    print("Yield Sign\n")
    hYield_sign = QLabsYieldSign(qlabs)
    hYield_sign.spawn(location=[91.562, 63, 0.5], rotation=[0,0,math.pi/2], scale=[1,1,1], configuration=0, waitForConfirmation=True)

    time.sleep(0.5)

    hsv_min = np.array([50,100,0])
    hsv_max = np.array([90,255,255])
    color_image, mask_image = get_color_and_mask(hCamera, [50, 1700, 50, 3900], hsv_min, hsv_max, showDebugImages=False)
    color_image = gammaCorrection(color_image, 0.6)
    
    
    save_masked_image('../docs/source/pictures/yieldsign.png', color_image, mask_image, 0.6, previewImages)
    hYield_sign.destroy_all_actors_of_class()


    ### stop sign

    print("Stop Sign\n")
    hStopSign = QLabsStopSign(qlabs)
    hStopSign.spawn(location=[91.562, 63, 0.5], rotation=[0,0,math.pi/2], scale=[1,1,1], configuration=0, waitForConfirmation=True)

    time.sleep(0.5)

    hsv_min = np.array([50,100,0])
    hsv_max = np.array([90,255,255])
    color_image, mask_image = get_color_and_mask(hCamera, [50, 1700, 50, 3900], hsv_min, hsv_max, showDebugImages=False)
    color_image = gammaCorrection(color_image, 0.6)
    
    
    save_masked_image('../docs/source/pictures/stopsign.png', color_image, mask_image, 0.6, previewImages)
    hStopSign.destroy_all_actors_of_class()

    ### roundabout_sign

    print("Roundabout Sign\n")
    hRoundaboutSign = QLabsRoundaboutSign(qlabs)
    hRoundaboutSign.spawn(location=[91.562, 63, 0.5], rotation=[0,0,math.pi/2], scale=[1,1,1], configuration=0, waitForConfirmation=True)

    time.sleep(0.5)

    hsv_min = np.array([50,100,150])
    hsv_max = np.array([90,255,255])
    color_image, mask_image = get_color_and_mask(hCamera, [50, 1700, 50, 3900], hsv_min, hsv_max, showDebugImages=False)
    color_image = gammaCorrection(color_image, 0.6)

    save_masked_image('../docs/source/pictures/roundaboutsign.png', color_image, mask_image, 0.6, previewImages)
    hRoundaboutSign.destroy_all_actors_of_class()
    
    ### widgets

    print("Widgets\n")

    hWidgets = QLabsWidget(qlabs)
    
    hWidgets.spawn(location=[91.562-0.75, 63, 0.5], rotation=[0,0,math.pi/2], scale=[1,1,1], configuration=hWidgets.METAL_CAN, color=[1,0,0], measuredMass=0, IDTag=0, properties='', waitForConfirmation=True)
    hWidgets.spawn(location=[91.562-0.25, 63, 0.5], rotation=[0,0,math.pi/2], scale=[1,1,1], configuration=hWidgets.PLASTIC_BOTTLE, color=[1,0,0], measuredMass=0, IDTag=0, properties='', waitForConfirmation=True)
    #hWidgets.spawn(location=[91.562, 63, 0.5], rotation=[0,0,math.pi/2], scale=[2,2,2], configuration=hWidgets.AUTOCLAVE_CAGE, color=[1,0,0], measuredMass=0, IDTag=0, properties='', waitForConfirmation=True)
    hWidgets.spawn(location=[91.562+0.25, 63, 0.5], rotation=[0,0,math.pi/2], scale=[0.25,0.25,0.25], configuration=hWidgets.SPHERE, color=[1,0,0], measuredMass=0, IDTag=0, properties='', waitForConfirmation=True)
    hWidgets.spawn(location=[91.562 + 0.75, 63, 0.5], rotation=[0,0,math.pi/2], scale=[0.25,0.25,0.25], configuration=hWidgets.CYLINDER, color=[1,0,0], measuredMass=0, IDTag=0, properties='', waitForConfirmation=True)
    hWidgets.spawn(location=[91.562 + 1.25, 63, 0.75], rotation=[0,0,math.pi/2], scale=[0.25,0.25,0.25], configuration=hWidgets.CUBE, color=[1,0,0], measuredMass=0, IDTag=0, properties='', waitForConfirmation=True)

    time.sleep(1)

    hsv_min = np.array([50,100,50])
    hsv_max = np.array([90,255,255])
    color_image, mask_image = get_color_and_mask(hCamera, [1000, 2000, 700, 2500], hsv_min, hsv_max, 4, showDebugImages=False)
    color_image = gammaCorrection(color_image, 0.6)
    
    
    save_masked_image('../docs/source/pictures/widgets.png', color_image, mask_image, 0.6, previewImages)
    hWidgets.destroy_all_spawned_widgets()
    
    ### basic shapes

    hBasicShape = QLabsBasicShape(qlabs)
    hBasicShape.spawn(location=[91.562-2, 63, 1], rotation=[0,0,math.pi/2], scale=[1,1,1], configuration=0, waitForConfirmation=True)
    hBasicShape.spawn(location=[91.562, 63, 1], rotation=[0,0,math.pi/2], scale=[1,1,1], configuration=1, waitForConfirmation=True)
    hBasicShape.spawn(location=[91.562+2, 63, 1], rotation=[0,0,math.pi/2], scale=[1,1,1], configuration=2, waitForConfirmation=True)

    time.sleep(1)

    hsv_min = np.array([50,100,50])
    hsv_max = np.array([90,255,255])
    color_image, mask_image = get_color_and_mask(hCamera, [500, 2000, 50, 3700], hsv_min, hsv_max, showDebugImages=False)
    color_image = gammaCorrection(color_image, 0.6)

    save_masked_image('../docs/source/pictures/basicshapes.png', color_image, mask_image, 0.6, previewImages)

    
    ### traffic_light

    print("Traffic Light\n")
    hCamera2.possess()
    hTrafficLight = QLabsTrafficLight(qlabs)
    
    for count in range(3):
        if count==1 or 2:
            spacing = count*4
        hTrafficLight.spawn(location=[93.562 - spacing, 63, 0.5], rotation=[0,0,-math.pi], scale=[1,1,1], configuration=count, waitForConfirmation=True)

    time.sleep(0.5)

    hsv_min = np.array([50,100,150])
    hsv_max = np.array([90,255,255])
    color_image, mask_image = get_color_and_mask(hCamera2, [10, 1500, 10, 4000], hsv_min, hsv_max, 6)
    color_image = gammaCorrection(color_image, 0.8)
    
    
    save_masked_image('../docs/source/pictures/trafficlight.png', color_image, mask_image, 0.4, previewImages)

    hTrafficLight.destroy_all_actors_of_class()


    ### crosswalks


    ### qCars
    print("qCar\n")
    hCamera.possess()
    car = QLabsQCar(qlabs)
    car.spawn_id(actorNumber=0, location=[91.585, 59, 0.5], rotation=[0,0,math.pi/4], scale=[1,1,1], configuration=0, waitForConfirmation=True)

    time.sleep(0.5)

    hsv_min = np.array([50,100,150])
    hsv_max = np.array([90,255,255])
    color_image, mask_image = get_color_and_mask(hCamera, [400, 1900, 800, 2300], hsv_min, hsv_max, 6)
    color_image = gammaCorrection(color_image, 0.8)
    
    
    save_masked_image('../docs/source/pictures/qCar.png', color_image, mask_image, 0.4, previewImages)

    car.destroy_all_actors_of_class()


    print("\n\n------------------------------ Communications --------------------------------\n")
    """



    ############################ Banner shots #######################################
    qlabs.destroy_all_spawned_actors()


    #widgets
    hCamera = QLabsFreeCamera(qlabs)
    hCamera.spawn_degrees(location=[9.997, 28.452, 1.909], rotation=[0, -4.75, -0.303])
    hCamera.possess()

    hWidgets = QLabsWidget(qlabs)
    
    widgetWait = False
    x_size = 20

    for z in range(50):
        for x in range(x_size):
            widgetType = x % 3
            if widgetType > 3:
                widgetType = widgetType + 1

            widgetSize = np.array([0.4,0.4,0.4])*(0.1+random.random())

            hWidgets.spawn(location=[18, 22.861+12/x_size*x, z*0.2+1], rotation=[0,0,0], scale=widgetSize, configuration=widgetType, color=[1,0,0], measuredMass=0, IDTag=0, properties='', waitForConfirmation=widgetWait)

        time.sleep(0.01)
    time.sleep(1)

    hsv_min = np.array([50,100,50])
    hsv_max = np.array([90,255,255])
    color_image, temp = get_color_and_mask(hCamera, [500, 2000, 0, 4095], hsv_min, hsv_max, 3, False)
    color_image = gammaCorrection(color_image, 0.8)
    
    save_image('../docs/source/pictures/widget_banner.png', color_image, 0.4, previewImages) 


    qlabs.close()
    cv2.destroyAllWindows()
    print("Done!")  
 


main(previewImages = True)

