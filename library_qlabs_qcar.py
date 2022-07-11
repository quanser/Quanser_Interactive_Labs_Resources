from library_qlabs import QuanserInteractiveLabs, CommModularContainer
from quanser.common import GenericError
import math

import struct
import cv2
import numpy as np
        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsQCar:

    
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
    
    # Initialize class
    def __init__(self):

       return
       
    def spawn(self, qlabs, actorNumber, location, rotation, configuration=0, waitForConfirmation=True):
        return qlabs.spawn(actorNumber, self.ID_QCAR, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1.0, 1.0, 1.0, configuration, waitForConfirmation)
    
    def spawn_degrees(self, qlabs, actorNumber, location, rotation, configuration=0, waitForConfirmation=True):
        
        return qlabs.spawn(actorNumber, self.ID_QCAR, location[0], location[1], location[2], rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi, 1.0, 1.0, 1.0, configuration, waitForConfirmation)
    
    
    def set_transform_and_request_state(self, qlabs, actorNumber, x, y, z, roll, pitch, yaw, enableDynamics, headlights, leftTurnSignal, rightTurnSignal, brake, honk, waitForConfirmation=True):
        c = CommModularContainer()
        c.classID = self.ID_QCAR
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_QCAR_SET_TRANSFORM_AND_REQUEST_STATE
        c.payload = bytearray(struct.pack(">ffffffBBBBBB", x, y, z, roll, pitch, yaw, enableDynamics, headlights, leftTurnSignal, rightTurnSignal, brake, honk))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if waitForConfirmation:
            qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            if waitForConfirmation:
                c = qlabs.wait_for_container(self.ID_QCAR, actorNumber, self.FCN_QCAR_TRANSFORM_STATE_RESPONSE)
                return c
                    
            return True
        else:
            return False    
            
    def set_velocity_and_request_state(self, qlabs, actorNumber, forward, turn, headlights, leftTurnSignal, rightTurnSignal, brake, honk, waitForConfirmation=True):
        c = CommModularContainer()
        c.classID = self.ID_QCAR
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_QCAR_SET_VELOCITY_AND_REQUEST_STATE
        c.payload = bytearray(struct.pack(">ffBBBBB", forward, turn, headlights, leftTurnSignal, rightTurnSignal, brake, honk))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if waitForConfirmation:
            qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            if waitForConfirmation:
                c = qlabs.wait_for_container(self.ID_QCAR, actorNumber, self.FCN_QCAR_VELOCITY_STATE_RESPONSE)
                return c
                    
            return True
        else:
            return False             
            
    def possess(self, qlabs, actorNumber, camera):
        c = CommModularContainer()
        c.classID = self.ID_QCAR
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_QCAR_POSSESS
        c.payload = bytearray(struct.pack(">B", camera))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            c = qlabs.wait_for_container(self.ID_QCAR, actorNumber, self.FCN_QCAR_POSSESS_ACK)
                    
            return True
        else:
            return False              

    def get_camera_data(self, qlabs, actorNumber, camera):   
    
        c = CommModularContainer()
        c.classID = self.ID_QCAR
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_QCAR_CAMERA_DATA_REQUEST
        c.payload = bytearray(struct.pack(">I", camera))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            c = qlabs.wait_for_container(self.ID_QCAR, actorNumber, self.FCN_QCAR_CAMERA_DATA_RESPONSE)
            self._jpg_buffer = cv2.imdecode(np.frombuffer(bytearray(c.payload[8:len(c.payload)]), dtype=np.uint8, count=-1, offset=0), 1)
            
            
            return True, self._jpg_buffer
        else:
            return False, self._jpg_buffer
            

