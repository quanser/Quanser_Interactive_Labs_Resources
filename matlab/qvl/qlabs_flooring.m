classdef qlabs_flooring < qlabs_actor
    properties
%         This class is for spawning static floors.

        ID_FLOORING = 10090
%         Class ID
    
        FLOORING_QCAR_MAP_LARGE = 0
        FLOORING_QCAR_MAP_SMALL = 1
    end
    methods
        function obj = qlabs_flooring(qlabs, verbose)
            arguments
                qlabs quanser_interactive_labs
                verbose logical = false
            end
            obj = obj@qlabs_actor(qlabs, verbose);
    
            obj.classID = obj.ID_FLOORING;
        end
    end
end