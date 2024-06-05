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

fprintf('\n\n------------------------------ Communications --------------------------------\n\n');

qlabs =  QuanserInteractiveLabs();
connection_established = qlabs.open('localhost');

if connection_established == false
    disp("Failed to open connection.")
    return
end


disp('Connected')

num_destroyed = qlabs.destroy_all_spawned_actors();

fprintf('%d actors destroyed', num_destroyed);

% initialize our variables
% note that you can use the ..Coordinate Helper to pick locations for your actor.
LOCATION_START_P1 = [-6.85, 40.396, 0.005];
ROTATION_P1P2 = [0,0,pi/2];
SCALE = [1,1,1];

LOCATION_START_P2 = [-8.53, 40.641, 0.005];
LOCATION_START_P3 = [-11.884, 40.292, 0.005];
ROTATION_P3 = [0,0,90];

LOCATION_END_P1 = [-7.637, 51, 0.005];
LOCATION_END_P2 = [-11.834, 51, 0.005];
LOCATION_END_P3 = [-23.71, 43.245, 0.005];

% create a camera in this qlabs instance
camera = QLabsFreeCamera(qlabs);

%place the custom camera at a specified location and rotation using radians
camera.spawn([-0.457, 43.807, 8.82], [-0, 0.606, 3.127]);

% to switch our view from our current camera to the new camera we just initialized to
% be able to view where our people will spawn
camera.possess();

% creates an instance of the person
person1 = QLabsPerson(qlabs);

% place the person at a specified location and rotation using radians
% spawn_id allows us to specify the internal number for the actor
person1.spawn_id(0, LOCATION_START_P1, ROTATION_P1P2, SCALE, 0, 1);

% creates a second instance of a person
person2 = QLabsPerson(qlabs);

% place the person at a specified location and rotation using radians
% spawn creates the internal number for the actor automatically using
% the next available actor number
person2.spawn(LOCATION_START_P2, ROTATION_P1P2, SCALE, 1, 1)

% creates a third instance of a person
person3 = QLabsPerson(qlabs, 1);

% place the person at a specified location and rotation using degrees
% spawn_degrees creates the internal number for the actor automatically using the next
% available number and takes the inputted rotation as degrees
person3.spawn_degrees(LOCATION_START_P3, ROTATION_P3, SCALE, 2, 1);

% move the 3 people created to a new location
person1.move_to(LOCATION_END_P1, person1.WALK, 1);
person2.move_to(LOCATION_END_P2, person2.JOG, 1);
person3.move_to(LOCATION_END_P3, person3.RUN, 1);

pause(3);
qlabs.close();
