from library_qlabs import quanser_interactive_labs, comm_modular_container
from quanser.common import GenericError
import math

import struct
import cv2
import numpy as np
        
        
######################### MODULAR CONTAINER CLASS #########################

class qlab_qcar:

    # Define class-level variables   
    container_size = 0
    class_id = 0       # What device type is this?
    device_number = 0   # Increment if there are more than one of the same device ID
    device_function = 0 # Command/reponse
    payload = bytearray()
    
    _jpg_buffer = bytearray()
    
       
    ID_QCAR = 160
    FCN_QCAR_SET_VELOCITY_AND_REQUEST_STATE = 10
    FCN_QCAR_VELOCITY_STATE_RESPONSE = 11
    FCN_QCAR_SET_TRANSFORM_AND_REQUEST_STATE = 12
    FCN_QCAR_TRANSFORM_STATE_RESPONSE = 13
    FCN_QCAR_POSSESS = 20
    FCN_QCAR_POSSESS_ACK = 21
    FCN_QCAR_CAMERA_DATA_REQUEST = 100
    FCN_QCAR_CAMERA_DATA_RESPONSE = 101
    
    CAMERA_CSI_RIGHT = 0
    CAMERA_CSI_BACK = 1
    CAMERA_CSI_LEFT = 2
    CAMERA_CSI_FRONT = 3
    CAMERA_RGB = 4
    CAMERA_DEPTH = 5
    CAMERA_OVERHEAD = 6
    CAMERA_TRAILING = 7
    
    # Initilize class
    def __init__(self):

       return
       
    def spawn(self, qlabs, device_num, location, rotation, configuration=0, wait_for_confirmation=True):
        return qlabs.spawn(device_num, self.ID_QCAR, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1.0, 1.0, 1.0, configuration, wait_for_confirmation)
    
    def spawn_degrees(self, qlabs, device_num, location, rotation, configuration=0, wait_for_confirmation=True):
        rotation[0] = rotation[0]/180*math.pi
        rotation[1] = rotation[1]/180*math.pi
        rotation[2] = rotation[2]/180*math.pi
        
        return qlabs.spawn(device_num, self.ID_QCAR, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1.0, 1.0, 1.0, configuration, wait_for_confirmation)
    
    
    def set_transform_and_request_state(self, qlabs, device_num, x, y, z, roll, pitch, yaw, enable_dynamics, headlights, left_turn, right_turn, brake, honk, wait_for_confirmation=True):
        c = comm_modular_container()
        c.class_id = self.ID_QCAR
        c.device_number = device_num
        c.device_function = self.FCN_QCAR_SET_TRANSFORM_AND_REQUEST_STATE
        c.payload = bytearray(struct.pack(">ffffffBBBBBB", x, y, z, roll, pitch, yaw, enable_dynamics, headlights, left_turn, right_turn, brake, honk))
        c.container_size = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if wait_for_confirmation:
            qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            if wait_for_confirmation:
                c = qlabs.wait_for_container(self.ID_QCAR, device_num, self.FCN_QCAR_TRANSFORM_STATE_RESPONSE)
                return c
                    
            return True
        else:
            return False    
            
    def set_velocity_and_request_state(self, qlabs, device_num, forward, turn, headlights, left_turn, right_turn, brake, honk, wait_for_confirmation=True):
        c = comm_modular_container()
        c.class_id = self.ID_QCAR
        c.device_number = device_num
        c.device_function = self.FCN_QCAR_SET_VELOCITY_AND_REQUEST_STATE
        c.payload = bytearray(struct.pack(">ffBBBBB", forward, turn, headlights, left_turn, right_turn, brake, honk))
        c.container_size = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if wait_for_confirmation:
            qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            if wait_for_confirmation:
                c = qlabs.wait_for_container(self.ID_QCAR, device_num, self.FCN_QCAR_VELOCITY_STATE_RESPONSE)
                return c
                    
            return True
        else:
            return False             
            
    def possess(self, qlabs, device_num, camera):
        c = comm_modular_container()
        c.class_id = self.ID_QCAR
        c.device_number = device_num
        c.device_function = self.FCN_QCAR_POSSESS
        c.payload = bytearray(struct.pack(">B", camera))
        c.container_size = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            c = qlabs.wait_for_container(self.ID_QCAR, device_num, self.FCN_QCAR_POSSESS_ACK)
                    
            return True
        else:
            return False              

    def get_camera_data(self, qlabs, device_num, camera):   
    
        c = comm_modular_container()
        c.class_id = self.ID_QCAR
        c.device_number = device_num
        c.device_function = self.FCN_QCAR_CAMERA_DATA_REQUEST
        c.payload = bytearray(struct.pack(">I", camera))
        c.container_size = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            c = qlabs.wait_for_container(self.ID_QCAR, device_num, self.FCN_QCAR_CAMERA_DATA_RESPONSE)
            self._jpg_buffer = cv2.imdecode(np.frombuffer(bytearray(c.payload[8:len(c.payload)]), dtype=np.uint8, count=-1, offset=0), 1)
            
            
            return True, self._jpg_buffer
        else:
            return False, self._jpg_buffer
            

