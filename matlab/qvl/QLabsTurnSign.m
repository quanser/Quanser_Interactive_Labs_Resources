classdef QLabsTurnSign < QLabsActor
    properties
        ID_TURN_SIGN = 10230
    end

    methods
        function obj = QLabsTurnSign(qlabs, verbose)
            arguments
                qlabs QuanserInteractiveLabs
                verbose logical = false
            end

            obj = obj@QLabsActor(qlabs, verbose);

            obj.classID = obj.ID_TURN_SIGN;

            return
        end
    end
end