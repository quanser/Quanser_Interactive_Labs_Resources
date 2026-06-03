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
newPathEntry = fullfile(getenv('QAL_DIR'), '0_libraries', 'matlab', 'qvl');
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

qlabs = QuanserInteractiveLabs();
disp("Connecting to QLabs");

connection_established = qlabs.open('localhost');

if connection_established == false
	disp("Failed to open connection.")
	return
end


disp('Connected')

qlabs.destroy_all_spawned_actors();


%%% Stop Sign

hSign = QLabsStopSign(qlabs);
hSign.spawn_degrees([0, 0, 0], [0,0,180], [1,1,1], 0);
hSign.spawn_degrees([2, 0, 0], [0,0,180], [1,1,1], 1);


%%% Yield Sign

hSign = QLabsYieldSign(qlabs);
hSign.spawn_degrees([0, 1, 0], [0,0,180], [1,1,1], 0);
hSign.spawn_degrees([2, 1, 0], [0,0,180], [1,1,1], 1);


%%% Roundabout Sign

hSign = QLabsRoundaboutSign(qlabs)
hSign.spawn_degrees([0, 2, 0], [0,0,180], [1,1,1], 0);
hSign.spawn_degrees([2, 2, 0], [0,0,180], [1,1,1], 1);
hSign.spawn_degrees([4, 2, 0], [0,0,180], [1,1,1], 2);


%%% Crossing Sign

hSign = QLabsCrossingSign(qlabs);
hSign.spawn_degrees([0, 3, 0], [0,0,180], [1,1,1], 0);
hSign.spawn_degrees([2, 3, 0], [0,0,180], [1,1,1], 1);
hSign.spawn_degrees([4, 3, 0], [0,0,180], [1,1,1], 2);


%%% Obstacle Sign

hSign = QLabsObstacleSign(qlabs);
hSign.spawn_degrees([0, 4, 0], [0,0,180], [1,1,1], 0);
hSign.spawn_degrees([2, 4, 0], [0,0,180], [1,1,1], 1);
hSign.spawn_degrees([4, 4, 0], [0,0,180], [1,1,1], 2);



%%% Turn Sign

hSign = QLabsTurnSign(qlabs);
hSign.spawn_degrees([0,  5, 0], [0,0,180], [1,1,1], 0);
hSign.spawn_degrees([2,  5, 0], [0,0,180], [1,1,1], 1);
hSign.spawn_degrees([4,  5, 0], [0,0,180], [1,1,1], 2);
hSign.spawn_degrees([6,  5, 0], [0,0,180], [1,1,1], 3);
hSign.spawn_degrees([8,  5, 0], [0,0,180], [1,1,1], 4);
hSign.spawn_degrees([10, 5, 0], [0,0,180], [1,1,1], 5);
hSign.spawn_degrees([12, 5, 0], [0,0,180], [1,1,1], 6);
hSign.spawn_degrees([14, 5, 0], [0,0,180], [1,1,1], 7);



%%% Speed Sign
  
hSign = QLabsSpeedSign(qlabs);

for count = 0:11
	hSign.spawn_degrees([2*count,  6, 0], [0,0,180], [1,1,1], 0);
	hSign.set_speed((count+1)*10);
end


qlabs.close();
disp('All done!');