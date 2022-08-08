from library_qlabs_common import QLabsCommon
from library_qlabs import CommModularContainer

import math
import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsBasicShape:
    """ This class is for spawning both static and dynamic basic shapes. """
    
    ID_BASIC_SHAPE = 200
    """Class ID"""

    SHAPE_CUBE = 0
    """ """
    SHAPE_CYLINDER = 1
    """ """
    SHAPE_SPHERE = 2
    """ """
       
    
    FCN_BASIC_SHAPE_SET_MATERIAL_PROPERTIES = 10
    """ """
    FCN_BASIC_SHAPE_SET_MATERIAL_PROPERTIES_ACK = 11
    """ """
    FCN_BASIC_SHAPE_SET_PHYSICS_PROPERTIES = 12
    """ """
    FCN_BASIC_SHAPE_SET_PHYSICS_PROPERTIES_ACK = 13
    """ """
    FCN_BASIC_SHAPE_ENABLE_DYNAMICS = 14
    """ """
    FCN_BASIC_SHAPE_ENABLE_DYNAMICS_ACK = 15
    """ """
    FCN_BASIC_SHAPE_SET_TRANSFORM = 16
    """ """
    FCN_BASIC_SHAPE_SET_TRANSFORM_ACK = 17
    """ """
    
    # Initialize class
    def __init__(self):

       return
       
    def spawn(self, qlabs, actorNumber, location, rotation, scale, configuration=SHAPE_CUBE, waitForConfirmation=True):
        """Spawns a yield sign in an instance of QLabs at a specific location and rotation using radians.

        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param location: An array of floats for x, y and z coordinates
        :param rotation: An array of floats for the roll, pitch, and yaw in radians
        :param scale: An array of floats for the scale in the x, y, and z directions.
        :param configuration: Use the constants defined for selecting the shapes.
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
        return QLabsCommon().spawn(qlabs, actorNumber, self.ID_BASIC_SHAPE, location, rotation, scale, configuration, waitForConfirmation)
 
    def spawn_degrees(self, qlabs, actorNumber, location, rotation, scale, configuration=SHAPE_CUBE, waitForConfirmation=True):
        """Spawns a yield sign in an instance of QLabs at a specific location and rotation using degrees.

        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param location: An array of floats for x, y and z coordinates
        :param rotation: An array of floats for the roll, pitch, and yaw in degrees
        :param scale: An array of floats for the scale in the x, y, and z directions.
        :param configuration: Use the constants defined for selecting the shapes.
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
        return QLabsCommon().spawn(qlabs, actorNumber, self.ID_BASIC_SHAPE,  location, [rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi], scale, configuration, waitForConfirmation)
 
    def spawn_and_parent_with_relative_transform(self, qlabs, actorNumber, location, rotation, scale, configuration, parentClass, parentActorNumber, parentComponent, waitForConfirmation=True):
        return QLabsCommon().spawn_and_parent_with_relative_transform(qlabs, actorNumber, self.ID_BASIC_SHAPE, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2], configuration, parentClass, parentActorNumber, parentComponent, waitForConfirmation)
   
    def set_material_properties(self, qlabs, actorNumber, color, roughness=0.4, metallic=False, waitForConfirmation=True):
        c = CommModularContainer()
        c.classID = self.ID_BASIC_SHAPE
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_BASIC_SHAPE_SET_MATERIAL_PROPERTIES
        c.payload = bytearray(struct.pack(">ffffB", color[0], color[1], color[2], roughness, metallic))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if waitForConfirmation:
            qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            if waitForConfirmation:
                c = qlabs.wait_for_container(self.ID_BASIC_SHAPE, actorNumber, self.FCN_BASIC_SHAPE_SET_MATERIAL_PROPERTIES_ACK)
                return True
                    
            return True
        else:
            return False    
            
    def set_physics_properties(self, qlabs, actorNumber, mass, linearDampign, angularDamping, enableDynamics, waitForConfirmation=True):
        c = CommModularContainer()
        c.classID = self.ID_BASIC_SHAPE
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_BASIC_SHAPE_SET_PHYSICS_PROPERTIES
        c.payload = bytearray(struct.pack(">fffB", mass, linearDampign, angularDamping, enableDynamics))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if waitForConfirmation:
            qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            if waitForConfirmation:
                c = qlabs.wait_for_container(self.ID_BASIC_SHAPE, actorNumber, self.FCN_BASIC_SHAPE_SET_PHYSICS_PROPERTIES_ACK)
                return True
                    
            return True
        else:
            return False             
            
    def set_enable_dynamics(self, qlabs, actorNumber, enableDynamics, waitForConfirmation=True):
        c = CommModularContainer()
        c.classID = self.ID_BASIC_SHAPE
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_BASIC_SHAPE_ENABLE_DYNAMICS
        c.payload = bytearray(struct.pack(">B", enableDynamics))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if waitForConfirmation:
            qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            if waitForConfirmation:
                c = qlabs.wait_for_container(self.ID_BASIC_SHAPE, actorNumber, self.FCN_BASIC_SHAPE_ENABLE_DYNAMICS_ACK)
                return True
                    
            return True
        else:
            return False       


    def set_transform(self, qlabs, actorNumber, location, rotation, scale, waitForConfirmation=True):
        c = CommModularContainer()
        c.classID = self.ID_BASIC_SHAPE
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_BASIC_SHAPE_SET_TRANSFORM
        c.payload = bytearray(struct.pack(">fffffffff", location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2]))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if waitForConfirmation:
            qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            if waitForConfirmation:
                c = qlabs.wait_for_container(self.ID_BASIC_SHAPE, actorNumber, self.FCN_BASIC_SHAPE_SET_TRANSFORM_ACK)
                return c
                    
            return True
        else:
            return False        

    def set_transform_degrees(self, qlabs, actorNumber, location, rotation, scale, waitForConfirmation=True):
    
        return self.set_transform(qlabs, actorNumber, location, [x/180*math.pi for x in rotation], scale, waitForConfirmation)   
