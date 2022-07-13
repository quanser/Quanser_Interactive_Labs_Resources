from library_qlabs import QuanserInteractiveLabs, CommModularContainer

import struct
import os
import platform
       
       
class QLabsCommon:
    """This contains a set of methods that are common to many classes. Many of these are wrapped with actor-specific versions."""

    FCN_UNKNOWN = 0
    """Function ID is not recognized."""
    FCN_REQUEST_PING = 1
    """Request a response from an actor to test if it is present."""
    FCN_RESPONSE_PING = 2
    """Response from an actor to confirming it is present."""
    FCN_REQUEST_WORLD_TRANSFORM = 3
    """Request a world transform from the actor to read its current location, rotation, and scale."""
    FCN_RESPONSE_WORLD_TRANSFORM = 4
    """Response from an actor with its current location, rotation, and scale."""

    # Initialize QLabs
    def __init__(self):
        """ Constructor Method """
        pass
            
    def destroy_all_spawned_actors(self, qlabs):
        """Find and destroy all spawned actors and widgets. This is a blocking operation.

        :param qlabs: A QuanserInteractiveLabs object.
        :type qlabs: QuanserInteractiveLabs object
        :return: The number of actors deleted. -1 if failed.
        :rtype: int32

        """
        actorNumber = 0
        c = CommModularContainer()
        
        c.classID = CommModularContainer.ID_GENERIC_ACTOR_SPAWNER
        c.actorNumber = actorNumber
        c.actorFunction = CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ALL_SPAWNED_ACTORS
        c.payload = bytearray()
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)        

        if (qlabs.send_container(c)):
            c = qlabs.wait_for_container(CommModularContainer.ID_GENERIC_ACTOR_SPAWNER, actorNumber, CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ALL_SPAWNED_ACTORS_ACK)
            if len(c.payload) == 4:
                num_actors_destroyed, = struct.unpack(">I", c.payload[0:4])
                return num_actors_destroyed
            else:
                return -1
        
        else:
            return -1
            
    def destroy_spawned_actor(self, qlabs, classID, actorNumber):
        """Find and destroy a specific actor. This is a blocking operation.
        
        :param qlabs: A QuanserInteractiveLabs object.
        :param classID: See the ID_ variables in the respective library classes for the class identifier
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :type qlabs: QuanserInteractiveLabs object
        :type classID: uint32
        :type actorNumber: uint32
        :return: The number of actors destroyed. -1 if failed.
        :rtype: int32

        """   
        c = CommModularContainer()
        
        c.classID = CommModularContainer.ID_GENERIC_ACTOR_SPAWNER
        c.actorNumber = 0
        c.actorFunction = CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ACTOR
        c.payload = bytearray(struct.pack(">II", classID, actorNumber))
        
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)        

        if (qlabs.send_container(c)):
            c = qlabs.wait_for_container(CommModularContainer.ID_GENERIC_ACTOR_SPAWNER, 0, CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ACTOR_ACK)
            if len(c.payload) == 4:
                num_actors_destroyed, = struct.unpack(">I", c.payload[0:4])
                return num_actors_destroyed
            else:
                return -1
        else:
            return -1            
            
    def spawn(self, qlabs, actorNumber, classID, location=[0,0,0], rotation=[0,0,0], scale=[1,1,1], configuration=0, waitForConfirmation=True):
        """Spawns a new actor.

        :param qlabs: A QuanserInteractiveLabs object.
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param classID: See the ID_ variables in the respective library classes for the class identifier
        :param location: An array of floats for x, y and z coordinates
        :param rotation: An array of floats for the roll, pitch, and yaw in radians
        :param scale: An array of floats for the scale in the x, y, and z directions. Scale values of 0.0 should not be used.
        :param configuration: (Optional) Spawn configuration. See class library for configuration options.
        :param waitForConfirmation: (Optional) Make this operation blocking until confirmation of the spawn has occurred.
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :type classID: uint32
        :type location: float array[3]
        :type rotation: float array[3]
        :type scale: float array[3]
        :type configuration: uint32
        :type waitForConfirmation: boolean
        :return: 0 if successful, 1 class not available, 2 actor number not available or already in use, 3 unknown error, -1 communications error
        :rtype: int32

        """
        c = CommModularContainer()
        c.classID = CommModularContainer.ID_GENERIC_ACTOR_SPAWNER
        c.actorNumber = 0
        c.actorFunction = CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_SPAWN
        c.payload = bytearray(struct.pack(">IIfffffffffI", classID, actorNumber, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2], configuration))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if waitForConfirmation:
            qlabs.flush_receive()        
                
        if (qlabs.send_container(c)):
        
            if waitForConfirmation:
                c = qlabs.wait_for_container(CommModularContainer.ID_GENERIC_ACTOR_SPAWNER, 0, CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_SPAWN_ACK)
                if len(c.payload) == 1:
                    status, = struct.unpack(">B", c.payload[0:1])
                    return status
                else:
                    return -1
            
            return 0
        else:
            return -1 
            
    def spawn_and_parent_with_relative_transform(self, qlabs, actorNumber, classID, location=[0,0,0], rotation=[0,0,0], scale=[1,1,1], configuration=0, parentClassID=0, parentActorNumber=0, parentComponent=0, waitForConfirmation=True):
        """Spawns a new actor relative to an existing actor and creates an kinematic relationship.

        :param qlabs: A QuanserInteractiveLabs object.
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param classID: See the ID_ variables in the respective library classes for the class identifier
        :param location: An array of floats for x, y and z coordinates
        :param rotation: An array of floats for the roll, pitch, and yaw in radians
        :param scale: An array of floats for the scale in the x, y, and z directions. Scale values of 0.0 should not be used.
        :param configuration: (Optional) Spawn configuration. See class library for configuration options.
        :param parentClassID: See the ID_ variables in the respective library classes for the class identifier
        :param parentActorNumber: User defined unique identifier for the class actor in QLabs
        :param parentComponent: `0` for the origin of the parent actor, see the parent class for additional reference frame options
        :param waitForConfirmation: (Optional) Make this operation blocking until confirmation of the spawn has occurred.
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :type classID: uint32
        :type location: float array[3]
        :type rotation: float array[3]
        :type scale: float array[3]
        :type configuration: uint32
        :type parentClassID: uint32
        :type parentActorNumber: uint32
        :type parentComponent: uint32
        :type waitForConfirmation: boolean
        :return: If waitForConfirmation = `False` then returns `True` if spawn was successful, `False` otherwise.  If waitForConfirmation = `True`, returns a container detailed response information if successful, otherwise `False`.
        :rtype: boolean

        """
        c = CommModularContainer()
        c.classID = CommModularContainer.ID_GENERIC_ACTOR_SPAWNER
        c.actorNumber = 0
        c.actorFunction = CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_SPAWN_AND_PARENT_RELATIVE
        c.payload = bytearray(struct.pack(">IIfffffffffIIII", classID, actorNumber, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2], configuration, parentClassID, parentActorNumber, parentComponent))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if waitForConfirmation:
            qlabs.flush_receive()        
                
        if (qlabs.send_container(c)):
        
            if waitForConfirmation:
                c = qlabs.wait_for_container(CommModularContainer.ID_GENERIC_ACTOR_SPAWNER, 0, CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_SPAWN_AND_PARENT_RELATIVE_ACK)
                return c
            
            return True
        else:
            return False                              
            
    def ping_actor(self, qlabs, actorNumber, classID):
        """Check if an actor of the specified class and actor number is present in the QLabs environment.
        
        :param qlabs: A QuanserInteractiveLabs object.
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param classID: See the ID_ variables in the respective library classes for the class identifier
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :type classID: uint32
        :return: `True` if successful, `False` otherwise
        :rtype: boolean
        """

        c = CommModularContainer()
        c.classID = classID
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_REQUEST_PING
        c.payload = bytearray()
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flush_receive()        
                
        if (qlabs.send_container(c)):
        
            c = qlabs.wait_for_container(classID, actorNumber, self.FCN_RESPONSE_PING)

            if c.payload[0] > 0:
                return True
            else:
                return False
        else:
            return False 
    
    def get_world_transform(self, qlabs, actorNumber, classID):
        """Get the location, rotation, and scale in world coordinates of the specified actor
        
        :param qlabs: A QuanserInteractiveLabs object.
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param classID: See the ID_ variables in the respective library classes for the class identifier
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :type classID: uint32
        :return: success, location, rotation, scale
        :rtype: boolean, float array[3], float array[3], float array[3]
        """

        c = CommModularContainer()
        c.classID = classID
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_REQUEST_WORLD_TRANSFORM
        c.payload = bytearray()
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)

        location = [0,0,0]
        rotation = [0,0,0]
        scale = [0,0,0]
        
        qlabs.flush_receive()        
                
        if (qlabs.send_container(c)):
        
            c = qlabs.wait_for_container(classID, actorNumber, self.FCN_RESPONSE_WORLD_TRANSFORM)

            if len(c.payload) == 36:
                location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2], = struct.unpack(">fffffffff", c.payload[0:36])
                return True, location, rotation, scale
            else:
                return False, location, rotation, scale
        else:
            return False, location, rotation, scale