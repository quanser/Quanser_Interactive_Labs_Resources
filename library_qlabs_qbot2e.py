from library_qlabs import QuanserInteractiveLabs, CommModularContainer
from quanser.common import GenericError
import math

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsQBot2e:

       
    ID_QBOT = 20
    
    FCN_QBOT_COMMAND_AND_REQUEST_STATE = 10
    FCN_QBOT_COMMAND_AND_REQUEST_STATE_RESPONSE = 11
    FCN_QBOT_POSSESS = 20
    FCN_QBOT_POSSESS_ACK = 21
    
    
    VIEWPOINT_RGB = 0
    VIEWPOINT_DEPTH = 1
    VIEWPOINT_TRAILING = 2
    
    # Initialize class
    def __init__(self):

       return
       
    def spawn(self, qlabs, deviceNumber, location, rotation, configuration=0, waitForConfirmation=True):
        return qlabs.spawn(deviceNumber, self.ID_QBOT, location[0], location[1], location[2]+0.1, rotation[0], rotation[1], rotation[2], 1.0, 1.0, 1.0, configuration, waitForConfirmation)
   
    def spawn_degrees(self, qlabs, deviceNumber, location, rotation, configuration=0, waitForConfirmation=True):
    
        return qlabs.spawn(deviceNumber, self.ID_QBOT, location[0], location[1], location[2]+0.1, rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi, 1.0, 1.0, 1.0, configuration, waitForConfirmation)
   
   
    def possess(self, qlabs, deviceNumber, camera):
        c = CommModularContainer()
        c.classID = self.ID_QBOT
        c.deviceNumber = deviceNumber
        c.deviceFunction = self.FCN_QBOT_POSSESS
        c.payload = bytearray(struct.pack(">B", camera))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            c = qlabs.wait_for_container(self.ID_QBOT, deviceNumber, self.FCN_QBOT_POSSESS_ACK)
                    
            return True
        else:
            return False
            
    def command_and_request_state(self, qlabs, deviceNumber, rightWheelSpeed, leftWheelSpeed):
        c = CommModularContainer()
        c.classID = self.ID_QBOT
        c.deviceNumber = deviceNumber
        c.deviceFunction = self.FCN_QBOT_COMMAND_AND_REQUEST_STATE
        c.payload = bytearray(struct.pack(">ff", rightWheelSpeed, leftWheelSpeed))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            c = qlabs.wait_for_container(self.ID_QBOT, deviceNumber, self.FCN_QBOT_COMMAND_AND_REQUEST_STATE_RESPONSE)
                    
            return True
        else:
            return False
            
