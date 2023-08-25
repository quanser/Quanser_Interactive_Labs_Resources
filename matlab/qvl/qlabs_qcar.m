classdef qlabs_qcar < qlabs_actor
    properties
%         This class is for spawning QCars.

        ID_QCAR = 160
%         Class ID
        FCN_QCAR_SET_VELOCITY_AND_REQUEST_STATE = 10
        FCN_QCAR_VELOCITY_STATE_RESPONSE = 11
        FCN_QCAR_SET_TRANSFORM_AND_REQUEST_STATE = 12
        FCN_QCAR_TRANSFORM_STATE_RESPONSE = 13
        FCN_QCAR_POSSESS = 20
        FCN_QCAR_POSSESS_ACK = 21
        FCN_QCAR_GHOST_MODE = 22
        FCN_QCAR_GHOST_MODE_ACK = 23
        FCN_QCAR_CAMERA_DATA_REQUEST = 100
        FCN_QCAR_CAMERA_DATA_RESPONSE = 101
        FCN_QCAR_LIDAR_DATA_REQUEST = 110
        FCN_QCAR_LIDAR_DATA_RESPONSE = 111
    
    
        CAMERA_CSI_RIGHT = 0
%         Image capture resolution: 820x410
        CAMERA_CSI_BACK = 1
%         Image capture resolution: 820x410
        CAMERA_CSI_LEFT = 2
%         Image capture resolution: 820x410
        CAMERA_CSI_FRONT = 3
%         Image capture resolution: 820x410
        CAMERA_RGB = 4
%         Image capture resolution: 640x480
        CAMERA_DEPTH = 5
%         Image capture resolution: 640x480
        CAMERA_OVERHEAD = 6
%         Note: The mouse scroll wheel can be used to zoom in and out in this mode.
        CAMERA_TRAILING = 7
%         Note: The mouse scroll wheel can be used to zoom in and out in this mode.
    
        sensor_scaling = 1

    end

    methods
        
        function obj = qlabs_qcar(qlabs, verbose)
            arguments
                qlabs quanser_interactive_labs
                verbose logical = false
            end
            obj = obj@qlabs_actor(qlabs, verbose);

            obj.classID = obj.ID_QCAR;
        end

        function success = spawn_id(obj, actorNumber, location, rotation, scale, configuration, waitForConfirmation)
            arguments
                obj qlabs_qcar
                actorNumber single
                location (1,3) single = [0 0 0]
                rotation (1,3) single = [0 0 0]
                scale (1,3) single = [1 1 1]
                configuration single = 0
                waitForConfirmation logical = true
            end
            
%             Spawns a new QCar actor.
% 
%             :param actorNumber: User defined unique identifier for the class actor in QLabs
%             :param location: (Optional) An array of floats for x, y and z coordinates
%             :param rotation: (Optional) An array of floats for the roll, pitch, and yaw in radians
%             :param scale: (Optional) An array of floats for the scale in the x, y, and z directions. Scale values of 0.0 should not be used and only uniform scaling is recommended. Sensor scaling will be based on scale[0].
%             :param configuration: (Optional) Spawn configuration. See class library for configuration options.
%             :param waitForConfirmation: (Optional) Make this operation blocking until confirmation of the spawn has occurred.
%             :type actorNumber: uint32
%             :type location: float array[3]
%             :type rotation: float array[3]
%             :type scale: float array[3]
%             :type configuration: uint32
%             :type waitForConfirmation: boolean
%             :return:
%                 - **status** - 0 if successful, 1 class not available, 2 actor number not available or already in use, 3 unknown error, -1 communications error
%             :rtype: int32

            obj.sensor_scaling = double(scale(1));
            success = spawn_id@qlabs_actor(obj, actorNumber, location, rotation, scale, configuration, waitForConfirmation);
            return
        end

        function success = spawn_id_degrees(obj, actorNumber, location, rotation, scale, configuration, waitForConfirmation)
            arguments
                obj qlabs_qcar
                actorNumber single
                location (1,3) single = [0 0 0]
                rotation (1,3) single = [0 0 0]
                scale (1,3) single = [1 1 1]
                configuration single = 0
                waitForConfirmation logical = true
            end

%             Spawns a new QCar actor.
% 
%             :param actorNumber: User defined unique identifier for the class actor in QLabs
%             :param location: (Optional) An array of floats for x, y and z coordinates
%             :param rotation: (Optional) An array of floats for the roll, pitch, and yaw in radians
%             :param scale: (Optional) An array of floats for the scale in the x, y, and z directions. Scale values of 0.0 should not be used and only uniform scaling is recommended. Sensor scaling will be based on scale[0].
%             :param configuration: (Optional) Spawn configuration. See class library for configuration options.
%             :param waitForConfirmation: (Optional) Make this operation blocking until confirmation of the spawn has occurred.
%             :type actorNumber: uint32
%             :type location: float array[3]
%             :type rotation: float array[3]
%             :type scale: float array[3]
%             :type configuration: uint32
%             :type waitForConfirmation: boolean
%             :return:
%                 - **status** - 0 if successful, 1 class not available, 2 actor number not available or already in use, 3 unknown error, -1 communications error
%             :rtype: int32

            obj.sensor_scaling = double(scale(1));
            success = spawn_id_degrees@qlabs_actor(obj, actorNumber, location, rotation, scale, configuration, waitForConfirmation);
            return
        end

        function success = spawn(obj, location, rotation, scale, configuration, waitForConfirmation)
            arguments
                obj qlabs_qcar
                location (1,3) single = [0 0 0]
                rotation (1,3) single = [0 0 0]
                scale (1,3) single = [1 1 1]
                configuration single = 0
                waitForConfirmation logical = true
            end

%             Spawns a new QCar actor with the next available actor number within this class.
% 
%             :param location: (Optional) An array of floats for x, y and z coordinates
%             :param rotation: (Optional) An array of floats for the roll, pitch, and yaw in radians
%             :param scale: (Optional) An array of floats for the scale in the x, y, and z directions. Scale values of 0.0 should not be used and only uniform scaling is recommended. Sensor scaling will be based on scale[0].
%             :param configuration: (Optional) Spawn configuration. See class library for configuration options.
%             :param waitForConfirmation: (Optional) Make this operation blocking until confirmation of the spawn has occurred. Note that if this is False, the returned actor number will be invalid.
%             :type location: float array[3]
%             :type rotation: float array[3]
%             :type scale: float array[3]
%             :type configuration: uint32
%             :type waitForConfirmation: boolean
%             :return:
%                 - **status** - 0 if successful, 1 class not available, 3 unknown error, -1 communications error.
%                 - **actorNumber** - An actor number to use for future references.
%             :rtype: int32, int32

            obj.sensor_scaling = double(scale(1));
            success = spawn@qlabs_actor(obj, location, rotation, scale, configuration, waitForConfirmation);
            return
        end

        function success = spawn_degrees(obj, location, rotation, scale, configuration, waitForConfirmation)
            arguments
                obj qlabs_qcar
                location (1,3) single = [0 0 0]
                rotation (1,3) single = [0 0 0]
                scale (1,3) single = [1 1 1]
                configuration single = 0
                waitForConfirmation logical = true
            end

%             Spawns a new QCar actor with the next available actor number within this class.
% 
%             :param location: (Optional) An array of floats for x, y and z coordinates
%             :param rotation: (Optional) An array of floats for the roll, pitch, and yaw in degrees
%             :param scale: (Optional) An array of floats for the scale in the x, y, and z directions. Scale values of 0.0 should not be used and only uniform scaling is recommended. Sensor scaling will be based on scale[0].
%             :param configuration: (Optional) Spawn configuration. See class library for configuration options.
%             :param waitForConfirmation: (Optional) Make this operation blocking until confirmation of the spawn has occurred. Note that if this is False, the returned actor number will be invalid.
%             :type location: float array[3]
%             :type rotation: float array[3]
%             :type scale: float array[3]
%             :type configuration: uint32
%             :type waitForConfirmation: boolean
%             :return:
%                 - **status** - 0 if successful, 1 class not available, 3 unknown error, -1 communications error.
%                 - **actorNumber** - An actor number to use for future references.
%             :rtype: int32, int32

            obj.sensor_scaling = double(scale(1));
            success = spawn_degrees@qlabs_actor(obj, location, rotation, scale, configuration, waitForConfirmation);
            return
        end

        function success = spawn_id_and_parent_with_relative_transform(obj, actorNumber, location, rotation, scale, configuration, parentClassID, parentActorNumber, parentComponent, waitForConfirmation)
            arguments
                obj qlabs_qcar
                actorNumber single
                location (1,3) single = [0 0 0]
                rotation (1,3) single = [0 0 0]
                scale (1,3) single = [1 1 1]
                configuration single = 0
                parentClassID single = 0
                parentActorNumber single = 0
                parentComponent single = 0
                waitForConfirmation logical = true
            end

%             Spawns a new QCar actor relative to an existing actor and creates a kinematic relationship.
% 
%             :param actorNumber: User defined unique identifier for the class actor in QLabs
%             :param location: (Optional) An array of floats for x, y and z coordinates
%             :param rotation: (Optional) An array of floats for the roll, pitch, and yaw in radians
%             :param scale: (Optional) An array of floats for the scale in the x, y, and z directions. Scale values of 0.0 should not be used and only uniform scaling is recommended. Sensor scaling will be based on scale[0].
%             :param configuration: (Optional) Spawn configuration. See class library for configuration options.
%             :param parentClassID: See the ID variables in the respective library classes for the class identifier
%             :param parentActorNumber: User defined unique identifier for the class actor in QLabs
%             :param parentComponent: `0` for the origin of the parent actor, see the parent class for additional reference frame options
%             :param waitForConfirmation: (Optional) Make this operation blocking until confirmation of the spawn has occurred.
%             :type actorNumber: uint32
%             :type location: float array[3]
%             :type rotation: float array[3]
%             :type scale: float array[3]
%             :type configuration: uint32
%             :type parentClassID: uint32
%             :type parentActorNumber: uint32
%             :type parentComponent: uint32
%             :type waitForConfirmation: boolean
%             :return:
%                 - **status** - 0 if successful, 1 class not available, 2 actor number not available or already in use, 3 cannot find the parent actor, 4 unknown error, -1 communications error
%             :rtype: int32

            obj.sensor_scaling = double(scale(1));
            success = spawn_id_and_parent_with_relative_transform(actorNumber, location, rotation, scale, configuration, parentClassID, parentActorNumber, parentComponent, waitForConfirmation);
            return
        end

        function success = spawn_id_and_parent_with_relative_degrees(obj, actorNumber, location, rotation, scale, configuration, parentClassID, parentActorNumber, parentComponent, waitForConfirmation)
            arguments
                obj qlabs_qcar
                actorNumber single
                location (1,3) single = [0 0 0]
                rotation (1,3) single = [0 0 0]
                scale (1,3) single = [1 1 1]
                configuration single = 0
                parentClassID single = 0
                parentActorNumber single = 0
                parentComponent = 0
                waitForConfirmation logical = true
            end

%             Spawns a new QCar actor relative to an existing actor and creates a kinematic relationship.
% 
%             :param actorNumber: User defined unique identifier for the class actor in QLabs
%             :param location: (Optional) An array of floats for x, y and z coordinates
%             :param rotation: (Optional) An array of floats for the roll, pitch, and yaw in degrees
%             :param scale: (Optional) An array of floats for the scale in the x, y, and z directions. Scale values of 0.0 should not be used and only uniform scaling is recommended. Sensor scaling will be based on scale[0].
%             :param configuration: (Optional) Spawn configuration. See class library for configuration options.
%             :param parentClassID: See the ID variables in the respective library classes for the class identifier
%             :param parentActorNumber: User defined unique identifier for the class actor in QLabs
%             :param parentComponent: `0` for the origin of the parent actor, see the parent class for additional reference frame options
%             :param waitForConfirmation: (Optional) Make this operation blocking until confirmation of the spawn has occurred.
%             :type actorNumber: uint32
%             :type location: float array[3]
%             :type rotation: float array[3]
%             :type scale: float array[3]
%             :type configuration: uint32
%             :type parentClassID: uint32
%             :type parentActorNumber: uint32
%             :type parentComponent: uint32
%             :type waitForConfirmation: boolean
%             :return:
%                 - **status** - 0 if successful, 1 class not available, 2 actor number not available or already in use, 3 cannot find the parent actor, 4 unknown error, -1 communications error
%             :rtype: int32

            obj.sensor_scaling = double(scale(1));
            success = spawn_id_and_parent_with_relative_degrees(actorNumber, location, rotation, scale, configuration, parentClassID, parentActorNumber, parentComponent, waitForConfirmation);
            return
        end

        function [success, location, rotation, forward_vector, up_vector, front_bumper_hit, rear_bumper_hit] = set_transform_and_request_state(obj, location, rotation, enableDynamics, headlights, leftTurnSignal, rightTurnSignal, brakeSignal, reverseSignal, waitForConfirmation)
            arguments
                obj qlabs_qcar
                location (1,3) single
                rotation (1,3) single
                enableDynamics logical
                headlights logical
                leftTurnSignal logical
                rightTurnSignal logical
                brakeSignal logical
                reverseSignal logical
                waitForConfirmation logical = true
            end

%             Sets the location, rotation, and other car properties. Note that setting the location ignores collisions so ensure that the location is free of obstacles that may trap the actor if it is subsequently used in a dynamic mode. This transform can also be used to "playback" previously recorded position data without the need for a full dynamic model.
% 
%             :param location: An array of floats for x, y and z coordinates in full-scale units. Multiply physical QCar locations by 10 to get full scale locations.
%             :param rotation: An array of floats for the roll, pitch, and yaw in radians
%             :param enableDynamics: (default True) Enables or disables gravity for set transform requests.
%             :param headlights: Enable the headlights
%             :param leftTurnSignal: Enable the left turn signal
%             :param rightTurnSignal: Enable the right turn signal
%             :param brakeSignal: Enable the brake lights (does not affect the motion of the vehicle)
%             :param reverseSignal: Play a honking sound
%             :param waitForConfirmation: (Optional) Wait for confirmation of the spawn before proceeding. This makes the method a blocking operation. NOTE: Return data will only be valid if waitForConfirmation is True.
%             :type location: float array[3]
%             :type rotation: float array[3]
%             :type enableDynamics: boolean
%             :type headlights: boolean
%             :type leftTurnSignal: boolean
%             :type rightTurnSignal: boolean
%             :type brakeSignal: boolean
%             :type reverseSignal: boolean
%             :type waitForConfirmation: boolean
%             :return:
%                 - **status** - True if successful or False otherwise
%                 - **location** - in full scale
%                 - **rotation** - in radians
%                 - **forward vector** - unit scale vector
%                 - **up vector** - unit scale vector
%                 - **front bumper hit** - True if in contact with a collision object, False otherwise
%                 - **rear bumper hit** - True if in contact with a collision object, False otherwise
%             :rtype: boolean, float array[3], float array[3], float array[3], float array[3], boolean, boolean

            if isempty(obj.is_actor_number_valid)
                return
            end

            obj.c.classID = obj.ID_QCAR;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_QCAR_SET_TRANSFORM_AND_REQUEST_STATE;
            obj.c.payload = [flip(typecast(single(location(1)), 'uint8')) ...
                             flip(typecast(single(location(2)), 'uint8')) ...
                             flip(typecast(single(location(3)), 'uint8')) ...
                             flip(typecast(single(rotation(1)), 'uint8')) ...
                             flip(typecast(single(rotation(2)), 'uint8')) ...
                             flip(typecast(single(rotation(3)), 'uint8')) ...
                             uint8(enableDynamics) ...
                             uint8(headlights) ...
                             uint8(leftTurnSignal) ...
                             uint8(rightTurnSignal) ...
                             uint8(brakeSignal) ...
                             uint8(reverseSignal)];
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);

            if waitForConfirmation
                obj.qlabs.flush_receive()
            end

            success = false;
            location = [0 0 0];
            rotation = [0 0 0];
            forward_vector = [0 0 0];
            up_vector = [0 0 0];
            front_bumper_hit = false;
            rear_bumper_hit = false;

            if (obj.qlabs.send_container(obj.c))
                if waitForConfirmation
                    rc = obj.qlabs.wait_for_container(obj.ID_QCAR, obj.actorNumber, obj.FCN_QCAR_TRANSFORM_STATE_RESPONSE);

                    if isempty(rc)
                        return
                    end

                    if length(obj.c.payload) == 50
                        location(1) = typecast(flip(rc.payload(1:4)), 'single');
                        location(2) = typecast(flip(rc.payload(5:8)), 'single');
                        location(3) = typecast(flip(rc.payload(9:12)), 'single');
                        rotation(1) = typecast(flip(rc.payload(13:16)), 'single');
                        rotation(2) = typecast(flip(rc.payload(17:20)), 'single');
                        rotation(3) = typecast(flip(rc.payload(21:24)), 'single');
                        forward_vector(1) = typecast(flip(rc.payload(25:28)), 'single');
                        forward_vector(2) = typecast(flip(rc.payload(29:32)), 'single');
                        forward_vector(3) = typecast(flip(rc.payload(33:36)), 'single');
                        up_vector(1) = typecast(flip(rc.payload(37:40)), 'single');
                        up_vector(2) = typecast(flip(rc.payload(41:44)), 'single');
                        up_vector(3) = typecast(flip(rc.payload(45:48)), 'single');
                        front_bumper_hit = typecast(rc.payload(49), 'logical');
                        rear_bumper_hit = typecast(rc.payload(50), 'logical');
                        
                        success = true;
                        return
                    else
                        return
                    end
                else
                    success = true;
                    return
                end
            else
                success = false;
                return
            end
        end

        function [success, location, rotation, forward_vector, up_vector, front_bumper_hit, rear_bumper_hit] = set_transform_and_request_state_degrees(obj, location, rotation, enableDynamics, headlights, leftTurnSignal, rightTurnSignal, brakeSignal, reverseSignal, waitForConfirmation)
            arguments
                obj qlabs_qcar
                location (1,3) single
                rotation (1,3) single
                enableDynamics logical
                headlights logical
                leftTurnSignal logical
                rightTurnSignal logical
                brakeSignal logical
                reverseSignal logical
                waitForConfirmation logical = true
            end

%             Sets the location, rotation, and other car properties. Note that setting the location ignores collisions so ensure that the location is free of obstacles that may trap the actor if it is subsequently used in a dynamic mode. This transform can also be used to "playback" previously recorded position data without the need for a full dynamic model.
% 
%             :param location: An array of floats for x, y and z coordinates in full-scale units. Multiply physical QCar locations by 10 to get full scale locations.
%             :param rotation: An array of floats for the roll, pitch, and yaw in degrees
%             :param enableDynamics: (default True) Enables or disables gravity for set transform requests.
%             :param headlights: Enable the headlights
%             :param leftTurnSignal: Enable the left turn signal
%             :param rightTurnSignal: Enable the right turn signal
%             :param brakeSignal: Enable the brake lights (does not affect the motion of the vehicle)
%             :param reverseSignal: Play a honking sound
%             :param waitForConfirmation: (Optional) Wait for confirmation of the spawn before proceeding. This makes the method a blocking operation. NOTE: Return data will only be valid if waitForConfirmation is True.
%             :type location: float array[3]
%             :type rotation: float array[3]
%             :type enableDynamics: boolean
%             :type headlights: boolean
%             :type leftTurnSignal: boolean
%             :type rightTurnSignal: boolean
%             :type brakeSignal: boolean
%             :type reverseSignal: boolean
%             :type waitForConfirmation: boolean
%             :return:
%                 - **status** - True if successful or False otherwise
%                 - **location** - in full scale
%                 - **rotation** - in radians
%                 - **forward vector** - unit scale vector
%                 - **up vector** - unit scale vector
%                 - **front bumper hit** - True if in contact with a collision object, False otherwise
%                 - **rear bumper hit** - True if in contact with a collision object, False otherwise
%             :rtype: boolean, float array[3], float array[3], float array[3], float array[3], boolean, boolean

            [success, location, rotation, forward_vector, up_vector, front_bumper_hit, rear_bumper_hit] = obj.set_transform_and_request_state(location, rotation/180*pi, enableDynamics, headlights, leftTurnSignal, rightTurnSignal, brakeSignal, reverseSignal, waitForConfirmation);
            return
        end

        function [success, location, rotation, front_bumper_hit, rear_bumper_hit] = set_velocity_and_request_state(obj, forward, turn, headlights, leftTurnSignal, rightTurnSignal, brakeSignal, reverseSignal)
            arguments
                obj qlabs_qcar
                forward single
                turn single
                headlights logical
                leftTurnSignal logical
                rightTurnSignal logical
                brakeSignal logical
                reverseSignal logical
            end

%             Sets the velocity, turn angle in radians, and other car properties.
% 
%             :param forward: Speed in m/s of a full-scale car. Multiply physical QCar speeds by 10 to get full scale speeds.
%             :param turn: Turn angle in radians. Positive values turn right.
%             :param headlights: Enable the headlights
%             :param leftTurnSignal: Enable the left turn signal
%             :param rightTurnSignal: Enable the right turn signal
%             :param brakeSignal: Enable the brake lights (does not affect the motion of the vehicle)
%             :param reverseSignal: Play a honking sound
%             :type actorNumber: float
%             :type turn: float
%             :type enableDynamics: boolean
%             :type headlights: boolean
%             :type leftTurnSignal: boolean
%             :type rightTurnSignal: boolean
%             :type brakeSignal: boolean
%             :type reverseSignal: boolean
%             :return:
%                 - **status** - True if successful, False otherwise
%                 - **location**
%                 - **rotation** - in radians
%                 - **front bumper hit** - True if in contact with a collision object, False otherwise
%                 - **rear bumper hit** - True if in contact with a collision object, False otherwise
%             :rtype: boolean, float array[3], float array[3], boolean, boolean

            if isempty(obj.is_actor_number_valid)
                success = false;
                location = [0 0 0];
                rotation = [0 0 0];
                front_bumper_hit = false;
                rear_bumper_hit = false;

                return
            end

            obj.c.classID = obj.ID_QCAR;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_QCAR_SET_VELOCITY_AND_REQUEST_STATE;
            %c.payload = bytearray(struct.pack(">ffBBBBB", forward, turn, headlights, leftTurnSignal, rightTurnSignal, brakeSignal, reverseSignal))
            obj.c.payload = [flip(typecast(single(forward), 'uint8')) ...
                             flip(typecast(single(turn), 'uint8')) ...
                             uint8(headlights) ...
                             uint8(leftTurnSignal) ...
                             uint8(rightTurnSignal) ...
                             uint8(brakeSignal) ...
                             uint8(reverseSignal)];
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);

            success = false;
            location = [0 0 0];
            rotation = [0 0 0];
            front_bumper_hit = false;
            rear_bumper_hit = false;

            obj.qlabs.flush_receive();

            if (obj.qlabs.send_container(obj.c))
                rc = obj.qlabs.wait_for_container(obj.ID_QCAR, obj.actorNumber, obj.FCN_QCAR_VELOCITY_STATE_RESPONSE);

                if isempty(rc)
                    success = false;
                    return
                end

                if length(obj.c.payload) == 26
                    location(1) = typecast(flip(rc.payload(1:4)), 'single');
                    location(2) = typecast(flip(rc.payload(5:8)), 'single');
                    location(3) = typecast(flip(rc.payload(9:12)), 'single');
                    rotation(1) = typecast(flip(rc.payload(13:16)), 'single');
                    rotation(2) = typecast(flip(rc.payload(17:20)), 'single');
                    rotation(3) = typecast(flip(rc.payload(21:24)), 'single');
                    front_bumper_hit = typecast(rc.payload(25), 'logical');
                    rear_bumper_hit = typecast(rc.payload(26), 'logical');
                    
                    success = true;
                    return
                else
                    return
                end
            else
                return
            end
        end

        function [success, location, rotation, front_bumper_hit, rear_bumper_hit] = set_velocity_and_request_state_degrees(obj, forward, turn, headlights, leftTurnSignal, rightTurnSignal, brakeSignal, reverseSignal)
            arguments
                obj qlabs_qcar
                forward single
                turn single
                headlights logical
                leftTurnSignal logical
                rightTurnSignal logical
                brakeSignal logical
                reverseSignal logical
            end

%             Sets the velocity, turn angle in degrees, and other car properties.
% 
%             :param forward: Speed in m/s of a full-scale car. Multiply physical QCar speeds by 10 to get full scale speeds.
%             :param turn: Turn angle in degrees. Positive values turn right.
%             :param headlights: Enable the headlights
%             :param leftTurnSignal: Enable the left turn signal
%             :param rightTurnSignal: Enable the right turn signal
%             :param brakeSignal: Enable the brake lights (does not affect the motion of the vehicle)
%             :param reverseSignal: Play a honking sound
%             :type turn: float
%             :type enableDynamics: boolean
%             :type headlights: boolean
%             :type leftTurnSignal: boolean
%             :type rightTurnSignal: boolean
%             :type brakeSignal: boolean
%             :type reverseSignal: boolean
%             :return:
%                 - **status** - `True` if successful, `False` otherwise
%                 - **location**
%                 - **rotation** - in radians
%                 - **front bumper hit** - `True` if in contact with a collision object, `False` otherwise
%                 - **rear bumper hit** - `True` if in contact with a collision object, `False` otherwise
%             :rtype: boolean, float array[3], float array[3], boolean, boolean

            [success, location, rotation, front_bumper_hit, rear_bumper_hit] = obj.set_velocity_and_request_state(forward, turn/180*pi, headlights, leftTurnSignal, rightTurnSignal, brakeSignal, reverseSignal);
            return
        end

        function success = possess(obj, camera)
            arguments
                obj qlabs_qcar
                camera uint8 = obj.CAMERA_TRAILING
            end
            success = false;

%             Possess (take control of) a QCar in QLabs with the selected camera.
% 
%             :param camera: Pre-defined camera constant. See CAMERA constants for available options. Default is the trailing camera.
%             :type camera: uint32
%             :return:
%                 - **status** - `True` if possessing the camera was successful, `False` otherwise
%             :rtype: boolean

            if isempty(obj.is_actor_number_valid)
                return
            end

            obj.c.classID = obj.ID_QCAR;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_QCAR_POSSESS;
            %c.payload = bytearray(struct.pack(">B", camera))
            obj.c.payload = [uint8(camera)];
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);

            obj.qlabs.flush_receive();

            if (obj.qlabs.send_container(obj.c))
                rc = obj.qlabs.wait_for_container(obj.ID_QCAR, obj.actorNumber, obj.FCN_QCAR_POSSESS_ACK);

                if isempty(rc)
                    return
                else
                    success = true;
                    return
                end
            else
                return
            end
        end

        function success = ghost_mode(obj, enable, color)
            arguments
                obj qlabs_qcar
                enable logical = true
                color (1,3) single = [0 1 0]
            end
            success = false;

%             Ghost mode changes the selected QCar actor into a transparent colored version. This can be useful as a reference actor or indicating a change in state.
% 
%             :param enable: Set the QCar to the defined transparent color, otherwise revert to the solid color scheme.
%             :param color: Red, Green, Blue components of the RGB color on a 0.0 to 1.0 scale.
%             :type camera: uint32
%             :type enable: boolean
%             :type color: float array[3]
%             :return:
%                 - **status** - `True` if possessing the camera was successful, `False` otherwise
%             :rtype: boolean

            if isempty(obj.is_actor_number_valid)
                return
            end

            obj.c.classID = obj.ID_QCAR;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_QCAR_GHOST_MODE;
            obj.c.payload = [uint8(enable) ...
                             flip(typecast(single(color(1)), 'uint8')) ...
                             flip(typecast(single(color(2)), 'uint8')) ...
                             flip(typecast(single(color(3)), 'uint8'))];
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);

            obj.qlabs.flush_receive();

            if (obj.qlabs.send_container(obj.c))
                rc = obj.qlabs.wait_for_container(obj.ID_QCAR, obj.actorNumber, obj.FCN_QCAR_GHOST_MODE_ACK);

                if isempty(rc)
                    return
                else
                    success = true;
                    return
                end
            else
                return
            end
        end
        
        % FUNCTION GET IMAGE %
        
        % FUNCTION GET LIDAR %
        function [success, sampled_angles, sampled_distance] = get_lidar(obj, samplePoints)
            arguments
                obj qlabs_qcar
                samplePoints single = 400
            end
            success = false;
            sampled_angles = NaN;
            sampled_distance = NaN;

%             Request LIDAR data from a QCar.
% 
%             :param samplePoints: (Optional) Change the number of points per revolution of the LIDAR.
%             :type samplePoints: uint32
%             :return: `True`, angles in radians, and distances in m if successful, `False`, none, and none otherwise
%             :rtype: boolean, float array, float array

            if isempty(obj.is_actor_number_valid)
                fprintf("actor number invalid")
                return
            end

            LIDAR_SAMPLES = 4096;
            LIDAR_RANGE = 80*obj.sensor_scaling;

%             The LIDAR is simulated by using 4 orthogonal virtual cameras that are 1 pixel high. The
%             lens distortion of these cameras must be removed to accurately calculate the XY position
%             of the depth samples.
            quarter_angle = linspace(0, 45, int32(LIDAR_SAMPLES/8));
            lens_curve = -0.0077*quarter_angle.*quarter_angle + 1.3506*quarter_angle;
            lens_curve_rad = lens_curve/180*pi;

            angles = [pi*4/2-1*flip(lens_curve_rad) ...
                      lens_curve_rad ...
                      (pi/2 - 1*flip(lens_curve_rad)) ...
                      (pi/2 + lens_curve_rad) ...
                      (pi - 1*flip(lens_curve_rad)) ...
                      (pi + lens_curve_rad) ...
                      (pi*3/2 - 1*flip(lens_curve_rad)) ...
                      (pi*3/2 + lens_curve_rad)];

            obj.c.classID = obj.ID_QCAR;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_QCAR_LIDAR_DATA_REQUEST;
            obj.c.payload = [];
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);

            obj.qlabs.flush_receive();

            if (obj.qlabs.send_container(obj.c))
                rc = obj.qlabs.wait_for_container(obj.ID_QCAR, obj.actorNumber, obj.FCN_QCAR_LIDAR_DATA_RESPONSE);

                if isempty(rc)
                    fprintf("Empty return container")
                    return
                end

                if ((length(rc.payload)-4)/2 ~= LIDAR_SAMPLES)
                    fprintf("Number of lidar samples incorrect %u", (length(rc.payload)-4)/2)
                    
                    return
                end

                distance = linspace(0, 0, LIDAR_SAMPLES);

                for count = 1:(LIDAR_SAMPLES-1)
                    % clamp any value at 65535 to 0
                    raw_value = mod(((double(rc.payload(5+count*2)) * 256 + double(rc.payload(6+count*2)) )), 65535);
               
                    %scale to LIDAR range
                    distance(count) = (raw_value/65535)*LIDAR_RANGE;
                end


                % Resample the data using a linear radia distribution to the desired number of points 
                % and realign the first index to be 0 (forward)
                
                sampled_angles = linspace(0, 2*pi, samplePoints+1);
                sampled_angles = sampled_angles (1:(end-1));
                sampled_distance = linspace(0, 0, samplePoints);

                index_raw = 513;
                for count = 1:samplePoints
                    while (angles(index_raw) < sampled_angles(count))
                        index_raw = mod((index_raw + 1), 4096)+1;
                    end

                    if (index_raw ~= 0)
                        if (angles(index_raw)-angles(index_raw-1)) == 0
                            sampled_distance(count) = distance(index_raw);
                        else
                            sampled_distance(count) = (distance(index_raw)-distance(index_raw-1))*(sampled_angles(count)-angles(index_raw-1))/(angles(index_raw)-angles(index_raw-1)) + distance(index_raw-1);
                        end
                    else
                        sampled_distance(count) = distance(index_raw);
                    end
                end
                %sampled_distance = sampled_distance;
                %sampled_angles = sampled_angles;
                success = true;
                return
            else
                return
            end
        end
    end
end