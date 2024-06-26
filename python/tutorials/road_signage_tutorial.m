% Road signage Library Example
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
hSystem.set_title_string('Road Signage Tutorial')


% Switch the camera angle to see where we will be spawning the rest of the objects
camera0 = QLabsFreeCamera(qlabs);
camera0.spawn([-20.14, 29.472, 2.071], [0, 0.203, -0.024]);
camera0.possess();


% Create two roundabouts in this qlabs instance
roundabout = QLabsRoundaboutSign(qlabs);
roundabout2 = QLabsRoundaboutSign(qlabs);

% Spawn the sign using radians and specifying the actorNumber
roundabout.spawn_id(0, [-17, 29, 0.0], [0, 0, pi], [1, 1, 1], 0, 1);
% Spawn the second sign using degrees and allowing the computer to
% generate an actorNumber internally
roundabout2.spawn_id_degrees(2, [-15, 29, 0.0], [0, 0, 180], [1, 1, 1], 0, 1);

% Wait to see the output
pause(1.5);

% Destroying the sign we just created
roundabout.destroy();
pause(1.5);

% Create two yield signs in this qlabs instance
yieldsign = QLabsYieldSign(qlabs);
yieldsign2 = QLabsYieldSign(qlabs);

% Spawn the sign using radians and specifying the actorNumber
yieldsign.spawn_id(0, [-17, 31, 0.0], [0, 0, pi], [1, 1, 1], 0, 1);
% Spawn the second sign using degrees and allowing the computer to
% generate an actorNumber internally
yieldsign2.spawn_degrees([-15, 31, 0.0], [0, 0, 180], [1, 1, 1], 0, 1);

% Wait to see the output
pause(1.5);

% Destroying the sign we just created
yieldsign.destroy();
pause(1.5);

% Create two stop signs in this qlabs instance
stop = QLabsStopSign(qlabs);
stop2 = QLabsStopSign(qlabs);

% Spawn the sign using radians
stop.spawn_id(1, [-16, 30, 0.0], [0, 0, pi], [1, 1, 1], 0, 1);
% Spawn the second sign using degrees and allowing the computer to
% generate an actorNumber internally
stop2.spawn_degrees([-15, 30, 0.0], [0, 0, 180], [1, 1, 1], 0, 1);

% Wait to see the output
pause(1.5);

% Destroying the sign we just created
stop.destroy();
pause(1.5);

% Destroy the signs one by one
roundabout2.destroy();
pause(1);

stop2.destroy();
pause(1);

yieldsign2.destroy();
pause(1);

% Closing qlabs
qlabs.close();
disp('Done!');

