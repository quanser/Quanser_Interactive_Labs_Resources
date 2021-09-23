from library_qlabs import quanser_interactive_labs, comm_modular_container
from quanser.common import GenericError
import math

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class qlab_delivery_tube:

    # Define class-level variables   
    container_size = 0
    class_id = 0       # What device type is this?
    device_number = 0   # Increment if there are more than one of the same device ID
    device_function = 0 # Command/reponse
    payload = bytearray()
    
       
    ID_DELIVERY_TUBE = 80
    
    FCN_DELIVERY_TUBE_SPAWN_BLOCK = 10
    FCN_DELIVERY_TUBE_SPAWN_BLOCK_ACK = 11
    FCN_DELIVERY_TUBE_SET_HEIGHT = 12
    FCN_DELIVERY_TUBE_SET_HEIGHT_ACK = 13
    
    BLOCK_CUBE = 0
    BLOCK_CYLINDER = 1
    BLOCK_SPHERE = 2
    
    CONFIG_HOVER = 0
    CONFIG_NO_HOVER = 1
    
    # Initilize class
    def __init__(self):

       return
       
    def spawn(self, qlabs, device_num, location, rotation, configuration=0, wait_for_confirmation=True):
        return qlabs.spawn(device_num, self.ID_DELIVERY_TUBE, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1, 1, 1, configuration, wait_for_confirmation)
 
    def spawn_degrees(self, qlabs, device_num, location, rotation, configuration=0, wait_for_confirmation=True):
        rotation[0] = rotation[0]/180*math.pi
        rotation[1] = rotation[1]/180*math.pi
        rotation[2] = rotation[2]/180*math.pi    
    
        return qlabs.spawn(device_num, self.ID_DELIVERY_TUBE, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1, 1, 1, configuration, wait_for_confirmation)
  
    
    
    def spawn_block(self, qlabs, device_num, block_type, mass, yaw_rotation, color):
        c = comm_modular_container()
        c.class_id = self.ID_DELIVERY_TUBE
        c.device_number = device_num
        c.device_function = self.FCN_DELIVERY_TUBE_SPAWN_BLOCK
        c.payload = bytearray(struct.pack(">Ifffff", block_type, mass, yaw_rotation, color[0], color[1], color[2]))
        c.container_size = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            c = qlabs.wait_for_container(self.ID_DELIVERY_TUBE, device_num, self.FCN_DELIVERY_TUBE_SPAWN_BLOCK_ACK)
                    
            return True
        else:
            return False 
            
    def set_height(self, qlabs, device_num, height):
        c = comm_modular_container()
        c.class_id = self.ID_DELIVERY_TUBE
        c.device_number = device_num
        c.device_function = self.FCN_DELIVERY_TUBE_SET_HEIGHT
        c.payload = bytearray(struct.pack(">f", height))
        c.container_size = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            c = qlabs.wait_for_container(self.ID_DELIVERY_TUBE, device_num, self.FCN_DELIVERY_TUBE_SET_HEIGHT_ACK)
                    
            return True
        else:
            return False             