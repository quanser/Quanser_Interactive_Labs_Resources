% Road signage Library Crosswalk Example
% -------------------------
% 
% .. note::
% 
%     Make sure you have Quanser Interactive Labs open before running this
%     example.  This example is designed to best be run in QCar Cityscape
%     or Cityscape Lite

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
hSystem.set_title_string('Crosswalk Tutorial')

% This function demonstrates some basic commands with the crosswalk class

% initialize a camera - See Camera Actor Library Reference for more information
cameraCrosswalk = QLabsFreeCamera(qlabs);
cameraCrosswalk.spawn([-19.286, 43, 5.5], [-0, 0.239, -0.043]);
cameraCrosswalk.possess();

% create three crosswalk instances in this qlabs instance
crosswalk = QLabsCrosswalk(qlabs);
crosswalk1 = QLabsCrosswalk(qlabs);
crosswalk2 = QLabsCrosswalk(qlabs);

% spawn crosswalk with radians in configuration 0
pause(0.5);
crosswalk.spawn_id(0, [-10.788, 45, 0.00], [0, 0, pi/2], [1, 1, 1], 0, 1);
% waits so we can see the output
pause(1.5);
% spawn crosswalk with degrees in config 1
crosswalk1.spawn_id_degrees(1, [-6.788, 45, 0.00], [0, 0, 90], [1, 1, 1], 1, 1);
% waits so we can see the output
pause(1.5);
% spawn crosswalk with degrees in config 2
crosswalk2.spawn_id_degrees(2, [-2.8, 45, 0.0], [0, 0, 90], [1, 1, 1], 2, 1);
pause(1.5);

crosswalk.destroy();
pause(1.5);

crosswalk1.destroy();
pause(1.5);

crosswalk2.destroy();

% Closing qlabs
qlabs.close();
disp('Done!');