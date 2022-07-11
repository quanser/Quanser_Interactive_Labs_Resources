from library_qlabs import QuanserInteractiveLabs, CommModularContainer
from quanser.common import GenericError
import math

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsTrafficLightSingle:

       
    ID_TRAFFIC_LIGHT_SINGLE = 10051
    
    FCN_TRAFFIC_LIGHT_SINGLE_SET_STATE = 10
    FCN_TRAFFIC_LIGHT_SINGLE_SET_STATE_ACK = 11
    
    STATE_RED = 0
    STATE_GREEN = 1
    STATE_YELLOW = 2
    
    # Initialize class
    def __init__(self):

       return
       
    def spawn(self, qlabs, actorNumber, location, rotation, scale, waitForConfirmation=True):
        return qlabs.spawn(actorNumber, self.ID_TRAFFIC_LIGHT_SINGLE, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2], 0, waitForConfirmation)
 
    def spawn_degrees(self, qlabs, actorNumber, location, rotation, scale, waitForConfirmation=True):
        
        return qlabs.spawn(actorNumber, self.ID_TRAFFIC_LIGHT_SINGLE, location[0], location[1], location[2], rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi, scale[0], scale[1], scale[2], 0, waitForConfirmation)
 
    def set_state(self, qlabs, actorNumber, state, waitForConfirmation=True):
        c = CommModularContainer()
        c.classID = self.ID_TRAFFIC_LIGHT_SINGLE
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_TRAFFIC_LIGHT_SINGLE_SET_STATE
        c.payload = bytearray(struct.pack(">B", state))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if waitForConfirmation:
            qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            if waitForConfirmation:
                c = qlabs.wait_for_container(self.ID_TRAFFIC_LIGHT_SINGLE, actorNumber, self.FCN_TRAFFIC_LIGHT_SINGLE_SET_STATE_ACK)
                    
            return True
        else:
            return False        