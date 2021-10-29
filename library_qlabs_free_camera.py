from library_qlabs import QuanserInteractiveLabs, CommModularContainer
from quanser.common import GenericError
import math

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsFreeCamera: 
       
    ID_FREE_CAMERA = 170
    FCN_FREE_CAMERA_POSSESS = 10
    FCN_FREE_CAMERA_POSSESS_ACK = 11
    FCN_FREE_CAMERA_SET_CAMERA_FEATURES = 12
    FCN_FREE_CAMERA_SET_CAMERA_FEATURES_ACK = 13

    
    # Initialize class
    def __init__(self):

       return
       
    def spawn(self, qlabs, deviceNumber, location, rotation):
        return qlabs.spawn(deviceNumber, self.ID_FREE_CAMERA, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1, 1, 1, 0, True)
           
    def spawnDegrees(self, qlabs, deviceNumber, location, rotation):
        rotation[0] = rotation[0]/180*math.pi
        rotation[1] = rotation[1]/180*math.pi
        rotation[2] = rotation[2]/180*math.pi
        
        return qlabs.spawn(deviceNumber, self.ID_FREE_CAMERA, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1, 1, 1, 0, True)
    
    
    def possess(self, qlabs, deviceNumber):
        c = CommModularContainer()
        c.classID = self.ID_FREE_CAMERA
        c.deviceNumber = deviceNumber
        c.deviceFunction = self.FCN_FREE_CAMERA_POSSESS
        c.payload = bytearray()
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flushReceive()  
        
        if (qlabs.sendContainer(c)):
            c = qlabs.waitForContainer(self.ID_FREE_CAMERA, deviceNumber, self.FCN_FREE_CAMERA_POSSESS_ACK)
                    
            return True
        else:
            return False   
        
        
