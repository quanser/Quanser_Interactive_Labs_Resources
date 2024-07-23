% Free Camera Library Example
% -------------------------
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

% Use hSystem to set the tutorial title on the qlabs display screen
hSystem = QLabsSystem(qlabs);
hSystem.set_title_string('Camera Tutorial')

% Create a camera in this qlabs instance
camera = QLabsFreeCamera(qlabs);

% Add a custom camera at a specified location and rotation using degrees
location = [-5.631, -1.467, 2.198];
rotation = [0, -2.386, -20.528];
camera.spawn_degrees(location, rotation);

% Switch our view from our current camera to the new camera we just initialized
camera.possess();

pause(3);

camera.set_camera_properties(60, 1, 2.0, 1.3);

[success, location, rotation, scale] = camera.get_world_transform();

ping = camera.ping();

% Take a image from the first camera angle 
if ping
    camera.set_image_capture_resolution();
    [success, image1] = camera.get_image();
    
    if ~success
        disp('Image decoding failure');
    end
end

pause(2);

% Initialize and spawn the second camera angle 
loc2 = [-33.17276819, 13.50500671, 2.282];
rot2 = [0, 0.077, 0.564];
camera2 = QLabsFreeCamera(qlabs);
x = camera2.spawn_id(2, loc2, rot2);
camera2.possess();

pause(2);

camera.destroy();

[success, location, rotation, scale] = camera2.get_world_transform();
camera2.set_camera_properties(40, true, 2.3, 0.6);

pause(2);

% Focus the camera 
for y = 1:51
    camera2.set_camera_properties(40, true, 2.3, (0.6 + ((y / 50)^3) * 23.7));
end

camera.set_image_capture_resolution();

% Take image of the second camera angle 
[success, image2] = camera.get_image();
disp(success);

pause(2);

% Initialize and spawn the third camera angle 
camera3 = QLabsFreeCamera(qlabs);
loc3 = [-21.456, 31.995, 3.745];
rot3 = [0, 18.814, 0.326];
camera3.spawn_degrees(loc3, rot3);
camera3.possess();

% Display a image of the first camera angle 
imshow(image1);

% Closing qlabs
qlabs.close();
disp('Done!');
            

