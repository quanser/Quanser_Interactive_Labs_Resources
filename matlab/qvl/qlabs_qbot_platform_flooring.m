classdef qlabs_qbot_platform_flooring < qlabs_actor
    properties
%         This class is for spawning static floors.

        ID_FLOORING = 10091
%         Class ID
    
        FLOORING_QBOT_PLATFORM_0 = 0
        FLOORING_QBOT_PLATFORM_1 = 1
        FLOORING_QBOT_PLATFORM_2 = 2
        FLOORING_QBOT_PLATFORM_3 = 3
        FLOORING_QBOT_PLATFORM_4 = 4
        FLOORING_QBOT_PLATFORM_5 = 5
    end
    methods
        function obj = qlabs_qbot_platform_flooring(qlabs, verbose)
            arguments
                qlabs quanser_interactive_labs
                verbose logical = false
            end
            obj = obj@qlabs_actor(qlabs, verbose);
    
            obj.classID = obj.ID_FLOORING;
        end
    end
end