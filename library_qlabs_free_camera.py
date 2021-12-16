from library_qlabs import QuanserInteractiveLabs, CommModularContainer
from quanser.common import GenericError
import math

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsFreeCamera: 
       
    ID_FREE_CAMERA = 170
    FCN_FREE_CAMERA_POSSESS = 10
    FCN_FREE_CAMERA_POSSESS_ACK = 11
    FCN_FREE_CAMERA_SET_CAMERA_PROPERTIES = 12
    FCN_FREE_CAMERA_SET_CAMERA_PROPERTIES_ACK = 13
    FCN_FREE_CAMERA_SET_TRANSFORM = 14
    FCN_FREE_CAMERA_SET_TRANSFORM_ACK = 15

    
    # Initialize class
    def __init__(self):

       return
       
    def spawn(self, qlabs, deviceNumber, location, rotation):
        return qlabs.spawn(deviceNumber, self.ID_FREE_CAMERA, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1, 1, 1, 0, True)
           
    def spawnDegrees(self, qlabs, deviceNumber, location, rotation):
        
        return qlabs.spawn(deviceNumber, self.ID_FREE_CAMERA, location[0], location[1], location[2], rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi, 1, 1, 1, 0, True)
    
    def spawnAndParentWithRelativeTransform(self, qlabs, deviceNumber, location, rotation, parentClass, parentDeviceNumber, parentComponent, waitForConfirmation=True):
        return qlabs.spawnAndParentWithRelativeTransform(deviceNumber, self.ID_FREE_CAMERA, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1, 1, 1, 0, parentClass, parentDeviceNumber, parentComponent, waitForConfirmation)
   
    def spawnAndParentWithRelativeTransformDegrees(self, qlabs, deviceNumber, location, rotation, parentClass, parentDeviceNumber, parentComponent, waitForConfirmation=True):
        
        return qlabs.spawnAndParentWithRelativeTransform(deviceNumber, self.ID_FREE_CAMERA, location[0], location[1], location[2], rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi, 1, 1, 1, 0, parentClass, parentDeviceNumber, parentComponent, waitForConfirmation)
   
    
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

    def setCameraProperties(self, qlabs, deviceNumber, fieldOfView, depthOfField, aperature, focusDistance):
        c = CommModularContainer()
        c.classID = self.ID_FREE_CAMERA
        c.deviceNumber = deviceNumber
        c.deviceFunction = self.FCN_FREE_CAMERA_SET_CAMERA_PROPERTIES
        c.payload = bytearray(struct.pack(">fBff", fieldOfView, depthOfField, aperature, focusDistance))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flushReceive()  
        
        if (qlabs.sendContainer(c)):
            c = qlabs.waitForContainer(self.ID_FREE_CAMERA, deviceNumber, self.FCN_FREE_CAMERA_SET_CAMERA_PROPERTIES_ACK)
                    
            return True
        else:
            return False
        
    def setTransform(self, qlabs, deviceNumber, location, rotation):
        c = CommModularContainer()
        c.classID = self.ID_FREE_CAMERA
        c.deviceNumber = deviceNumber
        c.deviceFunction = self.FCN_FREE_CAMERA_SET_TRANSFORM
        c.payload = bytearray(struct.pack(">ffffff", location[0], location[1], location[2], rotation[0], rotation[1], rotation[2]))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flushReceive()  
        
        if (qlabs.sendContainer(c)):
            c = qlabs.waitForContainer(self.ID_FREE_CAMERA, deviceNumber, self.FCN_FREE_CAMERA_SET_TRANSFORM_ACK)
                    
            return True
        else:
            return False     
