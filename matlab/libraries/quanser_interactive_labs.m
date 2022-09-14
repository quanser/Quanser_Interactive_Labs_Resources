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
		
		wait_for_container_timeout = 5;
    end
    
    methods
%%        
        function success = open(obj, hostname, timeout)     
            

            if nargin > 2
              defaultTimeout = timeout;
            else
              defaultTimeout = 10;
            end            
            
            % create a client connection
            obj.qlabs_stream = stream_connect(['tcpip://' hostname ':18000'], true);
            
            poll_result = stream_poll(obj.qlabs_stream, 1, 'connect');
            while ((poll_result == false) && (defaultTimeout > 0))
                poll_result = stream_poll(obj.qlabs_stream, 1, 'connect');
                defaultTimeout = defaultTimeout - 1;
            end
            
            success = poll_result;
            
        end
%%        
        function close(obj)
            if ~isempty(obj.qlabs_stream)
                stream_shutdown(obj.qlabs_stream);
                stream_close(obj.qlabs_stream);
                obj.qlabs_stream = [];
            end
        end
%%        
        function delete(obj)
            obj.close()  
        end
        
%%        
        function success = send_container(obj, container)
            
            byte_data = [typecast(int32(container.container_size+1), 'uint8') ...
                         uint8(123) ...
                         flip(typecast(int32(container.container_size), 'uint8')) ...
                         flip(typecast(int32(container.class_id), 'uint8')) ...
                         flip(typecast(int32(container.actor_number), 'uint8')) ...
                         uint8(container.actor_function) ...
                         container.payload];
            
                     
            [is_sent, would_block] = stream_send_array(obj.qlabs_stream, byte_data);           
            stream_flush(obj.qlabs_stream);
            success = is_sent;
        end
        
        
%%        
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
%%        
        function [c, is_more_containers] = get_next_container(obj)
            c = qlabs_comm_modular_container();
            is_more_containers = false;

            if (obj.receive_packet_container_index > 0)
                
                c.container_size  = typecast(uint8(flip(obj.receive_packet_buffer(obj.receive_packet_container_index+0:obj.receive_packet_container_index+3))), 'int32');
                c.class_id        = typecast(uint8(flip(obj.receive_packet_buffer(obj.receive_packet_container_index+4:obj.receive_packet_container_index+7))), 'int32');
                c.actor_number   = typecast(uint8(flip(obj.receive_packet_buffer(obj.receive_packet_container_index+8:obj.receive_packet_container_index+11))), 'int32');
                c.actor_function = uint8(obj.receive_packet_buffer(obj.receive_packet_container_index+12));
                
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
          
%%
		function set_wait_for_container_timeout(obj, timeout)
		
			if (timeout < 0)
				timeout = 0;
			end
			
			obj.wait_for_container_timeout = timeout;
		
		end
          
%%        
        function container = wait_for_container(obj, class_id, device_num, function_num)
            container = [];
            
			tic
			
            while(true)
                while (obj.receive_new_data() == false)
				
					if toc > obj.wait_for_container_timeout
						return
					end
                    
                end

                more_containers = true;

                while (more_containers)
                    [c, more_containers] = obj.get_next_container();

                    if c.class_id == class_id
                        if c.actor_number == device_num
                            if c.actor_function == function_num
                                container = c;
                                return;
                            end
                        end
                    end
                end
            end
        end
    

%%        
        function flush_receive(obj)
            % get any data still in the receive buffer out
            
            [data, would_block] = stream_receive_int8s(obj.qlabs_stream, obj.BUFFER_SIZE);
            bytes_read = length(data);
        end
  

    end
end