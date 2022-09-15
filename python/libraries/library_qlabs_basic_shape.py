from library_qlabs import CommModularContainer
from library_qlabs_actor import QLabsActor

import numpy as np
import math
import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsBasicShape(QLabsActor):
    """ This class is for spawning both static and dynamic basic shapes."""
    
    ID_BASIC_SHAPE = 200
    """Class ID"""

    SHAPE_CUBE = 0
    SHAPE_CYLINDER = 1
    SHAPE_SPHERE = 2
       
    
    FCN_BASIC_SHAPE_SET_MATERIAL_PROPERTIES = 10
    FCN_BASIC_SHAPE_SET_MATERIAL_PROPERTIES_ACK = 11
    FCN_BASIC_SHAPE_SET_PHYSICS_PROPERTIES = 12
    FCN_BASIC_SHAPE_SET_PHYSICS_PROPERTIES_ACK = 13
    FCN_BASIC_SHAPE_ENABLE_DYNAMICS = 14
    FCN_BASIC_SHAPE_ENABLE_DYNAMICS_ACK = 15
    FCN_BASIC_SHAPE_SET_TRANSFORM = 16
    FCN_BASIC_SHAPE_SET_TRANSFORM_ACK = 17
    FCN_BASIC_SHAPE_ENABLE_COLLISIONS = 18
    FCN_BASIC_SHAPE_ENABLE_COLLISIONS_ACK = 19
    
    def __init__(self, qlabs, verbose=False):
       """ Constructor Method

       :param qlabs: A QuanserInteractiveLabs object
       :param verbose: (Optional) Print error information to the console.
       :type qlabs: object
       :type verbose: boolean
       """

       self._qlabs = qlabs
       self._verbose = verbose
       self._classID = self.ID_BASIC_SHAPE
       return
       
    def spawn_id(self, actorNumber, location, rotation, scale, configuration=SHAPE_CUBE, waitForConfirmation=True):
        """Spawns a Basic Shape in an instance of QLabs at a specific location and rotation using radians using a specific actor number.

        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param location: An array of floats for x, y and z coordinates
        :param rotation: An array of floats for the roll, pitch, and yaw in radians
        :param scale: An array of floats for the scale in the x, y, and z directions.
        :param configuration: Use the constants defined for selecting the shapes.
        :param waitForConfirmation: (Optional) Wait for confirmation of the spawn before proceeding. This makes the method a blocking operation.
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
 
    def spawn_id_degrees(self, actorNumber, location, rotation, scale, configuration=SHAPE_CUBE, waitForConfirmation=True):
        """Spawns a Basic Shape in an instance of QLabs at a specific location and rotation using degrees using a specific actor number.

        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param location: An array of floats for x, y and z coordinates
        :param rotation: An array of floats for the roll, pitch, and yaw in degrees
        :param scale: An array of floats for the scale in the x, y, and z directions.
        :param configuration: Use the constants defined for selecting the shapes.
        :param waitForConfirmation: (Optional) Wait for confirmation of the spawn before proceeding. This makes the method a blocking operation.
        :type actorNumber: uint32
        :type location: float array[3]
        :type rotation: float array[3]
        :type scale: float array[3]
        :type configuration: uint32
        :type waitForConfirmation: boolean
        :return: 0 if successful, 1 class not available, 2 actor number not available or already in use, 3 unknown error, -1 communications error
        :rtype: int32


        """
        return self._spawn_id(actorNumber, location, [rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi], scale, configuration, waitForConfirmation)
 
    def spawn(self, location, rotation, scale, configuration=SHAPE_CUBE, waitForConfirmation=True):
        """Spawns a Basic Shape in an instance of QLabs at a specific location and rotation using radians.

        :param location: An array of floats for x, y and z coordinates
        :param rotation: An array of floats for the roll, pitch, and yaw in radians
        :param scale: An array of floats for the scale in the x, y, and z directions.
        :param configuration: Use the constants defined for selecting the shapes.
        :param waitForConfirmation: (Optional) Wait for confirmation of the spawn before proceeding. This makes the method a blocking operation.
        :type location: float array[3]
        :type rotation: float array[3]
        :type scale: float array[3]
        :type configuration: uint32
        :type waitForConfirmation: boolean
        :return: 0 if successful, 1 class not available, 3 unknown error, -1 communications error. The actor number allocated to the new actor.
        :rtype: int32, int32
        """
        return self._spawn(location, rotation, scale, configuration, waitForConfirmation)

    def spawn_degrees(self, location, rotation, scale, configuration=SHAPE_CUBE, waitForConfirmation=True):
        """Spawns a Basic Shape in an instance of QLabs at a specific location and rotation using degrees.

        :param location: An array of floats for x, y and z coordinates
        :param rotation: An array of floats for the roll, pitch, and yaw in degrees
        :param scale: An array of floats for the scale in the x, y, and z directions.
        :param configuration: Use the constants defined for selecting the shapes.
        :param waitForConfirmation: (Optional) Wait for confirmation of the spawn before proceeding. This makes the method a blocking operation.
        :type location: float array[3]
        :type rotation: float array[3]
        :type scale: float array[3]
        :type configuration: uint32
        :type waitForConfirmation: boolean
        :return: 0 if successful, 1 class not available, 3 unknown error, -1 communications error. The actor number allocated to the new actor.
        :rtype: int32, int32
        """
        return self._spawn(location, [rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi], scale, configuration, waitForConfirmation)

    def spawn_id_and_parent_with_relative_transform(self, actorNumber, location, rotation, scale, configuration, parentClass, parentActorNumber, parentComponent=0, waitForConfirmation=True):
        """Spawns a Basic Shape in an instance of QLabs at a specific location and rotation in radians relative to a parent actor and binds it with that actor.

        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param location: An array of floats for x, y and z coordinates
        :param rotation: An array of floats for the roll, pitch, and yaw in radians.
        :param scale: An array of floats for the scale in the x, y, and z directions.
        :param configuration: Use the constants defined for selecting the shapes.
        :param parentClass: See the ID constant for the class of actor that you want to bind the new shape to.
        :param parentActorNumber: The user defined unique identifier previously defined for the parent actor in QLabs
        :param parentComponent: See the component definitions for the parent actor. Default component 0 is the origin (or base frame) of the parent actor.
        :param waitForConfirmation: (Optional) Wait for confirmation of the spawn before proceeding. This makes the method a blocking operation.
        :type actorNumber: uint32
        :type location: float array[3]
        :type rotation: float array[3]
        :type scale: float array[3]
        :type configuration: uint32
        :type parentClass: uint32
        :type parentActorNumber: uint32
        :type parentComponent: uint32
        :type waitForConfirmation: boolean
        :return: 0 if successful, 1 class not available, 2 actor number not available or already in use, 3 cannot find the parent actor, 4 unknown error, -1 communications error
        :rtype: int32

        """

        return self._spawn_id_and_parent_with_relative_transform(actorNumber, location, rotation, scale, configuration, parentClass, parentActorNumber, parentComponent, waitForConfirmation)

    def spawn_id_and_parent_with_relative_transform_degrees(self, actorNumber, location, rotation, scale, configuration, parentClass, parentActorNumber, parentComponent=0, waitForConfirmation=True):
        """Spawns a Basic Shape in an instance of QLabs at a specific location and rotation in degrees relative to a parent actor and binds it with that actor.

        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param location: An array of floats for x, y and z coordinates
        :param rotation: An array of floats for the roll, pitch, and yaw in degrees.
        :param scale: An array of floats for the scale in the x, y, and z directions.
        :param configuration: Use the constants defined for selecting the shapes.
        :param parentClass: See the ID constant for the class of actor that you want to bind the new shape to.
        :param parentActorNumber: The user defined unique identifier previously defined for the parent actor in QLabs
        :param parentComponent: See the component definitions for the parent actor. Default component 0 is the origin (or base frame) of the parent actor.
        :param waitForConfirmation: (Optional) Wait for confirmation of the spawn before proceeding. This makes the method a blocking operation.
        :type actorNumber: uint32
        :type location: float array[3]
        :type rotation: float array[3]
        :type scale: float array[3]
        :type configuration: uint32
        :type parentClass: uint32
        :type parentActorNumber: uint32
        :type parentComponent: uint32
        :type waitForConfirmation: boolean
        :return: 0 if successful, 1 class not available, 2 actor number not available or already in use, 3 cannot find the parent actor, 4 unknown error, -1 communications error
        :rtype: int32

        """

        return self.spawn_id_and_parent_with_relative_transform(actorNumber, location, [rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi], scale, configuration, parentClass, parentActorNumber, parentComponent, waitForConfirmation)
   
   
    def set_material_properties(self, colour, roughness=0.4, metallic=False, waitForConfirmation=True):
        """Sets the visual surface properties of the shape.

        :param colour: Red, Green, Blue components of the RGB colour on a 0.0 to 1.0 scale.
        :param roughness: A value between 0.0 (completely smooth and reflective) to 1.0 (completely rough and diffuse). Note that reflections are rendered using screen space reflections. Only objects visible in the camera view will be rendered in the reflection of the object.
        :param metallic: Metallic (True) or non-metallic (False)
        :param waitForConfirmation: (Optional) Wait for confirmation of the operation before proceeding. This makes the method a blocking operation.
        :type colour: float array[3]
        :type roughness: float
        :type metallic: boolean
        :type waitForConfirmation: boolean
        :return: True if successful, False otherwise
        :rtype: boolean

        """
        if (not self._is_actor_number_valid()):
            return False

        c = CommModularContainer()
        c.classID = self.ID_BASIC_SHAPE
        c.actorNumber = self.actorNumber
        c.actorFunction = self.FCN_BASIC_SHAPE_SET_MATERIAL_PROPERTIES
        c.payload = bytearray(struct.pack(">ffffB", colour[0], colour[1], colour[2], roughness, metallic))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if waitForConfirmation:
            self._qlabs.flush_receive()  
        
        if (self._qlabs.send_container(c)):
            if waitForConfirmation:
                c = self._qlabs.wait_for_container(self.ID_BASIC_SHAPE, self.actorNumber, self.FCN_BASIC_SHAPE_SET_MATERIAL_PROPERTIES_ACK)
                if (c == None):
                    return False
                else:
                    return True
                    
            return True
        else:
            return False    
            

    def set_enable_dynamics(self, enableDynamics, waitForConfirmation=True):
        """Sets the visual surface properties of the shape.

        :param enableDynamics: Enable (True) or disable (False) the shape dynamics. A dynamic actor can be pushed with other static or dynamic actors.  A static actor will generate collisions, but will not be affected by interactions with other actors.
        :param waitForConfirmation: (Optional) Wait for confirmation of the operation before proceeding. This makes the method a blocking operation.
        :type enableDynamics: boolean
        :type waitForConfirmation: boolean
        :return: True if successful, False otherwise
        :rtype: boolean

        """
        if (not self._is_actor_number_valid()):
            return False

        c = CommModularContainer()
        c.classID = self.ID_BASIC_SHAPE
        c.actorNumber = self.actorNumber
        c.actorFunction = self.FCN_BASIC_SHAPE_ENABLE_DYNAMICS
        c.payload = bytearray(struct.pack(">B", enableDynamics))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if waitForConfirmation:
            self._qlabs.flush_receive()  
        
        if (self._qlabs.send_container(c)):
            if waitForConfirmation:
                c = self._qlabs.wait_for_container(self.ID_BASIC_SHAPE, self.actorNumber, self.FCN_BASIC_SHAPE_ENABLE_DYNAMICS_ACK)
                if (c == None):
                    return False
                else:
                    return True
                    
            return True
        else:
            return False   

    def set_enable_collisions(self, enableCollisions, waitForConfirmation=True):
        """Enables and disables physics collisions. When disabled, other physics or velocity-based actors will be able to pass through.

        :param enableCollisions: Enable (True) or disable (False) the collision. 
        :param waitForConfirmation: (Optional) Wait for confirmation of the operation before proceeding. This makes the method a blocking operation.
        :type enableCollisions: boolean
        :type waitForConfirmation: boolean
        :return: True if successful, False otherwise
        :rtype: boolean

        """
        if (not self._is_actor_number_valid()):
            return False

        c = CommModularContainer()
        c.classID = self.ID_BASIC_SHAPE
        c.actorNumber = self.actorNumber
        c.actorFunction = self.FCN_BASIC_SHAPE_ENABLE_COLLISIONS
        c.payload = bytearray(struct.pack(">B", enableCollisions))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if waitForConfirmation:
            self._qlabs.flush_receive()  
        
        if (self._qlabs.send_container(c)):
            if waitForConfirmation:
                c = self._qlabs.wait_for_container(self.ID_BASIC_SHAPE, self.actorNumber, self.FCN_BASIC_SHAPE_ENABLE_COLLISIONS_ACK)
                if (c == None):
                    return False
                else:
                    return True
                    
            return True
        else:
            return False   

    def set_physics_properties(self, mass, linearDamping, angularDamping, enableDynamics, waitForConfirmation=True):
        """Sets the dynamic properties of the shape.

        :param mass: Sets the mass of the actor in kilograms.
        :param linearDamping: Sets the damping of the actor for linear motions.
        :param angularDamping: Sets the damping of the actor for angular motions.
        :param enableDynamics: Enable (True) or disable (False) the shape dynamics. A dynamic actor can be pushed with other static or dynamic actors.  A static actor will generate collisions, but will not be affected by interactions with other actors.
        :param waitForConfirmation: (Optional) Wait for confirmation of the operation before proceeding. This makes the method a blocking operation.
        
        :type mass: float
        :type linearDamping: float
        :type angularDamping: float
        :type enableDynamics: boolean
        :type waitForConfirmation: boolean
        :return: True if successful, False otherwise
        :rtype: boolean

        """
        if (not self._is_actor_number_valid()):
            return False

        c = CommModularContainer()
        c.classID = self.ID_BASIC_SHAPE
        c.actorNumber = self.actorNumber
        c.actorFunction = self.FCN_BASIC_SHAPE_SET_PHYSICS_PROPERTIES
        c.payload = bytearray(struct.pack(">fffB", mass, linearDamping, angularDamping, enableDynamics))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if waitForConfirmation:
            self._qlabs.flush_receive()  
        
        if (self._qlabs.send_container(c)):
            if waitForConfirmation:
                c = self._qlabs.wait_for_container(self.ID_BASIC_SHAPE, self.actorNumber, self.FCN_BASIC_SHAPE_SET_PHYSICS_PROPERTIES_ACK)
                if (c == None):
                    return False
                else:
                    return True
                    
            return True
        else:
            return False             
            
    


    def set_transform(self, location, rotation, scale, waitForConfirmation=True):
        """Sets the location, rotation in radians, and scale. If a shape is parented to another actor then the location, rotation, and scale are relative to the parent actor.

        :param location: An array of floats for x, y and z coordinates in full-scale units. Multiply physical QCar locations by 10 to get full scale locations.
        :param rotation: An array of floats for the roll, pitch, and yaw in radians
        :param scale: An array of floats for the scale in the x, y, and z directions.
        :param waitForConfirmation: (Optional) Wait for confirmation of the operation before proceeding. This makes the method a blocking operation.
        :type location: float array[3]
        :type rotation: float array[3]
        :type scale: float array[3]
        :type waitForConfirmation: boolean
        :return: True if successful or False otherwise
        :rtype: boolean
        """
        if (not self._is_actor_number_valid()):
            return False

        c = CommModularContainer()
        c.classID = self.ID_BASIC_SHAPE
        c.actorNumber = self.actorNumber
        c.actorFunction = self.FCN_BASIC_SHAPE_SET_TRANSFORM
        c.payload = bytearray(struct.pack(">fffffffff", location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2]))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if waitForConfirmation:
            self._qlabs.flush_receive()  
        
        if (self._qlabs.send_container(c)):
            if waitForConfirmation:
                c = self._qlabs.wait_for_container(self.ID_BASIC_SHAPE, self.actorNumber, self.FCN_BASIC_SHAPE_SET_TRANSFORM_ACK)
                if (c == None):
                    return False
                else:
                    return True

            return True
        else:
            return False  
            


    def set_transform_degrees(self, location, rotation, scale, waitForConfirmation=True):
        """Sets the location, rotation in degrees, and scale. If a shape is parented to another actor then the location, rotation, and scale are relative to the parent actor.

        :param location: An array of floats for x, y and z coordinates in full-scale units. Multiply physical QCar locations by 10 to get full scale locations.
        :param rotation: An array of floats for the roll, pitch, and yaw in degrees
        :param scale: An array of floats for the scale in the x, y, and z directions.
        :param waitForConfirmation: (Optional) Wait for confirmation of the operation before proceeding. This makes the method a blocking operation.
        :type location: float array[3]
        :type rotation: float array[3]
        :type scale: float array[3]
        :type waitForConfirmation: boolean
        :return: True if successful or False otherwise
        :rtype: boolean
        """
    
        return self.set_transform(location, [rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi], scale, waitForConfirmation)   


    def _rotate_vector_2d_degrees(self, vector, angle):
        """Internal helper function to rotate a vector on the z plane.

        :param vector: Vector to rotate
        :param angle: Rotation angle in radians
        :type vector: float array[3]
        :type angle: float 
        :return: Rotated vector
        :rtype: float array[3]
        """

        result = [0,0,vector[2]]

        result[0] = math.cos(angle)*vector[0] - math.sin(angle)*vector[1]
        result[1] = math.sin(angle)*vector[0] + math.cos(angle)*vector[1]
    
        return result

    def spawn_id_box_walls_from_end_points(self, actorNumber, startLocation, endLocation, height, thickness, colour=[1,1,1], waitForConfirmation=True):
        """Given a start and end point, this helper method calculates the position, rotation, and scale required to place a box on top of this line. 

        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param startLocation: An array of floats for x, y and z coordinates.
        :param endLocation: An array of floats for x, y and z coordinates.
        :param height: The height of the wall.
        :param thickness: The width or thickness of the wall.
        :param colour: Red, Green, Blue components of the RGB colour on a 0.0 to 1.0 scale.
        :param waitForConfirmation: (Optional) Wait for confirmation of the operation before proceeding. This makes the method a blocking operation.
        :type actorNumber: uint32
        :type startLocation: float array[3]
        :type endLocation: float array[3]
        :type height: float
        :type thickness: float
        :type colour: float array[3]
        :type waitForConfirmation: boolean
        :return: True if successful or False otherwise
        :rtype: boolean
        """


        length = math.sqrt(pow(startLocation[0] - endLocation[0],2) + pow(startLocation[1] - endLocation[1],2) + pow(startLocation[2] - endLocation[2],2))
        location = [(startLocation[0] + endLocation[0])/2, (startLocation[1] + endLocation[1])/2, (startLocation[2] + endLocation[2])/2]
    
        yRotation = -math.asin( (endLocation[2] - startLocation[2])/(length) )
        zRotation = math.atan2( (endLocation[1] - startLocation[1]), (endLocation[0] - startLocation[0]))
    
        shiftedLocation = [location[0]+math.sin(yRotation)*math.cos(zRotation)*height/2, location[1]+math.sin(yRotation)*math.sin(zRotation)*height/2, location[2]+math.cos(yRotation)*height/2]
    
        if (0 == self.spawn_id(actorNumber, shiftedLocation, [0, yRotation, zRotation], [length, thickness, height], self.SHAPE_CUBE, waitForConfirmation)):
            if (True == self.set_material_properties(colour, 1, False, waitForConfirmation)):
                return True
            else:
                return False

        else:
            return False
    
    
    def spawn_id_box_walls_from_center(self, actorNumbers, centerLocation, yaw, xSize, ySize, zHeight, wallThickness, floorThickness=0, wallColour=[1,1,1], floorColour=[1,1,1], waitForConfirmation=True):
        """Creates a container-like box with 4 walls and an optional floor. 

        :param actorNumbers: An array of 5 user defined unique identifiers for the class actors in QLabs.
        :param centerLocation: An array of floats for x, y and z coordinates.
        :param yaw: Rotation about the z axis in radians.
        :param xSize: Size of the box in the x direction.
        :param ySize: Size of the box in the y direction.
        :param zSize: Size of the box in the z direction.
        :param wallThickness: The thickness of the walls.
        :param floorThickness: (Optional) The thickness of the floor. Setting this to 0 will spawn a box without a floor.
        :param wallColour: (Optional) Red, Green, Blue components of the wall colour on a 0.0 to 1.0 scale.
        :param floorColour: (Optional) Red, Green, Blue components of the floor colour on a 0.0 to 1.0 scale.
        :param waitForConfirmation: (Optional) Wait for confirmation of the operation before proceeding. This makes the method a blocking operation.

        :type actorNumbers: uint32 array[5]
        :type centerLocation: float array[3]
        :type yaw: float
        :type xSize: float
        :type ySize: float
        :type zSize: float
        :type wallThickness: float
        :type floorThickness: float
        :type wallColour: float array[3]
        :type floorColour: float array[3]
        :type waitForConfirmation: boolean

        :return: True if successful or False otherwise
        :rtype: boolean
        """
        origin = [centerLocation[0],  centerLocation[1], centerLocation[2] + zHeight/2 + floorThickness]

        location = np.add(origin, self._rotate_vector_2d_degrees([xSize/2 + wallThickness/2, 0, 0], yaw) )
        if (0 != self.spawn_id(actorNumbers[0], location, [0, 0, yaw], [wallThickness, ySize, zHeight], self.SHAPE_CUBE, waitForConfirmation)):
            return False
        if (True != self.set_material_properties(wallColour, 1, False, waitForConfirmation)):
            return False
    
        location = np.add(origin, self._rotate_vector_2d_degrees([ - xSize/2 - wallThickness/2, 0, 0], yaw) )
        if (0 != self.spawn_id(actorNumbers[1], location, [0, 0, yaw], [wallThickness, ySize, zHeight], self.SHAPE_CUBE, waitForConfirmation)):
            return False
        if (True != self.set_material_properties(wallColour, 1, False, waitForConfirmation)):
            return False
    
        
        location = np.add(origin, self._rotate_vector_2d_degrees([0, ySize/2 + wallThickness/2, 0], yaw) )
        if (0 != self.spawn_id(actorNumbers[2], location, [0, 0, yaw], [xSize + wallThickness*2, wallThickness, zHeight], self.SHAPE_CUBE, waitForConfirmation)):
            return False
        if (True != self.set_material_properties(wallColour, 1, False, waitForConfirmation)):
            return False
    
        
        location = np.add(origin, self._rotate_vector_2d_degrees([0, - ySize/2 - wallThickness/2, 0], yaw) )
        if (0 != self.spawn_id(actorNumbers[3], location, [0, 0, yaw], [xSize + wallThickness*2, wallThickness, zHeight], self.SHAPE_CUBE, waitForConfirmation)):
            return False
        if (True != self.set_material_properties(wallColour, 1, False, waitForConfirmation)):
            return False
        
        if (floorThickness > 0):
            if (0 != self.spawn_id(actorNumbers[4], [centerLocation[0], centerLocation[1], centerLocation[2]+ floorThickness/2], [0, 0, yaw], [xSize+wallThickness*2, ySize+wallThickness*2, floorThickness], self.SHAPE_CUBE, waitForConfirmation)):
                return False
            if (True != self.set_material_properties(floorColour, 1, False, waitForConfirmation)):
                return False

        return True

    def spawn_id_box_walls_from_center_degrees(self, actorNumbers, centerLocation, yaw, xSize, ySize, zHeight, wallThickness, floorThickness=0, wallColour=[1,1,1], floorColour=[1,1,1], waitForConfirmation=True):
        """Creates a container-like box with 4 walls and an optional floor. 

        :param actorNumbers: An array of 5 user defined unique identifiers for the class actors in QLabs.
        :param centerLocation: An array of floats for x, y and z coordinates.
        :param yaw: Rotation about the z axis in degrees.
        :param xSize: Size of the box in the x direction.
        :param ySize: Size of the box in the y direction.
        :param zSize: Size of the box in the z direction.
        :param wallThickness: The thickness of the walls.
        :param floorThickness: (Optional) The thickness of the floor. Setting this to 0 will spawn a box without a floor.
        :param wallColour: (Optional) Red, Green, Blue components of the wall colour on a 0.0 to 1.0 scale.
        :param floorColour: (Optional) Red, Green, Blue components of the floor colour on a 0.0 to 1.0 scale.
        :param waitForConfirmation: (Optional) Wait for confirmation of the operation before proceeding. This makes the method a blocking operation.

        :type actorNumbers: uint32 array[5]
        :type centerLocation: float array[3]
        :type yaw: float
        :type xSize: float
        :type ySize: float
        :type zSize: float
        :type wallThickness: float
        :type floorThickness: float
        :type wallColour: float array[3]
        :type floorColour: float array[3]
        :type waitForConfirmation: boolean

        :return: True if successful or False otherwise
        :rtype: boolean
        """
        return self.spawn_id_box_walls_from_center(actorNumbers, centerLocation, yaw/180*math.pi, xSize, ySize, zHeight, wallThickness, floorThickness, wallColour, floorColour, waitForConfirmation)

    