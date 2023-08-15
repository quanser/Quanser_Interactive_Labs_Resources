classdef qlabs_qbot_platform < qlabs_actor
    properties
        %This class is for spawning QBotPlatforms.

        ID_QBOT_PLATFORM = 23
    
        FCN_QBOT_PLATFORM_COMMAND_AND_REQUEST_STATE = 10
        FCN_QBOT_PLATFORM_COMMAND_AND_REQUEST_STATE_RESPONSE = 11
        FCN_QBOT_PLATFORM_POSSESS = 20
        FCN_QBOT_PLATFORM_POSSESS_ACK = 21
        FCN_QBOT_PLATFORM_IMAGE_REQUEST = 100
        FCN_QBOT_PLATFORM_IMAGE_RESPONSE = 101
        FCN_QBOT_PLATFORM_LIDAR_DATA_REQUEST = 120
        FCN_QBOT_PLATFORM_LIDAR_DATA_RESPONSE = 121
        
    
        VIEWPOINT_RGB = 0
        VIEWPOINT_DEPTH = 1
        VIEWPOINT_DOWNWARD = 2
        VIEWPOINT_TRAILING = 3
     
        CAMERA_RGB = 0
        CAMERA_DEPTH = 1
        CAMERA_DOWNWARD = 2
    
        sensor_scaling = 1
    end
    methods
        function obj = qlabs_qbot_platform(qlabs, verbose)
            arguments
                qlabs quanser_interactive_labs
                verbose logical = False
            end
            obj = obj@qlabs_actor(qlabs, verbose);
    
            obj.classID = obj.ID_QBOT_PLATFORM;
        end
        
        function success = possess(obj, camera)
            arguments
                obj qlabs_qbot_platform
                camera single
            end
            success = false;
%             Possess (take control of) a QBot in QLabs with the selected camera.
% 
%             :param camera: Pre-defined camera constant. See CAMERA constants for available options. Default is the trailing camera.
%             :type camera: uint32
%             :return:
%                 - **status** - `True` if possessing the camera was successful, `False` otherwise
%             :rtype: boolean

            obj.c.classID = obj.ID_QBOT_PLATFORM;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_QBOT_PLATFORM_POSSESS;
            obj.c.payload = uint8(camera);            
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);

            obj.qlabs.flush_receive();

            if (obj.qlabs.send_container(obj.c))
                rc = obj.qlabs.wait_for_container(obj.ID_QBOT_PLATFORM, obj.actorNumber, obj.FCN_QBOT_PLATFORM_POSSESS_ACK);
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

        function [success, location, forward, up, frontHit, leftHit, rightHit, gyro, heading, encoderLeft, encoderRight] = command_and_request_state(obj, rightWheelSpeed, leftWheelSpeed, leftLED, rightLED)
            arguments
                obj qlabs_qbot_platform
                rightWheelSpeed single
                leftWheelSpeed single
                leftLED (1,3) single = [1 0 0]
                rightLED (1,3) single = [1 0 0]
            end
            success = false;
%             Sets the velocity, turn angle in radians, and other car properties.
% 
%             :param forward: Speed in m/s of a full-scale car. Multiply physical QCar speeds by 10 to get full scale speeds.
%             :param turn: Turn angle in radians. Positive values turn right.
%             :param leftLED: Red, Green, Blue components of the RGB color on a 0.0 to 1.0 scale.
%             :param rightLED: Red, Green, Blue components of the RGB color on a 0.0 to 1.0 scale.
%             
%     
%             :type actorNumber: float
%             :type turn: float
%             :type leftLED: float array[3]
%             :type rightLED: float array[3]
%     
%             :return:
%                 - **status** - `True` if successful, `False` otherwise
%                 - **location** - world location in m
%                 - **forward vector** - unit scale vector
%                 - **up vector** - unit scale vector
%                 - **front bumper hit** - true if in contact with a collision object, False otherwise
%                 - **left bumper hit** - true if in contact with a collision object, False otherwise
%                 - **right bumper hit** - true if in contact with a collision object, False otherwise
%                 - **gyro** - turn rate in rad/s
%                 - **heading** - angle in rad
%                 - **encoder left** - in counts
%                 - **encoder right** - in counts
%     
%             :rtype: boolean, float array[3], float array[3], float array[3], boolean, boolean, boolean, float, float, uint32, uint32

            obj.c.classID = obj.ID_QBOT_PLATFORM;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_QBOT_PLATFORM_COMMAND_AND_REQUEST_STATE;
            obj.c.payload = [flip(typecast(single(rightWheelSpeed), 'uint8')) ...
                             flip(typecast(single(leftWheelSpeed), 'uint8')) ...
                             flip(typecast(single(leftLED(1)), 'uint8')) ...
                             flip(typecast(single(leftLED(2)), 'uint8')) ...
                             flip(typecast(single(leftLED(3)), 'uint8')) ...
                             flip(typecast(single(rightLED(1)), 'uint8')) ...
                             flip(typecast(single(rightLED(2)), 'uint8')) ...
                             flip(typecast(single(rightLED(3)), 'uint8'))];
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);

            location = [0,0,0];
            forward = [0,0,0];
            up = [0,0,0];
            frontHit = false;
            leftHit = false;
            rightHit = false;
            gyro = 0;
            heading = 0;
            encoderLeft = 0;
            encoderRight = 0;

            obj.qlabs.flush_receive()

            if (obj.qlabs.send_container(obj.c))
                rc = obj.qlabs.wait_for_container(obj.ID_QBOT_PLATFORM, obj.actorNumber, obj.FCN_QBOT_PLATFORM_COMMAND_AND_REQUEST_STATE_RESPONSE);

                if isempty(rc)
                    return
                end

                if length(obj.c.payload) == 55
                    [typecast(flip(single(location(1)), 'uint8')) ...
                     typecast(flip(single(location(2)), 'uint8')) ...
                     typecast(flip(single(location(3)), 'uint8')) ...
                     typecast(flip(single(forward(1)), 'uint8')) ...
                     typecast(flip(single(forward(2)), 'uint8')) ...
                     typecast(flip(single(forward(3)), 'uint8')) ...
                     typecast(flip(single(up(1)), 'uint8')) ...
                     typecast(flip(single(up(2)), 'uint8')) ...
                     typecast(flip(single(up(3)), 'uint8')) ...
                     typecast(flip(single(frontHit), 'logical')) ...
                     typecast(flip(single(leftHit), 'logical')) ...
                     typecast(flip(single(rightHit), 'logical')) ...
                     typecast(flip(single(gyro), 'uint8')) ...
                     typecast(flip(single(heading), 'uint8')) ...
                     typecast(flip(single(encoderLeft), 'uint8')) ...
                     typecast(flip(single(encoderRight), 'uint8'))];
                    
                    success = true;
                    return
                else
                    return
                end
            else
                return
            end
        end

        function [success, imageData] = get_image(obj, camera)
            arguments
                obj qlabs_qbot_platform
                camera single
            end
            success = false;
            imageData = [];
%             Request a JPG image from the QBot camera.
% 
%             :param camera: Camera number to view from.
%             
%             :type camera: byte
%     
%             :return:
%                 - **status** - `True` and image data if successful, `False` and empty otherwise
%                 - **imageData** - Image in a JPG format
%             :rtype: boolean, byte array with jpg data

            if isempty(obj.is_actor_number_valid())
                return
            end

            obj.c.classID = self.ID_QBOT_PLATFORM;
            obj.c.actorNumber = self.actorNumber;
            obj.c.actorFunction = self.FCN_QBOT_PLATFORM_IMAGE_REQUEST;
            obj.c.payload = uint8(camera);
            obj.c.containerSize = c.BASE_CONTAINER_SIZE + length(obj.c.payload);

            obj.qlabs.flush_receive();

            if (obj.qlabs.send_container(obj.c))
                rc = obj.qlabs.wait_for_container(obj.ID_QBOT_PLATFORM, obj.actorNumber, obj.FCN_QBOT_PLATFORM_IMAGE_RESPONSE);

                if isempty(rc)
                    return
                end

                [imageData, result] = qc_jpeg_decompress(rc.payload(5:end));
                
                success = true;
                return
                
            else
                return
            end
        end

        function [success, angle, distances] = get_lidar(obj, samplePoints)
            arguments
                obj qlabs_qbot_platform
                samplePoints single = 400
            end
            success = false;
            angle = [];
            distances = [];
%             Request LIDAR data from a QbotPlatform.
% 
%             :param samplePoints: (Optional) Change the number of points per revolution of the LIDAR.
%             :type samplePoints: uint32
%             :return: `True`, angles in radians, and distances in m if successful, `False`, none, and none otherwise
%             :rtype: boolean, float array, float array
            
            if isempty(obj.is_actor_number_valid())
                if (obj.verbose)
                    fprintf('actorNumber object variable empty. Use a spawn function to assign an actor or manually assign the actorNumber variable.')
                end
                return
            end

            LIDAR_SAMPLES = 4096;
            LIDAR_RANGE = 80*obj.sensor_scaling;

            % The LIDAR is simulated by using 4 orthogonal virtual cameras that are 1 pixel high. The
            % lens distortion of these cameras must be removed to accurately calculate the XY position
            % of the depth samples.

            quarter_angle = linspace(0, 45, int(LIDAR_SAMPLES/8));
            lens_curve = -0.0077*quarter_angle*quarter_angle + 1.3506*quarter_angle;
            lens_curve_rad = lens_curve/180*pi;

            angles = [pi*4/2-1*flip(lens_curve_rad) ...
                       lens_curve_rad ...
                       (pi/2 - 1*flip(lens_curve_rad)) ...
                       (pi/2 + lens_curve_rad) ...
                       (pi - 1*flip(lens_curve_rad)) ...
                       (pi + lens_curve_rad) ...
                       (pi*3/2 - 1*flip(lens_curve_rad)) ...
                       (pi*3/2 + lens_curve_rad)];

            obj.c.classID = obj.ID_QBOT_PLATFORM;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_QBOT_PLATFORM_LIDAR_DATA_REQUEST;
            obj.c.payload = uint8;
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);

            obj.qlabs.flush_receive();

            if (obj.qlabs.send_container(obj.c))
                rc = self.qlabs.wait_for_container(obj.ID_QBOT_PLATFORM, obj.actorNumber, obj.FCN_QBOT_PLATFORM_LIDAR_DATA_RESPONSE);

                if isempty(rc)
                    if (obj.verbose)
                        fprintf('Failed to receive return container.')
                    end
                    return
                end

                if ((length(obj.c.payload)-4)/2 ~= LIDAR_SAMPLES)
                    if (obj.verbose)
                        fprintf('Received %u bytes, expected %u', length(obj.payload), LIDAR_SAMPLES*2)
                    end
                    return
                end

                distance = linspace(0,0,LIDAR_SAMPLES);

                for count = LIDAR_SAMPLES-1
                    % clamp any value at 65535 to 0
                    raw_value = mod(((obj.c.payload(4+count*2) * 256 + obj.c.payload(5+count*2))), 65535);

                    % scale to LIDAR range
                    distance(count) = (raw_value/65535)*LIDAR_RANGE;
                end

                % Resample the data using a linear radial distribution to the desired number of points
                % and realign the first index to be 0 (forward)
                sampled_angles = linspace(0, 2*pi, num = samplePoints, endpoint = false);
                sampled_distance = linspace(0, 0, samplePoints);

                index_raw = 512;
                for count = samplePoints
                    while (angles(index_raw) < sampled_angles(count))
                        index_raw = mod((index_raw + 1), 4096);
                    end

                    if index_raw ~= 0
                        if (angles(index_raw)-angles(index_raw-1)) == 0
                            sampled_distance(count) = distance(index_raw);
                        else
                            sampled_distance(count) = (distance(index_raw)-distance(index_raw-1))*(sampled_angles(count)-angles(index_raw-1))/(angles(index_raw)-angles(index_raw-1)) + distance(index_raw-1);
                        end

                    else
                        sampled_distance(count) = distance(index_raw);
                    end
                end

                success = true;
                angle = sampled_angles;
                distances = distance;
                return
            else
                if (obj.verbose)
                    fprintf('Communications request for LIDAR data failed.')
                end
                return
            end
        end
    end
end