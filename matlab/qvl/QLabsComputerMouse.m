classdef QLabsComputerMouse < QLabsActor
    properties
        ID_COMPUTER_MOUSE = 10120;
    end
    methods
        function obj = QLabsComputerMouse(qlabs, verbose)

            arguments
                qlabs QuanserInteractiveLabs
                verbose logical = false
            end            

            obj = obj@QLabsActor(qlabs, verbose);

            obj.classID = obj.ID_COMPUTER_MOUSE;

            return
        end
    end
end
