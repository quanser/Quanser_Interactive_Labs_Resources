% Basic Shape Library Example
% ----------------------------
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
hSystem.set_title_string('Basic Shapes Tutorial');

% initialize our desired variables
% note that you can use the coordinate helper to pick locations for your camera.
loc = [-17.801, 31.145, 1.783];
rot = [0, -0.93, 6.9];

% create a camera in this qlabs instance
camera = QLabsFreeCamera(qlabs);
% add a custom camera at a specified location and rotation using degrees
camera.spawn_degrees(loc, rot);
% to switch our view from our current camera to the new camera we just initialized
camera.possess();

% initialize 4 cubes in our qlabs instance
cube0 = QLabsBasicShape(qlabs);
cube1 = QLabsBasicShape(qlabs);
cube2 = QLabsBasicShape(qlabs, 1);
cube3 = QLabsBasicShape(qlabs, 1);

% spawn one of the cubes using radians
cube0.spawn_id(0, [-10.202, 36.005, 0.5], [0, 0, pi/4], [0.5, 0.5, 0.5], cube0.SHAPE_CUBE, 1);

% ping this cube, expect True if cube does exist and the actorNumber hasn't been changed
cube0.ping();

% collecting the world transform coordinates of the cube
[success, loc, rot, scale] = cube0.get_world_transform();

% spawn a second cube using degrees
% the constants can come from both the object or directly from QLabsBasicShape
cube1.spawn_id_degrees(1, [-13.503, 33.677, 0.5], [0, 0, 45], [0.5, 0.5, 0.5], QLabsBasicShape.SHAPE_CUBE, 1);

% wait to see visualization
pause(1);

% destroy this created block
cube1.destroy();

% spawn a third and fourth cube relative to another parent actor already created in our qlabs instance using radians and then degrees respectively
cube2.spawn_id_and_parent_with_relative_transform(2, [0, 2, 0], [0, 0, pi/4], [1, 1, 1], cube2.SHAPE_CUBE, cube0.ID_BASIC_SHAPE, cube0.actorNumber, 0, 1);
cube3.spawn_id_and_parent_with_relative_transform_degrees(3, [0, -2, 0], [0, 0, 45], [1, 1, 1], cube3.SHAPE_CUBE, cube0.ID_BASIC_SHAPE, cube0.actorNumber, 0, 1);

% set the material properties to a metallic red and gold reflective surface
cube2.set_material_properties([1, 0, 0], 0.0, 1, 1);
cube3.set_material_properties([252/255, 144/255, 3/255], 0.0, 1, 1);

% have child actors rotate around the parent actor as their scale grows in size simultaneously
for y = 0:50
    cube0.set_transform([-10.202, 36.005, 0.5], [0, 0, pi/4 + 2*pi/50*y], [0.5+0.5*y/50, 0.5+0.5*y/50, 0.5+0.5*y/50]);
    cube2.set_transform([0, 2, 0], [0, 0, pi/4 - pi/25*y], [1, 1, 1]);
    cube3.set_transform_degrees([0, -2, 0], [0, 0, 45 - 180/25*y], [1, 1, 1]);
end

% initialize 6 spheres in our qlabs instance
sphere10 = QLabsBasicShape(qlabs);
sphere11 = QLabsBasicShape(qlabs);
sphere12 = QLabsBasicShape(qlabs);

sphere13 = QLabsBasicShape(qlabs);
sphere14 = QLabsBasicShape(qlabs);
sphere15 = QLabsBasicShape(qlabs);

% for the three first spheres, spawns spheres increasing in size using radians
sphere10.spawn_id(10, [-13.75, 32.5, 0.25], [0, 0, 0], [0.5, 0.5, 0.5], sphere10.SHAPE_SPHERE, 1);
sphere11.spawn_id(11, [-13.75, 31.5, 1], [0, 0, 0], [0.6, 0.6, 0.6], sphere11.SHAPE_SPHERE, 1);
sphere12.spawn_id(12, [-13.75, 30.5, 0.25], [0, 0, 0], [0.7, 0.7, 0.7], sphere12.SHAPE_SPHERE, 1);

% in qlabs, the color of shapes uses the RGB color space with 0 to 255 represented between 0 and 1.
% if you know what color you'd like to set your shape in RGB simply divide the red, green and blue numbers by 255.
% this script sets these spheres to red, green and blue respectively while increasing in roughness
sphere10.set_material_properties([1, 0, 0], 0.0, 0, 1);
sphere11.set_material_properties([0, 1, 0], 0.5, 0, 1);
sphere12.set_material_properties([0, 0, 1], 1.0, 0, 1);

% we want to now look at physics properties that are available to us in qlabs
% if we spawn three more spheres and set the properties of these spheres to
sphere13.spawn_id(13, [-11.253, 28.614, 1], [0, 0, 0], [0.6, 0.6, 0.6], sphere13.SHAPE_SPHERE, 1);
sphere14.spawn_id(14, [-8.669, 26.631, 1], [0, 0, 0], [0.6, 0.6, 0.6], sphere14.SHAPE_SPHERE, 1);
sphere15.spawn_id(15, [-8.685, 25.751, 1], [0, 0, 0], [0.6, 0.6, 0.6], sphere13.SHAPE_SPHERE, 1);

sphere13.set_physics_properties(1, 10, 0.0 , 0.0, 0.0, 0.7, sphere13.COMBINE_AVERAGE, 0.3, sphere13.COMBINE_AVERAGE, 1);
sphere13.set_enable_collisions(1, 1);
sphere15.set_physics_properties(1, 0.5, 0.0, 0.0, 0.0, 0.7, sphere15.COMBINE_AVERAGE, 0.3, sphere15.COMBINE_AVERAGE, 1);
sphere15.set_enable_collisions(1, 1);

sphere10.set_enable_dynamics(1, 1);
sphere11.set_enable_dynamics(1, 1);
sphere12.set_enable_dynamics(1, 1);
sphere13.set_enable_dynamics(1, 1);

boxSpawn = QLabsBasicShape(qlabs);
boxSpawn.spawn_id_box_walls_from_center([210, 211, 212, 213, 214], [-9.35, 26.5, 0.005], pi/4, 2, 2, 0.5, 0.1, 0.1, [1, 0, 0], [0, 0, 0], 1);

boxSpawn.spawn_id_box_walls_from_center_degrees([270, 271, 272, 273, 274], [-11.35, 28.5, 0.005], 45, 2, 2, 0.5, 0.1, 0.1, [1, 0, 0], [0, 0, 0], 1);
                                                

boxSpawn.spawn_id_box_walls_from_end_points(280, [-10.5, 32.5, 0.005], [-10.5, 30.5, 0.005], 0.1, 0.1, [0.2, 0.2, 0.2], 1);


[x, shapeHandle1] = boxSpawn.spawn([-6.945, 31.5, 0.5], [0, 0, pi/4], [1, 1, 1], boxSpawn.SHAPE_CUBE, 1);
[x, shapeHandle2] = boxSpawn.spawn([-6.945, 31.5, 1.375], [0, 0, 0], [0.75, 0.75, 0.75], boxSpawn.SHAPE_CUBE, 1);
[x, shapeHandle3] = boxSpawn.spawn([-6.945, 31.5, 2], [0, 0, pi/4], [0.5, 0.5, 0.5], boxSpawn.SHAPE_CUBE, 1);


[x, shapeHandle4] = boxSpawn.spawn_degrees([-6.945, 31.5, 2.50], [0, 0, 0], [0.5, 0.5, 0.5], boxSpawn.SHAPE_CUBE, 1);
[x, shapeHandle5] = boxSpawn.spawn_degrees([-6.945, 31.5, 2.875], [0, 0, 45], [0.25, 0.25, 0.25], boxSpawn.SHAPE_CUBE, 1);


boxSpawn.actorNumber = shapeHandle1;
boxSpawn.set_material_properties([0, 0, 0], 0.0, 0, 1);
boxSpawn.actorNumber = shapeHandle2;
boxSpawn.set_material_properties([1, 1, 1], 0.0, 0, 1);
boxSpawn.actorNumber = shapeHandle3;
boxSpawn.set_material_properties([0.5, 0.5, 0.5], 0.0, 0, 1);
boxSpawn.actorNumber = shapeHandle4;
boxSpawn.set_material_properties([0, 0, 0], 0.0, 0, 1);

% close qlabs
qlabs.close();
disp('Done !')

