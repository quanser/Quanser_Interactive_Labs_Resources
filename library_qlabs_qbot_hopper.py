from library_qlabs import QuanserInteractiveLabs, CommModularContainer
from quanser.common import GenericError
import math

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsQBotHopper:

       
    ID_QBOT_DUMPING_MECHANISM = 111
    
    FCN_QBOT_DUMPING_MECHANISM_COMMAND = 10
    FCN_QBOT_DUMPING_MECHANISM_COMMAND_ACK = 12
    
    
    VIEWPOINT_RGB = 0
    VIEWPOINT_DEPTH = 1
    VIEWPOINT_TRAILING = 2
    
    # Initialize class
    def __init__(self):

       return
       
    def spawn(self, qlabs, deviceNumber, location, rotation, configuration=0, waitForConfirmation=True):
        return qlabs.spawn(deviceNumber, self.ID_QBOT_DUMPING_MECHANISM, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1.0, 1.0, 1.0, configuration, waitForConfirmation)
        
    def spawnAndParentWithRelativeTransform(self, qlabs, deviceNumber, location, rotation, parentClass, parentDeviceNumber, parentComponent, waitForConfirmation=True):
        return qlabs.spawnAndParentWithRelativeTransform(deviceNumber, self.ID_QBOT_DUMPING_MECHANISM, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1.0, 1.0, 1.0, 0, parentClass, parentDeviceNumber, parentComponent, waitForConfirmation)
   
    def spawnDegrees(self, qlabs, deviceNumber, location, rotation, configuration=0, waitForConfirmation=True):
    
        return qlabs.spawn(deviceNumber, self.ID_QBOT_DUMPING_MECHANISM, location[0], location[1], location[2], rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi, 1.0, 1.0, 1.0, configuration, waitForConfirmation)
   
            
    def command(self, qlabs, deviceNumber, angle):
        c = CommModularContainer()
        c.classID = self.ID_QBOT_DUMPING_MECHANISM
        c.deviceNumber = deviceNumber
        c.deviceFunction = self.FCN_QBOT_DUMPING_MECHANISM_COMMAND
        c.payload = bytearray(struct.pack(">f", angle))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flushReceive()  
        
        if (qlabs.sendContainer(c)):
            c = qlabs.waitForContainer(self.ID_QBOT_DUMPING_MECHANISM, deviceNumber, self.FCN_QBOT_DUMPING_MECHANISM_COMMAND_ACK)
                    
            return True
        else:
            return False
            
    def commandDegrees(self, qlabs, deviceNumber, angle):
        self.command(qlabs, deviceNumber, angle/180*math.pi)