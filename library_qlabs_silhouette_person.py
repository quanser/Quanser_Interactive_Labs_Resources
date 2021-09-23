from library_qlabs import quanser_interactive_labs, comm_modular_container
from quanser.common import GenericError
import math

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class qlab_silhouette_person:

    # Define class-level variables   
    container_size = 0
    class_id = 0       # What device type is this?
    device_number = 0   # Increment if there are more than one of the same device ID
    device_function = 0 # Command/reponse
    payload = bytearray()
    
       
    ID_SILHOUETTE_PERSON = 10030
    FCN_SILHOUETTE_PERSON_MOVE_TO = 10
    FCN_SILHOUETTE_PERSON_MOVE_TO_ACK = 11
    
    # Initilize class
    def __init__(self):

       return
       
    def spawn(self, qlabs, device_num, location, rotation, scale, configuration=0, wait_for_confirmation=True):
        # To put the spawn point at the feet, offset z by 1m
        return qlabs.spawn(device_num, self.ID_SILHOUETTE_PERSON, location[0], location[1], location[2]+1.0, rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2], configuration, wait_for_confirmation)

    def spawn_degrees(self, qlabs, device_num, location, rotation, scale, configuration=0, wait_for_confirmation=True):
        rotation[0] = rotation[0]/180*math.pi
        rotation[1] = rotation[1]/180*math.pi
        rotation[2] = rotation[2]/180*math.pi    
    
        # To put the spawn point at the feet, offset z by 1m
        return qlabs.spawn(device_num, self.ID_SILHOUETTE_PERSON, location[0], location[1], location[2]+1.0, rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2], configuration, wait_for_confirmation)
    

        
    def move_to(self, qlabs, device_num, location, speed, wait_for_confirmation=True):
        c = comm_modular_container()
        c.class_id = self.ID_SILHOUETTE_PERSON
        c.device_number = device_num
        c.device_function = self.FCN_SILHOUETTE_PERSON_MOVE_TO
        c.payload = bytearray(struct.pack(">ffff", location[0], location[1], location[2], speed))
        c.container_size = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if wait_for_confirmation:
            qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            if wait_for_confirmation:
                c = qlabs.wait_for_container(self.ID_SILHOUETTE_PERSON, device_num, self.FCN_SILHOUETTE_PERSON_MOVE_TO_ACK)
                    
            return True
        else:
            return False    

