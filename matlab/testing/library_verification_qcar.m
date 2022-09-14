function library_verification_qcar()
    close all;
    clear all;
    clc;
    addpath('../libraries')
    
    fprintf('\n\n------------------------------ Communications --------------------------------\n\n');
    
    qlabs = quanser_interactive_labs;
    connection_established = qlabs.open('localhost');
    
    if connection_established == false
        disp("Failed to open connection.")
        return
    end
    
    disp('Connected')
    
    num_destroyed = qlabs_destroy_all_spawned_actors(qlabs);
    fprintf('%d actors destroyed', num_destroyed);
    
    
    fprintf('\n\n-------------------------------- Stop Sign ----------------------------------\n\n');
    StopSign = qlabs_stop_sign;
    status = StopSign.spawn_id(qlabs, 0, [-17, 37, 0.0], [0,0,pi], [1,1,1], true);
    eval(status, 0, 'StopSign.spawn_id')
    
    status = StopSign.spawn_id(qlabs, 0, [-17, 37, 0.0], [0,0,pi], [1,1,1], true);
    eval(status, 2, 'StopSign.spawn_id duplicate')
    
    status = StopSign.spawn_id_degrees(qlabs, 1, [-18, 37, 0.0], [0,0,180], [1,1,1], true);
    eval(status, 0, 'StopSign.spawn_id_degrees')
        
    [status, hStopSign] = StopSign.spawn(qlabs, [-19, 37, 0.0], [0,0,pi], [1,1,1], true);
    eval(status, 0, 'StopSign.spawn')
    fprintf(' Actor number: %d', hStopSign)
    
    [status, hStopSignB] = StopSign.spawn_degrees(qlabs, [-20, 37, 0.0], [0,0,180], [1,1,1], true);
    eval(status, 0, 'StopSign.spawn_degrees')
    fprintf(' Actor number: %d', hStopSign)
    
    status = StopSign.destroy(qlabs, hStopSignB);
    eval(status, 1, 'StopSign.destroy')
    
    
    
    fprintf('\n\n------------------------------ Communications --------------------------------\n');
    
    qlabs.close();
    disp('All done!');
end

function eval(return_value, expected_value, message)

    if (return_value == expected_value)
        fprintf('\nGood: %s (expected %d): %d', message, expected_value, return_value)
    else
        fprintf('\n*** ERROR: %s (expected %d): %d', message, expected_value, return_value)
    end
end