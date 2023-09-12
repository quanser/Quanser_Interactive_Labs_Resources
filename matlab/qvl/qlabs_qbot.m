classdef qlabs_qbot < qlabs_actor
    properties
        ID_QBOT = 20

        FCN_QBOT_COMMAND_AND_REQUEST_STATE = 10
        FCN_QBOT_COMMAND_AND_REQUEST_STATE_RESPONSE = 11
        FCN_QBOT_POSSESS = 20
        FCN_QBOT_POSSESS_ACK = 21
    
    
        VIEWPOINT_RGB = 0
        VIEWPOINT_DEPTH = 1
        VIEWPOINT_TRAILING = 2
    end
    methods
        function obj = qlabs_qbot(qlabs, verbose)
            arguments 
                qlabs quanser_interactive_labs
                verbose logical = False
            end
            
            obj = obj@qlabs_actor(qlabs, verbose);
    
            obj.classID = obj.ID_QBOT;
        end

        function success = possess(obj, camera)
            arguments
                obj qlabs_qbot
                camera single
            end
            success = false;

            obj.c.classID = obj.ID_QBOT;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_QBOT_POSSESS;
            obj.c.payload = uint8(camera);
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);

            obj.qlabs.flush_receive();

            if (obj.qlabs.send_container(obj.c))
                rc = qlabs.wait_for_container(obj.ID_QBOT, obj.actorNumber, obj.FCN_QBOT_POSSESS_ACK);
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
    end
end