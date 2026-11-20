classdef QLabsChair < QLabsActor
    properties
        ID_CHAIR = 10140;
    end
    methods
        function obj = QLabsChair(qlabs, verbose)

            arguments
                qlabs QuanserInteractiveLabs
                verbose logical = false
            end            

            obj = obj@QLabsActor(qlabs, verbose);

            obj.classID = obj.ID_CHAIR;

            return
        end
    end
end
