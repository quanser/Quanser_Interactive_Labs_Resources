classdef QLabsCrossingSign < QLabsActor
    properties
        ID_CROSSING_SIGN = 10210
    end

    methods
        function obj = QLabsCrossingSign(qlabs, verbose)
            arguments
                qlabs QuanserInteractiveLabs
                verbose logical = false
            end

            obj = obj@QLabsActor(qlabs, verbose);

            obj.classID = obj.ID_CROSSING_SIGN;

            return
        end
    end
end