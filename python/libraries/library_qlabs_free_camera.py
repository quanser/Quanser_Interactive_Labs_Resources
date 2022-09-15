from library_qlabs import CommModularContainer
from library_qlabs_actor import QLabsActor

import math
import struct
import cv2
import numpy as np
        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsFreeCamera(QLabsActor):
    """ This class supports the spawning and control of free movement cameras in QLabs open worlds."""

    ID_FREE_CAMERA = 170 
    """Class ID"""
    FCN_FREE_CAMERA_POSSESS = 10
    FCN_FREE_CAMERA_POSSESS_ACK = 11
    FCN_FREE_CAMERA_SET_CAMERA_PROPERTIES = 12
    FCN_FREE_CAMERA_SET_CAMERA_PROPERTIES_ACK = 13
    FCN_FREE_CAMERA_SET_TRANSFORM = 14
    FCN_FREE_CAMERA_SET_TRANSFORM_ACK = 15
    FCN_FREE_CAMERA_SET_IMAGE_RESOLUTION = 90
    FCN_FREE_CAMERA_SET_IMAGE_RESOLUTION_RESPONSE = 91
    FCN_FREE_CAMERA_REQUEST_IMAGE = 100
    FCN_FREE_CAMERA_RESPONSE_IMAGE = 101

    """ The current actor number of this class to be addressed. This can be modified at any time. """

   
    def __init__(self, qlabs, verbose=False):
       """ Constructor Method

       :param qlabs: A QuanserInteractiveLabs object
       :param verbose: (Optional) Print error information to the console.
       :type qlabs: object
       :type verbose: boolean
       """

       self._qlabs = qlabs
       self._verbose = verbose
       self._classID = self.ID_FREE_CAMERA
       return

    def spawn(self, location, rotation):
        
        """Spawns a camera in an instance of QLabs at a specific location and rotation using radians.

        :param location: An array of floats for x, y and z coordinates
        :param rotation: An array of floats for the roll, pitch, and yaw
        :type location: float array[3]
        :type rotation: float array[3]
        :return: Success value of 0 if successful, 1 class not available, 2 actor number not available or already in use, 3 unknown error, -1 communications error. Actor number ID to use for addressing the actor.
        :rtype: int32, int32
        """

        [status, actorNumber] = self._spawn(location, rotation, [1, 1, 1], 0, True)
        if (status == 0):
            self.actorNumber = actorNumber
        else:
            if (self._verbose):
                if (status == 1):
                    print('Class not available.')
                elif (status == 2):
                    print('Actor number already in use.')
                elif (status == -1):
                    print('Communication error.')
                else:
                    print('Unknown error')


            
        return status, actorNumber

    def spawn_degrees(self, location, rotation):
        """
        Spawns a camera in an instance of QLabs at a specific location and rotation using degrees.

        :param location: An array of floats for x, y and z coordinates
        :param rotation: An array of floats for the roll, pitch, and yaw
        :type location: float array[3]
        :type rotation: float array[3]
        :return: Success value of 0 if successful, 1 class not available, 2 actor number not available or already in use, 3 unknown error, -1 communications error. Actor number ID to use for addressing the actor.
        :rtype: int32, int32
        """
        
        return self.spawn(location, [rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi])

       
    def spawn_id(self, actorNumber, location, rotation):
        
        """Spawns a camera in an instance of QLabs at a specific location and rotation using radians using a specified actor number.

        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param location: An array of floats for x, y and z coordinates
        :param rotation: An array of floats for the roll, pitch, and yaw
        :type actorNumber: uint32
        :type location: float array[3]
        :type rotation: float array[3]
        :return: 0 if successful, 1 class not available, 2 actor number not available or already in use, 3 unknown error, -1 communications error
        :rtype: int32
        """
        status = self._spawn_id(actorNumber, location, rotation, [1, 1, 1], 0, True)
        
        if (status == 0):
            self.actorNumber = actorNumber
        else:
            if (self._verbose):
                if (status == 1):
                    print('Class not available.')
                elif (status == 2):
                    print('Actor number already in use.')
                elif (status == -1):
                    print('Communication error.')
                else:
                    print('Unknown error')

        return status
           
    def spawn_id_degrees(self, actorNumber, location, rotation):
        """
        Spawns a camera in an instance of QLabs at a specific location and rotation using degrees using a specified actor number.

        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param location: An array of floats for x, y and z coordinates
        :param rotation: An array of floats for the roll, pitch, and yaw
        :type actorNumber: uint32
        :type location: float array[3]
        :type rotation: float array[3]
        :return: 0 if successful, 1 class not available, 2 actor number not available or already in use, 3 unknown error, -1 communications error
        :rtype: int32
        """
        
        return self.spawn_id(actorNumber, location, [rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi])
    
    def spawn_id_and_parent_with_relative_transform(self, actorNumber, location, rotation, parentClassID, parentActorNumber, parentComponent):
        """
        Spawns a camera in an instance of QLabs at a specific location and rotation relative to the parent actor using radians.

        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param location: An array of floats for x, y and z coordinates
        :param rotation: An array of floats for the roll, pitch, yaw
        :param parentClassID: Parent class ID (Can be found in the class library)
        :param parentActorNumber: The unique actorNumber identifier for the parent class in QLabs
        :param ParentComponent: `0` for the origin of the parent actor, see the parent class for additional reference frame options
        :type actorNumber: uint32
        :type location: float array[3]
        :type rotation: float array[3]
        :type parentClassID: uint32
        :type parentActorNumber: uint32
        :type ParentComponent: uint32
        :return: 0 if successful, 1 class not available, 2 actor number not available or already in use, 3 cannot find the parent actor, 4 unknown error, -1 communications error
        :rtype: int32
        """
        status = self._spawn_id_and_parent_with_relative_transform(actorNumber, location, rotation, [1, 1, 1], 0, parentClassID, parentActorNumber, parentComponent, True)

        if (status == 0):
            self.actorNumber = actorNumber
        else:
            if (self._verbose):
                if (status == 1):
                    print('Class not available.')
                elif (status == 2):
                    print('Actor number already in use.')
                elif (status == 3):
                    print('Cannot find parent actor.')
                elif (status == -1):
                    print('Communication error.')
                else:
                    print('Unknown error')

        return status
   
    def spawn_id_and_parent_with_relative_transform_degrees(self, actorNumber, location, rotation, parentClassID, parentActorNumber, parentComponent):
        """
        Spawns a camera in an instance of QLabs at a specific location and rotation relative to the parent actor using degrees.
        
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param location: An array of floats for x, y and z coordinates
        :param rotation: An array of floats for the roll, pitch, yaw
        :param parentClassID: Parent class ID (Can be found in the class library)
        :param parentActorNumber: The unique actorNumber identifier for the parent class in QLabs
        :param ParentComponent: `0` for the origin of the parent actor, see the parent class for additional reference frame options
        :type actorNumber: uint32
        :type location: float array[3]
        :type rotation: float array[3]
        :type parentClassID: uint32
        :type parentActorNumber: uint32
        :type ParentComponent: uint32
        :return: 0 if successful, 1 class not available, 2 actor number not available or already in use, 3 cannot find the parent actor, 4 unknown error, -1 communications error
        :rtype: int32

        """
        return self.spawn_id_and_parent_with_relative_transform(actorNumber, location, [rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi], parentClassID, parentActorNumber, parentComponent)
   
    
    def possess(self):
        """
        Possess (take control of) a camera in QLabs.
        
        :return: `True` if possessing the camera was successful, `False` otherwise
        :rtype: boolean

        """
        if (not self._is_actor_number_valid()):
            return False

        c = CommModularContainer()
        c.classID = self.ID_FREE_CAMERA
        c.actorNumber = self.actorNumber
        c.actorFunction = self.FCN_FREE_CAMERA_POSSESS
        c.payload = bytearray()
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        self._qlabs.flush_receive()  
        
        if (self._qlabs.send_container(c)):
            c = self._qlabs.wait_for_container(self.ID_FREE_CAMERA, self.actorNumber, self.FCN_FREE_CAMERA_POSSESS_ACK)
            if (c == None):
                return False
            else:                     
                return True
        else:
            return False  

    def set_camera_properties(self, fieldOfView, depthOfField, aperature, focusDistance):
        """
        Sets the camera properties.
        
        :param fieldOfView: The field of view that the camera can see (range:5-150)
        :param depthOfField: The depth of field that the camera can see
        :param aperture: The amount of light allowed into the camera sensor (range:2.0-22.0)
        :param focusDistance: The focus distance that the camera can see (range:0.1-50.0)
        :type fieldOfView:
        :type depthOfField:
        :type aperture:
        :type focusDistance:
        :return: `True` if setting the camera properties was successful, `False` otherwise
        :rtype: boolean

        """
        if (not self._is_actor_number_valid()):
            return False

        c = CommModularContainer()
        c.classID = self.ID_FREE_CAMERA
        c.actorNumber = self.actorNumber
        c.actorFunction = self.FCN_FREE_CAMERA_SET_CAMERA_PROPERTIES
        c.payload = bytearray(struct.pack(">fBff", fieldOfView, depthOfField, aperature, focusDistance))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        self._qlabs.flush_receive()  
        
        if (self._qlabs.send_container(c)):
            c = self._qlabs.wait_for_container(self.ID_FREE_CAMERA, self.actorNumber, self.FCN_FREE_CAMERA_SET_CAMERA_PROPERTIES_ACK)
            if (c == None):
                return False
            else:                     
                return True
        else:
            return False
        
    def set_transform(self, location, rotation):
        """
        Change the location and rotation of a spawned camera in radians
        
        :param location: An array of floats for x, y and z coordinates
        :param rotation: An array of floats for the roll, pitch, yaw in radians
        :type location: array[3]
        :type rotation: array[3]
        :return: `True` if spawn was successful, `False` otherwise
        :rtype: boolean

        """
        if (not self._is_actor_number_valid()):
            return False

        c = CommModularContainer()
        c.classID = self.ID_FREE_CAMERA
        c.actorNumber = self.actorNumber
        c.actorFunction = self.FCN_FREE_CAMERA_SET_TRANSFORM
        c.payload = bytearray(struct.pack(">ffffff", location[0], location[1], location[2], rotation[0], rotation[1], rotation[2]))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)

        self._qlabs.flush_receive()  
        
        if (self._qlabs.send_container(c)):
            c = self._qlabs.wait_for_container(self.ID_FREE_CAMERA, self.actorNumber, self.FCN_FREE_CAMERA_SET_TRANSFORM_ACK)
            if (c == None):
                return False
            else:                     
                return True
        else:
            return False     

    def set_transform_degrees(self, location, rotation):
        """
        Change the location and rotation of a spawned camera in degrees
        
        :param location: An array of floats for x, y and z coordinates
        :param rotation: An array of floats for the roll, pitch, yaw in degrees
        :type location: array[3]
        :type rotation: array[3]
        :return: `True` if spawn was successful, `False` otherwise
        :rtype: boolean

        """
        return self.set_transform(location, [rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi]) 


    def set_image_capture_resolution(self, width=640, height=480):
        """Change the default width and height of image resolution for capture
        
        :param width: Must be an even number. Default 640
        :param height: Must be an even number. Default 480
        :type width: uint32
        :type height: uint32
        :return: `True` if spawn was successful, `False` otherwise
        :rtype: boolean
        """   
        if (not self._is_actor_number_valid()):
            return False

        c = CommModularContainer()
        c.classID = self.ID_FREE_CAMERA
        c.actorNumber = self.actorNumber
        c.actorFunction = self.FCN_FREE_CAMERA_SET_IMAGE_RESOLUTION
        c.payload = bytearray(struct.pack(">II", width, height))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        self._qlabs.flush_receive()  
        
        if (self._qlabs.send_container(c)):
            c = self._qlabs.wait_for_container(self.ID_FREE_CAMERA, self.actorNumber, self.FCN_FREE_CAMERA_SET_IMAGE_RESOLUTION_RESPONSE)
            if (c == None):
                return False
            else:                     
                return True
        else:
            return False

        

    def get_image(self):
        """Request an image from the camera actor. Note, set_image_capture_resolution must be set once per camera otherwise this method will fail.
        
        :return: Success, RGB image data
        :rtype: boolean, byte array[variable]
        """   

        if (not self._is_actor_number_valid()):
            return False, None

        c = CommModularContainer()
        c.classID = self.ID_FREE_CAMERA
        c.actorNumber = self.actorNumber
        c.actorFunction = self.FCN_FREE_CAMERA_REQUEST_IMAGE
        c.payload = bytearray()
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        self._qlabs.flush_receive()  
        
        if (self._qlabs.send_container(c)):
            c = self._qlabs.wait_for_container(self.ID_FREE_CAMERA, self.actorNumber, self.FCN_FREE_CAMERA_RESPONSE_IMAGE)
            if (c == None):
                return False, None

            data_size, = struct.unpack(">I", c.payload[0:4])

            jpg_buffer = cv2.imdecode(np.frombuffer(bytearray(c.payload[4:len(c.payload)]), dtype=np.uint8, count=-1, offset=0), 1)
            
            
            return True, jpg_buffer
        else:
            return False, None
