classdef QLabsQube2 < QLabsActor
    properties
        ID_QUBE2 = 60
    end

    methods
        function obj = QLabsQube2(qlabs, verbose)
            arguments
                qlabs QuanserInteractiveLabs
                verbose logical = false
            end

            obj = obj@QLabsActor(qlabs, verbose);

            obj.classID = obj.ID_QUBE2;

            return
        end
    end
end