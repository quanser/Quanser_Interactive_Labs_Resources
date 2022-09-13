classdef qlab_qcar < handle
    properties
        container_size = 0;
        class_id = 0;        % What device type is this?
        device_number = 0;   % Increment if there are more than one of the same device ID
        device_function = 0; % Command/response
        payload = [];


        ID_QCAR = 160;
        FCN_QCAR_SET_TRANSFORM_AND_REQUEST_STATE = 12;
        FCN_QCAR_STATE_RESPONSE = 13;
    end
    methods
        
        function spawn(obj, qlabs, device_num, location, rotation)
            configuration = 0;
            wait_for_confirmation = false;
            scale = [1 1 1];
            
            qlabs.spawn(device_num, obj.ID_QCAR, location, rotation, scale, configuration, wait_for_confirmation);
        end

    end
end