classdef QLabsTrafficCone < QLabsActor
    properties
        ID_TRAFFIC_CONE = 10000;
    end
    methods
        function obj = QLabsTrafficCone(qlabs, verbose)

            arguments
                qlabs QuanserInteractiveLabs
                verbose logical = false
            end

            obj = obj@QLabsActor(qlabs, verbose);

            obj.classID = obj.ID_TRAFFIC_CONE;


        end
    end
end