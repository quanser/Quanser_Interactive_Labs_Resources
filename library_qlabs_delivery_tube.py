from library_qlabs import QuanserInteractiveLabs, CommModularContainer
from quanser.common import GenericError
import math

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsDeliveryTube:

       
    ID_DELIVERY_TUBE = 80
    
    FCN_DELIVERY_TUBE_SPAWN_BLOCK = 10
    FCN_DELIVERY_TUBE_SPAWN_BLOCK_ACK = 11
    FCN_DELIVERY_TUBE_SET_HEIGHT = 12
    FCN_DELIVERY_TUBE_SET_HEIGHT_ACK = 13
    
    BLOCK_CUBE = 0
    BLOCK_CYLINDER = 1
    BLOCK_SPHERE = 2
    BLOCK_GEOSPHERE = 3
    
    CONFIG_HOVER = 0
    CONFIG_NO_HOVER = 1
    
    # Initialize class
    def __init__(self):

       return
       
    def spawn(self, qlabs, deviceNumber, location, rotation, configuration=0, waitForConfirmation=True):
        return qlabs.spawn(deviceNumber, self.ID_DELIVERY_TUBE, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1, 1, 1, configuration, waitForConfirmation)
 
    def spawnDegrees(self, qlabs, deviceNumber, location, rotation, configuration=0, waitForConfirmation=True):
        rotation[0] = rotation[0]/180*math.pi
        rotation[1] = rotation[1]/180*math.pi
        rotation[2] = rotation[2]/180*math.pi    
    
        return qlabs.spawn(deviceNumber, self.ID_DELIVERY_TUBE, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1, 1, 1, configuration, waitForConfirmation)
  
    
    
    def spawnBlock(self, qlabs, deviceNumber, blockType, mass, yawRotation, color):
        c = CommModularContainer()
        c.classID = self.ID_DELIVERY_TUBE
        c.deviceNumber = deviceNumber
        c.deviceFunction = self.FCN_DELIVERY_TUBE_SPAWN_BLOCK
        c.payload = bytearray(struct.pack(">Ifffff", blockType, mass, yawRotation, color[0], color[1], color[2]))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flushReceive()  
        
        if (qlabs.sendContainer(c)):
            c = qlabs.waitForContainer(self.ID_DELIVERY_TUBE, deviceNumber, self.FCN_DELIVERY_TUBE_SPAWN_BLOCK_ACK)
                    
            return True
        else:
            return False 
            
    def setHeight(self, qlabs, deviceNumber, height):
        c = CommModularContainer()
        c.classID = self.ID_DELIVERY_TUBE
        c.deviceNumber = deviceNumber
        c.deviceFunction = self.FCN_DELIVERY_TUBE_SET_HEIGHT
        c.payload = bytearray(struct.pack(">f", height))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flushReceive()  
        
        if (qlabs.sendContainer(c)):
            c = qlabs.waitForContainer(self.ID_DELIVERY_TUBE, deviceNumber, self.FCN_DELIVERY_TUBE_SET_HEIGHT_ACK)
                    
            return True
        else:
            return False             