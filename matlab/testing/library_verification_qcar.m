function library_verification_qcar()
    close all;
    clear all;
    clc;
    addpath('../qvl')
    
    fprintf('\n\n------------------------------ Communications --------------------------------\n\n');
    
    qlabs = quanser_interactive_labs;
    connection_established = qlabs.open('192.168.1.142');
    
    if connection_established == false
        disp("Failed to open connection.")
        return
    end

   
    disp('Connected')
    
    num_destroyed = qlabs.destroy_all_spawned_actors();
    
    fprintf('%d actors destroyed', num_destroyed);
    
    
    fprintf('\n\n-------------------------------- Stop Sign ----------------------------------\n\n');
    % Spawn two signs
    StopSign = qlabs_stop_sign(qlabs, true);
    status = StopSign.spawn_id(0, [1.193, 9.417, 0.005], [0,0,pi], [1,1,1], true);
    eval(status, 0, 'StopSign.spawn_id 0')
    
    status = StopSign.spawn_id(1, [1.193, 7.417, 0.005], [0,0,pi], [1,1,1], true);
    eval(status, 0, 'StopSign.spawn_id 1')
    
    % Destroy most recent
    status = StopSign.destroy();
    eval(status, 1, 'StopSign.destroy 1')

    % Second destroy should fail
    status = StopSign.destroy();
    eval(status, -1, 'StopSign.destroy 1')

    % Manually assign actor number then destory again
    StopSign.actorNumber = 0;
    status = StopSign.destroy();
    eval(status, 1, 'StopSign.destroy 0')

    % Spawn again with degrees
    status = StopSign.spawn_id_degrees(0, [1.193, 9.417, 0.005], [0,0,180], [1,1,1], true);
    eval(status, 0, 'StopSign.spawn_id_degrees 0')

    % Spawn with actor number auto-allocated
    [status, actorNumber] = StopSign.spawn([1.193, 7.417, 0.005], [0,0,pi], [1,1,1], true);
    eval(status, 0, 'StopSign.spawn (status)')
    eval(actorNumber, 1, 'StopSign.spawn (actorNumber)')

    % Spawn with actor number auto-allocated
    [status, actorNumber] = StopSign.spawn_degrees([1.193, 5.417, 0.005], [0,0,180], [1,1,1], true);
    eval(status, 0, 'StopSign.spawn (status)')
    eval(actorNumber, 2, 'StopSign.spawn (actorNumber)')    
    
    
    
    fprintf('\n\n------------------------------ Communications --------------------------------\n');
    
    qlabs.close();
    disp('All done!');
end

function eval(return_value, expected_value, message)

    if (return_value == expected_value)
        fprintf('Good: %s (expected %d): %d\n', message, expected_value, return_value)
    else
        fprintf('*** ERROR: %s (expected %d): %d\n', message, expected_value, return_value)
    end
end