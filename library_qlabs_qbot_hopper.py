from library_qlabs import quanser_interactive_labs, comm_modular_container
from quanser.common import GenericError
import math

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class qlab_qbot_hopper:

    # Define class-level variables   
    container_size = 0
    class_id = 0       # What device type is this?
    device_number = 0   # Increment if there are more than one of the same device ID
    device_function = 0 # Command/reponse
    payload = bytearray()
    
       
    ID_QBOT_DUMPING_MECHANISM = 111
    
    FCN_QBOT_DUMPING_MECHANISM_COMMAND = 10
    FCN_QBOT_DUMPING_MECHANISM_COMMAND_ACK = 12
    
    
    VIEWPOINT_RGB = 0
    VIEWPOINT_DEPTH = 1
    VIEWPOINT_TRAILING = 2
    
    # Initilize class
    def __init__(self):

       return
       
    def spawn(self, qlabs, device_num, location, rotation, configuration=0, wait_for_confirmation=True):
        return qlabs.spawn(device_num, self.ID_QBOT_DUMPING_MECHANISM, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1.0, 1.0, 1.0, configuration, wait_for_confirmation)
        
    def spawnAndParentWithRelativeTransform(self, qlabs, deviceNumber, location, rotation, parentClass, parentDeviceNum, parentComponent, wait_for_confirmation=True):
        return qlabs.spawnAndParentWithRelativeTransform(deviceNumber, self.ID_QBOT_DUMPING_MECHANISM, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1.0, 1.0, 1.0, 0, parentClass, parentDeviceNum, parentComponent, wait_for_confirmation)
   
    def spawnDegrees(self, qlabs, device_num, location, rotation, configuration=0, wait_for_confirmation=True):
        rotation[0] = rotation[0]/180*math.pi
        rotation[1] = rotation[1]/180*math.pi
        rotation[2] = rotation[2]/180*math.pi    
    
        return qlabs.spawn(device_num, self.ID_QBOT_DUMPING_MECHANISM, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1.0, 1.0, 1.0, configuration, wait_for_confirmation)
   
            
    def command(self, qlabs, device_num, angle):
        c = comm_modular_container()
        c.class_id = self.ID_QBOT_DUMPING_MECHANISM
        c.device_number = device_num
        c.device_function = self.FCN_QBOT_DUMPING_MECHANISM_COMMAND
        c.payload = bytearray(struct.pack(">f", angle))
        c.container_size = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            c = qlabs.wait_for_container(self.ID_QBOT_DUMPING_MECHANISM, device_num, self.FCN_QBOT_DUMPING_MECHANISM_COMMAND_ACK)
                    
            return True
        else:
            return False
            
    def commandDegrees(self, qlabs, device_num, angle):
        self.command(qlabs, device_num, angle/180*math.pi)