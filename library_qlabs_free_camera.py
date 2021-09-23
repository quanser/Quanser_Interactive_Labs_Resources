from library_qlabs import quanser_interactive_labs, comm_modular_container
from quanser.common import GenericError
import math

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class qlab_free_camera:

    # Define class-level variables   
    container_size = 0
    class_id = 0       # What device type is this?
    device_number = 0   # Increment if there are more than one of the same device ID
    device_function = 0 # Command/reponse
    payload = bytearray()
    
       
    ID_FREE_CAMERA = 170
    FCN_FREE_CAMERA_POSSESS = 10
    FCN_FREE_CAMERA_POSSESS_ACK = 11
    FCN_FREE_CAMERA_SET_CAMERA_FEATURES = 12
    FCN_FREE_CAMERA_SET_CAMERA_FEATURES_ACK = 13

    
    # Initilize class
    def __init__(self):

       return
       
    def spawn(self, qlabs, device_num, location, rotation):
        return qlabs.spawn(device_num, self.ID_FREE_CAMERA, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1, 1, 1, 0, True)
           
    def spawn_degrees(self, qlabs, device_num, location, rotation):
        rotation[0] = rotation[0]/180*math.pi
        rotation[1] = rotation[1]/180*math.pi
        rotation[2] = rotation[2]/180*math.pi
        
        return qlabs.spawn(device_num, self.ID_FREE_CAMERA, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1, 1, 1, 0, True)
    
    
    def possess(self, qlabs, device_num):
        c = comm_modular_container()
        c.class_id = self.ID_FREE_CAMERA
        c.device_number = device_num
        c.device_function = self.FCN_FREE_CAMERA_POSSESS
        c.payload = bytearray()
        c.container_size = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            c = qlabs.wait_for_container(self.ID_FREE_CAMERA, device_num, self.FCN_FREE_CAMERA_POSSESS_ACK)
                    
            return True
        else:
            return False   
        
        
