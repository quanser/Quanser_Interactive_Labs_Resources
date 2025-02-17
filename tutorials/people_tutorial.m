% Person Library Example
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

if onPath == 0
    path(path, newPathEntry)
    savepath
end

fprintf('\n\n----------------- Communications -------------------\n\n');

qlabs =  QuanserInteractiveLabs();
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
hSystem.set_title_string('People Tutorial')

% initialize our variables
% note that you can use the ..Coordinate Helper to pick locations for your actor.
LOCATION_START_P1 = [-6.8, 40.7, 0.005];
ROTATION_P1P2 = [0,0,pi/2];
SCALE = [1,1,1];

LOCATION_START_P2 = [-8.5, 40.7, 0.005];
LOCATION_START_P3 = [-11.9, 40.7,0.005];
ROTATION_P3 = [0,0,90];

LOCATION_END_P1 = [-7.6, 51, 0.005];
LOCATION_END_P2 = [-11.0, 48, 0.005];
LOCATION_END_P3 = [-23.7, 43, 0.005];

% create a camera in this qlabs instance
camera = QLabsFreeCamera(qlabs);

%place the custom camera at a specified location and rotation using radians
camera.spawn([-2.061, 43.916, 4.348], [0, 0.383, -3.097]);

% to switch our view from our current camera to the new camera we just initialized to
% be able to view where our people will spawn
camera.possess();

% creates an instance of the person
person1 = QLabsPerson(qlabs);

% place the person at a specified location and rotation using radians
% spawn_id allows us to specify the internal number for the actor
person1.spawn_id(0, LOCATION_START_P1, ROTATION_P1P2, SCALE, 6, 1);

% creates a second instance of a person
person2 = QLabsPerson(qlabs);

% place the person at a specified location and rotation using radians
% spawn creates the internal number for the actor automatically using
% the next available actor number
person2.spawn(LOCATION_START_P2, ROTATION_P1P2, SCALE, 7, 1)

% creates a third instance of a person
person3 = QLabsPerson(qlabs, 1);

% place the person at a specified location and rotation using degrees
% spawn_degrees creates the internal number for the actor automatically using the next
% available number and takes the inputted rotation as degrees
person3.spawn_degrees(LOCATION_START_P3, ROTATION_P3, SCALE, 8, 1);

% move the 3 people created to a new location
person1.move_to(LOCATION_END_P1, person1.WALK, 1);
person2.move_to(LOCATION_END_P2, person2.JOG, 1);
person3.move_to(LOCATION_END_P3, person3.RUN, 1);

pause(3);
qlabs.close();
