from library_qlabs import QuanserInteractiveLabs, CommModularContainer
from quanser.common import GenericError
import math

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsBottleTableAttachment:

       
    ID_BOTTLE_TABLE_ATTACHMENT = 101
    
    # Initialize class
    def __init__(self):

       return
       
    def spawn(self, qlabs, deviceNumber, location, rotation, waitForConfirmation=True):
        return qlabs.spawn(deviceNumber, self.ID_BOTTLE_TABLE_ATTACHMENT, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1, 1, 1, 0, waitForConfirmation)
 
    def spawnDegrees(self, qlabs, deviceNumber, location, rotation, waitForConfirmation=True):
        rotation[0] = rotation[0]/180*math.pi
        rotation[1] = rotation[1]/180*math.pi
        rotation[2] = rotation[2]/180*math.pi    
    
        return qlabs.spawn(deviceNumber, self.ID_BOTTLE_TABLE_ATTACHMENT, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1, 1, 1, 0, waitForConfirmation)
        
    def spawnAndParentWithRelativeTransform(self, qlabs, deviceNumber, location, rotation, parentClass, parentDeviceNum, parentComponent, waitForConfirmation=True):
        return qlabs.spawnAndParentWithRelativeTransform(deviceNumber, self.ID_BOTTLE_TABLE_ATTACHMENT, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1, 1, 1, 0, parentClass, parentDeviceNum, parentComponent, waitForConfirmation)
           
 

class QLabsBottleTableSupport:

       
    ID_BOTTLE_TABLE_SUPPORT = 102
    
    # Initialize class
    def __init__(self):

       return
       
    def spawn(self, qlabs, deviceNumber, location, rotation, waitForConfirmation=True):
        return qlabs.spawn(deviceNumber, self.ID_BOTTLE_TABLE_SUPPORT, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1, 1, 1, 0, waitForConfirmation)
 
    def spawnDegrees(self, qlabs, deviceNumber, location, rotation, waitForConfirmation=True):
        rotation[0] = rotation[0]/180*math.pi
        rotation[1] = rotation[1]/180*math.pi
        rotation[2] = rotation[2]/180*math.pi    
    
        return qlabs.spawn(deviceNumber, self.ID_BOTTLE_TABLE_SUPPORT, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1, 1, 1, 0, waitForConfirmation)
 
    def spawnAndParentWithRelativeTransform(self, qlabs, deviceNumber, location, rotation, parentClass, parentDeviceNum, parentComponent, waitForConfirmation=True):
        return qlabs.spawnAndParentWithRelativeTransform(deviceNumber, self.ID_BOTTLE_TABLE_SUPPORT, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1, 1, 1, 0, parentClass, parentDeviceNum, parentComponent, waitForConfirmation)
    
