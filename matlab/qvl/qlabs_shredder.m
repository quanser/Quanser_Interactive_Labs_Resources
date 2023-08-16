classdef qlabs_shredder < qlabs_actor
    properties
        ID_SHREDDER = 190

        RED = 0
        GREEN = 1
        BLUE = 2
        WHITE = 3
    end
    methods
        function obj = qlabs_shredder(qlabs, verbose)
            arguments
                qlabs quanser_interactive_labs
                verbose logical = false
            end
            obj = obj@qlabs_actor(qlabs, verbose);
    
            obj.classID = obj.ID_SHREDDER;
        end
    end
end