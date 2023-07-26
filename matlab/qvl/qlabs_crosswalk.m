classdef qlabs_crosswalk < qlabs_actor
    properties
        ID_CROSSWALK = 10010;
    end
    methods
        function obj = qlabs_crosswalk(qlabs, verbose)

            arguments
                qlabs quanser_interactive_labs
                verbose logical = false
            end

            obj = obj@qlabs_actor(qlabs, verbose);

            obj.classID = obj.ID_CROSSWALK;

        end            
            
%    methods        
%        function spawn(obj, qlabs, device_num, location, rotation, scale, configuration)
%            wait_for_confirmation = false;
%            
%            qlabs.spawn(device_num, obj.ID_CROSSWALK, location, rotation, scale, configuration, wait_for_confirmation);
%        end

    end
end