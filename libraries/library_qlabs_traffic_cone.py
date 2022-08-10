from library_qlabs_common import QLabsCommon
import math

        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsTrafficCone:
    """This class is for spawning traffic cones."""
       
    ID_TRAFFIC_CONE = 10000
    """Class ID"""

    def __init__(self):
        """ Constructor Method """
        return
       
    def spawn(self, qlabs, actorNumber, location, rotation, scale, configuration=0, waitForConfirmation=True):
        """Spawns a traffic cone in an instance of QLabs at a specific location and rotation using radians.

        :param qlabs: A QuanserInteractiveLabs object.
        :param actorNumber: User defined unique identifier for the class actor in QLabs.
        :param location: An array of floats for x, y and z coordinates.
        :param rotation: An array of floats for the roll, pitch, and yaw in radians.
        :param scale: An array of floats for the scale in the x, y, and z directions.
        :param configuration: (Optional) See the configuration section for the available spawn configurations.
        :param waitForConfirmation: (Optional) Wait for confirmation of the spawn before proceeding. This makes the method a blocking operation.
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :type location: float array[3]
        :type rotation: float array[3]
        :type scale: float array[3]
        :type configuration: uint32
        :type waitForConfirmation: boolean
        :return: 0 if successful, 1 class not available, 2 actor number not available or already in use, 3 unknown error, -1 communications error
        :rtype: int32


        """
        return QLabsCommon().spawn(qlabs, actorNumber, self.ID_TRAFFIC_CONE, location, rotation, scale, configuration, waitForConfirmation)
    
    def spawn_degrees(self, qlabs, actorNumber, location, rotation, scale, configuration=0, waitForConfirmation=True):
        """Spawns a traffic cone in an instance of QLabs at a specific location and rotation using degrees.

        :param qlabs: A QuanserInteractiveLabs object.
        :param actorNumber: User defined unique identifier for the class actor in QLabs.
        :param location: An array of floats for x, y and z coordinates.
        :param rotation: An array of floats for the roll, pitch, and yaw in degrees.
        :param scale: An array of floats for the scale in the x, y, and z directions.
        :param configuration: (Optional) See the configuration section for the available spawn configurations.
        :param waitForConfirmation: (Optional) Wait for confirmation of the spawn before proceeding. This makes the method a blocking operation.
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :type location: float array[3]
        :type rotation: float array[3]
        :type scale: float array[3]
        :type configuration: uint32
        :type waitForConfirmation: boolean
        :return: 0 if successful, 1 class not available, 2 actor number not available or already in use, 3 unknown error, -1 communications error
        :rtype: int32


        """    
        return QLabsCommon().spawn(qlabs, actorNumber, self.ID_TRAFFIC_CONE, location, [rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi], scale, configuration, waitForConfirmation)
 

    def destroy(self, qlabs, actorNumber):
        """Destroys a traffic cone in an instance of QLabs.

        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :return: The number of actors destroyed. -1 if failed.
        :rtype: int32

        """
        return QLabsCommon().destroy_spawned_actor(qlabs, self.ID_TRAFFIC_CONE, actorNumber)


    def ping(self, qlabs, actorNumber):
        """Checks if a traffic cone of the corresponding actor number exists in the QLabs environment.

        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :return: `True` if actor is present, `False` otherwise
        :rtype: boolean

        """
        return QLabsCommon().ping_actor(qlabs, actorNumber, self.ID_TRAFFIC_CONE)

    def get_world_transform(self, qlabs, actorNumber):
        """Get the location, rotation, and scale in world coordinates of the traffic cone
        
        :param qlabs: A QuanserInteractiveLabs object.
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :return: success, location, rotation, scale
        :rtype: boolean, float array[3], float array[3], float array[3]
        """    
        return QLabsCommon().get_world_transform(qlabs, actorNumber, self.ID_TRAFFIC_CONE)