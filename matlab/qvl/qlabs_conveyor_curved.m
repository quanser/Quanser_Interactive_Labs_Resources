classdef qlabs_conveyor_curved < qlabs_actor
    properties
        ID_CONVEYOR_CURVED = 211

        FCN_CONVEYOR_CURVED_SET_SPEED = 10
        FCN_CONVEYOR_CURVED_SET_SPEED_ACK = 11
    end
    methods
        function obj = qlabs_conveyor_curved(qlabs, verbose)
            arguments
                qlabs quanser_interactive_labs
                verbose logical = false
            end
            obj = obj@qlabs_actor(qlabs, verbose);
    
            obj.classID = obj.ID_CONVEYOR_CURVED;
        end

        function success = set_speed(obj, speed)
            arguments
                obj qlabs_conveyor_curved
                speed single
            end
            success = false;

            obj.c.classID = obj.ID_CONVEYOR_CURVED;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_CONVEYOR_CURVED_SET_SPEED;
            obj.c.payload = flip(typecast(single(speed), 'uint8'));
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);

            obj.qlabs.flush_receive();

            if (obj.qlabs.send_container(obj.c))
                rc = obj.qlabs.wait_for_container(obj.ID_CONVEYOR_CURVED, obj.actorNumber, obj.FCN_CONVEYOR_CURVED_SET_SPEED_ACK);

                success = true;
                return
            else
                return
            end
        end
    end
end