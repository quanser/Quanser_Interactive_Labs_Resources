from library_qlabs import QuanserInteractiveLabs, CommModularContainer
from quanser.common import GenericError
import math
import os

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsSRV02:

       
    ID_SRV02 = 40
    
    FCN_SRV02_COMMAND_AND_REQUEST_STATE = 10
    FCN_SRV02_COMMAND_AND_REQUEST_STATE_RESPONSE = 11

    
    # Initialize class
    def __init__(self):

       return
       
    def spawn(self, qlabs, deviceNum, location, rotation, configuration=0, waitForConfirmation=True):
        return qlabs.spawn(deviceNum, self.ID_SRV02, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1.0, 1.0, 1.0, configuration, waitForConfirmation)
   
    def spawnDegrees(self, qlabs, deviceNum, location, rotation, configuration=0, waitForConfirmation=True):
    
        return qlabs.spawn(deviceNum, self.ID_SRV02, location[0], location[1], location[2], rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi, 1.0, 1.0, 1.0, configuration, waitForConfirmation)
   
            
    def commandAndRequestState(self, qlabs, deviceNum, angle, waitForConfirmation=True):
        c = CommModularContainer()
        c.classID = self.ID_SRV02
        c.deviceNumber = deviceNum
        c.deviceFunction = self.FCN_SRV02_COMMAND_AND_REQUEST_STATE
        c.payload = bytearray(struct.pack(">ff", angle, 0))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
               
        qlabs.flushReceive()  
        
        if (qlabs.sendContainer(c)):
            if (waitForConfirmation):
                c = qlabs.waitForContainer(self.ID_SRV02, deviceNum, self.FCN_SRV02_COMMAND_AND_REQUEST_STATE_RESPONSE)
                    
            return True
        else:
            return False
            
    def commandAndRequestStateDegrees(self, qlabs, deviceNum, angle, waitForConfirmation=True):
    
        return self.commandAndRequestState(qlabs, deviceNum, angle/180*math.pi, waitForConfirmation)
    
    def startRTModel(self, device_num=0, QLabs_hostname='localhost'):
        cmd_string="quarc_run -D -r -t tcpip://localhost:17000 Turntable_Spawn.rt-linux_pi_3 -uri tcpip://localhost:17004 -hostname {} -devicenum {}".format(QLabs_hostname, device_num)
        os.system(cmd_string)
        return cmd_string
        
    def terminateRTModel(self):
        cmd_string="quarc_run -q -Q -t tcpip://localhost:17000 Turntable_Spawn.rt-linux_pi_3"
        os.system(cmd_string)
        return cmd_string    