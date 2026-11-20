classdef QLabsComputerMonitor < QLabsActor
    properties
        ID_COMPUTER_MONITOR = 10130;
    end
    methods
        function obj = QLabsComputerMonitor(qlabs, verbose)

            arguments
                qlabs QuanserInteractiveLabs
                verbose logical = false
            end            

            obj = obj@QLabsActor(qlabs, verbose);

            obj.classID = obj.ID_COMPUTER_MONITOR;

            return
        end
    end
end
