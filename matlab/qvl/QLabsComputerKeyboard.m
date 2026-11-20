classdef QLabsComputerKeyboard < QLabsActor
    properties
        ID_COMPUTER_KEYBOARD = 10110;
    end
    methods
        function obj = QLabsComputerKeyboard(qlabs, verbose)

            arguments
                qlabs QuanserInteractiveLabs
                verbose logical = false
            end            

            obj = obj@QLabsActor(qlabs, verbose);

            obj.classID = obj.ID_COMPUTER_KEYBOARD;

            return
        end
    end
end
