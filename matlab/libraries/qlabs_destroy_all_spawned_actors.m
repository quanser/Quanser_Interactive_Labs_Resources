function num_destroyed = qlabs_destroy_all_spawned_actors(qlabs)
    num_destroyed = 0;
    device_num = 0;

    c = qlabs_comm_modular_container();

    c.class_id = c.ID_GENERIC_ACTOR_SPAWNER;
    c.actor_number = device_num;
    c.actor_function = c.FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ALL_SPAWNED_ACTORS;
    c.payload = [];
    c.container_size = 13 + length(c.payload);

    if (qlabs.send_container(c))
        c = qlabs.wait_for_container(c.ID_GENERIC_ACTOR_SPAWNER, device_num, c.FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ALL_SPAWNED_ACTORS_ACK);
        num_destroyed = typecast(flip(c.payload), 'int32');
    end
end