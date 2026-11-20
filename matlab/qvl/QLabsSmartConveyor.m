classdef QLabsSmartConveyor < QLabsActor
    properties (Constant)
        ID_SMART_CONVEYOR = 260;

        FCN_SMART_CONVEYOR_SET_SPEED = 10
        FCN_SMART_CONVEYOR_SET_SPEED_ACK = 11
        FCN_SMART_CONVEYOR_SET_LED_MODE_AND_COLOR = 12
        FCN_SMART_CONVEYOR_SET_LED_MODE_AND_COLOR_ACK = 13
        FCN_SMART_CONVEYOR_SET_INDIVIDUAL_LED_COLORS = 14
        FCN_SMART_CONVEYOR_SET_INDIVIDUAL_LED_COLORS_ACK = 15

        LED_MODE_CUSTOM = 0
        % LEDs use the colors set with set_individual_led_colors
        LED_MODE_SOLID = 1
        % All LEDs show a single color
        LED_MODE_BIG_ANT = 2
        LED_MODE_LITTLE_ANT = 3
        LED_MODE_RAINBOW = 4

        NUM_LEDS = 100
        % Number of individually addressable LEDs
    end

    methods
        function obj = QLabsSmartConveyor(qlabs, verbose)

            arguments
                qlabs QuanserInteractiveLabs
                verbose logical = false
            end

            obj = obj@QLabsActor(qlabs, verbose);

            obj.classID = obj.ID_SMART_CONVEYOR;
        end

        %% Sets the belt speed.
        function success = set_speed(obj, speed, waitForConfirmation)
            arguments
                obj QLabsSmartConveyor
                speed double
                waitForConfirmation logical = true
            end

            payload = flip(typecast(single(speed), 'uint8'));
            success = obj.send_command(obj.FCN_SMART_CONVEYOR_SET_SPEED, obj.FCN_SMART_CONVEYOR_SET_SPEED_ACK, payload, waitForConfirmation);
        end

        %% Sets the LED mode and the color used by that mode.
        function success = set_led_mode_and_color(obj, mode, color, waitForConfirmation)
            arguments
                obj QLabsSmartConveyor
                mode int32
                color (1,3) double
                waitForConfirmation logical = true
            end

            payload = [flip(typecast(int32(mode), 'uint8')) ...
                       flip(typecast(single(color(1)), 'uint8')) ...
                       flip(typecast(single(color(2)), 'uint8')) ...
                       flip(typecast(single(color(3)), 'uint8'))];
            success = obj.send_command(obj.FCN_SMART_CONVEYOR_SET_LED_MODE_AND_COLOR, obj.FCN_SMART_CONVEYOR_SET_LED_MODE_AND_COLOR_ACK, payload, waitForConfirmation);
        end

        %% Sets the color of each LED. colors is a 3 x 100 matrix with one
        %  [r; g; b] column per LED. Use LED_MODE_CUSTOM to display them.
        function success = set_individual_led_colors(obj, colors, waitForConfirmation)
            arguments
                obj QLabsSmartConveyor
                colors (3,100) double
                waitForConfirmation logical = true
            end

            % Column-major order gives r, g, b for LED 1, then LED 2, and so on.
            payload = reshape(flip(reshape(typecast(single(colors(:)'), 'uint8'), 4, []), 1), 1, []);
            success = obj.send_command(obj.FCN_SMART_CONVEYOR_SET_INDIVIDUAL_LED_COLORS, obj.FCN_SMART_CONVEYOR_SET_INDIVIDUAL_LED_COLORS_ACK, payload, waitForConfirmation);
        end
    end

    methods (Access = private)
        function success = send_command(obj, actorFunction, ackFunction, payload, waitForConfirmation)
            success = false;

            if (not(obj.is_actor_number_valid()))
                return
            end

            obj.c.classID = obj.ID_SMART_CONVEYOR;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = actorFunction;
            obj.c.payload = payload;
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);

            if (waitForConfirmation)
                obj.qlabs.flush_receive()
            end

            if (obj.qlabs.send_container(obj.c))
                if waitForConfirmation
                    rc = obj.qlabs.wait_for_container(obj.ID_SMART_CONVEYOR, obj.actorNumber, ackFunction);
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
    end
end
