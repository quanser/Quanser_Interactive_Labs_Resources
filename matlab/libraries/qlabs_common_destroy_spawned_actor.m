function num_destroyed = qlabs_common_destroy_spawned_actor(qlabs, class_id, actor_number)
    num_destroyed = 0;

    c = qlabs_comm_modular_container();

    c.class_id = c.ID_GENERIC_ACTOR_SPAWNER;
    c.actor_number = 0;
    c.actor_function = c.FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ACTOR;
    c.payload = [flip(typecast(int32(class_id), 'uint8')) ...
                 flip(typecast(int32(actor_number), 'uint8'))];
    c.container_size = c.BASE_CONTAINER_SIZE + length(c.payload);

    if (qlabs.send_container(c))
        c = qlabs.wait_for_container(c.ID_GENERIC_ACTOR_SPAWNER, 0, c.FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ACTOR_ACK);
        if isempty(c)
            num_destroyed = -1;
        else
            num_destroyed = typecast(flip(c.payload), 'int32');
        end
    end
end