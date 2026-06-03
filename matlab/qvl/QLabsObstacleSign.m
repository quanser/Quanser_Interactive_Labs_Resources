classdef QLabsObstacleSign < QLabsActor
    properties
        ID_OBSTACLE_SIGN = 10220
    end

    methods
        function obj = QLabsObstacleSign(qlabs, verbose)
            arguments
                qlabs QuanserInteractiveLabs
                verbose logical = false
            end

            obj = obj@QLabsActor(qlabs, verbose);

            obj.classID = obj.ID_OBSTACLE_SIGN;

            return
        end
    end
end