% Road signage Library Traffic Lights Example
% -------------------------
% 
% .. note::
% 
%     Make sure you have Quanser Interactive Labs open before running this
%     example.  This example is designed to best be run in QCar Cityscape
%     or Cityscape Lite.

close all;
clear all;
clc;

% --------------------------------------------------------------
% Setting MATLAB Path for the libraries
% Always keep at the start, it will make sure it finds the correct references
newPathEntry = fullfile(getenv('QAL_DIR'), 'libraries', 'matlab', 'qvl');
pathCell = regexp(path, pathsep, 'split');
if ispc  % Windows is not case-sensitive
  onPath = any(strcmpi(newPathEntry, pathCell));
else
  onPath = any(strcmp(newPathEntry, pathCell));
end

if onPath == 0
    path(path, newPathEntry)
    savepath
end
% --------------------------------------------------------------

qlabs = QuanserInteractiveLabs();
connection_established = qlabs.open('localhost');

if connection_established == false
    disp("Failed to open connection.")
    return
end


disp('Connected')

num_destroyed = qlabs.destroy_all_spawned_actors();

fprintf('%d actors destroyed', num_destroyed);


% Initialize a camera
cameraTraffic = QLabsFreeCamera(qlabs);
cameraTraffic.spawn([0.131, 2.05, 2.047], [0, -0.068, 1.201]);
cameraTraffic.possess();

% Initialize three traffic light instances in qlabs
trafficLight1 = QLabsTrafficLight(qlabs);
trafficLight2 = QLabsTrafficLight(qlabs);
trafficLight3 = QLabsTrafficLight(qlabs);


% Spawn a traffic light in config 1 - vertical using radians and specifying a specific actorNumber
trafficLight1.spawn_id(0, [5.616, 14.131, 0.215], [0, 0, 0], [1, 1, 1], 0, 1);
trafficLight1.set_color(trafficLight1.COLOR_GREEN);

% Spawn a second traffic light using degrees in config 1 - vertical and specifying a specific actorNumber
trafficLight2.spawn_id_degrees(2, [-3.078, 14.136, 0.215], [0, 0, 180], [1, 1, 1], 1, 1);
trafficLight2.set_color(trafficLight2.COLOR_GREEN);

% Spawn traffic light using degrees in config 2 - horizontal and generating the actorNumber internally
trafficLight3.spawn_degrees([6.703, 5.6, 0.215], [0, 0, -90], [1, 1, 1], 2, 1);
trafficLight3.set_color(trafficLight3.COLOR_RED);


% Changing the state of the traffic lights from green to red
pause(2);

trafficLight1.set_color(trafficLight1.COLOR_YELLOW);
trafficLight2.set_color(trafficLight2.COLOR_YELLOW);

pause(1);

trafficLight1.set_color(trafficLight1.COLOR_RED);
trafficLight2.set_color(trafficLight2.COLOR_RED);

pause(1);

trafficLight3.set_color(trafficLight3.COLOR_GREEN);

% Closing qlabs
qlabs.close();
disp('Done!');