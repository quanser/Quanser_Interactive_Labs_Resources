% QCar 2 Library Example
% -------------------------
% This example will show you how to spawn cars, and use the qvl library commands
% to control the car and its related functions.
% 
% .. note::
% 
%     Make sure you have Quanser Interactive Labs open before running this
%     example.  This example is designed to best be run in QCar Cityscape.


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

% Use hSystem to set the tutorial title in the upper left of the qlabs window 
hSystem = QLabsSystem(qlabs);
hSystem.set_title_string('QCar Tutorial')

% Initialize QLabs
hCameraQCars = QLabsFreeCamera(qlabs);
hCameraQCars.spawn_id(1, [-15.075, 26.703, 6.074], [0, 0.564, -1.586]);
hCameraQCars.possess();

disp('---QCar---');

% Spawning the QCar with radians
hQCar0 = QLabsQCar2(qlabs);
hQCar0.spawn_id(0, [-8.700, 14.643, 0.005], [0, 0, pi/2], 1);

% Spawn and destroy the existing QCar
hQCar1 = QLabsQCar2(qlabs);
hQCar1.spawn_id(1, [-15.075, 26.703, 6.074], [0, 0, pi/2], 1);
hQCar1.destroy();

% Spawn a QCar with degrees
hQCar2 = QLabsQCar2(qlabs);
x = hQCar2.spawn_id_degrees(2, [-11.048, 14.643, 0.005], [0, 0, 90], 1);

% Pinging the QCar
hQCar2.ping();



% Set the velocity and direction of the QCar in radians while also turning on the headlights and right turn signal
hQCar2.set_velocity_and_request_state(1, -pi/6, true, false, true, false, false);
pause(1);

% Set the velocity to 0 and direction of the QCar in radians while keeping the headlights on and right turn signal on
hQCar2.set_velocity_and_request_state(0.0, -pi/6, true, false, true, false, false);

% Set the velocity to 1 and direction of the QCar in degrees while keeping the headlights on and turning on the left turn signal
hQCar2.set_velocity_and_request_state_degrees(1, 30, true, true, false, false, false);
pause(1);

% Set the velocity to 0 and direction of the QCar in degrees while keeping the headlights on and left turn signal on
[success, location, rotation, frontHit, rearHit] = hQCar2.set_velocity_and_request_state_degrees(0.0, 30, true, true, false, false, false);

% Possess another QCar
x = hQCar2.possess();

pause(0.1);

% Set the velocity to 1 of the QCar in radians while keeping the headlights, brakeSignal and reverseSignal on
hQCar2.set_velocity_and_request_state(1, 0, true, true, true, true, true);
pause(1);

% Set the velocity to 0 while keeping the headlights, brakeSignal and reverseSignal on and turning on the left turn signal and right turn signal
hQCar2.set_velocity_and_request_state(0.0, 0, true, true, true, true, true);

% Turn all the lights off
hQCar2.set_velocity_and_request_state(0, 0, false, false, false, false, false);

% Car bumper test
hCameraQCars.possess();

% Change the camera view to see the bumper test
hCameraQCars.set_transform([-17.045, 32.589, 6.042], [0, 0.594, -1.568]);

% Spawn some shapes for our bumper test
hCubeQCarBlocks = QLabsBasicShape(qlabs);
hCubeQCarBlocks.spawn_id(100, [-11.919, 26.289, 0.5], [0, 0, 0], [1, 1, 1], hCubeQCarBlocks.SHAPE_CUBE, true);
hCubeQCarBlocks.spawn_id(101, [-19.919, 26.289, 0.5], [0, 0, 0], [1, 1, 1], hCubeQCarBlocks.SHAPE_CUBE, true);

% Create another QCar
hQCar3 = QLabsQCar2(qlabs);
hQCar3.spawn_id(3, [-13.424, 26.299, 0.005], [0, 0, pi]);

% Have the QCar drive forward to hit the front block
for count = 1:10
    [x, location, rotation, frontHit, rearHit] = hQCar3.set_velocity_and_request_state(2, 0, false, false, false, false, false);
    pause(0.25);
end

% Put the QCar in ghost mode
hQCar3.ghost_mode();

% Have the QCar drive backwards to hit the back bumper
for count = 1:10
    [x, location, rotation, frontHit, rearHit] = hQCar3.set_velocity_and_request_state(-2, 0, false, false, false, false, false);
    pause(0.25);
end

% Change the color of ghost mode to red
hQCar3.ghost_mode(true, [1, 0, 0]);
pause(0.5);


% Set the velocity to 0 and turn all lights off
hQCar3.set_velocity_and_request_state(0, 0, false, false, false, false, false);

% Set the location of the QCar and request the state of the car. 
% If x== True and frontHit==True then the front bumper hit the block correctly.
[x, location, rotation, forward_vector, up_vector, frontHit, rearHit] = ...
    hQCar3.set_transform_and_request_state([-16.1, 26.299, 0.005], [0, 0, pi-0.01], ...
    true, false, false, false, false, false);
pause(0.5);

% Getting and saving the world transform of the QCar in Quanser Interactive Labs
[x, loc, rot, scale] = hQCar3.get_world_transform();

% Set the location of the QCar and request the state of the car.
% If x== True and rearHit==True then the back bumper hit the block correctly.
[x, location, rotation, forward_vector, up_vector, frontHit, rearHit] = ...
    hQCar3.set_transform_and_request_state_degrees([-13.1, 26.299, 0.005], ...
    [0, 0, 179], true, false, false, false, false, false);
pause(0.5);

% Turning off ghost mode for the QCar
hQCar3.ghost_mode(false, [1, 0, 0]);


% Possessing the overhead camera on the QCar
hQCar2.possess(hQCar2.CAMERA_OVERHEAD);
pause(0.5);

% Possessing the trailing camera on the QCar
hQCar2.possess(hQCar2.CAMERA_TRAILING);
pause(0.5);

% Possessing the front CSI camera on the QCar
hQCar2.possess(hQCar2.CAMERA_CSI_FRONT);
pause(0.5);

% Possessing the right CSI camera on the QCar
hQCar2.possess(hQCar2.CAMERA_CSI_RIGHT);
pause(0.5);

% Possessing the back CSI camera on the QCar
hQCar2.possess(hQCar2.CAMERA_CSI_BACK);
pause(0.5);

% Possessing the left CSI camera on the QCar
hQCar2.possess(hQCar2.CAMERA_CSI_LEFT);
pause(0.5);

% Possessing the front RealSense RGB camera on the QCar
hQCar2.possess(hQCar2.CAMERA_RGB);
pause(0.5);

% Possessing the RealSense depth camera on the QCar

hQCar2.possess(hQCar2.CAMERA_DEPTH);
pause(0.5);


% % Getting images from the different cameras
% [x, camera_image] = hQCar2.get_image(hQCar2.CAMERA_CSI_FRONT);
% [x, camera_image] = hQCar2.get_image(hQCar2.CAMERA_CSI_RIGHT);
% [x, camera_image] = hQCar2.get_image(hQCar2.CAMERA_CSI_BACK);
% [x, camera_image] = hQCar2.get_image(hQCar2.CAMERA_CSI_LEFT);
% [x, camera_image] = hQCar2.get_image(hQCar2.CAMERA_RGB);
% [x, camera_image] = hQCar2.get_image(hQCar2.CAMERA_DEPTH);


disp('LIDAR')

hQCar3.possess(hQCar3.CAMERA_OVERHEAD);

hFigure = figure();

disp('Reading from LIDAR... if QLabs crashes or output isn''t great, make sure FPS > 100')

% Have the QCar drive forward to hit the front block to show the live lidar.
% Speed can be changed by increasing or decreasing the value in the first
% parameter "forward" 
hQCar3.set_velocity_and_request_state(1, 0, false, false, false, false, false);
lidar_rate = 0.05;

for count = 0:25

    [success, angle, distance] = hQCar3.get_lidar(400);

    x = sin(angle).*distance;
    y = cos(angle).*distance;

    plot(x,y, '.');
    axis([-60 60 -60 60]);
    drawnow;
    pause(lidar_rate);
    
end

pause(5);

% Closing qlabs
qlabs.close();
disp('Done!');
close(hFigure);
