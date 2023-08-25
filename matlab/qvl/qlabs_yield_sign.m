classdef qlabs_yield_sign < qlabs_actor
    properties
        ID_YIELD_SIGN = 10070
    end

    methods
        function obj = qlabs_yield_sign(qlabs, verbose)
            arguments
                qlabs quanser_interactive_labs
                verbose logical = false
            end

            obj = obj@qlabs_actor(qlabs, verbose);

            obj.classID = obj.ID_YIELD_SIGN;

            return
        end
    end
end