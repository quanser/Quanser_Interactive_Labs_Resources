% Road Signage Library Traffic Cones Example
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
hSystem.set_title_string('Traffic Cones Tutorial')

% Switch the camera angle to see where we will be spawning the cones
camera0 = QLabsFreeCamera(qlabs);
camera0.spawn([-20.355, 27.374, 2.055], [-0, 0.308, -0.001]);
camera0.possess();

cone = QLabsTrafficCone(qlabs);
cone1 = QLabsTrafficCone(qlabs);
cone2 = QLabsTrafficCone(qlabs);
cone3 = QLabsTrafficCone(qlabs);
cone4 = QLabsTrafficCone(qlabs);

% Spawn a small traffic cone using radians
cone.spawn([-17, 28, 1.0], [0, 0, pi], [1, 1, 1], 0, 1);
% Wait to see the output
pause(1);

% Destroy the cone
cone.destroy();
% Wait to see the output
pause(1);

% Spawn another small traffic cone using radians in the same place
cone1.spawn_id(1, [-17, 28, 1.0], [0, 0, pi], [1, 1, 1], 0, 1);
% Spawn a construction pylon using degrees and generating the actorNumber internally
cone2.spawn_degrees([-15, 28, 1.0], [0, 0, 180], [1, 1, 1], 1, 1);
% Spawn a small cone with one color stripe initialized using actor number and a position in degrees
cone3.spawn_id_degrees(3, [-15, 26.5, 1.0], [0, 0, 90], [1, 1, 1], 2, 1);
% Spawn a bigger cone with two color stripes using radians and generating the actorNumber internally
cone4.spawn([-17, 26.5, 1.0], [0, 0, pi/4], [1, 1, 1], 3, 1);

% Wait to see the output
pause(1.5);

% The color changing 'set_material_properties' does not yet exist in matlab
%
% % Change the color of the cones (materialSlot 0 is the base color, and 1 is the stripes)
% cone1.set_material_properties(0, [0, 0, 1], 1); % Blue
% % Wait to see the output
% pause(0.5);
% 
% cone2.set_material_properties(0, [1, 0, 0], 1, 0); % Red
% cone2.set_material_properties(1, [1, 0.5, 0]);
% pause(0.5);
% 
% cone3.set_material_properties(0, [0, 1, 1]); % Cyan
% cone3.set_material_properties(1, [0, 0.3, 1], 1, 1);
% pause(0.5);
% 
% cone4.set_material_properties(0, [1, 0, 1], 0, 0); % Magenta
% cone4.set_material_properties(1, [0.3, 0, 1]);
% pause(0.5);
%
% cone1.set_material_properties(0, [0,1,0],0.5,0) # Green
% cone1.set_material_properties(1, [1,.5,0],0)
% pause(0.5)
% 
% cone2.set_material_properties(0, [1,1,0],1,1) # Yellow
% cone2.set_material_properties(1, [0,0,0],0)
% pause(0.5)
% 
% cone3.set_material_properties(0, [0.5,0.5,0.5],1,1) # Grey
% cone3.set_material_properties(1, [0.6,0.2,0.6],1,1)
% pause(0.5)
% 
% cone4.set_material_properties(0, [0.0,0.5,0.5],0,0) # Magenta
% cone4.set_material_properties(1, [0.5,0.5,0.0],1,1)
%
% pause(3);

cone1.destroy();
pause(1);

cone2.destroy();
pause(1);

cone3.destroy();
pause(1);

cone4.destroy();
pause(1);

% Closing qlabs
qlabs.close();
disp('Done!');