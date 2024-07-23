% Animal Example
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

qlabs =  QuanserInteractiveLabs();
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
hSystem.set_title_string('Animals Tutorial')

% initialize our variables
% Note that you can use the 
% Coordinate Helper to pick locations for your actor.

LOCATION_START_P1 = [-6.85, 40.396, 0.005];
ROTATION_P1P2 = [0,0,pi/2];
SCALE = [1,1,1];

LOCATION_START_P2 = [-8.53, 40.7, 0.005];
LOCATION_START_P3 = [-11.884, 40.292, 0.005];
ROTATION_P3 = [0,0,90];

LOCATION_END_P1 = [-7.637, 51, 0.005];
LOCATION_END_P2 = [-11.834, 51, 0.005];
LOCATION_END_P3 = [-23.71, 43.245, 0.005];

% create a camera in this qlabs instance
camera = QLabsFreeCamera(qlabs);

% place the custom camera at a specified location and rotation using radians
camera.spawn([-0., 43.807, 8.82], [-0, 0.606, 3.127]);

% to switch our view from our current camera
% to the new camera we just initialized 
% to be able to view where our animals will spawn
camera.possess();

% creates an instance of the Animal
goat = QLabsAnimal(qlabs);

% Animal configurations 
%
%   Goat = 0
%   Sheep = 1
%   Cow = 2

% place the animal at a specified location and rotation using radians
% spawn_id allows us to specify the internal number for the actor
goat.spawn_id(0, LOCATION_START_P1, ROTATION_P1P2, SCALE, 0, 1);

% creates a second instance of a animal 
sheep = QLabsAnimal(qlabs);

% place the animal at a specified location and rotation using radians
% spawn creates the internal number for the actor automatically using
% the next available actor number
sheep.spawn(LOCATION_START_P2, ROTATION_P1P2, SCALE, 1, 1)

% creates a third instance of a animal
cow = QLabsAnimal(qlabs, 1);

% place the animal at a specified location and rotation using degrees
% spawn_degrees creates the internal actor number
% automatically using the next available number 
% this function also takes the input rotation as degrees
cow.spawn_degrees(LOCATION_START_P3, ROTATION_P3, SCALE, 2, 1);

% move the 3 animals created to a new location
goat.move_to(LOCATION_END_P1, goat.GOAT_WALK, 1);
sheep.move_to(LOCATION_END_P2, sheep.SHEEP_RUN, 1);
cow.move_to(LOCATION_END_P3, cow.COW_RUN, 1);

% pause to change camera
pause(7);

% destroy each animal one by one 

goat.destroy();
pause(1);

sheep.destroy();
pause(1);

cow.destroy();
pause(1);

% re position camera
hCameraAnimals = QLabsFreeCamera(qlabs);
x = hCameraAnimals.spawn([25.243, 46.069, 1.628], [-0, 0.188, 1.098]);
hCameraAnimals.possess();

% Spawn a Goat and make it run to a specific location 
hGoat = QLabsAnimal(qlabs);
hGoat.spawn([26.206, 57, 1], [0,0,0], [1,1,1], hGoat.GOAT, true);
hGoat.move_to([27.214, 49.286, 0], hGoat.GOAT_RUN, true);
pause(3);

% Move the Goat at walking speed to your desired location 
hGoat.move_to([28.338, 47.826, 0], hGoat.GOAT_WALK, true);
pause(4);
hGoat.destroy();

% Spawn a Sheep and make it run to a specific location
hSheep = QLabsAnimal(qlabs);
hSheep.spawn([26.206, 57, 1], [0,0,0], [1,1,1], hSheep.SHEEP, true);
hSheep.move_to([27.214, 49.286, 0], hSheep.SHEEP_RUN, true);
pause(3);

% Move the Sheep at walking speed to your desired location 
hSheep.move_to([28.338, 47.826, 0], hSheep.SHEEP_WALK, true);
pause(4);
hSheep.destroy();

% Spawn a Cow and make it run to a specific location
hCow = QLabsAnimal(qlabs);
hCow.spawn([26.206, 57, 1], [0,0,0], [1,1,1], hCow.COW, true);
hCow.move_to([27.214, 49.286, 0], hCow.COW_RUN, true);
pause(3);

% Move the Cow at walking speed to your desired location
hCow.move_to([28.338, 47.826, 0], hCow.COW_WALK, true);
pause(6);

% close qlabs
qlabs.close();
disp('Done !')
