classdef qlabs_person < qlabs_character
    properties
        % This class implements spawning and AI navigation of the environment for human pedestrians
    
        ID_PERSON = 10030
    
        STANDING = 0
        % Speed constant for the move_to method. 
        WALK = 1.2
        % Speed constant for the move_to method. 
        JOG = 3.6
        % Speed constant for the move_to method. 
        RUN = 6.0
        % Speed constant for the move_to method. 
    end
    methods
        function obj = qlabs_person(qlabs, verbose)

            arguments
                qlabs quanser_interactive_labs
                verbose logical = false
            end

            obj = obj@qlabs_character(qlabs, verbose);

            obj.classID = obj.ID_PERSON;

        end
    end
end