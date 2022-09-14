from library_qlabs import QuanserInteractiveLabs, CommModularContainer
from quanser.common import GenericError
import math

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsTrafficLight:

       
    ID_TRAFFIC_LIGHT = 10051
    """Class ID"""
    
    FCN_TRAFFIC_LIGHT_SET_STATE = 10
    FCN_TRAFFIC_LIGHT_SET_STATE_ACK = 11
    
    STATE_RED = 0
    """State constant for red light"""
    STATE_GREEN = 1
    """State constant for green light"""
    STATE_YELLOW = 2
    """State constant for yellow light"""
    
    # Initialize class
    def __init__(self):
        """ Constructor Method """
        return

    def spawn(self, qlabs, actorNumber, location, rotation, scale, waitForConfirmation=True):
        """Spawns a stoplight in an instance of QLabs at a specific location and rotation using radians with a specified actor number.

        :param qlabs: A QuanserInteractiveLabs object.
        :param actorNumber: User defined unique identifier for the class actor in QLabs.
        :param location: An array of floats for x, y and z coordinates.
        :param rotation: An array of floats for the roll, pitch, and yaw in radians.
        :param scale: An array of floats for the scale in the x, y, and z directions.
        :param waitForConfirmation: (Optional) Wait for confirmation of the spawn before proceeding. This makes the method a blocking operation.
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :type location: float array[3]
        :type rotation: float array[3]
        :type scale: float array[3]
        :type waitForConfirmation: boolean
        :return: Success value of 0 if successful, 1 class not available, 2 actor number not available or already in use, 3 unknown error, -1 communications error. Actor number ID to use for addressing the actor.
        :rtype: int32, int32

        .. danger::

            TODO: Update traffic light artwork
            TODO: Add configuration options for different orientations
            TODO: Add helper functions for multi-light setups

        """
        return qlabs.spawn(actorNumber, self.ID_TRAFFIC_LIGHT_SINGLE, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2], 0, waitForConfirmation)
 
    def spawn_degrees(self, qlabs, actorNumber, location, rotation, scale, waitForConfirmation=True):
        """Spawns a stoplight in an instance of QLabs at a specific location and rotation using degrees with a specified actor number.

        :param qlabs: A QuanserInteractiveLabs object.
        :param actorNumber: User defined unique identifier for the class actor in QLabs.
        :param location: An array of floats for x, y and z coordinates.
        :param rotation: An array of floats for the roll, pitch, and yaw in degrees.
        :param scale: An array of floats for the scale in the x, y, and z directions.
        :param waitForConfirmation: (Optional) Wait for confirmation of the spawn before proceeding. This makes the method a blocking operation.
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :type location: float array[3]
        :type rotation: float array[3]
        :type scale: float array[3]
        :type waitForConfirmation: boolean
        :return: Success value of 0 if successful, 1 class not available, 2 actor number not available or already in use, 3 unknown error, -1 communications error. Actor number ID to use for addressing the actor.
        :rtype: int32, int32

        .. danger::

            TODO: Update traffic light artwork
            TODO: Add configuration options for different orientations
            TODO: Add helper functions for multi-light setups

        """        
        return qlabs.spawn(actorNumber, self.ID_TRAFFIC_LIGHT_SINGLE, location[0], location[1], location[2], rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi, scale[0], scale[1], scale[2], 0, waitForConfirmation)
 
       
    def spawn_id(self, qlabs, actorNumber, location, rotation, scale, waitForConfirmation=True):
        """Spawns a stoplight in an instance of QLabs at a specific location and rotation using radians with a specified actor number.

        :param qlabs: A QuanserInteractiveLabs object.
        :param actorNumber: User defined unique identifier for the class actor in QLabs.
        :param location: An array of floats for x, y and z coordinates.
        :param rotation: An array of floats for the roll, pitch, and yaw in radians.
        :param scale: An array of floats for the scale in the x, y, and z directions.
        :param waitForConfirmation: (Optional) Wait for confirmation of the spawn before proceeding. This makes the method a blocking operation.
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :type location: float array[3]
        :type rotation: float array[3]
        :type scale: float array[3]
        :type waitForConfirmation: boolean
        :return: `True` if spawn was successful, `False` otherwise
        :rtype: boolean

        .. danger::

            TODO: Update traffic light artwork
            TODO: Add configuration options for different orientations
            TODO: Add helper functions for multi-light setups

        """
        return qlabs.spawn_id(actorNumber, self.ID_TRAFFIC_LIGHT_SINGLE, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2], 0, waitForConfirmation)
 
    def spawn_id_degrees(self, qlabs, actorNumber, location, rotation, scale, waitForConfirmation=True):
        """Spawns a stoplight in an instance of QLabs at a specific location and rotation using degrees with a specified actor number.

        :param qlabs: A QuanserInteractiveLabs object.
        :param actorNumber: User defined unique identifier for the class actor in QLabs.
        :param location: An array of floats for x, y and z coordinates.
        :param rotation: An array of floats for the roll, pitch, and yaw in degrees.
        :param scale: An array of floats for the scale in the x, y, and z directions.
        :param waitForConfirmation: (Optional) Wait for confirmation of the spawn before proceeding. This makes the method a blocking operation.
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :type location: float array[3]
        :type rotation: float array[3]
        :type scale: float array[3]
        :type waitForConfirmation: boolean
        :return: `True` if spawn was successful, `False` otherwise
        :rtype: boolean

        .. danger::

            TODO: Update traffic light artwork
            TODO: Add configuration options for different orientations
            TODO: Add helper functions for multi-light setups

        """        
        return qlabs.spawn_id(actorNumber, self.ID_TRAFFIC_LIGHT_SINGLE, location[0], location[1], location[2], rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi, scale[0], scale[1], scale[2], 0, waitForConfirmation)
 
    def set_state(self, qlabs, actorNumber, state, waitForConfirmation=True):
        """Set the light state (red/yellow/green) of a traffic light actor

        :param qlabs: A QuanserInteractiveLabs object.
        :param actorNumber: User defined unique identifier for the class actor in QLabs.
        :param state: An integer constant corresponding to a light state (see class constants)
        :param waitForConfirmation: (Optional) Wait for confirmation of the state change before proceeding. This makes the method a blocking operation.
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :type state: uint32
        :type waitForConfirmation: boolean
        :return: `True` if spawn was successful, `False` otherwise
        :rtype: boolean

        """
        c = CommModularContainer()
        c.classID = self.ID_TRAFFIC_LIGHT_SINGLE
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_TRAFFIC_LIGHT_SINGLE_SET_STATE
        c.payload = bytearray(struct.pack(">B", state))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if waitForConfirmation:
            qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            if waitForConfirmation:
                c = qlabs.wait_for_container(self.ID_TRAFFIC_LIGHT_SINGLE, actorNumber, self.FCN_TRAFFIC_LIGHT_SINGLE_SET_STATE_ACK)
                    
            return True
        else:
            return False        