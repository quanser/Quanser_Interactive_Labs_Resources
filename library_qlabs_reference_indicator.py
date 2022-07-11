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
       
       
    def spawn(self, qlabs, actorNumber, location, rotation, scale, configuration=0, waitForConfirmation=True):
        return qlabs.spawn(actorNumber, self.ID_REF_IND, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2], configuration, waitForConfirmation)
 
    def spawn_degrees(self, qlabs, actorNumber, location, rotation, scale, configuration=0, waitForConfirmation=True):
        
        return qlabs.spawn(actorNumber, self.ID_REF_IND, location[0], location[1], location[2], rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi, scale[0], scale[1], scale[2], configuration, waitForConfirmation)
 
 
 
    def set_transform_and_color(self, qlabs, actorNumber, x, y, z, roll, pitch, yaw, sx, sy, sz, r, g, b, waitForConfirmation=True):
        c = CommModularContainer()
        c.classID = self.ID_REF_IND
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_REF_IND_SET_TRANSFORM_AND_COLOR
        c.payload = bytearray(struct.pack(">ffffffffffff", x, y, z, roll, pitch, yaw, sx, sy, sz, r, g, b ))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if waitForConfirmation:
            qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            if waitForConfirmation:
                c = qlabs.wait_for_container(self.FCN_REF_IND_SET_TRANSFORM_AND_COLOR, actorNumber, self.FCN_REF_IND_SET_TRANSFORM_AND_COLOR_ACK)
                return c
                    
            return True
        else:
            return False    
