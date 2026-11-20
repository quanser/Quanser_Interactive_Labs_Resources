classdef QLabsQube3 < QLabsActor
    properties
        ID_QUBE3 = 61
    end

    methods
        function obj = QLabsQube3(qlabs, verbose)
            arguments
                qlabs QuanserInteractiveLabs
                verbose logical = false
            end

            obj = obj@QLabsActor(qlabs, verbose);

            obj.classID = obj.ID_QUBE3;

            return
        end
    end
end