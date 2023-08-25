classdef qlabs_roundabout_sign < qlabs_actor
    properties
        ID_ROUNDABOUT_SIGN = 10060;
    end
    methods
        function obj = qlabs_roundabout_sign(qlabs, verbose) 

            arguments
                qlabs quanser_interactive_labs
                verbose logical = false
            end

        
%        function spawn(obj, qlabs, device_num, location, rotation, scale)
%            wait_for_confirmation = false;
%            configuration = 0;
%            
%            qlabs.spawn(device_num, obj.ID_ROUNDABOUT_SIGN, location, rotation, scale, configuration, wait_for_confirmation);
            
            obj = obj@qlabs_actor(qlabs, verbose);

            obj.classID = obj.ID_ROUNDABOUT_SIGN;
        end
    end
end