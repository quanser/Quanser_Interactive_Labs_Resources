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

fprintf('\n\n----------------- Communications -------------------\n\n');

qlabs = QuanserInteractiveLabs();
connection_established = qlabs.open('localhost');

if connection_established == false
    disp("Failed to open connection.")
    return
end


disp('Connected')

num_destroyed = qlabs.destroy_all_spawned_actors();

fprintf('%d actors destroyed', num_destroyed);

% Use hSystem to set the tutorial title on the qlabs display screen
hSystem = QLabsSystem(qlabs);
hSystem.set_title_string('Traffic Lights Tutorial')

% Initialize a camera
cameraTraffic = QLabsFreeCamera(qlabs);
cameraTraffic.spawn([0.131, 2.05, 2.047], [0, -0.068, 1.201]);
cameraTraffic.possess();

% Initialize three traffic light instances in qlabs
trafficLight = QLabsTrafficLight(qlabs);
trafficLight2 = QLabsTrafficLight(qlabs);
trafficLight3 = QLabsTrafficLight(qlabs);

% Initialize two crosswalk instances in qlabs 
crosswalk = QLabsCrosswalk(qlabs);
crosswalk1 = QLabsCrosswalk(qlabs);

% Spawn a traffic light in config 1 - vertical using radians and specifying a specific actorNumber
trafficLight.spawn_id(0, [5.616, 14.131, 0.215], [0, 0, 0], [1, 1, 1], 0, 1);

% Spawn a second traffic light using degrees in config 1 - vertical and specifying a specific actorNumber
trafficLight2.spawn_id_degrees(2, [-3.078, 14.136, 0.215], [0, 0, 180], [1, 1, 1], 1, 1);

% Spawn traffic light using degrees in config 2 - horizontal and generating the actorNumber internally
trafficLight3.spawn_degrees([6.703, 5.6, 0.215], [0, 0, -90], [1, 1, 1], 2, 1);

pause(0.5);

% Spawn crosswalk with radians in configuration 0
crosswalk.spawn_id(0, [1.3, 16.7, 0.005], [0, 0, 0], [1, 1, 1], 0, 1);

pause(1);

% Spawn crosswalk with radians in configuration 1
crosswalk1.spawn_id(1, [8.5, 10.21, 0.01], [0, 0, pi/2], [1, 1, 1], 1, 1);

% Changing the state of the traffic lights from green to red
pause(2);

trafficLight.set_state(trafficLight.STATE_YELLOW, 1);
trafficLight2.set_state(trafficLight2.STATE_YELLOW, 1);

pause(1);

trafficLight.set_state(trafficLight.STATE_RED, 1);
trafficLight2.set_state(trafficLight2.STATE_RED, 1);

pause(1);

trafficLight3.set_state(trafficLight3.STATE_GREEN, 1);

% Destroying a traffic light
trafficLight.destroy();

pause(1);

% Destroy the first crosswalk 
crosswalk.destroy();

pause(1);

% Destroy the first crosswalk 
crosswalk1.destroy();

% Closing qlabs
qlabs.close();
disp('Done!');