classdef qlabs_stop_sign < handle
    properties
        container_size = 0;
        class_id = 0;        % What device type is this?
        device_number = 0;   % Increment if there are more than one of the same device ID
        device_function = 0; % Command/response
        payload = [];


        ID_STOP_SIGN = 10020;
    end
    methods
        
        function status = spawn_id(obj, qlabs, actor_number, location, rotation, scale, wait_for_confirmation)
            if nargin == 6
                wait_for_confirmation = true;
            end     
                        
            configuration = 0;
            
            status = qlabs_common_spawn_id(qlabs, actor_number, obj.ID_STOP_SIGN, location, rotation, scale, configuration, wait_for_confirmation);
        end
		
		function [status, actor_number] = spawn(obj, qlabs, location, rotation, scale, wait_for_confirmation)
            if nargin == 5
                wait_for_confirmation = true;
            end     
                        
            configuration = 0;
            
            [status, actor_number] = qlabs_common_spawn(qlabs, obj.ID_STOP_SIGN, location, rotation, scale, configuration, wait_for_confirmation);
        end

    end
end