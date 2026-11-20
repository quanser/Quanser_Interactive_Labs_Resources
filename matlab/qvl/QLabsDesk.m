classdef QLabsDesk < QLabsActor
    properties
        ID_DESK = 10100;
    end
    methods
        function obj = QLabsDesk(qlabs, verbose)

            arguments
                qlabs QuanserInteractiveLabs
                verbose logical = false
            end            

            obj = obj@QLabsActor(qlabs, verbose);

            obj.classID = obj.ID_DESK;

            return
        end
    end
end
