classdef QLabsCrosswalk < QLabsActor
    properties
        ID_CROSSWALK = 10010;
    end
    methods
        function obj = QLabsCrosswalk(qlabs, verbose)

            arguments
                qlabs QuanserInteractiveLabs
                verbose logical = false
            end

            obj = obj@QLabsActor(qlabs, verbose);

            obj.classID = obj.ID_CROSSWALK;

        end            
    end
end