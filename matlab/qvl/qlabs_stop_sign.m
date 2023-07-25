classdef qlabs_stop_sign < qlabs_actor
    properties
        ID_STOP_SIGN = 10020;
    end
    methods
        function obj = qlabs_stop_sign(qlabs, verbose)

            arguments
                qlabs quanser_interactive_labs
                verbose logical = false
            end            

            obj = obj@qlabs_actor(qlabs, verbose);

            obj.classID = obj.ID_STOP_SIGN;
        end
    end
end