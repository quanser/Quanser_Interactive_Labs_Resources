% Walls Example
% -------------------------
% 
% .. note::
% 
%     Make sure you have Quanser Interactive Labs open before running this
%     example.  This example is designed to be run in the Plane, Studio,
%     or Warehouse environments.

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


% Open communications
qlabs =  QuanserInteractiveLabs();
connection_established = qlabs.open('localhost');

if connection_established == false
    disp("Failed to open connection.")
    return
end

disp('Connected')

% Remove any existing actors
num_destroyed = qlabs.destroy_all_spawned_actors();

% Initialize an instance of a custom camera
camera = QLabsFreeCamera(qlabs);
camera.spawn([2.295, -3.826, 1.504], [-0, 0.213, 1.957]);
camera.possess();


% Initialize instances of walls 
wall = QLabsWalls(qlabs);

% Use 'for' loops to spawn a line of walls
for y = 0:5
    wall.spawn_degrees([-0.5, y*1.05, 0.001]);
end

% Spawn a second line of walls but enable the dynamics
for y = 0:5
    wall.spawn_degrees([0.5, y*1.05, 0.001]);

    % Enable dynamics for this set of walls
    wall.set_enable_dynamics(true);
end


% Spawn a large sphere to demonstrate which walls are dynamic
sphere = QLabsBasicShape(qlabs);
sphere.spawn([0,2,3], [0,0,0], [1.5,1.5,1.5], sphere.SHAPE_SPHERE);
sphere.set_enable_dynamics(true);

% Closing qlabs
qlabs.close();
disp('Done!');









