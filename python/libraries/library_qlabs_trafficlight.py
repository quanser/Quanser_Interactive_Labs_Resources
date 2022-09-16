from library_qlabs import CommModularContainer
from library_qlabs_actor import QLabsActor

import math

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsTrafficLight(QLabsActor):

       
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
    
    def __init__(self, qlabs, verbose=False):
       """ Constructor Method

       :param qlabs: A QuanserInteractiveLabs object
       :param verbose: (Optional) Print error information to the console.
       :type qlabs: object
       :type verbose: boolean
       """

       self._qlabs = qlabs
       self._verbose = verbose
       self._classID = self.ID_TRAFFIC_LIGHT
       return

    def spawn(self, location, rotation, scale, configuration=0, waitForConfirmation=True):
        """Spawns a stoplight in an instance of QLabs at a specific location and rotation using radians with a specified actor number.

        :param location: An array of floats for x, y and z coordinates.
        :param rotation: An array of floats for the roll, pitch, and yaw in radians.
        :param scale: An array of floats for the scale in the x, y, and z directions.
        :param configuration: (Optional) See the configuration section for the available spawn configurations.
        :param waitForConfirmation: (Optional) Wait for confirmation of the spawn before proceeding. This makes the method a blocking operation.
        :type location: float array[3]
        :type rotation: float array[3]
        :type scale: float array[3]
        :type configuration: uint32
        :type waitForConfirmation: boolean
        :return: Success value of 0 if successful, 1 class not available, 2 actor number not available or already in use, 3 unknown error, -1 communications error. Actor number ID to use for addressing the actor.
        :rtype: int32, int32

        """
        return self._spawn(location, rotation, scale, configuration, waitForConfirmation)
 
    def spawn_degrees(self, location, rotation, scale, configuration=0, waitForConfirmation=True):
        """Spawns a stoplight in an instance of QLabs at a specific location and rotation using degrees with a specified actor number.

        :param location: An array of floats for x, y and z coordinates.
        :param rotation: An array of floats for the roll, pitch, and yaw in degrees.
        :param scale: An array of floats for the scale in the x, y, and z directions.
        :param configuration: (Optional) See the configuration section for the available spawn configurations.
        :param waitForConfirmation: (Optional) Wait for confirmation of the spawn before proceeding. This makes the method a blocking operation.
        :type location: float array[3]
        :type rotation: float array[3]
        :type scale: float array[3]
        :type configuration: uint32
        :type waitForConfirmation: boolean
        :return: Success value of 0 if successful, 1 class not available, 2 actor number not available or already in use, 3 unknown error, -1 communications error. Actor number ID to use for addressing the actor.
        :rtype: int32, int32


        """        
        return self.spawn(location, [rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi], scale, configuration, waitForConfirmation)
 
       
    def spawn_id(self, actorNumber, location, rotation, scale, configuration=0, waitForConfirmation=True):
        """Spawns a stoplight in an instance of QLabs at a specific location and rotation using radians with a specified actor number.

        :param actorNumber: User defined unique identifier for the class actor in QLabs.
        :param location: An array of floats for x, y and z coordinates.
        :param rotation: An array of floats for the roll, pitch, and yaw in radians.
        :param scale: An array of floats for the scale in the x, y, and z directions.
        :param configuration: (Optional) See the configuration section for the available spawn configurations.
        :param waitForConfirmation: (Optional) Wait for confirmation of the spawn before proceeding. This makes the method a blocking operation.
        :type actorNumber: uint32
        :type location: float array[3]
        :type rotation: float array[3]
        :type scale: float array[3]
        :type configuration: uint32
        :type waitForConfirmation: boolean
        :return: `True` if spawn was successful, `False` otherwise
        :rtype: boolean


        """
        return self._spawn_id(actorNumber, location, rotation, scale, configuration, waitForConfirmation)
 
    def spawn_id_degrees(self, actorNumber, location, rotation, scale, configuration=0, waitForConfirmation=True):
        """Spawns a stoplight in an instance of QLabs at a specific location and rotation using degrees with a specified actor number.

        :param actorNumber: User defined unique identifier for the class actor in QLabs.
        :param location: An array of floats for x, y and z coordinates.
        :param rotation: An array of floats for the roll, pitch, and yaw in degrees.
        :param scale: An array of floats for the scale in the x, y, and z directions.
        :param configuration: (Optional) See the configuration section for the available spawn configurations.
        :param waitForConfirmation: (Optional) Wait for confirmation of the spawn before proceeding. This makes the method a blocking operation.
        :type actorNumber: uint32
        :type location: float array[3]
        :type rotation: float array[3]
        :type scale: float array[3]
        :type configuration: uint32
        :type waitForConfirmation: boolean
        :return: `True` if spawn was successful, `False` otherwise
        :rtype: boolean


        """        
        return self.spawn_id(actorNumber, location, [rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi], scale, configuration, waitForConfirmation)
 
    def set_state(self, state, waitForConfirmation=True):
        """Set the light state (red/yellow/green) of a traffic light actor

        :param state: An integer constant corresponding to a light state (see class constants)
        :param waitForConfirmation: (Optional) Wait for confirmation of the state change before proceeding. This makes the method a blocking operation.
        :type state: uint32
        :type waitForConfirmation: boolean
        :return: `True` if successful, `False` otherwise
        :rtype: boolean

        """

        if (not self._is_actor_number_valid()):
            return False

        c = CommModularContainer()
        c.classID = self.ID_TRAFFIC_LIGHT
        c.actorNumber = self.actorNumber
        c.actorFunction = self.FCN_TRAFFIC_LIGHT_SET_STATE
        c.payload = bytearray(struct.pack(">B", state))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if waitForConfirmation:
            self._qlabs.flush_receive()  
        
        if (self._qlabs.send_container(c)):
            if waitForConfirmation:
                c = self._qlabs.wait_for_container(self.ID_TRAFFIC_LIGHT, self.actorNumber, self.FCN_TRAFFIC_LIGHT_SET_STATE_ACK)
                if (c == None):
                    return False 
                
            return True
        else:
            return False  
            
