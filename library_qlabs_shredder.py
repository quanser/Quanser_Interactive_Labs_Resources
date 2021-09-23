from library_qlabs import quanser_interactive_labs, comm_modular_container
from quanser.common import GenericError
import math

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class qlab_shredder:

    # Define class-level variables   
    container_size = 0
    class_id = 0       # What device type is this?
    device_number = 0   # Increment if there are more than one of the same device ID
    device_function = 0 # Command/reponse
    payload = bytearray()
    
       
    ID_SHREDDER = 190
    
    RED = 0
    GREEN = 1
    BLUE = 2
    WHITE = 3
    
    # Initilize class
    def __init__(self):

       return
       
       
    def spawn(self, qlabs, device_num, location, rotation, configuration=0, wait_for_confirmation=True):
        return qlabs.spawn(device_num, self.ID_SHREDDER, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1, 1, 1, configuration, wait_for_confirmation)
 
    def spawn_degrees(self, qlabs, device_num, location, rotation, configuration=0, wait_for_confirmation=True):
        rotation[0] = rotation[0]/180*math.pi
        rotation[1] = rotation[1]/180*math.pi
        rotation[2] = rotation[2]/180*math.pi    
    
        return qlabs.spawn(device_num, self.ID_SHREDDER, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1, 1, 1, configuration, wait_for_confirmation)
 