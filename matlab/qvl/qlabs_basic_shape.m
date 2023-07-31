classdef qlabs_basic_shape < qlabs_actor
    properties
        ID_BASIC_SHAPE = 200;

        SHAPE_CUBE = 0
        SHAPE_CYLINDER = 1
        SHAPE_SPHERE = 2
        SHAPE_CONE = 3

        COMBINE_AVERAGE = 0
        COMBINE_MIN = 1
        COMBINE_MULTIPLY = 2
        COMBINE_MAX = 3


        FCN_BASIC_SHAPE_SET_MATERIAL_PROPERTIES = 10
        FCN_BASIC_SHAPE_SET_MATERIAL_PROPERTIES_ACK = 11
        FCN_BASIC_SHAPE_GET_MATERIAL_PROPERTIES = 30
        FCN_BASIC_SHAPE_GET_MATERIAL_PROPERTIES_RESPONSE = 31
    
        FCN_BASIC_SHAPE_SET_PHYSICS_PROPERTIES = 20
        FCN_BASIC_SHAPE_SET_PHYSICS_PROPERTIES_ACK = 21
    
        FCN_BASIC_SHAPE_ENABLE_DYNAMICS = 14
        FCN_BASIC_SHAPE_ENABLE_DYNAMICS_ACK = 15
        FCN_BASIC_SHAPE_SET_TRANSFORM = 16
        FCN_BASIC_SHAPE_SET_TRANSFORM_ACK = 17
        FCN_BASIC_SHAPE_ENABLE_COLLISIONS = 18
        FCN_BASIC_SHAPE_ENABLE_COLLISIONS_ACK = 19
    end
    
    methods
        function obj = qlabs_basic_shape(qlabs, verbose)

            arguments
                qlabs quanser_interactive_labs
                verbose logical = false
            end            

            obj = obj@qlabs_actor(qlabs, verbose);

            obj.classID = obj.ID_BASIC_SHAPE;
        end

        function success = set_material_properties(obj, color, roughness, metallic, waitForConfirmation)
%             Sets the visual surface properties of the shape.
% 
%             :param color: Red, Green, Blue components of the RGB color on a 0.0 to 1.0 scale.
%             :param roughness: A value between 0.0 (completely smooth and reflective) to 1.0 (completely rough and diffuse). Note that reflections are rendered using screen space reflections. Only objects visible in the camera view will be rendered in the reflection of the object.
%             :param metallic: Metallic (True) or non-metallic (False)
%             :param waitForConfirmation: (Optional) Wait for confirmation of the operation before proceeding. This makes the method a blocking operation.
%             :type color: float array[3]
%             :type roughness: float
%             :type metallic: boolean
%             :type waitForConfirmation: boolean
%             :return: True if successful, False otherwise
%             :rtype: boolean
            
            arguments
                obj qlabs_basic_shape
                color (1,3) single
                roughness double = 0.4
                metallic logical = false
                waitForConfirmation logical = true
            end 

            success = false;


            if (not(obj.is_actor_number_valid()))
                return
            end

            obj.c.classID = obj.ID_BASIC_SHAPE;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_BASIC_SHAPE_SET_MATERIAL_PROPERTIES;

            obj.c.payload = [flip(typecast(single(color(1)), 'uint8')) ...
                         flip(typecast(single(color(2)), 'uint8')) ...
                         flip(typecast(single(color(3)), 'uint8')) ...
                         flip(typecast(single(roughness), 'uint8')) ...
                         uint32(metallic)];

            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);

            if (waitForConfirmation)
                obj.qlabs.flush_receive()
            end
            
            if (obj.qlabs.send_container(obj.c))
                if waitForConfirmation
                    rc = obj.qlabs.wait_for_container(obj.ID_BASIC_SHAPE, obj.actorNumber, obj.FCN_BASIC_SHAPE_SET_MATERIAL_PROPERTIES_ACK);
                    if isempty(rc)
                        if (obj.verbose == true)
                            fprintf('Timeout waiting for response.\n')
                        end
                        return
                    end
                end

                success = true;
            end
        end

        function [success, color, roughness, metallic] = get_material_properties(obj)
%                 Gets the visual surface properties of the shape.
% 
%                 :param color: Red, Green, Blue components of the RGB color on a 0.0 to 1.0 scale.
%                 :param roughness: A value between 0.0 (completely smooth and reflective) to 1.0 (completely rough and diffuse). Note that reflections are rendered using screen space reflections. Only objects visible in the camera view will be rendered in the reflection of the object.
%                 :param metallic: Metallic (True) or non-metallic (False)
%                 :param waitForConfirmation: (Optional) Wait for confirmation of the operation before proceeding. This makes the method a blocking operation.
%                 :type color: float array[3]
%                 :type roughness: float
%                 :type metallic: boolean
%                 :type waitForConfirmation: boolean
%                 :return:
%                     - **status** - True if successful or False otherwise
%                     - **color** - Red, Green, Blue components of the RGB color on a 0.0 to 1.0 scale.
%                     - **roughness** - A value between 0.0 (completely smooth and reflective) to 1.0 (completely rough and diffuse). 
%                     - **metallic** - Metallic (True) or non-metallic (False)
%                 :rtype: boolean, float array[3], float, boolean
            arguments
                obj qlabs_basic_shape
            end

            color = [0,0,0];
            roughness = 0;
            metallic = false;
            success = false;

            if (obj.is_actor_number_valid())
                obj.c.classID = self.ID_BASIC_SHAPE;
                obj.c.actorNumber = self.actorNumber;
                obj.c.actorFunction = self.FCN_BASIC_SHAPE_GET_MATERIAL_PROPERTIES;
                obj.c.payload = [];
                obj.c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload);

                obj.qlabs.flush_receive()

                if (obj.qlabs.send_container(obj.c))
                    
                    rc = obj.qlabs.wait_for_container(obj.ID_BASIC_SHAPE, obj.actorNumber, obj.FCN_BASIC_SHAPE_GET_MATERIAL_PROPERTIES_RESPONSE);
                    if isempty(rc)
                        if (obj.verbose == true)
                            disp('Timeout waiting for response.')
                        end
                    else
                        if length(rc.payload) == 17
                            color(1) = typecast(flip(rc.payload(1:4)), 'single');
                            color(2) = typecast(flip(rc.payload(5:8)), 'single');
                            color(3) = typecast(flip(rc.payload(9:12)), 'single');
                            roughness = typecast(flip(rc.payload(13:16)), 'single');
                            metallic = payload(17) > 0;
    
                            success = true;
                            return;
                        else
                            if (obj.verbose == true)
                                fprintf('Container payload does not match expected size.\n')
                            end                          
                            return
                        end
                        
                    end
                else
                    if (obj.verbose)
                        fprintf('spawn_id: Communication timeout (classID %u, actorNumber %u).\n', obj.classID, actorNumber);
                    end
                end
            end
        end
        
        function success = set_enable_dynamics(obj, enableDynamics, waitForConfirmation)
            arguments
                obj qlabs_basic_shape
                enableDynamics logical
                waitForConfirmation logical = true
            end
            
            success = false;
%                 Sets the visual surface properties of the shape.
% 
%                 :param enableDynamics: Enable (True) or disable (False) the shape dynamics. A dynamic actor can be pushed with other static or dynamic actors.  A static actor will generate collisions, but will not be affected by interactions with other actors.
%                 :param waitForConfirmation: (Optional) Wait for confirmation of the operation before proceeding. This makes the method a blocking operation.
%                 :type enableDynamics: boolean
%                 :type waitForConfirmation: boolean
%                 :return: True if successful, False otherwise
%                 :rtype: boolean
            
            if (not(obj.is_actor_number_valid()))
                return
            end
            
            obj.c.classID = obj.ID_BASIC_SHAPE;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_BASIC_SHAPE_ENABLE_DYNAMICS;
            obj.c.payload = [uint8(enableDynamics)];
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);

            if (waitForConfirmation)
                obj.qlabs.flush_receive();
            end

            if (obj.qlabs.send_container(obj.c))
                if waitForConfirmation
                    rc = obj.qlabs.wait_for_container(obj.ID_BASIC_SHAPE, obj.actorNumber, obj.FCN_BASIC_SHAPE_SET_MATERIAL_PROPERTIES_ACK);
                    if isempty(rc)
                        if (obj.verbose == true)
                            fprintf('Timeout waiting for response.\n')
                        end
                        return
                    end
                end

                success = true;
            end
        end 

        function success = set_enable_collisions(obj, enableCollisions, waitForConfirmation)
            arguments
                obj qlabs_basic_shape
                enableCollisions logical
                waitForConfirmation logical = true
            end
            success = false;
%                 Enables and disables physics collisions. When disabled, other physics or velocity-based actors will be able to pass through.
% 
%                 :param enableCollisions: Enable (True) or disable (False) the collision.
%                 :param waitForConfirmation: (Optional) Wait for confirmation of the operation before proceeding. This makes the method a blocking operation.
%                 :type enableCollisions: boolean
%                 :type waitForConfirmation: boolean
%                 :return: True if successful, False otherwise
%                 :rtype: boolean
            
            if (not(obj.is_actor_number_valid))
                return
            end

            obj.c.classID = obj.ID_BASIC_SHAPE;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_BASIC_SHAPE_ENABLE_COLLISIONS;
            obj.c.payload = [uint8(enableCollisions)];
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);

            if (waitForConfirmation)
                obj.qlabs.flush_receive();
            end

            if (obj.qlabs.send_container(obj.c))
                if waitForConfirmation
                    rc = obj.qlabs.wait_for_container(obj.ID_BASIC_SHAPE, obj.actorNumber, obj.FCN_BASIC_SHAPE_ENABLE_COLLISIONS_ACK);
                    if isempty(rc)
                        if (obj.verbose == true)
                            fprintf('Timeout waiting for response.\n')
                        end
                        return
                    end
                end

                success = true;
            end
        end

        function success = set_physics_properties(obj, enableDynamics, mass, linearDamping, angularDamping, staticFriction, dynamicFriction, frictionCombineMode, restitution, restitutionCombineMode, waitForConfirmation)
            arguments
                obj qlabs_basic_shape
                enableDynamics logical
                mass double = 0.4
                linearDamping double = 0.4
                angularDamping double = 0.4
                staticFriction double = 0.4
                dynamicFriction double = 0.4
                frictionCombineMode int32 = obj.COMBINE_AVERAGE
                restitution double = 0.3
                restitutionCombineMode int32 = obj.COMBINE_AVERAGE
                waitForConfirmation logical = true
                
            end
            success = false;
%                 Sets the dynamic properties of the shape.
%         
%                 :param enableDynamics: Enable (True) or disable (False) the shape dynamics. A dynamic actor can be pushed with other static or dynamic actors.  A static actor will generate collisions, but will not be affected by interactions with other actors.
%                 :param mass: (Optional) Sets the mass of the actor in kilograms.
%                 :param linearDamping: (Optional) Sets the damping of the actor for linear motions.
%                 :param angularDamping: (Optional) Sets the damping of the actor for angular motions.
%                 :param staticFriction: (Optional) Sets the coefficient of friction when the actor is at rest. A value of 0.0 is frictionless.
%                 :param dynamicFriction: (Optional) Sets the coefficient of friction when the actor is moving relative to the surface it is on. A value of 0.0 is frictionless.
%                 :param frictionCombineMode: (Optional) Defines how the friction between two surfaces with different coefficients should be calculated (see COMBINE constants).
%                 :param restitution: (Optional) The coefficient of restitution defines how plastic or elastic a collision is. A value of 0.0 is plastic and will absorb all energy. A value of 1.0 is elastic and will bounce forever. A value greater than 1.0 will add energy with each collision.
%                 :param restitutionCombineMode: (Optional) Defines how the restitution between two surfaces with different coefficients should be calculated (see COMBINE constants).
%                 :param waitForConfirmation: (Optional) Wait for confirmation of the operation before proceeding. This makes the method a blocking operation.
%         
%                 :type enableDynamics: boolean
%                 :type mass: float
%                 :type linearDamping: float
%                 :type angularDamping: float
%                 :type staticFriction: float
%                 :type dynamicFriction: float
%                 :type frictionCombineMode: byte
%                 :type restitution: float
%                 :type restitutionCombineMode: byte
%                 :type waitForConfirmation: boolean
%                 :return: True if successful, False otherwise
%                 :rtype: boolean

%                 mass = 1.0;
%                 linearDamping = 0.0;
%                 angularDamping = 0.0;
%                 staticFriction = 0.0;
%                 dynamicFriction = 0.7;
%                 frictionCombineMode = obj.COMBINE_AVERAGE;
%                 restitution = 0.3;
%                 restitutionCombineMode = obj.COMBINE_AVERAGE;

            if (not(obj.is_actor_number_valid()))
                return
            end

            obj.c.classID = obj.ID_BASIC_SHAPE;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_BASIC_SHAPE_SET_PHYSICS_PROPERTIES;
%                c.payload = bytearray(struct.pack(">BfffffBfB", enableDynamics, mass, linearDamping, angularDamping, staticFriction, dynamicFriction, frictionCombineMode, restitution, restitutionCombineMode))
            
            obj.c.payload = [uint32(enableDynamics) ...
                     flip(typecast(single(mass), 'uint8')) ...
                     flip(typecast(single(linearDamping), 'uint8')) ...
                     flip(typecast(single(angularDamping), 'uint8')) ...
                     flip(typecast(single(staticFriction), 'uint8')) ...
                     flip(typecast(single(dynamicFriction), 'uint8')) ...
                     uint32(frictionCombineMode) ...
                     flip(typecast(single(restitution), 'uint8')) ...
                     uint32(restitutionCombineMode)];

            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);

            if (waitForConfirmation)
                obj.qlabs.flush_receive();
            end
            
            if (obj.qlabs.send_container(obj.c))
                if waitForConfirmation
                    rc = obj.qlabs.wait_for_container(obj.ID_BASIC_SHAPE, obj.actorNumber, obj.FCN_BASIC_SHAPE_SET_PHYSICS_PROPERTIES_ACK);
                    if isempty(rc)
                        if (obj.verbose == true)
                            fprintf('Timeout waiting for response.\n')
                        end
                        return
                    end
                end

                success = true;
            end
        end

        function success = set_transform(obj, location, rotation, scale, waitForConfirmation)
%                 Sets the location, rotation in radians, and scale. If a shape is parented to another actor then the location, rotation, and scale are relative to the parent actor.
%                 
%                 :param location: An array of floats for x, y and z coordinates in full-scale units. 
%                 :param rotation: An array of floats for the roll, pitch, and yaw in radians
%                 :param scale: An array of floats for the scale in the x, y, and z directions.
%                 :param waitForConfirmation: (Optional) Wait for confirmation of the operation before proceeding. This makes the method a blocking operation.
%                 :type location: float array[3]
%                 :type rotation: float array[3]
%                 :type scale: float array[3]
%                 :type waitForConfirmation: boolean
%                 :return: True if successful or False otherwise
%                 :rtype: boolean

            arguments
                obj qlabs_basic_shape
                location (1,3) single = [0 0 0]
                rotation (1,3) single = [0 0 0]
                scale (1,3) single = [0 0 0]
                waitForConfirmation logical = true
            end 

            success = false;

            if (not(obj.is_actor_number_valid()))
                return
            end

            obj.c.classID = obj.ID_BASIC_SHAPE;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_BASIC_SHAPE_SET_TRANSFORM;
            obj.c.payload = [flip(typecast(single(location(1)), 'uint8')) ...
                     flip(typecast(single(location(2)), 'uint8')) ...
                     flip(typecast(single(location(3)), 'uint8')) ...
                     flip(typecast(single(rotation(1)), 'uint8')) ...
                     flip(typecast(single(rotation(2)), 'uint8')) ...
                     flip(typecast(single(rotation(3)), 'uint8')) ...
                     flip(typecast(single(scale(1)), 'uint8')) ...
                     flip(typecast(single(scale(2)), 'uint8')) ...
                     flip(typecast(single(scale(3)), 'uint8'))];
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);

            if (waitForConfirmation)
                obj.qlabs.flush_receive();
            end

            if (obj.qlabs.send_container(obj.c))
                if waitForConfirmation
                    rc = obj.qlabs.wait_for_container(obj.ID_BASIC_SHAPE, obj.actorNumber, obj.FCN_BASIC_SHAPE_SET_TRANSFORM_ACK);
                    if isempty(rc)
                        if (obj.verbose == true)
                            fprintf('Timeout waiting for response.\n')
                        end
                        return
                    end
                end

                success = true;
            end
        end

        function success = set_transform_degrees(obj, location, rotation, scale, waitForConfirmation)
            arguments
                obj qlabs_basic_shape
                location (1,3) single = [0 0 0]
                rotation (1,3) single = [0 0 0]
                scale (1,3) single = [0 0 0]
                waitForConfirmation logical = true
            end
%                 Sets the location, rotation in degrees, and scale. If a shape is parented to another actor then the location, rotation, and scale are relative to the parent actor.
%                 
%                 :param location: An array of floats for x, y and z coordinates in full-scale units.
%                 :param rotation: An array of floats for the roll, pitch, and yaw in degrees
%                 :param scale: An array of floats for the scale in the x, y, and z directions.
%                 :param waitForConfirmation: (Optional) Wait for confirmation of the operation before proceeding. This makes the method a blocking operation.
%                 :type location: float array[3]
%                 :type rotation: float array[3]
%                 :type scale: float array[3]
%                 :type waitForConfirmation: boolean
%                 :return: True if successful or False otherwise
%                 :rtype: boolean

            success = obj.set_transform(location, rotation/180*pi, scale, waitForConfirmation);
            
        end

        function result = rotate_vector_2d_degrees(obj, vector, angle)
            arguments
                obj qlabs_basic_shape
                vector (1,3) single
                angle double
            end
%                 Internal helper function to rotate a vector on the z plane.
%                 
%                 :param vector: Vector to rotate
%                 :param angle: Rotation angle in radians
%                 :type vector: float array[3]
%                 :type angle: float
%                 :return: Rotated vector
%                 :rtype: float array[3]

            result = [0,0,vector(3)];

            result(1) = cos(angle)*vector(1) - sin(angle)*vector(2);
            result(2) = sin(angle)*vector(1) + cos(angle)*vector(2);
            
            return
        end

        function success = spawn_id_box_wall_from_end_points(obj, actorNumber, startLocation, endLocation, height, thickness, color, waitForConfirmation)
            arguments
                obj qlabs_basic_shape
                actorNumber double
                startLocation (1,3) single
                endLocation (1,3) single
                height double
                thickness double
                color (1,3) single = [1 1 1]
                waitForConfirmation logical = true
            end
            success = false;
%                 Given a start and end point, this helper method calculates the position, rotation, and scale required to place a box on top of this line.
% 
%                 :param actorNumber: User defined unique identifier for the class actor in QLabs
%                 :param startLocation: An array of floats for x, y and z coordinates.
%                 :param endLocation: An array of floats for x, y and z coordinates.
%                 :param height: The height of the wall.
%                 :param thickness: The width or thickness of the wall.
%                 :param color: Red, Green, Blue components of the RGB color on a 0.0 to 1.0 scale.
%                 :param waitForConfirmation: (Optional) Wait for confirmation of the operation before proceeding. This makes the method a blocking operation.
%                 :type actorNumber: uint32
%                 :type startLocation: float array[3]
%                 :type endLocation: float array[3]
%                 :type height: float
%                 :type thickness: float
%                 :type color: float array[3]
%                 :type waitForConfirmation: boolean
%                 :return: True if successful or False otherwise
%                 :rtype: boolean

            length = sqrt(power(startLocation(1) - endLocation(1), 2) + power(startLocation(2) - endLocation(2), 2) + power(startLocation(3) - endLocation(3), 2));
            location = [(startLocation(1) + endLocation(1))/2, (startLocation(2) + endLocation(2))/2, (startLocation(3) + endLocation(3))/2];

            yRotation = asin( (endLocation(3) - startLocation(3))/(length) );
            zRotation = atan2( (endLocation(2) - startLocation(2)), (endLocation(1) - startLocation(1)) );

            shiftedLocation = [location(1)+sin(yRotation)*cos(zRotation)*height/2, location(2)+sin(yRotation)*sin(zRotation)*height/2, location(3)+cos(yRotation)*height/2];

            if (0 == obj.spawn_id(actorNumber, shiftedLocation, [0, yRotation, zRotation], [length, thickness, height], obj.SHAPE_CUBE, waitForConfirmation))
                if (true == obj.set_material_properties(color, 1, false, waitForConfirmation))
                    success = true;
                    return
                else
                    return
                end
                
                return
            end
        end

        function success = spawn_id_box_walls_from_center(obj, actorNumbers, centerLocation, yaw, xSize, ySize, zHeight, wallThickness, floorThickness, wallColor, floorColor, waitForConfirmation)
            arguments
                obj qlabs_basic_shape
                actorNumbers (1,5) single
                centerLocation (1,3) single
                yaw single
                xSize single
                ySize single
                zHeight single
                wallThickness single
                floorThickness single = 0
                wallColor (1,3) single = [1 1 1]
                floorColor (1,3) single = [1 1 1]
                waitForConfirmation logical = true
            end
            success = false;
%                 Creates a container-like box with 4 walls and an optional floor.
% 
%                 :param actorNumbers: An array of 5 user defined unique identifiers for the class actors in QLabs.
%                 :param centerLocation: An array of floats for x, y and z coordinates.
%                 :param yaw: Rotation about the z axis in radians.
%                 :param xSize: Size of the box in the x direction.
%                 :param ySize: Size of the box in the y direction.
%                 :param zSize: Size of the box in the z direction.
%                 :param wallThickness: The thickness of the walls.
%                 :param floorThickness: (Optional) The thickness of the floor. Setting this to 0 will spawn a box without a floor.
%                 :param wallColor: (Optional) Red, Green, Blue components of the wall color on a 0.0 to 1.0 scale.
%                 :param floorColor: (Optional) Red, Green, Blue components of the floor color on a 0.0 to 1.0 scale.
%                 :param waitForConfirmation: (Optional) Wait for confirmation of the operation before proceeding. This makes the method a blocking operation.
%         
%                 :type actorNumbers: uint32 array[5]
%                 :type centerLocation: float array[3]
%                 :type yaw: float
%                 :type xSize: float
%                 :type ySize: float
%                 :type zSize: float
%                 :type wallThickness: float
%                 :type floorThickness: float
%                 :type wallColor: float array[3]
%                 :type floorColor: float array[3]
%                 :type waitForConfirmation: boolean
%         
%                 :return: True if successful or False otherwise
%                 :rtype: boolean
            
            origin = [centerLocation(1), centerLocation(2), centerLocation(3) + zHeight/2 + floorThickness];

            location = origin + obj.rotate_vector_2d_degrees([xSize/2 + wallThickness/2, 0, 0], yaw);
            if (0 ~= obj.spawn_id(actorNumbers(1), location, [0, 0, yaw], [wallThickness, ySize, zHeight], obj.SHAPE_CUBE, waitForConfirmation))
                return
            end
            if (true ~= obj.set_material_properties(wallColor, 1, false, waitForConfirmation))
                return
            end

            location = origin + obj.rotate_vector_2d_degrees([ - xSize/2 - wallThickness/2, 0, 0], yaw);
            if (0 ~= obj.spawn_id(actorNumbers(2), location, [0, 0, yaw], [wallThickness, ySize, zHeight], obj.SHAPE_CUBE, waitForConfirmation))
                return
            end
            if (true ~= obj.set_material_properties(wallColor, 1, false, waitForConfirmation))
                return
            end

            location = origin + obj.rotate_vector_2d_degrees([0, ySize/2 + wallThickness/2, 0], yaw);
            if (0 ~= obj.spawn_id(actorNumbers(3), location, [0, 0, yaw], [xSize + wallThickness*2, wallThickness, zHeight], obj.SHAPE_CUBE, waitForConfirmation))
                return
            end
            if (true ~= obj.set_material_properties(wallColor, 1, false, waitForConfirmation))
                return
            end

            location = origin + obj.rotate_vector_2d_degrees([0, - ySize/2 - wallThickness/2, 0], yaw);
            if (0 ~= obj.spawn_id(actorNumbers(4), location, [0, 0, yaw], [xSize + wallThickness*2, wallThickness, zHeight], obj.SHAPE_CUBE, waitForConfirmation))
                return
            end
            if (true ~= obj.set_material_properties(wallColor, 1, false, waitForConfirmation))
                return
            end

            if (floorThickness > 0)
                if (0 ~= obj.spawn_id(actorNumbers(5), [centerLocation(1), centerLocation(2), centerLocation(3)+ floorThickness/2], [0, 0, yaw], [xSize+wallThickness*2, ySize+wallThickness*2, floorThickness], obj.SHAPE_CUBE, waitForConfirmation))
                    return
                end
                if (true ~= obj.set_material_properties(floorColor, 1, false, waitForConfirmation))
                    return
                end
            end

            success = true;
            return

        end

        function success = spawn_id_box_walls_from_center_degrees(obj, actorNumbers, centerLocation, yaw, xSize, ySize, zHeight, wallThickness, floorThickness, wallColor, waitForConfirmation)
            arguments
                obj qlabs_basic_shape
                actorNumbers (1,5) single
                centerLocation (1,3) single
                yaw single
                xSize single
                ySize single
                zHeight single
                wallThickness single
                floorThickness single = 0
                wallColor (1,3) single = [1 1 1]
                waitForConfirmation logical = true
            end
%                 Creates a container-like box with 4 walls and an optional floor.
% 
%                 :param actorNumbers: An array of 5 user defined unique identifiers for the class actors in QLabs.
%                 :param centerLocation: An array of floats for x, y and z coordinates.
%                 :param yaw: Rotation about the z axis in degrees.
%                 :param xSize: Size of the box in the x direction.
%                 :param ySize: Size of the box in the y direction.
%                 :param zSize: Size of the box in the z direction.
%                 :param wallThickness: The thickness of the walls.
%                 :param floorThickness: (Optional) The thickness of the floor. Setting this to 0 will spawn a box without a floor.
%                 :param wallColor: (Optional) Red, Green, Blue components of the wall color on a 0.0 to 1.0 scale.
%                 :param floorColor: (Optional) Red, Green, Blue components of the floor color on a 0.0 to 1.0 scale.
%                 :param waitForConfirmation: (Optional) Wait for confirmation of the operation before proceeding. This makes the method a blocking operation.
%         
%                 :type actorNumbers: uint32 array[5]
%                 :type centerLocation: float array[3]
%                 :type yaw: float
%                 :type xSize: float
%                 :type ySize: float
%                 :type zSize: float
%                 :type wallThickness: float
%                 :type floorThickness: float
%                 :type wallColor: float array[3]
%                 :type floorColor: float array[3]
%                 :type waitForConfirmation: boolean
%         
%                 :return: True if successful or False otherwise
%                 :rtype: boolean

            success = obj.spawn_id_box_walls_from_center(actorNumbers, centerLocation, yaw/180*pi, xSize, ySize, zHeight, wallThickness, floorThickness, wallColor, waitForConfirmation);
            return 

        end
    end
end