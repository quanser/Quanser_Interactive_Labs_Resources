classdef qlab_free_camera < handle
    properties
        container_size = 0;
        class_id = 0;        % What device type is this?
        device_number = 0;   % Increment if there are more than one of the same device ID
        device_function = 0; % Command/response
        payload = [];

        ID_FREE_CAMERA = 170;
        FCN_FREE_CAMERA_POSSESS = 10;
        FCN_FREE_CAMERA_POSSESS_ACK = 11;
        FCN_FREE_CAMERA_SET_CAMERA_FEATURES = 12;
        FCN_FREE_CAMERA_SET_CAMERA_FEATURES_ACK = 13;
    end
    methods
        
        function spawn(obj, qlabs, device_num, location, rotation, wait_for_confirmation)
            
            scale = [1 1 1];
            configuration = 0;
            
            qlabs.spawn(device_num, obj.ID_FREE_CAMERA, location, rotation, scale, configuration, wait_for_confirmation);
        end
        
        function success = possess(obj, qlabs, device_num)
            success = false;
            c = comm_modular_container();
            c.class_id = obj.ID_FREE_CAMERA;
            c.device_number = device_num;
            c.device_function = obj.FCN_FREE_CAMERA_POSSESS;
            c.payload = [];
            c.container_size = 10 + length(c.payload);

            qlabs.flush_receive()  

            if (qlabs.send_container(c))
                qlabs.wait_for_container(obj.ID_FREE_CAMERA, device_num, obj.FCN_FREE_CAMERA_POSSESS_ACK);
                success = true;
            end
        end
        
    end
end