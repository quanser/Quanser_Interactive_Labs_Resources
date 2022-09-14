function [status, actor_number] = qlabs_common_spawn(qlabs, class_id, location, rotation, scale, configuration, wait_for_confirmation)
    c = qlabs_comm_modular_container();
    c.class_id = c.ID_GENERIC_ACTOR_SPAWNER;
    c.actor_number = 0;
    c.actor_function = c.FCN_GENERIC_ACTOR_SPAWNER_SPAWN;


    c.payload = [flip(typecast(int32(class_id), 'uint8')) ...
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
	
	status = -1;
	actor_number = -1;

    if wait_for_confirmation
        qlabs.flush_receive();
    end

    if (qlabs.send_container(c))

        if wait_for_confirmation
            c = qlabs.wait_for_container(c.ID_GENERIC_ACTOR_SPAWNER, 0, c.FCN_GENERIC_ACTOR_SPAWNER_SPAWN_ACK);
			if isempty(c)
				status = -1;
				return
				
			end
			
			if length(c.payload) == 5
				status = c.payload(1);
				actor_number = typecast(uint8(flip(c.payload(2:5))), 'int32');
			else
				status = -1;
			end
            return;
        end

    end

end