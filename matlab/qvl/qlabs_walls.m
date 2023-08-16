classdef qlabs_walls < qlabs_actor
    properties
        % This class is for spawning both static and dynamic walls.
        
        ID_WALL = 10080
        % Class ID
    
        WALL_FOAM_BOARD = 0
    
        COMBINE_AVERAGE = 0
        COMBINE_MIN = 1
        COMBINE_MULTIPLY = 2
        COMBINE_MAX = 3
    
        FCN_WALLS_ENABLE_DYNAMICS = 14
        FCN_WALLS_ENABLE_DYNAMICS_ACK = 15
        FCN_WALLS_SET_TRANSFORM = 16
        FCN_WALLS_SET_TRANSFORM_ACK = 17
        FCN_WALLS_ENABLE_COLLISIONS = 18
        FCN_WALLS_ENABLE_COLLISIONS_ACK = 19
        FCN_WALLS_SET_PHYSICS_PROPERTIES = 20
        FCN_WALLS_SET_PHYSICS_PROPERTIES_ACK = 21
    end
    methods
        function obj = qlabs_walls(qlabs, verbose)
            arguments
                qlabs quanser_interactive_labs
                verbose logical = false
            end
            obj = obj@qlabs_actor(qlabs, verbose);
    
            obj.classID = obj.ID_WALL;
        end

        function success = set_enable_dynamics(obj, enableDynamics, waitForConfirmation)
            arguments
                obj qlabs_walls
                enableDynamics logical
                waitForConfirmation logical = true
            end
            success = false;
%             Sets the physics properties of the wall.
% 
%             :param enableDynamics: Enable (True) or disable (False) the wall dynamics. A dynamic actor can be pushed with other static or dynamic actors.  A static actor will generate collisions, but will not be affected by interactions with other actors.
%             :param waitForConfirmation: (Optional) Wait for confirmation of the operation before proceeding. This makes the method a blocking operation.
%             :type enableDynamics: boolean
%             :type waitForConfirmation: boolean
%             :return: True if successful, False otherwise
%             :rtype: boolean

            if isempty(obj.is_actor_number_valid())
                return
            end

            obj.c.classID = obj.ID_WALL;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_WALLS_ENABLE_DYNAMICS;
            obj.c.payload = flip(typecast(single(enableDynamics), 'uint8'));
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);

            if waitForConfirmation
                obj.qlabs.flush_receive();
            end

            if (obj.qlabs.send_container(obj.c))
                if waitForConfirmation
                    rc = obj.qlabs.wait_for_container(obj.ID_WALL, obj.actorNumber, obj.FCN_WALLS_ENABLE_DYNAMICS_ACK);

                    if isempty(rc)
                        return
                    else
                        success = true;
                        return
                    end
                end
                success = true;
                return
            else
                return
            end
        end

        function success = set_enable_collisions(obj, enableCollisions, waitForConfirmation)
            arguments
                obj qlabs_walls
                enableCollisions logical
                waitForConfirmation logical = true
            end
            success = true;

%             Enables and disables physics collisions. When disabled, other physics or velocity-based actors will be able to pass through.
% 
%             :param enableCollisions: Enable (True) or disable (False) the collision.
%             :param waitForConfirmation: (Optional) Wait for confirmation of the operation before proceeding. This makes the method a blocking operation.
%             :type enableCollisions: boolean
%             :type waitForConfirmation: boolean
%             :return: True if successful, False otherwise
%             :rtype: boolean

            if isempty(obj.is_actor_number_valid())
                return
            end

            obj.c.classID = obj.ID_WALL;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_WALLS_ENABLE_COLLISIONS;
            obj.c.payload = flip(typecast(single(enableCollisions), 'uint8'));
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);

            if waitForConfirmation
                obj.qlabs.flush_receive();
            end

            if (obj.qlabs.send_container(obj.c))
                if waitForConfirmation
                    rc = obj.qlabs.wait_for_container(obj.ID_WALL, obj.actorNumber, obj.FCN_WALLS_ENABLE_COLLISIONS_ACK);

                    if isempty(rc)
                        return
                    else
                        success = true;
                        return
                    end
                end
                success = true;
                return
            else
                return
            end
        end

        function success = set_physics_properties(obj, enableDynamics, mass, linearDamping, angularDamping, staticFriction, dynamicFriction, frictionCombineMode, restitution, restitutionCombineMode, waitForConfirmation)
            arguments
                obj qlabs_walls
                enableDynamics logical
                mass single = 1
                linearDamping single = 0.01
                angularDamping single = 0
                staticFriction single = 0
                dynamicFriction single = 0
                frictionCombineMode uint8 = obj.COMBINE_AVERAGE
                restitution single = 0.3
                restitutionCombineMode uint8 = obj.COMBINE_AVERAGE
                waitForConfirmation logical = true
            end
            success = false;
%             Sets the dynamic properties of the wall.
% 
%             :param enableDynamics: Enable (True) or disable (False) the wall dynamics. A dynamic actor can be pushed with other static or dynamic actors.  A static actor will generate collisions, but will not be affected by interactions with other actors.
%             :param mass: (Optional) Sets the mass of the actor in kilograms.
%             :param linearDamping: (Optional) Sets the damping of the actor for linear motions.
%             :param angularDamping: (Optional) Sets the damping of the actor for angular motions.
%             :param staticFriction: (Optional) Sets the coefficient of friction when the actor is at rest. A value of 0.0 is frictionless.
%             :param dynamicFriction: (Optional) Sets the coefficient of friction when the actor is moving relative to the surface it is on. A value of 0.0 is frictionless.
%             :param frictionCombineMode: (Optional) Defines how the friction between two surfaces with different coefficients should be calculated (see COMBINE constants).
%             :param restitution: (Optional) The coefficient of restitution defines how plastic or elastic a collision is. A value of 0.0 is plastic and will absorb all energy. A value of 1.0 is elastic and will bounce forever. A value greater than 1.0 will add energy with each collision.
%             :param restitutionCombineMode: (Optional) Defines how the restitution between two surfaces with different coefficients should be calculated (see COMBINE constants).
%             :param waitForConfirmation: (Optional) Wait for confirmation of the operation before proceeding. This makes the method a blocking operation.
%     
%             :type enableDynamics: boolean
%             :type mass: float
%             :type linearDamping: float
%             :type angularDamping: float
%             :type staticFriction: float
%             :type dynamicFriction: float
%             :type frictionCombineMode: byte
%             :type restitution: float
%             :type restitutionCombineMode: byte
%             :type waitForConfirmation: boolean
%             :return: True if successful, False otherwise
%             :rtype: boolean

            if isempty(obj.is_actor_number_valid())
                return
            end

            obj.c.classID = obj.ID_WALL;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_WALLS_SET_PHYSICS_PROPERTIES;
            obj.c.payload = [flip(typecast(single(enableDynamics), 'uint8')) ...
                             flip(typecast(single(mass), 'uint8')) ...
                             flip(typecast(single(linearDamping), 'uint8')) ...
                             flip(typecast(single(angularDamping), 'uint8')) ...
                             flip(typecast(single(staticFriction), 'uint8')) ...
                             flip(typecast(single(dynamicFriction), 'uint8')) ...
                             flip(typecast(single(frictionCombineMode), 'uint8')) ...
                             flip(typecast(single(restitution), 'uint8')) ...
                             flip(typecast(single(restitutionCombineMode), 'uint8'))];
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);

            if waitForConfirmation
                obj.qlabs.flush_receive();
            end

            if (obj.qlabs.send_container(obj.c))
                if waitForConfirmation
                    rc = obj.qlabs.wait_for_container(obj.ID_WALL, obj.actorNumber, obj.FCN_WALLS_SET_PHYSICS_PROPERTIES_ACK);

                    if isempty(rc)
                        return
                    else
                        success = true;
                        return
                    end
                end
                success = true;
                return
            else
                return
            end
        end

        function success = set_transform(obj, location, rotation, scale, waitForConfirmation)
            arguments
                obj qlabs_walls
                location (1,3) single
                rotation (1,3) single
                scale (1,3) single
                waitForConfirmation logical = true
            end
            success = false;

%             Sets the location, rotation in radians, and scale. If a wall is parented to another actor then the location, rotation, and scale are relative to the parent actor.
% 
%             :param location: An array of floats for x, y and z coordinates in full-scale units. Multiply physical QCar locations by 10 to get full scale locations.
%             :param rotation: An array of floats for the roll, pitch, and yaw in radians
%             :param scale: An array of floats for the scale in the x, y, and z directions.
%             :param waitForConfirmation: (Optional) Wait for confirmation of the operation before proceeding. This makes the method a blocking operation.
%             :type location: float array[3]
%             :type rotation: float array[3]
%             :type scale: float array[3]
%             :type waitForConfirmation: boolean
%             :return: True if successful or False otherwise
%             :rtype: boolean

            if isempty(obj.is_actor_number_valid())
                return
            end

            obj.c.classID = obj.ID_WALL;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_WALLS_SET_TRANSFORM;
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

            if waitForConfirmation
                obj.qlabs.flush_receive();
            end

            if (obj.qlabs.send_container(obj.c))
                if waitForConfirmation
                    rc = obj.qlabs.wait_for_container(obj.ID_WALL, obj.actorNumber, obj.FCN_WALLS_SET_TRANSFORM_ACK);

                    if isempty(rc)
                        return
                    else
                        success = true;
                        return
                    end
                end
                success = true;
                return
            else
                return
            end
        end

        function success = set_transform_degrees(obj, location, rotation, scale, waitForConfirmation)
            arguments
                obj qlabs_walls
                location (1,3) single
                rotation (1,3) single
                scale (1,3) single
                waitForConfirmation logical = true
            end

%             Sets the location, rotation in degrees, and scale. If a wall is parented to another actor then the location, rotation, and scale are relative to the parent actor.
% 
%             :param location: An array of floats for x, y and z coordinates in full-scale units. Multiply physical QCar locations by 10 to get full scale locations.
%             :param rotation: An array of floats for the roll, pitch, and yaw in degrees
%             :param scale: An array of floats for the scale in the x, y, and z directions.
%             :param waitForConfirmation: (Optional) Wait for confirmation of the operation before proceeding. This makes the method a blocking operation.
%             :type location: float array[3]
%             :type rotation: float array[3]
%             :type scale: float array[3]
%             :type waitForConfirmation: boolean
%             :return: True if successful or False otherwise
%             :rtype: boolean

            success = obj.set_transform(location, rotation/180*pi, scale, waitForConfirmation);
        end
    end
end