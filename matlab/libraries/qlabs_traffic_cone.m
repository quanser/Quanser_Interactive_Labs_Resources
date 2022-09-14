classdef qlabs_traffic_cone < handle
    properties
        container_size = 0;
        class_id = 0;        % What device type is this?
        device_number = 0;   % Increment if there are more than one of the same device ID
        device_function = 0; % Command/response
        payload = [];


        ID_TRAFFIC_CONE = 10000;
    end
    methods
        
        function spawn(obj, qlabs, device_num, location, rotation, scale, configuration)
            wait_for_confirmation = false;
            
            qlabs.spawn(device_num, obj.ID_TRAFFIC_CONE, location, rotation, scale, configuration, wait_for_confirmation);
        end

    end
end