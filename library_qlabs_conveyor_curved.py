from library_qlabs import QuanserInteractiveLabs, CommModularContainer
from quanser.common import GenericError
import math

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsConveyorCurved:

       
    ID_CONVEYOR_CURVED = 211
    
    FCN_CONVEYOR_CURVED_SET_SPEED = 10
    FCN_CONVEYOR_CURVED_SET_SPEED_ACK = 11
    
    
    # Initialize class
    def __init__(self):

       return
       
       
    def spawn(self, qlabs, deviceNumber, location, rotation, sections=0, waitForConfirmation=True):
        return qlabs.spawn(deviceNumber, self.ID_CONVEYOR_CURVED, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1, 1, 1, sections, waitForConfirmation)
 
    def spawnDegrees(self, qlabs, deviceNumber, location, rotation, sections=0, waitForConfirmation=True):
        return qlabs.spawn(deviceNumber, self.ID_CONVEYOR_CURVED, location[0], location[1], location[2], rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi, 1, 1, 1, sections, waitForConfirmation)
 
    def setSpeed(self, qlabs, deviceNumber, speed):
        c = CommModularContainer()
        c.classID = self.ID_CONVEYOR_CURVED
        c.deviceNumber = deviceNumber
        c.deviceFunction = self.FCN_CONVEYOR_CURVED_SET_SPEED
        c.payload = bytearray(struct.pack(">f", speed))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flushReceive()  
        
        if (qlabs.sendContainer(c)):
            c = qlabs.waitForContainer(self.ID_CONVEYOR_CURVED, deviceNumber, self.FCN_CONVEYOR_CURVED_SET_SPEED_ACK)
                    
            return True
        else:
            return False    