from library_qlabs_common import QLabsCommon
from library_qlabs import CommModularContainer

import math
import struct
import cv2
import numpy as np
        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsFreeCamera:
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
   
    def __init__(self):
       """ Constructor Method """
       return

    def spawn(self, qlabs, location, rotation):
        
        """Spawns a camera in an instance of QLabs at a specific location and rotation using radians using a specified actor number.

        :param qlabs: A QuanserInteractiveLabs object
        :param location: An array of floats for x, y and z coordinates
        :param rotation: An array of floats for the roll, pitch, and yaw
        :type qlabs: object
        :type location: float array[3]
        :type rotation: float array[3]
        :return: Success value of 0 if successful, 1 class not available, 2 actor number not available or already in use, 3 unknown error, -1 communications error. Actor number ID to use for addressing the actor.
        :rtype: int32, int32
        """
        return QLabsCommon().spawn(qlabs, self.ID_FREE_CAMERA, location, rotation, [1, 1, 1], 0, True)

       
    def spawn_id(self, qlabs, actorNumber, location, rotation):
        
        """Spawns a camera in an instance of QLabs at a specific location and rotation using radians using a specified actor number.

        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param location: An array of floats for x, y and z coordinates
        :param rotation: An array of floats for the roll, pitch, and yaw
        :type qlabs: object
        :type actorNumber: uint32
        :type location: float array[3]
        :type rotation: float array[3]
        :return: 0 if successful, 1 class not available, 2 actor number not available or already in use, 3 unknown error, -1 communications error
        :rtype: int32
        """
        return QLabsCommon().spawn_id(qlabs, actorNumber, self.ID_FREE_CAMERA, location, rotation, [1, 1, 1], 0, True)
           
    def spawn_id_degrees(self, qlabs, actorNumber, location, rotation):
        """
        Spawns a camera in an instance of QLabs at a specific location and rotation using degrees using a specified actor number.

        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param location: An array of floats for x, y and z coordinates
        :param rotation: An array of floats for the roll, pitch, and yaw
        :type qlabs: object
        :type actorNumber: uint32
        :type location: float array[3]
        :type rotation: float array[3]
        :return: 0 if successful, 1 class not available, 2 actor number not available or already in use, 3 unknown error, -1 communications error
        :rtype: int32
        """
        
        return QLabsCommon().spawn_id(qlabs, actorNumber, self.ID_FREE_CAMERA,  location, [rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi], [1, 1, 1], 0, True)
    
    def spawn_id_and_parent_with_relative_transform(self, qlabs, actorNumber, location, rotation, parentClassID, parentActorNumber, parentComponent):
        """
        Spawns a camera in an instance of QLabs at a specific location and rotation relative to the parent actor using radians.

        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param location: An array of floats for x, y and z coordinates
        :param rotation: An array of floats for the roll, pitch, yaw
        :param parentClassID: Parent class ID (Can be found in the class library)
        :param parentActorNumber: The unique actorNumber identifier for the parent class in QLabs
        :param ParentComponent: `0` for the origin of the parent actor, see the parent class for additional reference frame options
        :type qlabs: object
        :type actorNumber: uint32
        :type location: float array[3]
        :type rotation: float array[3]
        :type parentClassID: uint32
        :type parentActorNumber: uint32
        :type ParentComponent: uint32
        :return: 0 if successful, 1 class not available, 2 actor number not available or already in use, 3 cannot find the parent actor, 4 unknown error, -1 communications error
        :rtype: int32
        """
        return QLabsCommon().spawn_id_and_parent_with_relative_transform(qlabs, actorNumber, self.ID_FREE_CAMERA,  location, rotation, [1, 1, 1], 0, parentClassID, parentActorNumber, parentComponent, True)
   
    def spawn_id_and_parent_with_relative_transform_degrees(self, qlabs, actorNumber, location, rotation, parentClassID, parentActorNumber, parentComponent):
        """
        Spawns a camera in an instance of QLabs at a specific location and rotation relative to the parent actor using degrees.
        
        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param location: An array of floats for x, y and z coordinates
        :param rotation: An array of floats for the roll, pitch, yaw
        :param parentClassID: Parent class ID (Can be found in the class library)
        :param parentActorNumber: The unique actorNumber identifier for the parent class in QLabs
        :param ParentComponent: `0` for the origin of the parent actor, see the parent class for additional reference frame options
        :type qlabs: object
        :type actorNumber: uint32
        :type location: float array[3]
        :type rotation: float array[3]
        :type parentClassID: uint32
        :type parentActorNumber: uint32
        :type ParentComponent: uint32
        :return: 0 if successful, 1 class not available, 2 actor number not available or already in use, 3 cannot find the parent actor, 4 unknown error, -1 communications error
        :rtype: int32

        """
        return QLabsCommon().spawn_id_and_parent_with_relative_transform(qlabs, actorNumber, self.ID_FREE_CAMERA,location, [rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi], [1, 1, 1], 0, parentClassID, parentActorNumber, parentComponent, True)
   
    
    def possess(self, qlabs, actorNumber):
        """
        Possess (take control of) a camera in QLabs.
        
        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :type qlabs: object
        :type actorNumber: uint32
        :return: `True` if possessing the camera was successful, `False` otherwise
        :rtype: boolean

        """
        c = CommModularContainer()
        c.classID = self.ID_FREE_CAMERA
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_FREE_CAMERA_POSSESS
        c.payload = bytearray()
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            c = qlabs.wait_for_container(self.ID_FREE_CAMERA, actorNumber, self.FCN_FREE_CAMERA_POSSESS_ACK)
            if (c == None):
                return False
            else:                     
                return True
        else:
            return False  

    def set_camera_properties(self, qlabs, actorNumber, fieldOfView, depthOfField, aperature, focusDistance):
        """
        Sets the camera properties.
        
        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param fieldOfView: The field of view that the camera can see (range:5-150)
        :param depthOfField: The depth of field that the camera can see
        :param aperture: The amount of light allowed into the camera sensor (range:2.0-22.0)
        :param focusDistance: The focus distance that the camera can see (range:0.1-50.0)
        :type qlabs: object
        :type actorNumber: uint32
        :type fieldOfView:
        :type depthOfField:
        :type aperture:
        :type focusDistance:
        :return: `True` if setting the camera properties was successful, `False` otherwise
        :rtype: boolean

        """
        c = CommModularContainer()
        c.classID = self.ID_FREE_CAMERA
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_FREE_CAMERA_SET_CAMERA_PROPERTIES
        c.payload = bytearray(struct.pack(">fBff", fieldOfView, depthOfField, aperature, focusDistance))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            c = qlabs.wait_for_container(self.ID_FREE_CAMERA, actorNumber, self.FCN_FREE_CAMERA_SET_CAMERA_PROPERTIES_ACK)
            if (c == None):
                return False
            else:                     
                return True
        else:
            return False
        
    def set_transform(self, qlabs, actorNumber, location, rotation):
        """
        Change the location and rotation of a spawned camera in radians
        
        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param location: An array of floats for x, y and z coordinates
        :param rotation: An array of floats for the roll, pitch, yaw in radians
        :type qlabs: object
        :type actorNumber: uint32
        :type location: array[3]
        :type rotation: array[3]
        :return: `True` if spawn was successful, `False` otherwise
        :rtype: boolean

        """
        c = CommModularContainer()
        c.classID = self.ID_FREE_CAMERA
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_FREE_CAMERA_SET_TRANSFORM
        c.payload = bytearray(struct.pack(">ffffff", location[0], location[1], location[2], rotation[0], rotation[1], rotation[2]))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)

        qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            c = qlabs.wait_for_container(self.ID_FREE_CAMERA, actorNumber, self.FCN_FREE_CAMERA_SET_TRANSFORM_ACK)
            if (c == None):
                return False
            else:                     
                return True
        else:
            return False     

    def set_transform_degrees(self, qlabs, actorNumber, location, rotation):
        """
        Change the location and rotation of a spawned camera in degrees
        
        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param location: An array of floats for x, y and z coordinates
        :param rotation: An array of floats for the roll, pitch, yaw in degrees
        :type qlabs: object
        :type actorNumber: uint32
        :type location: array[3]
        :type rotation: array[3]
        :return: `True` if spawn was successful, `False` otherwise
        :rtype: boolean

        """
        c = CommModularContainer()
        c.classID = self.ID_FREE_CAMERA
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_FREE_CAMERA_SET_TRANSFORM
        c.payload = bytearray(struct.pack(">ffffff", location[0], location[1], location[2], rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            c = qlabs.wait_for_container(self.ID_FREE_CAMERA, actorNumber, self.FCN_FREE_CAMERA_SET_TRANSFORM_ACK)
            if (c == None):
                return False
            else:                     
                return True
        else:
            return False 

    def destroy(self, qlabs, actorNumber):
        """Destroys a camera in an instance of QLabs.

        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :return: The number of actors destroyed. -1 if failed.
        :rtype: int32

        """
        return QLabsCommon().destroy_spawned_actor(qlabs, self.ID_FREE_CAMERA, actorNumber)


    def ping(self, qlabs, actorNumber):
        """Checks if a camera of the corresponding actor number exists in the QLabs environment.

        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :return: `True` if actor is present, `False` otherwise
        :rtype: boolean

        """
        return QLabsCommon().ping_actor(qlabs, actorNumber, self.ID_FREE_CAMERA)

    def get_world_transform(self, qlabs, actorNumber):
        """Get the location, rotation, and scale in world coordinates of the camera
        
        :param qlabs: A QuanserInteractiveLabs object.
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :return: success, location, rotation, scale
        :rtype: boolean, float array[3], float array[3], float array[3]
        """    
        return QLabsCommon().get_world_transform(qlabs, actorNumber, self.ID_FREE_CAMERA)

    def set_image_capture_resolution(self, qlabs, actorNumber, width=640, height=480):
        """Change the default width and height of image resolution for capture
        
        :param qlabs: A QuanserInteractiveLabs object.
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param width: Must be an even number. Default 640
        :param height: Must be an even number. Default 480
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :type width: uint32
        :type height: uint32
        :return: `True` if spawn was successful, `False` otherwise
        :rtype: boolean
        """   

        c = CommModularContainer()
        c.classID = self.ID_FREE_CAMERA
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_FREE_CAMERA_SET_IMAGE_RESOLUTION
        c.payload = bytearray(struct.pack(">II", width, height))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            c = qlabs.wait_for_container(self.ID_FREE_CAMERA, actorNumber, self.FCN_FREE_CAMERA_SET_IMAGE_RESOLUTION_RESPONSE)
            if (c == None):
                return False
            else:                     
                return True
        else:
            return False

        

    def get_image(self, qlabs, actorNumber):
        """Request an image from the camera actor. Note, set_image_capture_resolution must be set once per camera otherwise this method will fail.
        
        :param qlabs: A QuanserInteractiveLabs object.
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :return: Success, RGB image data
        :rtype: boolean, byte array[variable]
        """   
        c = CommModularContainer()
        c.classID = self.ID_FREE_CAMERA
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_FREE_CAMERA_REQUEST_IMAGE
        c.payload = bytearray()
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            c = qlabs.wait_for_container(self.ID_FREE_CAMERA, actorNumber, self.FCN_FREE_CAMERA_RESPONSE_IMAGE)
            if (c == None):
                return False, None

            data_size, = struct.unpack(">I", c.payload[0:4])

            jpg_buffer = cv2.imdecode(np.frombuffer(bytearray(c.payload[4:len(c.payload)]), dtype=np.uint8, count=-1, offset=0), 1)
            
            
            return True, jpg_buffer
        else:
            return False, None
