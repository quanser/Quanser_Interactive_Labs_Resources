classdef QLabsSpeedSign < QLabsActor
    properties
        ID_SPEED_SIGN = 10240

		FCN_SPEED_SIGN_SET_SPEED = 10
		FCN_SPEED_SIGN_SET_SPEED_ACK = 11
    end

    methods
        function obj = QLabsSpeedSign(qlabs, verbose)
            arguments
                qlabs QuanserInteractiveLabs
                verbose logical = false
            end

            obj = obj@QLabsActor(qlabs, verbose);

            obj.classID = obj.ID_SPEED_SIGN;

            return
        end
		
		function success = set_speed(obj, speed, waitForConfirmation)
            arguments
                obj QLabsSpeedSign
                speed uint32
				waitForConfirmation logical = true
            end
            success = false;

			% Set the speed displayed on the sign

            if isempty(obj.is_actor_number_valid)
                return
            end

            obj.c.classID = obj.ID_SPEED_SIGN;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_SPEED_SIGN_SET_SPEED;
            obj.c.payload = flip(typecast(int32(speed), 'uint8'));
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);

            obj.qlabs.flush_receive();

            if (obj.qlabs.send_container(obj.c))
                rc = obj.qlabs.wait_for_container(obj.ID_SPEED_SIGN, obj.actorNumber, obj.FCN_SPEED_SIGN_SET_SPEED_ACK);

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