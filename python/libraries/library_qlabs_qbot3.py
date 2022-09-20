from library_qlabs import CommModularContainer
from library_qlabs_actor import QLabsActor

import cv2
import numpy as np
import math
import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsQBot3(QLabsActor):

       
    ID_QBOT3 = 22
    
    FCN_QBOT3_COMMAND_AND_REQUEST_STATE = 10
    FCN_QBOT3_COMMAND_AND_REQUEST_STATE_RESPONSE = 11
    FCN_QBOT3_POSSESS = 20
    FCN_QBOT3_POSSESS_ACK = 21
    FCN_QBOT3_RGB_REQUEST = 100
    FCN_QBOT3_RGB_RESPONSE = 101
    FCN_QBOT3_DEPTH_REQUEST = 110
    FCN_QBOT3_DEPTH_RESPONSE = 111
    
    
    VIEWPOINT_RGB = 0
    VIEWPOINT_DEPTH = 1
    VIEWPOINT_TRAILING = 2
    
    def __init__(self, qlabs, verbose=False):
       """ Constructor Method

       :param qlabs: A QuanserInteractiveLabs object
       :param verbose: (Optional) Print error information to the console.
       :type qlabs: object
       :type verbose: boolean
       """

       self._qlabs = qlabs
       self._verbose = verbose
       self.classID = self.ID_QBOT3
       return
     
   
    def possess(self, camera):
        c = CommModularContainer()
        c.classID = self.ID_QBOT3
        c.actorNumber = self.actorNumber
        c.actorFunction = self.FCN_QBOT3_POSSESS
        c.payload = bytearray(struct.pack(">B", camera))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        self._qlabs.flush_receive()  
        
        if (self._qlabs.send_container(c)):
            c = self._qlabs.wait_for_container(self.ID_QBOT3, self.actorNumber, self.FCN_QBOT3_POSSESS_ACK)
                    
            return True
        else:
            return False
            
    def command_and_request_state(self, rightWheelSpeed, leftWheelSpeed):
        c = CommModularContainer()
        c.classID = self.ID_QBOT3
        c.actorNumber = self.actorNumber
        c.actorFunction = self.FCN_QBOT3_COMMAND_AND_REQUEST_STATE
        c.payload = bytearray(struct.pack(">ff", rightWheelSpeed, leftWheelSpeed))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        self._qlabs.flush_receive()  
        
        if (self._qlabs.send_container(c)):
            c = self._qlabs.wait_for_container(self.ID_QBOT3, self.actorNumber, self.FCN_QBOT3_COMMAND_AND_REQUEST_STATE_RESPONSE)
                    
            return True
        else:
            return False
            

    def get_image_rgb(self):   
        """
        Request a JPG image from the QBot camera.

        :return: 
            - **status** - `True` and image data if successful, `False` and empty otherwise
            - **imageData** - Image in a JPG format
        :rtype: boolean, byte array with jpg data

        """   
        
        if (not self._is_actor_number_valid()):
            return False, None
    
        c = CommModularContainer()
        c.classID = self.ID_QBOT3
        c.actorNumber = self.actorNumber
        c.actorFunction = self.FCN_QBOT3_RGB_REQUEST
        c.payload = bytearray()
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        self._qlabs.flush_receive()  
        
        if (self._qlabs.send_container(c)):
            c = self._qlabs.wait_for_container(self.ID_QBOT3, self.actorNumber, self.FCN_QBOT3_RGB_RESPONSE)

            if (c == None):
                return False, None

            
            jpg_buffer = cv2.imdecode(np.frombuffer(bytearray(c.payload[4:len(c.payload)]), dtype=np.uint8, count=-1, offset=0), 1)
            
            
            return True, jpg_buffer
        else:
            return False, None

    def get_image_depth(self):   
        """
        Request a JPG image from the QBot camera.

        :return: 
            - **status** - `True` and image data if successful, `False` and empty otherwise
            - **imageData** - Image in a JPG format
        :rtype: boolean, byte array with jpg data

        """   
        
        if (not self._is_actor_number_valid()):
            return False, None
    
        c = CommModularContainer()
        c.classID = self.ID_QBOT3
        c.actorNumber = self.actorNumber
        c.actorFunction = self.FCN_QBOT3_DEPTH_REQUEST
        c.payload = bytearray()
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        self._qlabs.flush_receive()  
        
        if (self._qlabs.send_container(c)):
            c = self._qlabs.wait_for_container(self.ID_QBOT3, self.actorNumber, self.FCN_QBOT3_DEPTH_RESPONSE)

            if (c == None):
                return False, None


            jpg_buffer = cv2.imdecode(np.frombuffer(bytearray(c.payload[4:len(c.payload)]), dtype=np.uint8, count=-1, offset=0), 1)
            
            
            return True, jpg_buffer
        else:
            return False, None