import sys
sys.path.insert(0, "../")

from qvl.qlabs import QuanserInteractiveLabs

from qvl.qbot import qlab_qbot
from qvl.qbot3 import QLabsQBot3
from qvl.qbot2e import QLabsQBot2e
from qvl.qbot_platform import QLabsQBotPlatform
from qvl.walls import QLabsWalls
from qvl.reference_frame import QLabsReferenceFrame
from qvl.shredder import QLabsShredder
from qvl.delivery_tube import QLabsDeliveryTube
from qvl.qarm import QLabsQArm
from qvl.conveyor_curved import QLabsConveyorCurved
from qvl.flooring import QLabsFlooring
from qvl.conveyor_straight import QLabsConveyorStraight

from library_verification_report import verificationReport

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

##########################################

library_path = '.../qvl'

##########################################

ignore_list = ['autoclave', \
               'bottle_table', \
               'qbot_hopper', \
               'srv02', \
               'weigh_scale', \
               'qube_servo_2',\
               'actor',\
               'yield_sign',\
               'stop_sign',\
               'roundabout_sign',\
               'traffic_cone',\
               'crosswalk',\
               'basic_shape',\
               'qcar',\
               'environment_outdoors',\
               'person',\
               'spline_line',\
               'widget',\
               'traffic_light',\
               'image_utilities']

def main():
    os.system('cls')

    print("----------------- Checking that all libraries are being tested -------------------\n")
    vr.PrintWSHeader("Library Test List")
    #vr.checkValidationLibraryList()

    print("\n\n------------------------------ Communications --------------------------------\n")

    vr.PrintWSHeader("Communications")
    qlabs = QuanserInteractiveLabs()
    cv2.startWindowThread()

    print("Connecting to QLabs...")
    try:
        qlabs.open("localhost")
    except:
        print("Unable to connect to QLabs")
        vr.PrintWS(0, "Connection success")
        return

    print("Connected")
    vr.PrintWS(1, "Connection success")

    print("\n\n------------------------------ Testing Libraries --------------------------------\n")

    ### QLabs
    vr.PrintWSHeader("Common")
    x = "Destroyed {} actors.".format(qlabs.destroy_all_spawned_actors())
    print(x)
    vr.PrintWS(2, x)

    print("\n\n------------------------------ Qbot --------------------------------\n")
    vr.PrintWSHeader("Qbot")


    print("\n\n------------------------------ Qbot2e --------------------------------\n")
    vr.PrintWSHeader("Qbot2e")


    print("\n\n------------------------------ Qbot3 --------------------------------\n")
    vr.PrintWSHeader("Qbot3")


    print("\n\n------------------------------ QLabsQBotPlatform --------------------------------\n")
    vr.PrintWSHeader("QLabsQBotPlatform")




vr = verificationReport('QBot Validation Report.xlsx', 'library_verification_qbot.py', library_path)
vr.ignore_list = ignore_list

main()

vr.WriteFileBuffer()