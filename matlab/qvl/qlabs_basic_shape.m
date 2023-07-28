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

        function set_material_properties(obj, color, roughness, metallic, waitForConfirmation)
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

            if (not(obj.is_actor_number_valid()))
                return
            end

            obj.c.classID = self.ID_BASIC_SHAPE;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_BASIC_SHAPE_SET_MATERIAL_PROPERTIES;

            obj.c.payload = [flip(typecast(single(color(1)), 'uint8')) ...
                         flip(typecast(single(color(2)), 'uint8')) ...
                         flip(typecast(single(color(3)), 'uint8')) ...
                         flip(typecast(single(roughness), 'uint8')) ...
                         uint32(metallic)];

            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + len(c.payload);

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
                    end
                end

                success = true;
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
                        
                        rc = obj.qlabs.wait_for_container(self.ID_BASIC_SHAPE, self.actorNumber, self.FCN_BASIC_SHAPE_GET_MATERIAL_PROPERTIES_RESPONSE);
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
            
            function set_enable_dynamics(obj, enableDynamics, waitForConfirmation)
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
                obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + len(c.payload);

                if (waitForConfirmation)
                    obj.qlabs.flush_receive();
                end

                if (obj.qlabs.send_container(obj.c))
                    if (waitForConfirmation)
                        rc = obj.qlabs.wait_for_container(obj.ID_BASIC_SHAPE, obj.actorNumber, obj.FCN_BASIC_SHAPE_SET_MATERIAL_PROPERTIES_ACK);
                        if isempty(rc)
                            if (obj.verbose == true)
                                fprintf('Timeout waiting for response.\n')
                            end
                        end
                    end
                end
            end 

            function set_enable_collisions(self, enableCollisions, waitForConfirmation)
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
                obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + len(c.payload);

                if (waitForConfirmation)
                    obj.qlabs.flush_receive();
                end

                if (obj.qlabs.send_container(obj.c))
                    if (waitForConfirmation)
                        rc = obj.qlabs.wait_for_container(obj.ID_BASIC_SHAPE, obj.actorNumber, obj.FCN_BASIC_SHAPE_ENABLE_COLLISIONS_ACK);
                         if isempty(rc)
                            if (obj.verbose == true)
                                fprintf('Timeout waiting for response.\n')
                            end
                         end
                    end
                end
            end

            function set_physics_properties(obj, enableDynamics, mass, linearDamping, angularDamping, staticFriction, dynamicFriction, frictionCombineMode, restitution, restitutionCombineMode, waitForConfirmation)
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

                mass = 1.0;
                linearDamping = 0.0;
                angularDamping = 0.0;
                staticFriction = 0.0;
                dynamicFriction = 0.7;
                frictionCombineMode = COMBINE_AVERAGE;
                restitution = 0.3;
                restitutionCombineMode = COMBINE_AVERAGE;

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

                obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + len(c.payload);

                if (waitForConfirmation)
                    obj.qlabs.flush_receive();
                end
                
                if (obj.qlabs.send_container(obj.c))
                    if (waitForConfirmation)
                        rc = obj.qlabs.wait_for_container(obj.ID_BASIC_SHAPE, obj.actorNumber, obj.FCN_BASIC_SHAPE_ENABLE_COLLISIONS_ACK);
                         if isempty(rc)
                            if (obj.verbose == true)
                                fprintf('Timeout waiting for response.\n')
                            end
                         end
                    end
                end
            end
        end
    end
end