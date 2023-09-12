classdef qlabs_reference_frame < qlabs_actor
    properties
%         This class supports the spawning of reference frame actors in the QLabs open worlds.

        ID_REFERENCE_FRAME = 10040
%         Class ID
        FCN_REFERENCE_FRAME_SET_TRANSFORM = 10
        FCN_REFERENCE_FRAME_SET_TRANSFORM_ACK = 11
        FCN_REFERENCE_FRAME_SET_ICON_SCALE = 12
        FCN_REFERENCE_FRAME_SET_ICON_SCALE_ACK = 13
    end
    methods
        function obj = qlabs_reference_frame(qlabs, verbose)
            arguments
                qlabs quanser_interactive_labs
                verbose logical = false
            end
            obj = obj@qlabs_actor(qlabs, verbose);
    
            obj.classID = obj.ID_REFERENCE_FRAME;
        end

        function success = set_transform(obj, location, rotation, scale, waitForConfirmation)
            arguments
                obj qlabs_reference_frame
                location (1,3) single
                rotation (1,3) single
                scale (1,3) single
                waitForConfirmation logical = true
            end
            success = false;

%             Change the location, rotation, and scale of a spawned reference frame in radians
% 
%             :param location: An array of floats for x, y and z coordinates
%             :param rotation: An array of floats for the roll, pitch, yaw in radians
%             :param scale: An array of floats for x, y and z coordinates
%             :param waitForConfirmation: (Optional) Make this operation blocking until confirmation of the operation has occurred.
%             :type location: array[3]
%             :type rotation: array[3]
%             :type scale: array[3]
%             :type waitForConfirmation: boolean
%             :return: `True` if spawn was successful, `False` otherwise
%             :rtype: boolean

            if isempty(obj.is_actor_number_valid())
                return
            end

            obj.c.classID = obj.ID_REFERENCE_FRAME;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_REFERENCE_FRAME_SET_TRANSFORM;
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

            obj.qlabs.flush_receive();

            if (obj.qlabs.send_container(obj.c))
                if waitForConfirmation
                    rc = obj.qlabs.wait_for_container(obj.ID_REFERENCE_FRAME, obj.actorNumber, obj.FCN_REFERENCE_FRAME_SET_TRANSFORM_ACK);

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
                obj qlabs_reference_frame
                location (1,3) single
                rotation (1,3) single
                scale (1,3) single
                waitForConfirmation logical = true
            end

%             Change the location and rotation of a spawned reference frame in degrees
% 
%             :param location: An array of floats for x, y and z coordinates
%             :param rotation: An array of floats for the roll, pitch, yaw in degrees
%             :param scale: An array of floats for x, y and z coordinates
%             :param waitForConfirmation: (Optional) Make this operation blocking until confirmation of the operation has occurred.
%             :type location: array[3]
%             :type rotation: array[3]
%             :type scale: array[3]
%             :type waitForConfirmation: boolean
%             :return: `True` if spawn was successful, `False` otherwise
%             :rtype: boolean

            success = obj.set_transform(location, rotation, scale, waitForConfirmation);
            return
        end

        function success = set_icon_scale(obj, scale, waitForConfirmation)
            arguments
                obj qlabs_reference_frame
                scale (1,3) single
                waitForConfirmation logical = true
            end
            success = false;
%             Change the scale of the axis icon only (if a visible configuration was selected) relative to the actor scale. This scale will not affect any child actors.
% 
%             :param scale: An array of floats for x, y and z coordinates
%             :param waitForConfirmation: (Optional) Make this operation blocking until confirmation of the operation has occurred.
%             :type scale: array[3]
%             :type waitForConfirmation: boolean
%             :return: `True` if successful, `False` otherwise
%             :rtype: boolean

            if isempty(obj.is_actor_number_valid())
                return
            end

            obj.c.classID = obj.ID_REFERENCE_FRAME;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_REFERENCE_FRAME_SET_ICON_SCALE;
            obj.c.payload = [flip(typecast(single(scale(1)), 'uint8')) ...
                             flip(typecast(single(scale(2)), 'uint8')) ...
                             flip(typecast(single(scale(3)), 'uint8'))];
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);

            if (obj.qlabs.send_container(obj.c))
                if waitForConfirmation
                    rc = obj.qlabs.wait_for_container(obj.ID_REFERENCE_FRAME, obj.actorNumber, obj.FCN_REFERENCE_FRAME_SET_ICON_SCALE_ACK);

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
    end
end