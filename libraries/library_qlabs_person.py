from library_qlabs import CommModularContainer
from library_qlabs_common import QLabsCommon
import math

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsPerson:
    """ This class implements spawning and AI navigation of the environment for human pedestrians."""
       
    ID_PERSON = 10030
    
    STANDING = 0
    """ Speed constant for the move_to method. """
    WALK = 1.2
    """ Speed constant for the move_to method. """
    JOG = 3.6
    """ Speed constant for the move_to method. """
    RUN = 6.0
    """ Speed constant for the move_to method. """
    
    
    
    FCN_PERSON_MOVE_TO = 10
    FCN_PERSON_MOVE_TO_ACK = 11


    def __init__(self):
        """ Constructor Method """
        return
       
    def spawn(self, qlabs, actorNumber, location, rotation, scale, configuration=0, waitForConfirmation=True):
        """Spawns a person in an instance of QLabs at a specific location and rotation using radians.

        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param location: An array of floats for x, y and z coordinates in full-scale units. Multiply physical QCar locations by 10 to get full scale locations.
        :param rotation: An array of floats for the roll, pitch, and yaw in radians
        :param scale: An array of floats for the x, y, and z scale
        :param configuration: (Optional) Select the style of person to be spawned. See the Configuration section for more details.
        :param waitForConfirmation: (Optional) Wait for confirmation of the spawn before proceeding. This makes the method a blocking operation.
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :type location: float array[3]
        :type rotation: float array[3]
        :type scale: float array[3]
        :type configuration: int32
        :type waitForConfirmation: boolean
        :return: 0 if successful, 1 class not available, 2 actor number not available or already in use, 3 unknown error, -1 communications error
        :rtype: int32
        
        .. tip::

            The origin of the person is in the center of the body so by default, it will be spawned 1m above the surface of the target. An additional vertical offset may be required if the surface is sloped to prevent the actor from falling through the world ground surface.

        .. tip::

            If you would like to use the `move_to` method, the actor must be spawned in a valid nav area.
        """
        return QLabsCommon().spawn(qlabs, actorNumber, self.ID_PERSON, [location[0], location[1], location[2]+1.0], [rotation[0], rotation[1], rotation[2]], scale, configuration, waitForConfirmation)

    def spawn_degrees(self, qlabs, actorNumber, location, rotation, scale, configuration=0, waitForConfirmation=True):
        """Spawns a person in an instance of QLabs at a specific location and rotation using degrees.

        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param location: An array of floats for x, y and z coordinates in full-scale units. Multiply physical QCar locations by 10 to get full scale locations.
        :param rotation: An array of floats for the roll, pitch, and yaw in degrees
        :param scale: An array of floats for the x, y, and z scale
        :param configuration: (Optional) Select the style of person to be spawned. See the Configuration section for more details.
        :param waitForConfirmation: (Optional) Wait for confirmation of the spawn before proceeding. This makes the method a blocking operation.
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :type location: float array[3]
        :type rotation: float array[3]
        :type scale: float array[3]
        :type configuration: int32
        :type waitForConfirmation: boolean
        :return: 0 if successful, 1 class not available, 2 actor number not available or already in use, 3 unknown error, -1 communications error
        :rtype: int32
        
        .. tip::

            The origin of the person is in the center of the body so by default, it will be spawned 1m above the surface of the target. An additional vertical offset may be required if the surface is sloped to prevent the actor from falling through the world ground surface.

        .. tip::

            If you would like to use the `move_to` method, the actor must be spawned in a valid nav area.

        """
        return QLabsCommon().spawn(qlabs, actorNumber, self.ID_PERSON, [location[0], location[1], location[2]+1.0], [rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi], scale, configuration, waitForConfirmation)
    

        
    def move_to(self, qlabs, actorNumber, location, speed, waitForConfirmation=True):
        """Spawns a person in an instance of QLabs at a specific location and rotation using degrees.

        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param location: A target destination as an array of floats for x, y and z coordinates in full-scale units.
        :param speed: The speed at which the person should walk to the destination (refer to the constants for recommended speeds)
        :param waitForConfirmation: (Optional) Wait for confirmation before proceeding. This makes the method a blocking operation, but only until the command is received. The time for the actor to traverse to the destination is always non-blocking.
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :type location: float array[3]
        :type speed: float
        :type waitForConfirmation: boolean
        :return: `True` if successful, `False` otherwise
        :rtype: boolean
        
        .. tip::

            Ensure the start and end locations are in valid nav areas so the actor can find a path to the destination.

        """    
        c = CommModularContainer()
        c.classID = self.ID_PERSON
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_PERSON_MOVE_TO
        c.payload = bytearray(struct.pack(">ffff", location[0], location[1], location[2], speed))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if waitForConfirmation:
            qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            if waitForConfirmation:
                c = qlabs.wait_for_container(self.ID_PERSON, actorNumber, self.FCN_PERSON_MOVE_TO_ACK)
                if (c == None):
                    return False
                else:                     
                    return True  
            return True
        else:
            return False    

    def destroy(self, qlabs, actorNumber):
        """Destroys a person in an instance of QLabs.

        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :return: The number of actors destroyed. -1 if failed.
        :rtype: int32

        """
        return QLabsCommon().destroy_spawned_actor(qlabs, self.ID_PERSON, actorNumber)


    def ping(self, qlabs, actorNumber):
        """Checks if a person of the corresponding actor number exists in the QLabs environment.

        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :return: `True` if actor is present, `False` otherwise
        :rtype: boolean

        """
        return QLabsCommon().ping_actor(qlabs, actorNumber, self.ID_PERSON)

    def get_world_transform(self, qlabs, actorNumber):
        """Get the location, rotation, and scale in world coordinates of the person
        
        :param qlabs: A QuanserInteractiveLabs object.
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :return: success, location, rotation in radians
        :rtype: boolean, float array[3], float array[3]
        """    
        success, location, rotation, scale = QLabsCommon().get_world_transform(qlabs, actorNumber, self.ID_PERSON)

        return  success, location, rotation

    def get_world_transform_degrees(self, qlabs, actorNumber):
        """Get the location, rotation, and scale in world coordinates of the person
        
        :param qlabs: A QuanserInteractiveLabs object.
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :return: success, location, rotation in degrees
        :rtype: boolean, float array[3], float array[3]
        """    
        success, location, rotation, scale = QLabsCommon().get_world_transform(qlabs, actorNumber, self.ID_PERSON)
        rotation_deg = rotation_deg = [rotation[0]/math.pi*180, rotation[1]/math.pi*180, rotation[2]/math.pi*180]

        return  success, location, rotation_deg