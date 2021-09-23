from library_qlabs import quanser_interactive_labs, comm_modular_container
from quanser.common import GenericError
import math

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class qlab_autoclave:

    # Define class-level variables   
    container_size = 0
    class_id = 0       # What device type is this?
    device_number = 0   # Increment if there are more than one of the same device ID
    device_function = 0 # Command/reponse
    payload = bytearray()
    
       
    ID_AUTOCLAVE = 140
    FCN_AUTOCLAVE_SET_DRAWER = 10
    FCN_AUTOCLAVE_SET_DRAWER_ACK = 11
    
    RED = 0
    GREEN = 1
    BLUE = 2
    
    
    # Initilize class
    def __init__(self):

       return
       
       
    def spawn(self, qlabs, device_num, location, rotation, configuration=0, wait_for_confirmation=True):
        return qlabs.spawn(device_num, self.ID_AUTOCLAVE, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1, 1, 1, configuration, wait_for_confirmation)
 
    def spawn_degrees(self, qlabs, device_num, location, rotation, configuration=0, wait_for_confirmation=True):
        rotation[0] = rotation[0]/180*math.pi
        rotation[1] = rotation[1]/180*math.pi
        rotation[2] = rotation[2]/180*math.pi
        
        return qlabs.spawn(device_num, self.ID_AUTOCLAVE, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1, 1, 1, configuration, wait_for_confirmation)
 
 
    def set_drawer(self, qlabs, device_num, open_drawer, wait_for_confirmation=True):
        c = comm_modular_container()
        c.class_id = self.ID_AUTOCLAVE
        c.device_number = device_num
        c.device_function = self.FCN_AUTOCLAVE_SET_DRAWER
        c.payload = bytearray(struct.pack(">B", open_drawer ))
        c.container_size = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if wait_for_confirmation:
            qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            if wait_for_confirmation:
                c = qlabs.wait_for_container(self.ID_AUTOCLAVE, device_num, self.FCN_AUTOCLAVE_SET_DRAWER_ACK)
                return c
                    
            return True
        else:
            return False    
