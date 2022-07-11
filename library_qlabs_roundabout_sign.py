from library_qlabs import QuanserInteractiveLabs, CommModularContainer
from quanser.common import GenericError
import math

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsRoundaboutSign:

       
    ID_ROUNDABOUT_SIGN = 10060
    
    # Initialize class
    def __init__(self):

       return
       
    def spawn(self, qlabs, actorNumber, location, rotation, scale, waitForConfirmation=True):
        return qlabs.spawn(actorNumber, self.ID_ROUNDABOUT_SIGN, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2], 0, waitForConfirmation)
 
    def spawn_degrees(self, qlabs, actorNumber, location, rotation, scale, waitForConfirmation=True):
    
        return qlabs.spawn(actorNumber, self.ID_ROUNDABOUT_SIGN, location[0], location[1], location[2], rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi, scale[0], scale[1], scale[2], 0, waitForConfirmation)
 
