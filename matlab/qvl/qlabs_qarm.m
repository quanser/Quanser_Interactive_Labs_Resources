classdef qlabs_qarm < qlabs_actor
    properties
        ID_QARM = 10  
    end
    methods
        function obj = qlabs_qarm(qlabs, verbose)
            arguments
                qlabs quanser_interactive_labs
                verbose logical = false
            end
            obj = obj@qlabs_actor(qlabs, verbose);
    
            obj.classID = obj.ID_QARM;
        end
    end
end