classdef QLabsTrafficLight < QLabsActor
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
        function obj = QLabsTrafficLight(qlabs, verbose)

            arguments
                qlabs QuanserInteractiveLabs
                verbose logical = false
            end            

            obj = obj@QLabsActor(qlabs, verbose);

            obj.classID = obj.ID_TRAFFIC_LIGHT;
        end

        function success = set_state(obj, state, waitForConfirmation)
            arguments
                obj QLabsTrafficLight
                state single
                waitForConfirmation logical = true
            end
%             Set the light state (red/yellow/green) of a traffic light actor

            success = false;

            if (not(obj.is_actor_number_valid()))
               return 
            end
            
            obj.c.classID = obj.ID_TRAFFIC_LIGHT;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_TRAFFIC_LIGHT_SET_STATE;
            obj.c.payload = [uint8(state)];
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);

            
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