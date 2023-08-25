classdef qlabs_traffic_cone < qlabs_actor
    properties
        ID_TRAFFIC_CONE = 10000;
    end
    methods
        function obj = qlabs_traffic_cone(qlabs, verbose)

            arguments
                qlabs quanser_interactive_labs
                verbose logical = false
            end

            obj = obj@qlabs_actor(qlabs, verbose);

            obj.classID = obj.ID_TRAFFIC_CONE;



%         function spawn(obj, qlabs, device_num, location, rotation, scale, configuration)
%             wait_for_confirmation = false;
%             
%             qlabs.spawn(device_num, obj.ID_TRAFFIC_CONE, location, rotation, scale, configuration, wait_for_confirmation);
%         end
        end
    end
end