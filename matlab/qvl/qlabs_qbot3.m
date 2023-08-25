classdef qlabs_qbot3 < qlabs_actor
    properties
        ID_QBOT3 = 22

        FCN_QBOT3_COMMAND_AND_REQUEST_STATE = 10
        FCN_QBOT3_COMMAND_AND_REQUEST_STATE_RESPONSE = 11
        FCN_QBOT3_POSSESS = 20
        FCN_QBOT3_POSSESS_ACK = 21
        FCN_QBOT3_RGB_REQUEST = 100
        FCN_QBOT3_RGB_RESPONSE = 101
        FCN_QBOT3_DEPTH_REQUEST = 110
        FCN_QBOT3_DEPTH_RESPONSE = 111
    
    
        VIEWPOINT_RGB = 0
        VIEWPOINT_DEPTH = 1
        VIEWPOINT_TRAILING = 2  
    end
    methods
        function obj = qlabs_qbot3(qlabs, verbose)
            arguments
                qlabs quanser_interactive_labs
                verbose logical = false
            end
            obj = obj@qlabs_actor(qlabs, verbose);
    
            obj.classID = obj.ID_QBOT3;
        end
        
        function success = possess(obj, camera)
            arguments
                obj qlabs_qbot3
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

            obj.c.classID = obj.ID_QBOT3;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_QBOT3_POSSESS;
            obj.c.payload = uint8(camera);            
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);

            obj.qlabs.flush_receive();

            if (obj.qlabs.send_container(obj.c))
                rc = obj.qlabs.wait_for_container(obj.ID_QBOT3, obj.actorNumber, obj.FCN_QBOT3_POSSESS_ACK);

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

        function [success, location, forward, up, frontHit, leftHit, rightHit, gyro, heading, encoderLeft, encoderRight] = command_and_request_state(obj, rightWheelSpeed, leftWheelSpeed)
            arguments
                obj qlabs_qbot3
                rightWheelSpeed single
                leftWheelSpeed single
            end
            success = false;

%             Sets the velocity, turn angle in radians, and other car properties.
% 
%             :param forward: Speed in m/s of a full-scale car. Multiply physical QCar speeds by 10 to get full scale speeds.
%             :param turn: Turn angle in radians. Positive values turn right.
%     
%             :type actorNumber: float
%             :type turn: float
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

            obj.c.classID = obj.ID_QBOT3;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_QBOT3_COMMAND_AND_REQUEST_STATE;
            obj.c.payload = [flip(typecast(single(rightWheelSpeed), 'uint8')) ...
                             flip(typecast(single(leftWheelSpeed), 'uint8'))];
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

            obj.qlabs.flush_receive();

            if (obj.qlabs.send_container(obj.c))
                rc = obj.qlabs.wait_for_container(obj.ID_QBOT3, obj.actorNumber, obj.FCN_QBOT3_COMMAND_AND_REQUEST_STATE_RESPONSE);

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

        function [success, imageData] = get_image_rgb(obj)
            arguments
                obj qlabs_qbot3
            end
            success = false;
            imageData = [];

%             Request a JPG image from the QBot camera.
% 
%             :return:
%                 - **status** - `True` and image data if successful, `False` and empty otherwise
%                 - **imageData** - Image in a JPG format
%             :rtype: boolean, byte array with jpg data

            if isempty(obj.is_actor_number_valid())
                return
            end

            obj.c.classID = obj.ID_QBOT3;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_QBOT3_RGB_REQUEST;
            obj.c.payload = [];
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);

            obj.qlabs.flush_receive();

            if (obj.qlabs.send_container(obj.c))
                rc = obj.qlabs.wait_for_container(obj.ID_QBOT3, obj.actorNumber, obj.FCN_QBOT3_RGB_RESPONSE);

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

        function [success, imageData] = get_image_depth(obj)
            arguments
                obj qlabs_qbot3
            end
            success = false;
            imageData = [];

%             Request a JPG image from the QBot camera.
% 
%             :return:
%                 - **status** - `True` and image data if successful, `False` and empty otherwise
%                 - **imageData** - Image in a JPG format
%             :rtype: boolean, byte array with jpg data

            if isempty(obj.is_actor_number_valid())
                return
            end

            obj.c.classID = obj.ID_QBOT3;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_QBOT3_DEPTH_REQUEST;
            obj.c.payload = [];
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);

            obj.qlabs.flush_receive();

            if (obj.qlabs.send_container(obj.c))
                rc = obj.qlabs.wait_for_container(obj.ID_QBOT3, obj.actorNumber, obj.FCN_QBOT3_DEPTH_RESPONSE);

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
    end
end