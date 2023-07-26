classdef qlabs_free_camera < qlabs_actor
    properties

        ID_FREE_CAMERA = 170;
    
        FCN_FREE_CAMERA_POSSESS = 10;
        FCN_FREE_CAMERA_POSSESS_ACK = 11;
        FCN_FREE_CAMERA_SET_CAMERA_PROPERTIES = 12;
        FCN_FREE_CAMERA_SET_CAMERA_PROPERTIES_ACK = 13;
        FCN_FREE_CAMERA_SET_TRANSFORM = 14;
        FCN_FREE_CAMERA_SET_TRANSFORM_ACK = 15;
        FCN_FREE_CAMERA_SET_IMAGE_RESOLUTION = 90;
        FCN_FREE_CAMERA_SET_IMAGE_RESOLUTION_RESPONSE = 91;
        FCN_FREE_CAMERA_REQUEST_IMAGE = 100;
        FCN_FREE_CAMERA_RESPONSE_IMAGE = 101;
    end
    methods
        %%
        function obj = qlabs_free_camera(qlabs, verbose)

            arguments
                qlabs quanser_interactive_labs
                verbose logical = false
            end            

            obj = obj@qlabs_actor(qlabs, verbose);

            obj.classID = obj.ID_FREE_CAMERA;
        end

        %%
        function success = possess(obj, actorNumber)
            success = false;
            obj.c.classID = obj.ID_FREE_CAMERA;
            obj.c.actorNumber = actorNumber;
            obj.c.actorFunction = obj.FCN_FREE_CAMERA_POSSESS;
            obj.c.payload = [];
            obj.c.containerSize = 10 + length(c.payload);

            qlabs.flush_receive()  

            if (obj.qlabs.send_container(c))
                rc = obj.qlabs.wait_for_container(obj.ID_FREE_CAMERA, actorNumber, obj.FCN_FREE_CAMERA_POSSESS_ACK);
                
                if isempty(rc)
                    if (obj.verbose)
                        fprintf('possess: Communication timeout (classID %u), actorNumber %u).\n', obj.classID, obj.actorNumber);
                    end
                    return
                end     
                
                success = true;
            else
                if (obj.verbose)
                    fprintf('possess: Communication failure (classID %u), actorNumber %u).\n', obj.classID, obj.actorNumber);
                end
            end
        end

%%
    function success = set_transform(obj, location, rotation)
        success = false;


        if (not(is_actor_number_valid(obj)))
            return
        end

        obj.c.classID = obj.ID_FREE_CAMERA;
        obj.c.actorNumber = actorNumber;
        obj.c.actorFunction = obj.FCN_FREE_CAMERA_SET_TRANSFORM;
        obj.c.payload = [flip(typecast(single(location(1)), 'uint8')) ...
                     flip(typecast(single(location(2)), 'uint8')) ...
                     flip(typecast(single(location(3)), 'uint8')) ...
                     flip(typecast(single(rotation(1)), 'uint8')) ...
                     flip(typecast(single(rotation(2)), 'uint8')) ...
                     flip(typecast(single(rotation(3)), 'uint8'))];
        obj.c.containerSize = 10 + length(c.payload);


        obj.qlabs.flush_receive()

        if (obj.qlabs.send_container(obj.c))
            rc = obj.qlabs.wait_for_container(self.ID_FREE_CAMERA, self.actorNumber, self.FCN_FREE_CAMERA_SET_TRANSFORM_ACK);
            if isempty(rc)
                if (obj.verbose)
                        fprintf('possess: Communication timeout (classID %u), actorNumber %u).\n', obj.classID, obj.actorNumber);
                end
                return
            else
                success = true;
                return
            end
        else
            if (obj.verbose)
                    fprintf('possess: Communication failure (classID %u), actorNumber %u).\n', obj.classID, obj.actorNumber);
            end
            return 
        end
        
    end
end