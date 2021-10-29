from library_qlabs import quanser_interactive_labs, comm_modular_container
from quanser.common import GenericError
import math

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class qlab_srv02:

    # Define class-level variables   
    container_size = 0
    class_id = 0       # What device type is this?
    device_number = 0   # Increment if there are more than one of the same device ID
    device_function = 0 # Command/reponse
    payload = bytearray()
    
       
    ID_SRV02 = 40
    
    FCN_SRV02_COMMAND_AND_REQUEST_STATE = 10
    FCN_SRV02_COMMAND_AND_REQUEST_STATE_RESPONSE = 11

    
    # Initilize class
    def __init__(self):

       return
       
    def spawn(self, qlabs, deviceNum, location, rotation, configuration=0, wait_for_confirmation=True):
        return qlabs.spawn(deviceNum, self.ID_SRV02, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1.0, 1.0, 1.0, configuration, wait_for_confirmation)
   
    def spawnDegrees(self, qlabs, deviceNum, location, rotation, configuration=0, wait_for_confirmation=True):
        rotation[0] = rotation[0]/180*math.pi
        rotation[1] = rotation[1]/180*math.pi
        rotation[2] = rotation[2]/180*math.pi    
    
        return qlabs.spawn(deviceNum, self.ID_SRV02, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1.0, 1.0, 1.0, configuration, wait_for_confirmation)
   
            
    def commandAndRequestState(self, qlabs, deviceNum, angle):
        c = comm_modular_container()
        c.class_id = self.ID_SRV02
        c.device_number = deviceNum
        c.device_function = self.FCN_SRV02_COMMAND_AND_REQUEST_STATE
        c.payload = bytearray(struct.pack(">ff", angle, 0))
        c.container_size = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            c = qlabs.wait_for_container(self.ID_SRV02, deviceNum, self.FCN_SRV02_COMMAND_AND_REQUEST_STATE_RESPONSE)
                    
            return True
        else:
            return False
            
    def commandAndRequestStateDegrees(self, qlabs, deviceNum, angle):
    
        return self.commandAndRequestState(qlabs, deviceNum, angle/180*math.pi)
    