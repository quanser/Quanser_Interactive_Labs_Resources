from library_qlabs import quanser_interactive_labs, comm_modular_container
from quanser.common import GenericError
import math

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class qlab_qbot:

    # Define class-level variables   
    container_size = 0
    class_id = 0       # What device type is this?
    device_number = 0   # Increment if there are more than one of the same device ID
    device_function = 0 # Command/reponse
    payload = bytearray()
    
       
    ID_QBOT = 20
    
    FCN_QBOT_COMMAND_AND_REQUEST_STATE = 10
    FCN_QBOT_COMMAND_AND_REQUEST_STATE_RESPONSE = 11
    FCN_QBOT_POSSESS = 20
    FCN_QBOT_POSSESS_ACK = 21
    
    
    VIEWPOINT_RGB = 0
    VIEWPOINT_DEPTH = 1
    VIEWPOINT_TRAILING = 2
    
    # Initilize class
    def __init__(self):

       return
       
    def spawn(self, qlabs, device_num, location, rotation, configuration=0, wait_for_confirmation=True):
        return qlabs.spawn(device_num, self.ID_QBOT, location[0], location[1], location[2]+0.1, rotation[0], rotation[1], rotation[2], 1.0, 1.0, 1.0, configuration, wait_for_confirmation)
   
    def spawn_degrees(self, qlabs, device_num, location, rotation, configuration=0, wait_for_confirmation=True):
        rotation[0] = rotation[0]/180*math.pi
        rotation[1] = rotation[1]/180*math.pi
        rotation[2] = rotation[2]/180*math.pi    
    
        return qlabs.spawn(device_num, self.ID_QBOT, location[0], location[1], location[2]+0.1, rotation[0], rotation[1], rotation[2], 1.0, 1.0, 1.0, configuration, wait_for_confirmation)
   
   
    def possess(self, qlabs, device_num, camera):
        c = comm_modular_container()
        c.class_id = self.ID_QBOT
        c.device_number = device_num
        c.device_function = self.FCN_QBOT_POSSESS
        c.payload = bytearray(struct.pack(">B", camera))
        c.container_size = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            c = qlabs.wait_for_container(self.ID_QBOT, device_num, self.FCN_QBOT_POSSESS_ACK)
                    
            return True
        else:
            return False
            
    def start_RT_model(self, device_num=0, QLabsHostname='localhost'):
        cmd_string="quarc_run -D -r -t tcpip://{}:17000 QBot2e_Spawn.rt-win64 -hostname localhost -devicenum {}".format(QLabsHostname, device_num)
        os.system(cmd_string)
        return cmd_string
        
    def terminate_RT_model(self, QLabsHostname):
        cmd_string="quarc_run -q -t tcpip://{}:17000 QBot2e_Spawn.rt-win64".format(QArm_hostname)
        os.system(cmd_string)
        return cmd_string