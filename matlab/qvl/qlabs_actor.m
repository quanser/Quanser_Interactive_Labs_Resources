classdef qlabs_actor < handle
    properties
        c = [];


        % This the base actor class.
    
        FCN_UNKNOWN = 0;
        % Function ID is not recognized.
        FCN_REQUEST_PING = 1;
        % Request a response from an actor to test if it is present.
        FCN_RESPONSE_PING = 2;
        % Response from an actor to confirming it is present.
        FCN_REQUEST_WORLD_TRANSFORM = 3;
        % Request a world transform from the actor to read its current location, rotation, and scale.
        FCN_RESPONSE_WORLD_TRANSFORM = 4;
        % Response from an actor with its current location, rotation, and scale.
        FCN_SET_CUSTOM_PROPERTIES = 5;
        % Set custom properties of measured mass, ID, and/or property string.
        FCN_SET_CUSTOM_PROPERTIES_ACK = 6;
        % Set custom properties acknowledgment.
        FCN_REQUEST_CUSTOM_PROPERTIES = 7;
        % Request the custom properties of measured mass, ID, and/or property string previously assigned to the actor.
        FCN_RESPONSE_CUSTOM_PROPERTIES = 8;
        % Response containing the custom properties of measured mass, ID, and/or property string previously assigned to the actor.

        actorNumber = [];
        % The current actor number of this class to be addressed. This will
        % be set by spawn methods and cleared by destroy methods. It will not 
        % be modified by the destroy all actors.  This can be manually altered 
        % at any time to use one object to address multiple actors.

        qlabs = [];
        verbose = false;
        classID = 0;
    end
    methods
        %%
        function obj = qlabs_actor(qlabs, verbose)

            arguments
                qlabs quanser_interactive_labs
                verbose logical = false
            end            

            obj = obj@handle();

            obj.qlabs = qlabs;
            obj.verbose = verbose;
            obj.c = qlabs_comm_modular_container();
        end

        %%

        function value = is_actor_number_valid(obj)
            if isempty(obj.actorNumber) == true
                if (obj.verbose == true)
                    fprintf('actorNumber member variable empty. Use a spawn function to assign an actor or manually assign the actorNumber variable.\n')
                end
               
                value = false;
            else
                value = true;
            end
        end        

        %%
        function num_destroyed = destroy(obj)
            % Find and destroy a specific actor. This is a blocking operation.

            if not(is_actor_number_valid(obj))
                num_destroyed = -1;
                return;
            end

            obj.c.classID = obj.c.ID_GENERIC_ACTOR_SPAWNER;
            obj.c.actorNumber = 0;
            obj.c.actorFunction = obj.c.FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ACTOR;
            obj.c.payload = [flip(typecast(int32(obj.classID), 'uint8')) ...
                         flip(typecast(int32(obj.actorNumber), 'uint8'))];
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);  

            if (obj.qlabs.send_container(obj.c))
                rc = obj.qlabs.wait_for_container(obj.c.ID_GENERIC_ACTOR_SPAWNER, 0, obj.c.FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ACTOR_ACK);
                if isempty(rc)
                    if (obj.verbose == true)
                        disp('Timeout waiting for response.')
                    end
                    num_destroyed = -1;
                else
                    if length(rc.payload) == 4
                        num_destroyed = typecast(flip(rc.payload(1:4)), 'int32');

                        obj.actorNumber = [];
                        return;
                    else
                        if (obj.verbose == true)
                            fprintf('Container payload does not match expected size.\n')
                        end                          
                        num_destroyed = -1;
                        return
                    end
                    
                end
            end

        end


        %%
        function num_destroyed = destroy_all_actors_of_class(obj)
            % Find and destroy all actors of this class. This is a blocking operation.

            obj.c.classID = obj.c.ID_GENERIC_ACTOR_SPAWNER;
            obj.c.actorNumber = 0;
            obj.c.actorFunction = obj.c.FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ALL_ACTORS_OF_CLASS;
            obj.c.payload = [flip(typecast(int32(obj.classID), 'uint8'))];
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);  

            if (obj.qlabs.send_container(obj.c))
                rc = obj.qlabs.wait_for_container(obj.c.ID_GENERIC_ACTOR_SPAWNER, 0, obj.c.FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ALL_ACTORS_OF_CLASS_ACK);
                if isempty(rc)
                    if (obj.verbose == true)
                        fprint('Timeout waiting for response.\n')
                    end
                    num_destroyed = -1;
                else
                    if length(rc.payload) == 4
                        num_destroyed = typecast(flip(rc.payload(1:4)), 'int32');

                        obj.actorNumber = [];
                        return;
                    else
                        if (obj.verbose == true)
                            fprintf('Container payload does not match expected size.\n')
                        end                        
                        num_destroyed = -1;
                        return
                    end
                    
                end
            end

        end



        %%
        function status = spawn_id(obj, actorNumber, location, rotation, scale, configuration, waitForConfirmation)

            arguments
                obj qlabs_actor
                actorNumber int32
                location (1,3) double = [0 0 0]
                rotation (1,3) double = [0 0 0]
                scale (1,3) double = [0 0 0]
                configuration int32 = 0 
                waitForConfirmation logical = true
            end  
            
            obj.c.classID = obj.c.ID_GENERIC_ACTOR_SPAWNER;
            obj.c.actorNumber = 0;
            obj.c.actorFunction = obj.c.FCN_GENERIC_ACTOR_SPAWNER_SPAWN_ID;
            
            status = -1;
            
            
            obj.c.payload = [flip(typecast(int32(obj.classID), 'uint8')) ...
                         flip(typecast(int32(actorNumber), 'uint8')) ...
                         flip(typecast(single(location(1)), 'uint8')) ...
                         flip(typecast(single(location(2)), 'uint8')) ...
                         flip(typecast(single(location(3)), 'uint8')) ...
                         flip(typecast(single(rotation(1)), 'uint8')) ...
                         flip(typecast(single(rotation(2)), 'uint8')) ...
                         flip(typecast(single(rotation(3)), 'uint8')) ...
                         flip(typecast(single(scale(1)), 'uint8')) ...
                         flip(typecast(single(scale(2)), 'uint8')) ...
                         flip(typecast(single(scale(3)), 'uint8')) ...
                         flip(typecast(int32(configuration), 'uint8'))];
            
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);
            
            if waitForConfirmation
                obj.qlabs.flush_receive()
            end
            
            if (obj.qlabs.send_container(obj.c))
            
                if waitForConfirmation
                    rc = obj.qlabs.wait_for_container(obj.c.ID_GENERIC_ACTOR_SPAWNER, 0, obj.c.FCN_GENERIC_ACTOR_SPAWNER_SPAWN_ID_ACK);
                    if isempty(rc)
                        if (obj.verbose)
                            fprintf('spawn_id: Communication timeout (classID %u, actorNumber %u).\n', obj.classID, actorNumber);
                        end
                        return
                        
                    end
                    
                    if length(rc.payload) == 1
                        status = rc.payload(1);

                        if (status == 0)
                            obj.actorNumber = actorNumber;
    
                        elseif (obj.verbose)
                            if (status == 1)
                                fprintf('spawn_id: Class not available (classID %u, actorNumber %u).\n', obj.classID, actorNumber);
                            elseif (status == 2)
                                fprintf('spawn_id: Actor number not available or already in use (classID %u, actorNumber %u).\n', obj.classID, actorNumber);
                            elseif (status == -1)
                                fprintf('spawn_id: Communication error (classID %u, actorNumber %u).\n', obj.classID, actorNumber);
                            else
                                fprintf('spawn_id: Unknown error (classID %u, actorNumber %u).\n', obj.classID, actorNumber);
                            end
                        end
                        
                    else
                        if (obj.verbose)
                            fprintf('spawn: Communication error (classID %u, actorNumber %u).\n', obj.classID, actorNumber);
                        end
                        return
                    end
                    return;
                else
                    obj.actorNumber = actorNumber;
                    status = 0;
                end
            else
                if (obj.verbose)
                    fprintf('spawn_id: Communication failed (classID %u, actorNumber %u).\n', obj.classID, actorNumber);
                end
                return             
            end

        end


 %%
        function status = spawn_id_degrees(obj, actorNumber, location, rotation, scale, configuration, waitForConfirmation)

            arguments
                obj qlabs_actor
                actorNumber int32
                location (1,3) double = [0 0 0]
                rotation (1,3) double = [0 0 0]
                scale (1,3) double = [0 0 0]
                configuration int32 = 0 
                waitForConfirmation logical = true
            end  
            
            status = spawn_id(obj, actorNumber, location, rotation/180*pi, scale, configuration, waitForConfirmation);

        end

        %%
        function [status, actorNumber] = spawn(obj, location, rotation, scale, configuration, waitForConfirmation)

            arguments
                obj qlabs_actor
                location (1,3) double = [0 0 0]
                rotation (1,3) double = [0 0 0]
                scale (1,3) double = [0 0 0]
                configuration int32 = 0 
                waitForConfirmation logical = true
            end  
            
            obj.c.classID = obj.c.ID_GENERIC_ACTOR_SPAWNER;
            obj.c.actorNumber = 0;
            obj.c.actorFunction = obj.c.FCN_GENERIC_ACTOR_SPAWNER_SPAWN;
            
            status = -1;
            actorNumber = -1;
            
            obj.c.payload = [flip(typecast(int32(obj.classID), 'uint8')) ...
                         flip(typecast(single(location(1)), 'uint8')) ...
                         flip(typecast(single(location(2)), 'uint8')) ...
                         flip(typecast(single(location(3)), 'uint8')) ...
                         flip(typecast(single(rotation(1)), 'uint8')) ...
                         flip(typecast(single(rotation(2)), 'uint8')) ...
                         flip(typecast(single(rotation(3)), 'uint8')) ...
                         flip(typecast(single(scale(1)), 'uint8')) ...
                         flip(typecast(single(scale(2)), 'uint8')) ...
                         flip(typecast(single(scale(3)), 'uint8')) ...
                         flip(typecast(int32(configuration), 'uint8'))];
            
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);
            
            if waitForConfirmation
                obj.qlabs.flush_receive()
            end
            
            if (obj.qlabs.send_container(obj.c))
            
                if waitForConfirmation
                    rc = obj.qlabs.wait_for_container(obj.c.ID_GENERIC_ACTOR_SPAWNER, 0, obj.c.FCN_GENERIC_ACTOR_SPAWNER_SPAWN_RESPONSE);
                    if isempty(rc)
                        if (obj.verbose)
                            fprintf('spawn_id: Communication timeout (classID %u).\n', obj.classID);
                        end

                        status = -1;
                        return
                        
                    end
                    
                    if length(rc.payload) == 5
                        status = rc.payload(1);
                        actorNumber = typecast(flip(rc.payload(2:5)), 'int32');

                        if (status == 0)
                            obj.actorNumber = actorNumber;
    
                        elseif (obj.verbose)
                            if (status == 1)
                                fprintf('spawn_id: Class not available (classID %u).\n', obj.classID);
                            elseif (status == -1)
                                fprintf('spawn_id: Communication error (classID %u).\n', obj.classID);
                            else
                                fprintf('spawn_id: Unknown error (classID %u).\n', obj.classID);
                            end
                        end
                        
                    else
                        if (obj.verbose)
                            fprintf('spawn: Communication error (classID %u, actorNumber %u).\n', obj.classID, actorNumber);
                        end

                        status = -1;
                    end
                    return;
                end
            
                status = 0;
            end

        end      

        %%
        function [status, actorNumber] = spawn_degrees(obj, location, rotation, scale, configuration, waitForConfirmation)

            arguments
                obj qlabs_actor
                location (1,3) double = [0 0 0]
                rotation (1,3) double = [0 0 0]
                scale (1,3) double = [0 0 0]
                configuration int32 = 0 
                waitForConfirmation logical = true
            end  
            
            [status, actorNumber] = spawn(obj, location, rotation/180*pi, scale, configuration, waitForConfirmation);
        end             


        %%        
        function status = spawn_id_and_parent_with_relative_transform(obj, actorNumber, location, rotation, scale, configuration, parentClassID, parentActorNumber, parentComponent, waitForConfirmation)
    
            arguments
                obj qlabs_actor
                actorNumber int32
                location (1,3) double = [0 0 0]
                rotation (1,3) double = [0 0 0]
                scale (1,3) double = [0 0 0]
                configuration int32 = 0 
                parentClassID int32 = 0
                parentActorNumber int32 = 0
                parentComponent int32 = 0
                waitForConfirmation logical = true
            end  


            status = -1;

            obj.c.classID = obj.c.ID_GENERIC_ACTOR_SPAWNER;
            obj.c.actorNumber = 0;
            obj.c.actorFunction = obj.c.FCN_GENERIC_ACTOR_SPAWNER_SPAWN_AND_PARENT_RELATIVE;
            obj.c.payload = [flip(typecast(int32(obj.classID), 'uint8')) ...
                         flip(typecast(int32(actorNumber), 'uint8')) ...
                         flip(typecast(single(location(1)), 'uint8')) ...
                         flip(typecast(single(location(2)), 'uint8')) ...
                         flip(typecast(single(location(3)), 'uint8')) ...
                         flip(typecast(single(rotation(1)), 'uint8')) ...
                         flip(typecast(single(rotation(2)), 'uint8')) ...
                         flip(typecast(single(rotation(3)), 'uint8')) ...
                         flip(typecast(single(scale(1)), 'uint8')) ...
                         flip(typecast(single(scale(2)), 'uint8')) ...
                         flip(typecast(single(scale(3)), 'uint8')) ...
                         flip(typecast(int32(configuration), 'uint8')) ...
                         flip(typecast(int32(parentClassID), 'uint8')) ...
                         flip(typecast(int32(parentActorNumber), 'uint8')) ...
                         flip(typecast(int32(parentComponent), 'uint8'))];
            
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);


            if waitForConfirmation
                obj.qlabs.flush_receive()
            end
            
            if (obj.qlabs.send_container(obj.c))
            
                if waitForConfirmation
                    rc = obj.qlabs.wait_for_container(obj.c.ID_GENERIC_ACTOR_SPAWNER, 0, obj.c.FCN_GENERIC_ACTOR_SPAWNER_SPAWN_AND_PARENT_RELATIVE_ACK);
                    if isempty(rc)
                        if (obj.verbose)
                            fprintf('spawn_id_and_parent_with_relative_transform: Communication timeout (classID %u, actorNumber %u).\n', obj.classID, actorNumber);
                        end

                        return
                        
                    end
                    
                    if length(rc.payload) == 1
                        status = rc.payload(1);

                        if (status == 0)
                            obj.actorNumber = actorNumber;
    
                        elseif (obj.verbose)
                            if (status == 1)
                                fprintf('spawn_id_and_parent_with_relative_transform: Class not available (classID %u, actorNumber %u).\n', obj.classID, actorNumber);
                            elseif (status == 2)
                                fprintf('spawn_id_and_parent_with_relative_transform: Actor number not available or already in use (classID %u, actorNumber %u).\n', obj.classID, actorNumber);
                            elseif (status == 3)
                                fprintf('spawn_id_and_parent_with_relative_transform:  Cannot find parent (classID %u, actorNumber %u).\n', obj.classID, actorNumber);
                            elseif (status == -1)
                                fprintf('spawn_id_and_parent_with_relative_transform: Communication error (classID %u, actorNumber %u).\n', obj.classID, actorNumber);
                            else
                                fprintf('spawn_id_and_parent_with_relative_transform: Unknown error (classID %u, actorNumber %u).\n', obj.classID, actorNumber);
                            end
                        end
                        
                    else
                        if (obj.verbose)
                            fprintf('spawn_id_and_parent_with_relative_transform: Communication error (classID %u, actorNumber %u).\n', obj.classID, actorNumber);
                        end

                    end
                    return;
                end
                obj.actorNumber = actorNumber;
                status = 0;
            else
                if (obj.verbose)
                    fprintf('spawn_id_and_parent_with_relative_transform: Communication failed (classID %u, actorNumber %u).\n', obj.classID, actorNumber);
                end

            end

        end

        %%
        function status = spawn_id_and_parent_with_relative_transform_degrees(obj, actorNumber, location, rotation, scale, configuration, parentClassID, parentActorNumber, parentComponent, waitForConfirmation)
    
            arguments
                obj qlabs_actor
                actorNumber int32
                location (1,3) double = [0 0 0]
                rotation (1,3) double = [0 0 0]
                scale (1,3) double = [0 0 0]
                configuration int32 = 0 
                parentClassID int32 = 0
                parentActorNumber int32 = 0
                parentComponent int32 = 0
                waitForConfirmation logical = true
            end  

            status = spawn_id_and_parent_with_relative_transform(obj, actorNumber, location, rotation, scale, configuration, parentClassID, parentActorNumber, parentComponent, waitForConfirmation);
            
        end
    
        %%
        function success = ping(obj)
            % Checks if the actor is still present in the environment. Note that if you did not spawn
            % the actor with one of the spawn functions, you may need to manually set the actorNumber member variable.
    
            success = false;

            if (not(obj.is_actor_number_valid()))
                return
            end
    
            obj.c.classID = obj.classID;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_REQUEST_PING;
            obj.c.payload = [];
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);
    
            obj.qlabs.flush_receive()
    
            if (obj.qlabs.send_container(obj.c))
    
                rc = obj.qlabs.wait_for_container(obj.classID, obj.actorNumber, obj.FCN_RESPONSE_PING);

                if isempty(rc)
                    if (obj.verbose)
                        fprintf('ping: Communication timeout (classID %u, actorNumber %u).\n', obj.classID, obj.actorNumber);
                    end

                    return
                    
                end
                
                if length(rc.payload) == 1
                    status = rc.payload(1);
                    
                    if (status == 1)
                        success = true;
                    end
                    
                else
                    if (obj.verbose)
                        fprintf('ping: Communication error (classID %u, actorNumber %u).\n', obj.classID, obj.actorNumber);
                    end
                end
            end
        end    

        %%

        function [success, location, rotation, scale] = get_world_transform(obj)
            % Get the location, rotation, and scale in world coordinates of the actor.
    
            location = [0,0,0];
            rotation = [0,0,0];
            scale = [0,0,0];
            success = false;
    
            if (not(obj.is_actor_number_valid()))
                return
            end
    
            obj.c.classID = obj.classID;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_REQUEST_WORLD_TRANSFORM;
            obj.c.payload = [];
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);
    
    
    
            obj.qlabs.flush_receive()
    
            if (obj.qlabs.send_container(obj.c))
    
                rc = obj.qlabs.wait_for_container(obj.classID, obj.actorNumber, obj.FCN_RESPONSE_WORLD_TRANSFORM);
    
                if isempty(rc)
                    if (obj.verbose)
                        fprintf('get_world_transform: Communication timeout (classID %u, actorNumber %u).\n', obj.classID, obj.actorNumber);
                    end
    
                    return
                    
                end
                
                if length(rc.payload) == 36
                    location(1) = typecast(flip(rc.payload(1:4)), 'single');
                    location(2) = typecast(flip(rc.payload(5:8)), 'single');
                    location(3) = typecast(flip(rc.payload(9:12)), 'single');
    
                    rotation(1) = typecast(flip(rc.payload(13:16)), 'single');
                    rotation(2) = typecast(flip(rc.payload(17:20)), 'single');
                    rotation(3) = typecast(flip(rc.payload(21:24)), 'single');
                    
                    scale(1) = typecast(flip(rc.payload(25:28)), 'single');
                    scale(2) = typecast(flip(rc.payload(29:32)), 'single');
                    scale(3) = typecast(flip(rc.payload(33:36)), 'single');
                    
                    success = true;
                    return
                else
                    if (obj.verbose)
                        fprintf('get_world_transform: Communication error (classID %u, actorNumber %u).\n', obj.classID, obj.actorNumber);
                    end
                    return
                end
            else
                if (obj.verbose)
                    fprintf('get_world_transform: Communication error (classID %u, actorNumber %u).\n', obj.classID, obj.actorNumber);
                end
                return
            end
        end


        %%
        function [success, location, rotation, scale] = get_world_transform_degrees(obj)
            % Get the location, rotation, and scale in world coordinates of the actor.

            [success, location, rotation, scale] = obj.get_world_transform(obj);

            rotation = rotation/pi*180;

        end
    
    
        %%
        function status = parent_with_relative_transform(obj, location, rotation, scale, parentClassID, parentActorNumber, parentComponent, waitForConfirmation)
            % Parents one existing actor to another to create a kinematic relationship.
    

            arguments
                obj qlabs_actor
                location (1,3) double = [0 0 0]
                rotation (1,3) double = [0 0 0]
                scale (1,3) double = [0 0 0]
                parentClassID int32 = 0
                parentActorNumber int32 = 0
                parentComponent int32 = 0
                waitForConfirmation logical = true
            end  

            status = -1;
            
            obj.c.classID = obj.ID_GENERIC_ACTOR_SPAWNER;
            obj.c.actorNumber = 0;
            obj.c.actorFunction = obj.c.FCN_GENERIC_ACTOR_SPAWNER_PARENT_RELATIVE;
            obj.c.payload = [flip(typecast(int32(obj.classID), 'uint8')) ...
                         flip(typecast(int32(obj.actorNumber), 'uint8')) ...
                         flip(typecast(single(location(1)), 'uint8')) ...
                         flip(typecast(single(location(2)), 'uint8')) ...
                         flip(typecast(single(location(3)), 'uint8')) ...
                         flip(typecast(single(rotation(1)), 'uint8')) ...
                         flip(typecast(single(rotation(2)), 'uint8')) ...
                         flip(typecast(single(rotation(3)), 'uint8')) ...
                         flip(typecast(single(scale(1)), 'uint8')) ...
                         flip(typecast(single(scale(2)), 'uint8')) ...
                         flip(typecast(single(scale(3)), 'uint8')) ...
                         flip(typecast(int32(parentClassID), 'uint8')) ...
                         flip(typecast(int32(parentActorNumber), 'uint8')) ...
                         flip(typecast(int32(parentComponent), 'uint8'))];
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + len(obj.c.payload);
    

            if waitForConfirmation
                obj.qlabs.flush_receive()
            end
            
            if (obj.qlabs.send_container(obj.c))
            
                if waitForConfirmation
                    rc = obj.qlabs.wait_for_container(obj.c.ID_GENERIC_ACTOR_SPAWNER, 0, obj.c.FCN_GENERIC_ACTOR_SPAWNER_PARENT_RELATIVE_ACK);
                    if isempty(rc)
                        if (obj.verbose)
                            fprintf('parent_with_relative_transform: Communication timeout (classID %u, actorNumber %u).\n', obj.classID, obj.actorNumber);
                        end
                        return
                        
                    end
                    
                    if length(rc.payload) == 1
                        status = rc.payload(1);

                        if (status == 0)
                            return
    
                        elseif (obj.verbose)
                            if (status == 1)
                                fprintf('parent_with_relative_transform (classID %u, actorNumber %u): Class not available.\n', obj.classID, obj.actorNumber);
                            elseif (status == 2)
                                fprintf('parent_with_relative_transform (classID %u, actorNumber %u):  Cannot find parent (classID %u, actorNumber %u).\n', obj.classID, obj.actorNumber, parentClassID, parentActorNumber);
                            elseif (status == -1)
                                fprintf('parent_with_relative_transform (classID %u, actorNumber %u): Communication error.\n', obj.classID, obj.actorNumber);
                            else
                                fprintf('parent_with_relative_transform (classID %u, actorNumber %u): Unknown error.\n', obj.classID, obj.actorNumber);
                            end
                        end
                        
                    else
                        if (obj.verbose)
                            fprintf('parent_with_relative_transform (classID %u, actorNumber %u): Communication error.\n', obj.classID, obj.actorNumber);
                        end

                    end
                    return;
                end
                status = 0;
            else
                if (obj.verbose)
                    fprintf('parent_with_relative_transform: Communication failed (classID %u, actorNumber %u).\n', obj.classID, obj.actorNumber);
                end

            end
        end


        %%
    
    
        function status = parent_with_relative_transform_degrees(obj, location, rotation, scale, parentClassID, parentActorNumber, parentComponent, waitForConfirmation)
            % Parents one existing actor to another to create a kinematic relationship.

            arguments
                obj qlabs_actor
                location (1,3) double = [0 0 0]
                rotation (1,3) double = [0 0 0]
                scale (1,3) double = [0 0 0]
                parentClassID int32 = 0
                parentActorNumber int32 = 0
                parentComponent int32 = 0
                waitForConfirmation logical = true
            end

            status = parent_with_relative_transform(obj, location, rotation/180*pi, scale, parentClassID, parentActorNumber, parentComponent, waitForConfirmation);
        end

        %%
        function status = parent_with_current_world_transform(obj, parentClassID, parentActorNumber, parentComponent, waitForConfirmation)
            % Parents one existing actor to another to create a kinematic relationship.
    

            arguments
                obj qlabs_actor
                parentClassID int32 = 0
                parentActorNumber int32 = 0
                parentComponent int32 = 0
                waitForConfirmation logical = true
            end  

            status = -1;
            
            obj.c.classID = obj.ID_GENERIC_ACTOR_SPAWNER;
            obj.c.actorNumber = 0;
            obj.c.actorFunction = obj.c.FCN_GENERIC_ACTOR_SPAWNER_PARENT_CURRENT_WORLD;
            obj.c.payload = [flip(typecast(int32(obj.classID), 'uint8')) ...
                         flip(typecast(int32(obj.actorNumber), 'uint8')) ...
                         flip(typecast(int32(parentClassID), 'uint8')) ...
                         flip(typecast(int32(parentActorNumber), 'uint8')) ...
                         flip(typecast(int32(parentComponent), 'uint8'))];
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + len(obj.c.payload);
    

            if waitForConfirmation
                obj.qlabs.flush_receive()
            end
            
            if (obj.qlabs.send_container(obj.c))
            
                if waitForConfirmation
                    rc = obj.qlabs.wait_for_container(obj.c.ID_GENERIC_ACTOR_SPAWNER, 0, obj.c.FCN_GENERIC_ACTOR_SPAWNER_PARENT_CURRENT_WORLD_ACK);
                    if isempty(rc)
                        if (obj.verbose)
                            fprintf('parent_with_current_world_transform: Communication timeout (classID %u, actorNumber %u).\n', obj.classID, obj.actorNumber);
                        end
                        return
                        
                    end
                    
                    if length(rc.payload) == 1
                        status = rc.payload(1);

                        if (status == 0)
                            return
    
                        elseif (obj.verbose)
                            if (status == 1)
                                fprintf('parent_with_current_world_transform (classID %u, actorNumber %u): Class not available.\n', obj.classID, obj.actorNumber);
                            elseif (status == 2)
                                fprintf('parent_with_current_world_transform (classID %u, actorNumber %u):  Cannot find parent (classID %u, actorNumber %u).\n', obj.classID, obj.actorNumber, parentClassID, parentActorNumber);
                            elseif (status == -1)
                                fprintf('parent_with_current_world_transform (classID %u, actorNumber %u): Communication error.\n', obj.classID, obj.actorNumber);
                            else
                                fprintf('parent_with_current_world_transform (classID %u, actorNumber %u): Unknown error.\n', obj.classID, obj.actorNumber);
                            end
                        end
                        
                    else
                        if (obj.verbose)
                            fprintf('parent_with_current_world_transform (classID %u, actorNumber %u): Communication error.\n', obj.classID, obj.actorNumber);
                        end

                    end
                    return;
                end
                status = 0;
            else
                if (obj.verbose)
                    fprintf('parent_with_current_world_transform: Communication failed (classID %u, actorNumber %u).\n', obj.classID, obj.actorNumber);
                end

            end
        end        

        %%
        function status = parent_break(obj, waitForConfirmation)
            % Breaks any relationship with a parent actor (if it exists) and preserves the current world transform
    
            obj.c.classID = obj.c.ID_GENERIC_ACTOR_SPAWNER;
            obj.c.actorNumber = 0;
            obj.c.actorFunction = obj.c.FCN_GENERIC_ACTOR_SPAWNER_PARENT_BREAK_WITH_CURRENT_WORLD;
            obj.c.payload = [flip(typecast(int32(obj.classID), 'uint8')) ...
                         flip(typecast(int32(obj.actorNumber), 'uint8'))];
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);
    

            if waitForConfirmation
                obj.qlabs.flush_receive()
            end
            
            if (obj.qlabs.send_container(obj.c))
            
                if waitForConfirmation
                    rc = obj.qlabs.wait_for_container(obj.c.ID_GENERIC_ACTOR_SPAWNER, 0, obj.c.FCN_GENERIC_ACTOR_SPAWNER_PARENT_BREAK_WITH_CURRENT_WORLD_ACK);
                    if isempty(rc)
                        if (obj.verbose)
                            fprintf('parent_break: Communication timeout (classID %u, actorNumber %u).\n', obj.classID, obj.actorNumber);
                        end
                        return
                        
                    end
                    
                    if length(rc.payload) == 1
                        status = rc.payload(1);

                        if (status == 0)
                            return
    
                        elseif (obj.verbose)
                            if (status == 1)
                                fprintf('parent_break (classID %u, actorNumber %u): Cannot find this actor.\n', obj.classID, obj.actorNumber);
                            else
                                fprintf('parent_break (classID %u, actorNumber %u): Unknown error.\n', obj.classID, obj.actorNumber);
                            end
                        end
                        
                    else
                        if (obj.verbose)
                            fprintf('parent_break (classID %u, actorNumber %u): Communication error.\n', obj.classID, obj.actorNumber);
                        end

                    end
                    return;
                end
                status = 0;
            else
                if (obj.verbose)
                    fprintf('parent_break: Communication failed (classID %u, actorNumber %u).\n', obj.classID, obj.actorNumber);
                end

            end
        end

        %%
        function success = set_custom_properties(obj, measuredMass, IDTag, properties, waitForConfirmation)
            % Assigns custom properties to an actor.

            arguments
                obj qlabs_actor
                measuredMass single = 0.0
                IDTag int32 = 0
                properties string = ""
                waitForConfirmation logical = true
            end    

            if (not(obj.is_actor_number_valid()))
                return 
            end            
    
            obj.c.classID = obj.classID;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_SET_CUSTOM_PROPERTIES;
            obj.c.payload = [flip(typecast(int32(measuredMass), 'single')) ...
                             flip(typecast(int32(IDTag), 'uint8')) ...
                             flip(typecast(int32(length(char(properties)), 'uint8'))) ...
                             uint8(char(properties))];
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);
    
            success = false;

            if waitForConfirmation
                obj.qlabs.flush_receive()
            end
            
            if (obj.qlabs.send_container(obj.c))
            
                if waitForConfirmation
                    rc = obj.qlabs.wait_for_container(obj.c.ID_GENERIC_ACTOR_SPAWNER, 0, obj.c.FCN_SET_CUSTOM_PROPERTIES_ACK);
                    if isempty(rc)
                        if (obj.verbose)
                            fprintf('set_custom_properties: Communication timeout (classID %u, actorNumber %u).\n', obj.classID, obj.actorNumber);
                        end
                        return
                        
                    end
                end
                
                success = true;
                return;
            
            else
                if (obj.verbose)
                    fprintf('set_custom_properties: Communication failed (classID %u, actorNumber %u).\n', obj.classID, obj.actorNumber);
                end

            end
        end


        %%
        function [success, measuredMass, IDTag, properties] = get_custom_properties(obj)
            % Gets previously assigned custom properties to an actor.
    
            measuredMass = 0.0;
            IDTag = 0;
            properties = "";
            success = false;
    
            if (not(obj.is_actor_number_valid()))
                return 
            end

            obj.c.classID = obj.classID;
            obj.c.actorNumber = obj.actorNumber;
            obj.c.actorFunction = obj.FCN_REQUEST_CUSTOM_PROPERTIES;
            obj.c.payload = [];
            obj.c.containerSize = obj.c.BASE_CONTAINER_SIZE + length(obj.c.payload);
    

            obj.qlabs.flush_receive()
            
            if (obj.qlabs.send_container(obj.c))
            
                rc = obj.qlabs.wait_for_container(obj.c.ID_GENERIC_ACTOR_SPAWNER, 0, obj.c.FCN_RESPONSE_CUSTOM_PROPERTIES);
                if isempty(rc)
                    if (obj.verbose)
                        fprintf('get_custom_properties: Communication timeout (classID %u, actorNumber %u).\n', obj.classID, obj.actorNumber);
                    end
                    return
                    
                elseif  length(rc.payload) >= 12
                    measuredMass = typecast(flip(rc.payload(1:4)), 'single');
                    IDTag = typecast(flip(rc.payload(5:8)), 'int32');
                    stringLength = typecast(flip(rc.payload(9:12)), 'int32');
    
                    if (stringLength > 0)
                        if (length(rc.payload) == 12 + stringLength)
                            properties = char(rc.payload(13:(13+stringLength)));
                        else
                            if (obj.verbose)
                                fprintf('get_custom_properties: Custom string properties length does not match packet size (classID %u, actorNumber %u).\n', obj.classID, obj.actorNumber);
                            end
                        end
                    end
                    
                    success = true;
                    return
                else
                    if (obj.verbose)
                        fprintf('get_custom_properties: Custom properties data not the expected size (classID %u, actorNumber %u).\n', obj.classID, obj.actorNumber);
                    end
                    return
                end
                    
            else
                if (obj.verbose)
                    fprintf('get_custom_properties: Communication failed (classID %u, actorNumber %u).\n', obj.classID, obj.actorNumber);
                end

            end
        end


    end % end of methods


    
end


