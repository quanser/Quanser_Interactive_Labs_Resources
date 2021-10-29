from library_qlabs import QuanserInteractiveLabs, CommModularContainer
from quanser.common import GenericError
import math

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsReferenceIndicator:

    
       
    ID_REF_IND = 10040
    FCN_REF_IND_SET_TRANSFORM_AND_COLOR = 10
    FCN_REF_IND_SET_TRANSFORM_AND_COLOR_ACK = 11
    
    # Initialize class
    def __init__(self):

       return
       
       
    def spawn(self, qlabs, deviceNumber, location, rotation, scale, configuration=0, waitForConfirmation=True):
        return qlabs.spawn(deviceNumber, self.ID_REF_IND, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2], configuration, waitForConfirmation)
 
    def spawnDegrees(self, qlabs, deviceNumber, location, rotation, scale, configuration=0, waitForConfirmation=True):
        rotation[0] = rotation[0]/180*math.pi
        rotation[1] = rotation[1]/180*math.pi
        rotation[2] = rotation[2]/180*math.pi
        
        return qlabs.spawn(deviceNumber, self.ID_REF_IND, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2], configuration, waitForConfirmation)
 
 
 
    def setTransformAndColor(self, qlabs, deviceNumber, x, y, z, roll, pitch, yaw, sx, sy, sz, r, g, b, waitForConfirmation=True):
        c = CommModularContainer()
        c.classID = self.ID_REF_IND
        c.deviceNumber = deviceNumber
        c.deviceFunction = self.FCN_REF_IND_SET_TRANSFORM_AND_COLOR
        c.payload = bytearray(struct.pack(">ffffffffffff", x, y, z, roll, pitch, yaw, sx, sy, sz, r, g, b ))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if waitForConfirmation:
            qlabs.flushReceive()  
        
        if (qlabs.sendContainer(c)):
            if waitForConfirmation:
                c = qlabs.waitForContainer(self.FCN_REF_IND_SET_TRANSFORM_AND_COLOR, deviceNumber, self.FCN_REF_IND_SET_TRANSFORM_AND_COLOR_ACK)
                return c
                    
            return True
        else:
            return False    
