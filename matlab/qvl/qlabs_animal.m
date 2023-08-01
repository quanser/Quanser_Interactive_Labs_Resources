classdef qlabs_animal < qlabs_character
    properties
%         This class implements spawning and AI navigation of the environment for animals."""
        
        ID_ANIMAL = 10031
    
        GOAT = 0
%          Configuration constant. 
        SHEEP = 1
%          Configuration constant. 
        COW = 2
%          Configuration constant. 
    
    
        GOAT_STANDING = 0
%          Speed constant for the move_to method. 
        GOAT_WALK = 0.8
%          Speed constant for the move_to method. 
        GOAT_RUN = 4.0
%          Speed constant for the move_to method. 

        SHEEP_STANDING = 0
%          Speed constant for the move_to method. 
        SHEEP_WALK = 0.60
%          Speed constant for the move_to method. 
        SHEEP_RUN = 3.0
%          Speed constant for the move_to method. 
    
        COW_STANDING = 0
%          Speed constant for the move_to method. 
        COW_WALK = 1.0
%          Speed constant for the move_to method. 
        COW_RUN = 6.0
%          Speed constant for the move_to method.  
    end 

    methods
        function obj = qlabs_animal(qlabs, verbose)

            arguments
                qlabs quanser_interactive_labs
                verbose logical = false
            end            

            obj = obj@qlabs_character(qlabs, verbose);

            obj.classID = obj.ID_ANIMAL;
        end
    end
end