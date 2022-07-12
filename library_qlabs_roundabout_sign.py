from library_qlabs import QuanserInteractiveLabs, CommModularContainer
from quanser.common import GenericError
import math

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsRoundaboutSign:
    """This class is for spawning roundabout signs."""
       
    ID_ROUNDABOUT_SIGN = 10060
    """Class ID"""
    
    # Initialize class
    def __init__(self):
        """ Constructor Method """
        return
       
    def spawn(self, qlabs, actorNumber, location, rotation, scale, waitForConfirmation=True):
        """Spawns a roundabout sign in an instance of QLabs at a specific location and rotation using radians.

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
        :type configuration: uint32
        :type waitForConfirmation: boolean
        :return: `True` if spawn was successful, `False` otherwise
        :rtype: boolean
        """
        return qlabs.spawn(actorNumber, self.ID_ROUNDABOUT_SIGN, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2], 0, waitForConfirmation)
 
    def spawn_degrees(self, qlabs, actorNumber, location, rotation, scale, waitForConfirmation=True):
        """Spawns a roundabout sign in an instance of QLabs at a specific location and rotation using degrees.

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
        :type configuration: uint32
        :type waitForConfirmation: boolean
        :return: `True` if spawn was successful, `False` otherwise
        :rtype: boolean
        """    
        return qlabs.spawn(actorNumber, self.ID_ROUNDABOUT_SIGN, location[0], location[1], location[2], rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi, scale[0], scale[1], scale[2], 0, waitForConfirmation)
 
