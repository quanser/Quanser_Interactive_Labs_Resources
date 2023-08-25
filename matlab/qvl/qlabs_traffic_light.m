classdef qlabs_traffic_light < qlabs_actor
    properties
        ID_TRAFFIC_LIGHT = 10051;

        FCN_TRAFFIC_LIGHT_SET_STATE = 10
        FCN_TRAFFIC_LIGHT_SET_STATE_ACK = 11

        STATE_RED = 0
        %State constant for red light
        STATE_GREEN = 1
        %State constant for green light
        STATE_YELLOW = 2
        %State constant for yellow light
    end
    methods
        function obj = qlabs_traffic_light(qlabs, verbose)

            arguments
                qlabs quanser_interactive_labs
                verbose logical = false
            end            

            obj = obj@qlabs_actor(qlabs, verbose);

            obj.classID = obj.ID_TRAFFIC_LIGHT;
        end

        function success = set_state(obj, state, waitForConfirmation)
%             Set the light state (red/yellow/green) of a traffic light actor
% 
%             :param state: An integer constant corresponding to a light state (see class constants)
%             :param waitForConfirmation: (Optional) Wait for confirmation of the state change before proceeding. This makes the method a blocking operation.
%             :type state: uint32
%             :type waitForConfirmation: boolean
%             :return: `True` if successful, `False` otherwise
%             :rtype: boolean

            success = false;

            if (not(obj.is_actor_number_valid()))
               return 
            end
            
            obj.c.classID = obj.ID_TRAFFIC_LIGHT;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_TRAFFIC_LIGHT_SET_STATE;
            obj.c.payload = [uint8(state)];
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);

%             if waitForConfirmation
%                 self.qlabs._flush_receive()
            
            if (obj.qlabs.send_container(obj.c))
                if waitForConfirmation
                    rc = obj.qlabs.wait_for_container(obj.ID_TRAFFIC_LIGHT, obj.actorNumber, obj.FCN_TRAFFIC_LIGHT_SET_STATE_ACK);
                    if isempty(rc)
                        if (obj.verbose == true)
                            fprintf('Timeout waiting for response.\n')
                        end
                    end
                end

                success = true;
            end

        end
    end
end