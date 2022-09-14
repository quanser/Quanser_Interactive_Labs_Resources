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
fprintf('Stop sign return (expect 0): %d\n', status);

status = StopSign.spawn_id(qlabs, 0, [-17, 37, 0.0], [0,0,pi], [1,1,1], true);
fprintf('Duplicate stop sign return (expect 2): %d\n', status);

[status, hStopSign] = StopSign.spawn(qlabs, [-18, 37, 0.0], [0,0,pi], [1,1,1], true);
fprintf('Autogenerate stopsign ID (expect 0): %d, actor number: %d\n', status, hStopSign);



fprintf('\n\n------------------------------ Communications --------------------------------\n');

qlabs.close();
disp('All done!');