from library_qlabs_actor import QLabsActor
import math

        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsTrafficCone(QLabsActor):
    """This class is for spawning traffic cones."""
       
    ID_TRAFFIC_CONE = 10000
    """Class ID"""

    def __init__(self, qlabs, verbose=False):
       """ Constructor Method

       :param qlabs: A QuanserInteractiveLabs object
       :param verbose: (Optional) Print error information to the console.
       :type qlabs: object
       :type verbose: boolean
       """

       self._qlabs = qlabs
       self._verbose = verbose
       self._classID = self.ID_TRAFFIC_CONE
       return

    def spawn(self, location, rotation, scale, configuration=0, waitForConfirmation=True):
        """Spawns a traffic cone in an instance of QLabs at a specific location and rotation using radians with a specified actor number.

        :param qlabs: A QuanserInteractiveLabs object.
        :param location: An array of floats for x, y and z coordinates.
        :param rotation: An array of floats for the roll, pitch, and yaw in radians.
        :param scale: An array of floats for the scale in the x, y, and z directions.
        :param configuration: (Optional) See the configuration section for the available spawn configurations.
        :param waitForConfirmation: (Optional) Wait for confirmation of the spawn before proceeding. This makes the method a blocking operation.
        :type qlabs: QuanserInteractiveLabs object
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
        """Spawns a traffic cone in an instance of QLabs at a specific location and rotation using degrees with a specified actor number.

        :param qlabs: A QuanserInteractiveLabs object.
        :param location: An array of floats for x, y and z coordinates.
        :param rotation: An array of floats for the roll, pitch, and yaw in degrees.
        :param scale: An array of floats for the scale in the x, y, and z directions.
        :param configuration: (Optional) See the configuration section for the available spawn configurations.
        :param waitForConfirmation: (Optional) Wait for confirmation of the spawn before proceeding. This makes the method a blocking operation.
        :type qlabs: QuanserInteractiveLabs object
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
        """Spawns a traffic cone in an instance of QLabs at a specific location and rotation using radians with a specified actor number.

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
        return self._spawn_id(actorNumber, location, rotation, scale, configuration, waitForConfirmation)
    
    def spawn_id_degrees(self, actorNumber, location, rotation, scale, configuration=0, waitForConfirmation=True):
        """Spawns a traffic cone in an instance of QLabs at a specific location and rotation using degrees with a specified actor number.

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
        return self.spawn_id(actorNumber, location, [rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi], scale, configuration, waitForConfirmation)
 
