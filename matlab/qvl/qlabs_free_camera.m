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
        function success = possess(obj)
            success = false;

            if (not(is_actor_number_valid(obj)))
                return
            end

            obj.c.classID = obj.ID_FREE_CAMERA;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_FREE_CAMERA_POSSESS;
            obj.c.payload = [];
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);

            obj.qlabs.flush_receive();

            if (obj.qlabs.send_container(obj.c))
                rc = obj.qlabs.wait_for_container(obj.ID_FREE_CAMERA, obj.actorNumber, obj.FCN_FREE_CAMERA_POSSESS_ACK);
                
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
            
            arguments
                obj qlabs_actor
                location (1,3) double = [0 0 0]
                rotation (1,3) double = [0 0 0]
            end
            
            
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
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);
    
    
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
        
        %%
        function success = set_transform_degrees(obj, location, rotation)
            
            arguments
                obj qlabs_actor
                location (1,3) double = [0 0 0]
                rotation (1,3) double = [0 0 0]
            end
            
            
            success = set_transform(obj, location, rotation/180*pi);
            
        end    
    

        %%
        def set_camera_properties(self, fieldOfView, depthOfField, aperture, focusDistance):
            """
            Sets the camera properties. When depthOfField is enabled, the camera will produce more realistic (and cinematic) results by adding some blur to the view at distances closer and further away from a given focal distance. For more blur, use a large aperture (small value) and a narrow field of view.
    
            :param fieldOfView: The field of view that the camera can see (range:5-150 degrees). When depthOfField is True, smaller values will increase focal blur at distances relative to the focusDistance.
            :param depthOfField: Enable or disable the depth of field visual effect
            :param aperture: The amount of light allowed into the camera sensor (range:2.0-22.0). Smaller values (larger apertures) increase the light and decrease the depth of field. This parameter is only active when depthOfField is True.
            :param focusDistance: The distance to the focal plane of the camera. (range:0.1-50.0 meters).  This parameter is only active when depthOfField is True.
            :type fieldOfView: int
            :type depthOfField: boolean
            :type aperture: float
            :type focusDistance: float
            :return: `True` if setting the camera properties was successful, `False` otherwise
            :rtype: boolean
    
            """
            if (not self._is_actor_number_valid()):
                return False
    
            c = CommModularContainer()
            c.classID = self.ID_FREE_CAMERA
            c.actorNumber = self.actorNumber
            c.actorFunction = self.FCN_FREE_CAMERA_SET_CAMERA_PROPERTIES
            c.payload = bytearray(struct.pack(">fBff", fieldOfView, depthOfField, aperture, focusDistance))
            c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
    
            self._qlabs.flush_receive()
    
            if (self._qlabs.send_container(c)):
                c = self._qlabs.wait_for_container(self.ID_FREE_CAMERA, self.actorNumber, self.FCN_FREE_CAMERA_SET_CAMERA_PROPERTIES_ACK)
                if (c == None):
                    return False
                else:
                    return True
            else:
                return False    


% def set_image_capture_resolution(self, width=640, height=480):
%         """Change the default width and height of image resolution for capture
% 
%         :param width: Must be an even number. Default 640
%         :param height: Must be an even number. Default 480
%         :type width: uint32
%         :type height: uint32
%         :return: `True` if spawn was successful, `False` otherwise
%         :rtype: boolean
%         """
%         if (not self._is_actor_number_valid()):
%             return False
% 
%         c = CommModularContainer()
%         c.classID = self.ID_FREE_CAMERA
%         c.actorNumber = self.actorNumber
%         c.actorFunction = self.FCN_FREE_CAMERA_SET_IMAGE_RESOLUTION
%         c.payload = bytearray(struct.pack(">II", width, height))
%         c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
% 
%         self._qlabs.flush_receive()
% 
%         if (self._qlabs.send_container(c)):
%             c = self._qlabs.wait_for_container(self.ID_FREE_CAMERA, self.actorNumber, self.FCN_FREE_CAMERA_SET_IMAGE_RESOLUTION_RESPONSE)
%             if (c == None):
%                 return False
%             else:
%                 return True
%         else:
%             return False
% 
% 
% 
%     def get_image(self):
%         """Request an image from the camera actor. Note, set_image_capture_resolution must be set once per camera otherwise this method will fail.
% 
%         :return: Success, RGB image data
%         :rtype: boolean, byte array[variable]
%         """
% 
%         if (not self._is_actor_number_valid()):
%             return False, None
% 
%         c = CommModularContainer()
%         c.classID = self.ID_FREE_CAMERA
%         c.actorNumber = self.actorNumber
%         c.actorFunction = self.FCN_FREE_CAMERA_REQUEST_IMAGE
%         c.payload = bytearray()
%         c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
% 
%         self._qlabs.flush_receive()
% 
%         if (self._qlabs.send_container(c)):
%             c = self._qlabs.wait_for_container(self.ID_FREE_CAMERA, self.actorNumber, self.FCN_FREE_CAMERA_RESPONSE_IMAGE)
%             if (c == None):
%                 return False, None
% 
%             data_size, = struct.unpack(">I", c.payload[0:4])
% 
%             jpg_buffer = cv2.imdecode(np.frombuffer(bytearray(c.payload[4:len(c.payload)]), dtype=np.uint8, count=-1, offset=0), 1)
% 
% 
%             return True, jpg_buffer
%         else:
%             return False, None

    end % methods
end % class