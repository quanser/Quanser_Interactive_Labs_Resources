% MultiAgent Example
% ----------------------------------
% 
% .. note::
% 
% Make sure you have the teaching or research resources from the Quanser website 
% downloaded. It will not find the necessary files if you do not have them.
% 
% Make sure to only try to spawn robots your Quanser Interactive Labs license
% allows for. It will not spawn robots you do not have access to. 
% 
% Make sure you have Quanser Interactive Labs open before running this
% example.  This example is designed to best be run in any of the Open World environments.
% 

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

fprintf('\n\n------------------------------ Communications --------------------------------\n\n');

qlabs =  QuanserInteractiveLabs();
connection_established = qlabs.open('localhost');

if connection_established == false
    disp("Failed to open connection.")
    return
end

disp('Connected')

num_destroyed = qlabs.destroy_all_spawned_actors();
pause(1)
num_destroyed = qlabs.destroy_all_spawned_actors();

fprintf('%d actors destroyed', num_destroyed, '');


% Initialize an instance of a camera 
camera = QLabsFreeCamera(qlabs);

% Set the spawn of the camera in a specific location 
camera.spawn_degrees([0.063, 1.9, 0.603], [0, 9.186, -83.687])

% Spawn the camera
camera.possess();

% Spawn random objects in the scene
rectangle2 = QLabsBasicShape(qlabs);
rectangle2.spawn([-1,-.8,0], [0,0,0], [.2,.2,1], QLabsBasicShape.SHAPE_CUBE, true);
rectangle2.set_material_properties([0,1,0]);
pause(1);

cone = QLabsBasicShape(qlabs);
cone.spawn([0.7,-.4,0], [0,0,0], [.2,.2,1], QLabsBasicShape.SHAPE_CONE, true);
cone.set_material_properties([0,0,1]);
pause(0.5);

% Closing qlabs
qlabs.close();
disp('Finish Objects Spawn!');

%%

myRobots = {};

% Adding a new robot to the list
% comment out robots that you may not be licensed for

%QCar 2 needs to be spawned at a smaller scale since it is made to work in
% cityscape where it is made to spawn the size of a real car. 
% as a 1/10th car, spawning at 0.1 scale will make it the size of the real
% QCar 2
myRobots{end+1} = struct(...
    "RobotType", "QCar2",  ...
    "Location", [-.5, 0, 0],  ...
    "Rotation", [0, 0, 90],  ...
    "Scale", .1, ...
    "ActorNumber" , 5  ... % set actor number to 5
);

myRobots{end+1} = struct(...
    "RobotType", "QD2",  ...
    "Location", [1, 0.5, 0],  ...
    "Rotation", [0, 0, 90],  ...
    "Scale", 1 ...
);

myRobots{end+1} = struct(...
    "RobotType", "QBP",  ...
    "Location", [.15, -.3, -0],  ...
    "Rotation", [0, 0, 90],  ...
    "Scale", 1 ...
);


% Spawn robots
mySpawns = MultiAgent(myRobots);

% cell array with of qlabs actor objects of the robots that were spawned. Use when using functions from qlabs library.
actors = mySpawns.robotActors; 
disp(actors)
disp(actors{1}.actorNumber)
disp(actors{1}.classID)

% this is how to still use the actor functions with the spawns
% setting the qcar 2 into ghost mode and to purple
% these functions are directly from qvl.QLabsQCar2
pause(1);
actors{1}.ghost_mode(true,[1,0,1]);
pause(1);
actors{1}.ghost_mode(true,[0,0,1]);
pause(1);
actors{1}.ghost_mode(false);

actorsDict = mySpawns.robotsDict; 
disp(actorsDict.QC2_5.hilPort)
disp(actorsDict.QBP_0.videoPort)

% struct of structs of all spawned robots. Includes the information that is saved into the JSON file.

mySpawns.qlabs.close()










