classdef QLabsSRV02 < QLabsActor
    properties (Constant)
        ID_SRV02 = 40;

        FCN_SRV02_COMMAND_AND_REQUEST_STATE = 10
        FCN_SRV02_COMMAND_AND_REQUEST_STATE_RESPONSE = 11
    end

    methods
        function obj = QLabsSRV02(qlabs, verbose)

            arguments
                qlabs QuanserInteractiveLabs
                verbose logical = false
            end

            obj = obj@QLabsActor(qlabs, verbose);

            obj.classID = obj.ID_SRV02;
        end

        %% Commands the SRV02 load angle in radians.
        function success = command_and_request_state(obj, angle, waitForConfirmation)
            arguments
                obj QLabsSRV02
                angle double
                waitForConfirmation logical = true
            end

            success = false;

            if (not(obj.is_actor_number_valid()))
                return
            end

            obj.c.classID = obj.ID_SRV02;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_SRV02_COMMAND_AND_REQUEST_STATE;
            obj.c.payload = [flip(typecast(single(angle), 'uint8')) ...
                             flip(typecast(single(0), 'uint8'))];
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);

            if (waitForConfirmation)
                obj.qlabs.flush_receive()
            end

            if (obj.qlabs.send_container(obj.c))
                if waitForConfirmation
                    rc = obj.qlabs.wait_for_container(obj.ID_SRV02, obj.actorNumber, obj.FCN_SRV02_COMMAND_AND_REQUEST_STATE_RESPONSE);
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

        %% Commands the SRV02 load angle in degrees.
        function success = command_and_request_state_degrees(obj, angle, waitForConfirmation)
            arguments
                obj QLabsSRV02
                angle double
                waitForConfirmation logical = true
            end

            success = obj.command_and_request_state(angle/180*pi, waitForConfirmation);
        end
    end
end
