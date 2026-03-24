% QDrone 2 Library Example
% -------------------------
% This example will show you how to spawn qdrones, and use the qvl library commands
% to control the drone and its related functions.
% 
% .. note::
% 
%     Make sure you have Quanser Interactive Labs open before running this
%     example.  This example is designed to best be run in the open warehouse or plane.


close all;
clear all;
clc;

% --------------------------------------------------------------
% Setting MATLAB Path for the libraries
% Always keep at the start, it will make sure it finds the correct references
newPathEntry = fullfile(getenv('QAL_DIR'), '0_libraries', 'matlab', 'qvl');
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

fprintf('%d actors destroyed\n', num_destroyed);

% Use hSystem to set the tutorial title in the upper left of the qlabs window 
hSystem = QLabsSystem(qlabs);
hSystem.set_title_string('QDrone Tutorial')

% Initialize QLabs with free camera
hCamera = QLabsFreeCamera(qlabs);
hCamera.spawn_id(1, [-1.683, 2.333, 1.787], [-0, 0.391, -1.541]);
hCamera.possess();

fprintf('\n---QDrone---\n');

% Spawning the QDrone with radians
myQDrone = QLabsQDrone2(qlabs);
myQDrone.spawn_id(0, [-2, 0, 0], [0, 0, pi/2], 1);
pause(1);

% Spawn another QDrone with degrees
myQDrone2 = QLabsQDrone2(qlabs);
myQDrone2.spawn_degrees(2, [0, 0, 0], [0, 0, 45], 1);
x = myQDrone2.ping();
fprintf('QDrone 2 ping test: %d\n', x);
pause(2);

% Destroy the second drone and ping to verify
myQDrone2.destroy();
x = myQDrone2.ping();
fprintf('QDrone 2 ping test after destroy: %d\n', x);

% Setting the velocity of the drone in the z direction to make it go up and down
velocities = [.2, .5, .8, -.8, -.5, -.2];

for count = 1:6
    velocity_z = velocities(count);
    x = myQDrone.set_velocity_and_request_state(1, [0, 0, velocity_z], [0, 0, 0]);
    pause(1);
end

% Set velocity to zero with specific orientation
myQDrone.set_velocity_and_request_state_degrees(1, [0, 0, 0], [0, 0, 90]);
pause(1);

% Disable motors
myQDrone.set_velocity_and_request_state(0, [0, 0, 0], [0, 0, 0]);
pause(1);

% Adding a few shapes to the scene for understanding the camera views
rectangle = QLabsBasicShape(qlabs);
rectangle.spawn([0, 0, 0], [0, 0, 0], [.2, .2, 1], rectangle.SHAPE_CUBE, 1);
rectangle.set_material_properties([1, 0, 0]);
pause(0.25);

rectangle2 = QLabsBasicShape(qlabs);
rectangle2.spawn([-4, -3, 0], [0, 0, 0], [.2, .2, 1], rectangle.SHAPE_CUBE, 1);
rectangle2.set_material_properties([0, 1, 0]);
pause(0.25);

cone = QLabsBasicShape(qlabs);
cone.spawn([-1.4, 0, 0], [0, 0, 0], [.2, .2, 1], rectangle.SHAPE_CONE, 1);
cone.set_material_properties([0, 0, 1]);
pause(0.25);

rectangle3 = QLabsBasicShape(qlabs);
rectangle3.spawn([-2, 1.5, 0], [0, 0, 0], [.2, .2, 1], rectangle.SHAPE_CUBE, 1);
pause(1);

% Set transform and dynamics
myQDrone.set_transform_and_dynamics([-2, 0, 1], [0, 0, pi/2], 1, 1);
pause(1.5);

% Cycle through camera views
cameras = [myQDrone.VIEWPOINT_CSI_LEFT, myQDrone.VIEWPOINT_CSI_BACK, ...
           myQDrone.VIEWPOINT_CSI_RIGHT, myQDrone.VIEWPOINT_RGB, ...
           myQDrone.VIEWPOINT_DEPTH, myQDrone.VIEWPOINT_DOWNWARD, ...
           myQDrone.VIEWPOINT_OPTICAL_FLOW, myQDrone.VIEWPOINT_OVERHEAD, ...
           myQDrone.VIEWPOINT_TRAILING];

cameraNames = {'LEFT', 'BACK', 'RIGHT', 'RGB', 'DEPTH', 'DOWNWARD', 'OPTICAL FLOW', 'OVERHEAD', 'TRAILING'};

for count = 1:9
    x = myQDrone.possess(cameras(count));
    hSystem.set_title_string(cameraNames{count});
    pause(1.5);
end

% Return to free camera view
hCamera.possess();
hSystem.set_title_string('QDrone Tutorial');

% Set transform and get world transform in radians
myQDrone.set_transform_and_dynamics([-2, 0, 1.2], [0, 0, pi/2], 1, 1);
[~, location, orientation, ~] = myQDrone.get_world_transform();
fprintf('World Transform (radians): Location = [%f, %f, %f], Orientation = [%f, %f, %f]\n', ...
    location(1), location(2), location(3), orientation(1), orientation(2), orientation(3));
pause(1);

% Set transform and get world transform in degrees
myQDrone.set_transform_and_dynamics([-2, 0, 0], [0, 0, pi/2], 1, 1);
[~, location, orientation, ~] = myQDrone.get_world_transform_degrees();
fprintf('World Transform (degrees): Location = [%f, %f, %f], Orientation = [%f, %f, %f]\n', ...
    location(1), location(2), location(3), orientation(1), orientation(2), orientation(3));
pause(1);

% Getting images from the different cameras
fprintf('\nGetting images from various cameras...\n');

[status, camera_number, camera_image] = myQDrone.get_image(myQDrone.CAMERA_CSI_LEFT);
fprintf('CSI LEFT camera retrieved: status = %d\n', status);
imshow(camera_image)
pause(1)

[status, camera_number, camera_image] = myQDrone.get_image(myQDrone.CAMERA_CSI_RIGHT);
fprintf('CSI RIGHT camera retrieved: status = %d\n', status);
imshow(camera_image)
pause(1)

[status, camera_number, camera_image] = myQDrone.get_image(myQDrone.CAMERA_CSI_BACK);
fprintf('CSI BACK camera retrieved: status = %d\n', status);
imshow(camera_image)
pause(1)

[status, camera_number, camera_image] = myQDrone.get_image(myQDrone.CAMERA_RGB);
fprintf('RGB camera retrieved: status = %d\n', status);
imshow(camera_image)
pause(1)

[status, camera_number, camera_image] = myQDrone.get_image(myQDrone.CAMERA_DEPTH);
fprintf('DEPTH camera retrieved: status = %d\n', status);
imshow(camera_image)
pause(1)

[status, camera_number, camera_image] = myQDrone.get_image(myQDrone.CAMERA_DOWNWARD);
fprintf('DOWNWARD camera retrieved: status = %d\n', status);
imshow(camera_image)
pause(1)

[status, camera_number, camera_image] = myQDrone.get_image(myQDrone.CAMERA_OPTICAL_FLOW);
fprintf('OPTICAL FLOW camera retrieved: status = %d\n', status);
imshow(camera_image)
pause(1)

% Closing qlabs
qlabs.close();
disp('Done!');
