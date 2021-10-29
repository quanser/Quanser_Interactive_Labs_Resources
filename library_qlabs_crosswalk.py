from library_qlabs import QuanserInteractiveLabs, CommModularContainer
from quanser.common import GenericError
import math

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsCrosswalk:

       
    ID_CROSSWALK = 10010
    
    # Initialize class
    def __init__(self):

       return
       
       
    def spawn(self, qlabs, deviceNumber, location, rotation, scale, configuration=0, waitForConfirmation=True):
        return qlabs.spawn(deviceNumber, self.ID_CROSSWALK,location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2], configuration, waitForConfirmation)
 
    def spawnDegrees(self, qlabs, deviceNumber, location, rotation, scale, configuration=0, waitForConfirmation=True):
        rotation[0] = rotation[0]/180*math.pi
        rotation[1] = rotation[1]/180*math.pi
        rotation[2] = rotation[2]/180*math.pi
    
        return qlabs.spawn(deviceNumber, self.ID_CROSSWALK,location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2], configuration, waitForConfirmation)
 
