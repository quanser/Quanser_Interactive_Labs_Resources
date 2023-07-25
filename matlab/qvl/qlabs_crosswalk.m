classdef qlabs_crosswalk < handle
    properties
        container_size = 0;
        class_id = 0;        % What device type is this?
        device_number = 0;   % Increment if there are more than one of the same device ID
        device_function = 0; % Command/response
        payload = [];


        ID_CROSSWALK = 10010;
    end
    methods
        
        function spawn(obj, qlabs, device_num, location, rotation, scale, configuration)
            wait_for_confirmation = false;
            
            qlabs.spawn(device_num, obj.ID_CROSSWALK, location, rotation, scale, configuration, wait_for_confirmation);
        end

    end
end