classdef QLabsComputer < QLabsActor
    properties
        ID_COMPUTER = 10150;
    end
    methods
        function obj = QLabsComputer(qlabs, verbose)

            arguments
                qlabs QuanserInteractiveLabs
                verbose logical = false
            end            

            obj = obj@QLabsActor(qlabs, verbose);

            obj.classID = obj.ID_COMPUTER;

            return
        end
    end
end
