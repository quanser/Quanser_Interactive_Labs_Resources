classdef qlab_stop_sign < handle
    properties
        container_size = 0;
        class_id = 0;        % What device type is this?
        device_number = 0;   % Increment if there are more than one of the same device ID
        device_function = 0; % Command/response
        payload = [];


        ID_STOP_SIGN = 10020;
    end
    methods
        
        function spawn(obj, qlabs, device_num, location, rotation, scale)
            wait_for_confirmation = false;
            configuration = 0;
            
            qlabs.spawn(device_num, obj.ID_STOP_SIGN, location, rotation, scale, configuration, wait_for_confirmation);
        end

    end
end