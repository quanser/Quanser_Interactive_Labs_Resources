% Splines Tutorial
% -------------------------
% 
% .. note::
% 
%     Make sure you have Quanser Interactive Labs open before running this
%     example.  This example is designed to be run ONLY in the Plane environment. 

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

disp('Connected');

num_destroyed = qlabs.destroy_all_spawned_actors();

fprintf('%d actors destroyed', num_destroyed, '');

% Use hSystem to set the tutorial title on the qlabs display screen
hSystem = QLabsSystem(qlabs);
hSystem.set_title_string('Splines Tutorial');


% Initialize an instance of a camera 
camera = QLabsFreeCamera(qlabs);

% Set the spawn of the camera in a specific location 
camera.spawn([5.971, 11.781, 30.704], [0, 1.569, 1.57], 0, 1);

% Spawn the camera
camera.possess();

height = 0;
width = 1;
color = [0,0,0];

% create splines to create virtual roads of 1m of thickness
% Using the same initialization of QLabsSplineLine because the 
% actors will not have to be referenced again. So overwriting them 
% once they are spawned is not a problem. 

%  In functions (not spawn) that do not have a height value, height needs
% to be specified in the spawn function as a Z translation
splineRoads = QLabsSplineLine(qlabs);
splineRoads.spawn([10,10,height], [0,0,0], [1,1,1], 1);
splineRoads.rounded_rectangle_from_center(.5, 20, 20, width, color);

splineRoads.spawn( [0,0,0], [0,0,0],  [1,1,1],   1);
splineRoads.set_points(color, [[0,13.8,height,width];[6,16.8,height,width]; [11,12,height,width]; [15.5, 14.5, height,width]; [20, 11, height,width]], false);

splineRoads.spawn( [14,4.5,height], [0,0,0], [1,1,1],1);
splineRoads.circle_from_center(3, width, color, 8);

splineRoads.spawn( [0,0,0], [0,0,0], [1,1,1], 1);
splineRoads.set_points(color,  [[13.7,13.1,height,width];[14.8,11.8,height,width];[15.5,7.15,height,width]], false);

splineRoads.spawn( [0,0,0], [0,0,0], [1,1,1], 1);
splineRoads.set_points(color,  [[10.987, 4.199,height,width];[9.399, 6.559, height,width];[3.002, 4.034,height,width];[1.112, 3.004, height,width];[-0.045, 4.465, height,width]], false);

splineRoads.spawn( [0,0,0],[0,0,0], [1,1,1], 1);
splineRoads.set_points(color,  [[3, 20,height,width];[3, 4, height,width]], false);

splineRoads.spawn( [0,0,0], [0,0,0], [1,1,1], 1);
splineRoads.set_points(color,  [[8.7, 14.2, height,width];[8.7,0,height,width]], false);

splineRoads.spawn( [20,20,height], [0,0,0], [1,1,1], 1);
splineRoads.arc_from_center(5, pi, 3*pi/2, width, color);

pause(1);

% create same splines with color and .1 m of thickness to simulate lines in the road
% the next lines are a copy of the above one under a different name to differentiate
% both sets of lines. Height needs to be higher than the road since overlays will 
% reproduce weirdly in QLabs. 
height = .02;
width = .1;
color = [1,1,0];

splineLines = QLabsSplineLine(qlabs);
splineLines.spawn([10,10,height], [0,0,0], [1,1,1], 1);
splineLines.rounded_rectangle_from_center(.5, 20, 20, width, color);

splineLines.spawn( [0,0,0], [0,0,0],  [1,1,1],   1);
splineLines.set_points(color, [[0,13.8,height,width];[6,16.8,height,width]; [11,12,height,width]; [15.5, 14.5, height,width]; [20, 11, height,width]], false);

splineLines.spawn( [14,4.5,height], [0,0,0], [1,1,1],1);
splineLines.circle_from_center(3, width, color, 8);

splineLines.spawn( [0,0,0], [0,0,0], [1,1,1], 1);
splineLines.set_points(color,  [[13.7,13.1,height,width];[14.8,11.8,height,width];[15.5,7.15,height,width]], false);

splineLines.spawn( [0,0,0], [0,0,0], [1,1,1], 1);
splineLines.set_points(color,  [[10.987, 4.199,height,width];[9.399, 6.559, height,width];[3.002, 4.034,height,width];[1.112, 3.004, height,width];[-0.045, 4.465, height,width]], false);

splineLines.spawn( [0,0,0],[0,0,0], [1,1,1], 1);
splineLines.set_points(color,  [[3, 20,height,width];[3, 4, height,width]], false);

splineLines.spawn( [0,0,0], [0,0,0], [1,1,1], 1);
splineLines.set_points(color,  [[8.7, 14.2, height,width];[8.7,0,height,width]], false);

splineLines.spawn( [20,20,height], [0,0,0], [1,1,1], 1);
splineLines.arc_from_center(5, pi, 3*pi/2, width, color);

% Closing qlabs
qlabs.close();
disp('Done!');
