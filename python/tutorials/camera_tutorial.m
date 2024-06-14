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

%  initialize our desired variables
%  note that you can use the coordinate helper to pick locations for your camera.
location = [-5.631, -1.467, 2.198]; % -53.022, -7.491, 14.475 -58.881, -11.077, 14.475
rotation = [0, -2.386, -20.528];

% create a camera in this Quanser Interactive Labs instance
camera = QLabsFreeCamera(qlabs);

% add a custom camera at a specified location and rotation using radians
camera.spawn_degrees(location, rotation);

% to switch our view from our current camera to the new camera we just initialized
camera.possess();

% time wait to demonstrate the difference between the default camera settings
% and after we've set the camera properties
pause(3);

% set the properties of our camera to customize it - this is not required
% default camera is set to a FOV: 90 degrees with DOF disabled
% (which disables aperture and focal distance)
camera.set_camera_properties(60, 1, 2.0, 1.3);

% collect the current world transform information from the actor camera (should be
% the same as the one we set).
[success, location, rotation, scale] = camera.get_world_transform();

% ping the existing camera -- we will expect this to return "True", since the camera
% does indeed exist.
camera.ping();

% set the image resolution height and width - here we are just setting them to be
% the default 640x480
camera.FCN_FREE_CAMERA_SET_IMAGE_RESOLUTION();

% request an image from the camera 
camera.get_image();

qlabs.close();
