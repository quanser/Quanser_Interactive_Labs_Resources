from library_qlabs import CommModularContainer
from quanser.common import GenericError
import math
import os
import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class qlab_qbot:

    # Define class-level variables   
    containerSize = 0
    classID = 0       # What device type is this?
    actorNumber = 0   # Increment if there are more than one of the same device ID
    actorFunction = 0 # Command/reponse
    payload = bytearray()
    
       
    ID_QBOT = 20
    
    FCN_QBOT_COMMAND_AND_REQUEST_STATE = 10
    FCN_QBOT_COMMAND_AND_REQUEST_STATE_RESPONSE = 11
    FCN_QBOT_POSSESS = 20
    FCN_QBOT_POSSESS_ACK = 21
    
    
    VIEWPOINT_RGB = 0
    VIEWPOINT_DEPTH = 1
    VIEWPOINT_TRAILING = 2
    
    # Initilize class
    def __init__(self):

       return
       
    def spawn(self, qlabs, actorNumber, location, rotation, configuration=0, waitForConfirmation=True):
        return qlabs.spawn(actorNumber, self.ID_QBOT, location[0], location[1], location[2]+0.1, rotation[0], rotation[1], rotation[2], 1.0, 1.0, 1.0, configuration, waitForConfirmation)
   
    def spawn_degrees(self, qlabs, actorNumber, location, rotation, configuration=0, waitForConfirmation=True):
    
        return qlabs.spawn(actorNumber, self.ID_QBOT, location[0], location[1], location[2]+0.1, rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi, 1.0, 1.0, 1.0, configuration, waitForConfirmation)
   
   
    def possess(self, qlabs, actorNumber, camera):
        c = CommModularContainer()
        c.classID = self.ID_QBOT
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_QBOT_POSSESS
        c.payload = bytearray(struct.pack(">B", camera))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            c = qlabs.wait_for_container(self.ID_QBOT, actorNumber, self.FCN_QBOT_POSSESS_ACK)
                    
            return True
        else:
            return False
            
    def start_RT_model(self, actorNumber=0, QLabsHostname='localhost'):
        cmdString="quarc_run -D -r -t tcpip://{}:17000 QBot2e_Spawn.rt-win64 -hostname localhost -devicenum {}".format(QLabsHostname, actorNumber)
        os.system(cmdString)
        return cmdString
        
    def terminate_RT_model(self, QLabsHostname):
        cmdString="quarc_run -q -t tcpip://{}:17000 QBot2e_Spawn.rt-win64".format(QLabsHostname)
        os.system(cmdString)
        return cmdString