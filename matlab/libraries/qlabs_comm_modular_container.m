classdef qlabs_comm_modular_container < handle
    properties
        container_size = 0;
        class_id = 0;       % What device type is this?
        device_number = 0;   % Increment if there are more than one of the same device ID
        device_function = 0; % Command/reponse
        payload = [];


        ID_GENERIC_ACTOR_SPAWNER = 135;
        FCN_GENERIC_ACTOR_SPAWNER_SPAWN_ID = 10;
        FCN_GENERIC_ACTOR_SPAWNER_SPAWN_ID_ACK = 11;
        FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ACTOR = 12;
        FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ACTOR_ACK = 13;
        FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ALL_SPAWNED_ACTORS = 14;
        FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ALL_SPAWNED_ACTORS_ACK = 15;
        FCN_GENERIC_ACTOR_SPAWNER_REGENERATE_CACHE_LIST = 16;
        FCN_GENERIC_ACTOR_SPAWNER_REGENERATE_CACHE_LIST_ACK = 17;
		FCN_GENERIC_ACTOR_SPAWNER_SPAWN = 22;
        FCN_GENERIC_ACTOR_SPAWNER_SPAWN_ACK = 23;
        
        ID_UE4_SYSTEM = 1000;

        ID_SIMULATION_CODE = 1001;
        FCN_SIMULATION_CODE_RESET = 200;

        ID_UNKNOWN = 0;

        FCN_UNKNOWN = 0
        FCN_REQUEST_PING = 1
        FCN_RESPONSE_PING = 2
        FCN_REQUEST_WORLD_TRANSFORM = 3
        FCN_RESPONSE_WORLD_TRANSFORM = 4
    end
end