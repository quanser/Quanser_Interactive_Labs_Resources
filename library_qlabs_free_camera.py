from library_qlabs import QuanserInteractiveLabs, CommModularContainer
from quanser.common import GenericError
import math

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsFreeCamera:
    """ This class documents the QLabs Free Camera."""

    ID_FREE_CAMERA = 170 
    """ """
    FCN_FREE_CAMERA_POSSESS = 10
    """ """
    FCN_FREE_CAMERA_POSSESS_ACK = 11
    """ """
    FCN_FREE_CAMERA_SET_CAMERA_PROPERTIES = 12
    """ """
    FCN_FREE_CAMERA_SET_CAMERA_PROPERTIES_ACK = 13
    """ """
    FCN_FREE_CAMERA_SET_TRANSFORM = 14
    """ """
    FCN_FREE_CAMERA_SET_TRANSFORM_ACK = 15
    """ """

    
    # Initialize class
    def __init__(self):
       """ Constructor Method """
       return
       
    def spawn(self, qlabs, actorNumber, location, rotation):
        
        """Spawns a camera in an instance of QLabs at a specific location and rotation using radians.

        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param location: An array of floats for x, y and z coordinates
        :param rotation: An array of floats for the roll, pitch, yaw
        :type qlabs: object
        :type actorNumber: uint32
        :type location: array[3]
        :type rotation: array[3]
        :return: `True` if spawn was successful, `False` otherwise
        :rtype: boolean

        .. caution::

            No two actor numbers can be the same for the same class!

        """
        return qlabs.spawn(actorNumber, self.ID_FREE_CAMERA, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1, 1, 1, 0, True)
           
    def spawn_degrees(self, qlabs, actorNumber, location, rotation):
        """
        Spawns a camera in an instance of QLabs at a specific location and rotation using degrees.

        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param location: An array of floats for x, y and z coordinates
        :param rotation: An array of floats for the roll, pitch, yaw
        :type qlabs: object
        :type actorNumber: uint32
        :type location: array[3]
        :type rotation: array[3]
        :return: `True` if spawn was successful, `False` otherwise
        :rtype: boolean
        """
        
        return qlabs.spawn(actorNumber, self.ID_FREE_CAMERA, location[0], location[1], location[2], rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi, 1, 1, 1, 0, True)
    
    def spawn_and_parent_with_relative_transform(self, qlabs, actorNumber, location, rotation, parentClassID, parentActorNumber, parentComponent, waitForConfirmation=True):
        """
        Spawns a camera in an instance of QLabs at a specific location and rotation relative to the parent actor using radians.

        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param location: An array of floats for x, y and z coordinates
        :param rotation: An array of floats for the roll, pitch, yaw
        :param parentClassID: Parent class ID (Can be found in the class library)
        :param parentActorNumber: The unique actorNumber identifier for the parent class in QLabs
        :param ParentComponent: `0` for the origin of the parent actor, see the parent class for additional reference frame options
        :param waitForConfirmation: Wait for acknowledgement from QLabs to proceed, this is a blocking operation
            defaults to True
        :type qlabs: object
        :type actorNumber: uint32
        :type location: array[3]
        :type rotation: array[3]
        :type parentClassID: uint32
        :type parentActorNumber: uint32
        :type ParentComponent: uint32
        :return: `True` if spawn was successful (or if waitForConfirmation set to `False`), `False` otherwise
        :rtype: boolean
        """
        return qlabs.spawn_and_parent_with_relative_transform(actorNumber, self.ID_FREE_CAMERA, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1, 1, 1, 0, parentClassID, parentActorNumber, parentComponent, waitForConfirmation)
   
    def spawn_and_parent_with_relative_transform_degrees(self, qlabs, actorNumber, location, rotation, parentClassID, parentActorNumber, parentComponent, waitForConfirmation=True):
        """
        Spawns a camera in an instance of QLabs at a specific location and rotation relative to the parent actor using degrees.
        
        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param location: An array of floats for x, y and z coordinates
        :param rotation: An array of floats for the roll, pitch, yaw
        :param parentClassID: Parent class ID (Can be found in the class library)
        :param parentActorNumber: The unique actorNumber identifier for the parent class in QLabs
        :param ParentComponent: `0` for the origin of the parent actor, see the parent class for additional reference frame options
        :param waitForConfirmation: Wait for acknowledgement from QLabs to proceed, this is a blocking operation
            defaults to True
        :type qlabs: object
        :type actorNumber: uint32
        :type location: array[3]
        :type rotation: array[3]
        :type parentClassID: uint32
        :type parentActorNumber: uint32
        :type ParentComponent: uint32
        :return: `True` if spawn was successful (or if waitForConfirmation set to `False`), `False` otherwise
        :rtype: boolean

        """
        return qlabs.spawn_and_parent_with_relative_transform(actorNumber, self.ID_FREE_CAMERA, location[0], location[1], location[2], rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi, 1, 1, 1, 0, parentClassID, parentActorNumber, parentComponent, waitForConfirmation)
   
    
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
                    
            return True
        else:
            return False  

    def set_camera_properties(self, qlabs, actorNumber, fieldOfView, depthOfField, aperature, focusDistance):
        """
        Sets the camera properties.
        
        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param fieldOfView: The field of view that the camera can see (range:5-150)
        :param depthOfField: The depth of feild that the camera can see
        :param aperature: The amount of light allowed into the camera sensor (range:2.0-22.0)
        :param focusDistance: The focus distance that the camera can see (range:0.1-50.0)
        :type qlabs: object
        :type actorNumber: uint32
        :type fieldOfView:
        :type depthOfField:
        :type aperature:
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
                    
            return True
        else:
            return False
        
    def set_transform(self, qlabs, actorNumber, location, rotation):
        """
        Change the location and rotation of a spawned camera.
        
        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param location: An array of floats for x, y and z coordinates
        :param rotation: An array of floats for the roll, pitch, yaw
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
                    
            return True
        else:
            return False     
