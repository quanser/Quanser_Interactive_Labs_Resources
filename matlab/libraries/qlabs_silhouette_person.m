classdef qlabs_silhouette_person < handle
    properties
        container_size = 0;
        class_id = 0;        % What device type is this?
        device_number = 0;   % Increment if there are more than one of the same device ID
        device_function = 0; % Command/response
        payload = [];

        ID_SILHOUETTE_PERSON = 10030;
        FCN_SILHOUETTE_PERSON_MOVE_TO = 10;
        FCN_SILHOUETTE_PERSON_MOVE_TO_ACK = 11;
    end
    methods
        
        function spawn(obj, qlabs, device_num, location, rotation, scale, configuration, wait_for_confirmation)
            
            qlabs.spawn(device_num, obj.ID_SILHOUETTE_PERSON, location+[0 0 1], rotation, scale, configuration, wait_for_confirmation);
        end
        
        function c = move_to(obj, qlabs, device_num, target_location, speed, wait_for_confirmation)
            c = comm_modular_container();
            c.class_id = obj.ID_SILHOUETTE_PERSON;
            c.device_number = device_num;
            c.device_function = obj.FCN_SILHOUETTE_PERSON_MOVE_TO;
            %c.payload = bytearray(struct.pack(">ffff", x, y, z, speed))
            
            c.payload = [flip(typecast(single(target_location(1)), 'uint8')) ...
                         flip(typecast(single(target_location(2)), 'uint8')) ...
                         flip(typecast(single(target_location(3)), 'uint8')) ...
                         flip(typecast(single(speed), 'uint8'))];
            
            c.container_size = 10 + length(c.payload);

            if wait_for_confirmation
                qlabs.flush_receive()  
            end

            if (qlabs.send_container(c))
                if wait_for_confirmation
                    c = qlabs.wait_for_container(obj.ID_SILHOUETTE_PERSON, device_num, obj.FCN_SILHOUETTE_PERSON_MOVE_TO_ACK);
                end
            end
        end
    end
end