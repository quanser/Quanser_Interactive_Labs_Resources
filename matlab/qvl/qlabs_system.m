classdef qlabs_system < handle
    properties
%         The System is a special class that allows you to modify elements of the user interface and application.

        ID_SYSTEM = 1000
%         Class ID.s
        FCN_SYSTEM_SET_TITLE_STRING = 10
        FCN_SYSTEM_SET_TITLE_STRING_ACK = 11
    
        c = []
        qlabs = []
        verbose = false
    end
    methods
        function obj = qlabs_system(qlabs, verbose)

            arguments
                qlabs quanser_interactive_labs
                verbose logical = false
            end            

            obj = obj@handle();

            obj.qlabs = qlabs;
            obj.verbose = verbose;
            obj.c = qlabs_comm_modular_container();
        end

        function success = set_title_string(obj, titleString, waitForConfirmation)
            arguments
                obj qlabs_system
                titleString string
                waitForConfirmation logical = true
            end
            success = false;

%             Sets the title string in the upper left of the window to custom text. This can be useful when doing screen recordings or labeling experiment configurations.
% 
%             :param titleString: User defined string to replace the default title text
%             :param waitForConfirmation: (Optional) Wait for confirmation of the before proceeding. This makes the method a blocking operation.
%             :type titleString: string
%             :type waitForConfirmation: boolean
%             :return: `True` if successful, `False` otherwise.
%             :rtype: boolean

            obj.c.classID = obj.ID_SYSTEM;
            obj.c.actorNumber = 0;
            obj.c.actorFunction = obj.FCN_SYSTEM_SET_TITLE_STRING;
            obj.c.payload = [flip(typecast(int32(length(char(titleString))), 'uint8')) ...
                             uint8(char(titleString))];
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);

            if waitForConfirmation
                obj.qlabs.flush_receive();
            end

            if (obj.qlabs.send_container(obj.c))
                if waitForConfirmation
                    rc = obj.qlabs.wait_for_container(obj.ID_SYSTEM, 0, obj.FCN_SYSTEM_SET_TITLE_STRING_ACK);

                    if isempty(rc)
                        return
                    else
                        success = true;
                        return
                    end
                end
                success = true;
                return
            else
                return
            end
        end
    end
end