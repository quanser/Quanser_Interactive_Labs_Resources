classdef quanser_interactive_labs < handle
    properties
        %server_stream = []
        %client_connection = []
        qlabs_stream = []
        
        BUFFER_SIZE = 65537

        read_buffer = [];
        send_buffer = [];

        receive_packet_buffer = [];
        receive_packet_size = 0;
        receive_packet_container_index = 0;
    end
    methods
        function success = open(obj, hostname)
            success = false;            
            
            % create a client connection
            obj.qlabs_stream = stream_connect(['tcpip://' hostname ':18000'], true);
            
            % see if you could accept a connection with a timeout of 5s
            while (stream_poll(obj.qlabs_stream, 5, 'connect') == false)

            end
            
            if (stream_poll(obj.qlabs_stream, 5, 'connect') == false)
                success = false;
            else
                success = true;
            end
        end
        
        function close(obj)
            if ~isempty(obj.qlabs_stream)
                stream_shutdown(obj.qlabs_stream);
                stream_close(obj.qlabs_stream);
                obj.qlabs_stream = [];
            end
        end
        
        function delete(obj)
            obj.close()  
        end
        
        function success = send_container(obj, container)
            
            byte_data = [typecast(int32(container.container_size+1), 'uint8') ...
                         uint8(123) ...
                         flip(typecast(int32(container.container_size), 'uint8')) ...
                         flip(typecast(int32(container.class_id), 'uint8')) ...
                         flip(typecast(int32(container.device_number), 'uint8')) ...
                         uint8(container.device_function) ...
                         container.payload];
            
                     
            [is_sent, would_block] = stream_send_array(obj.qlabs_stream, byte_data);           
            stream_flush(obj.qlabs_stream);
            success = is_sent;
        end
        
        
        
        function new_data = receive_new_data(obj)
            new_data = false;

            [data, would_block] = stream_receive_int8s(obj.qlabs_stream, obj.BUFFER_SIZE);
            bytes_read = length(data);
            data = typecast(data, 'uint8');


            while bytes_read > 0
                
                obj.receive_packet_buffer = [obj.receive_packet_buffer data];


                [data, would_block] = stream_receive_int8s(obj.qlabs_stream, obj.BUFFER_SIZE);
                bytes_read = length(data);
                
            end

            
            if length(obj.receive_packet_buffer) > 5
                if (obj.receive_packet_buffer(5) == 123)

                    obj.receive_packet_size = typecast(uint8(obj.receive_packet_buffer(1:4)), 'int32');
                    obj.receive_packet_size = obj.receive_packet_size + 4;


                    if length(obj.receive_packet_buffer) >= obj.receive_packet_size

                        obj.receive_packet_container_index = 6;
                        new_data = true;
                    end

                else
                    %print("Error parsing multiple packets in receive buffer.  Clearing internal buffers.")
                    obj.receive_packet_buffer = [];
                end

            end
        end
        
        function [c, is_more_containers] = get_next_container(obj)
            c = comm_modular_container();
            is_more_containers = false;

%             fprintf('In container parsing...\n');
            if (obj.receive_packet_container_index > 0)
%                 fprintf('Container index > 0...\n');
                
                c.container_size  = typecast(uint8(flip(obj.receive_packet_buffer(obj.receive_packet_container_index+0:obj.receive_packet_container_index+3))), 'int32');
                c.class_id        = typecast(uint8(flip(obj.receive_packet_buffer(obj.receive_packet_container_index+4:obj.receive_packet_container_index+7))), 'int32');
                c.device_number   = typecast(uint8(flip(obj.receive_packet_buffer(obj.receive_packet_container_index+8:obj.receive_packet_container_index+11))), 'int32');
                c.device_function = uint8(obj.receive_packet_buffer(obj.receive_packet_container_index+12));
                
%                 fprintf('Container size: %d\n', c.container_size);
%                 fprintf('Class ID: %d\n', c.class_id);
%                 fprintf('Device num: %d\n', c.device_number);
%                 fprintf('Device fcn: %d\n', c.device_function);
                
                
                PayloadStart = obj.receive_packet_container_index+13;
                PayloadEnd = obj.receive_packet_container_index + c.container_size - 1;
                
                c.payload = obj.receive_packet_buffer(PayloadStart:PayloadEnd);

                obj.receive_packet_container_index = obj.receive_packet_container_index + c.container_size;

                if (obj.receive_packet_container_index >= obj.receive_packet_size)

                    is_more_containers = false;

                    if length(obj.receive_packet_buffer) == obj.receive_packet_size
                        % The data buffer contains only the one packet.  Clear the buffer.
                        obj.receive_packet_buffer = [];
                    else
                        % Remove the packet from the data buffer.  There is another packet in the buffer already.
                        obj.receive_packet_buffer = obj.receive_packet_buffer((obj.receive_packet_container_index):(length(obj.receive_packet_buffer)));
                    end
                    
                    obj.receive_packet_container_index = 0;

                else
                    is_more_containers = true;
                end


            end
        end
                    
        
        function container = wait_for_container(obj, class_id, device_num, function_num)
            container = [];
            
            while(true)
%                 fprintf('Receive new data... ');
                while (obj.receive_new_data() == false)
                    
                end

%                 fprintf('Got data (%d bytes).\n', length(obj.receive_packet_buffer));
                more_containers = true;

                while (more_containers)
                    [c, more_containers] = obj.get_next_container();
%                     fprintf('Got container:\n')
%                     fprintf('class ID: %d\n', c.class_id)
%                     fprintf('device_number: %d\n', c.device_number)
%                     fprintf('device_function: %d\n', c.device_function)

                    if c.class_id == class_id
                        if c.device_number == device_num
                            if c.device_function == function_num
                                container = c;
                                return;
                            end
                        end
                    end
                end
            end
        end
        
        function num_destroyed = destroy_all_spawned_actors(obj)
            num_destroyed = 0;
            device_num = 0;
            
            c = comm_modular_container();

            c.class_id = c.ID_GENERIC_ACTOR_SPAWNER;
            c.device_number = device_num;
            c.device_function = c.FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ALL_SPAWNED_ACTORS;
            c.payload = [];
            c.container_size = 13 + length(c.payload);
            
            if (obj.send_container(c))
                c = obj.wait_for_container(c.ID_GENERIC_ACTOR_SPAWNER, device_num, c.FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ALL_SPAWNED_ACTORS_ACK);
                num_destroyed = typecast(flip(c.payload), 'int32');
            end
        end
        
        function flush_receive(obj)
            % get any data still in the receive buffer out
            
            [data, would_block] = stream_receive_int8s(obj.qlabs_stream, obj.BUFFER_SIZE);
            bytes_read = length(data);
        end
        
        function c = spawn(obj, device_num, ID, location, rotation, scale, configuration, wait_for_confirmation)
            c = comm_modular_container();
            c.class_id = c.ID_GENERIC_ACTOR_SPAWNER;
            c.device_number = 0;
            c.device_function = c.FCN_GENERIC_ACTOR_SPAWNER_SPAWN;
            
            
            c.payload = [flip(typecast(int32(ID), 'uint8')) ...
                         flip(typecast(int32(device_num), 'uint8')) ...
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

            c.container_size = 13 + length(c.payload);

            if wait_for_confirmation
                obj.flush_receive()
            end

            if (obj.send_container(c))

                if wait_for_confirmation
                    c = obj.wait_for_container(c.ID_GENERIC_ACTOR_SPAWNER, 0, c.FCN_GENERIC_ACTOR_SPAWNER_SPAWN_ACK);
                    return;
                end
                
            end
            
            c = [];
        end

    end
end