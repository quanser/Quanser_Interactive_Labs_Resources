% Widget Library Example
% -------------------------
% 
% .. note::
% 
%     Make sure you have Quanser Interactive Labs open before running this
%     example.  This example is designed to best be run in QCar Cityscape

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

% Creates a server connection with Quanser Interactive Labs and manages the communications
qlabs = QuanserInteractiveLabs();
connection_established = qlabs.open('localhost');

if connection_established == false
    disp("Failed to open connection.")
    return
end

disp('Connected')

num_destroyed = qlabs.destroy_all_spawned_actors();
fprintf('%d actors destroyed', num_destroyed);

main(qlabs);

% ------------ functions ----------

function widgets(qlabs)
    % Initialize the widget class in qlabs
    widget = QLabsWidget(qlabs);

    % Enable shadows for objects
    widget.widget_spawn_shadow(true);

    % Create 10 cubes of varying shades of red
    for count = 0:9
        widget.spawn_degrees([-11.000, 30.000 + count*0.01, 1 + count*0.6], [90, 0, 0], [0.5, 0.5, 0.5], ...
            widget.CUBE, [1, 0 + count*0.03, 0 + count*0.02], 0, 0, '', 1);
    end

    pause(2);

    % Create 20 grey metal cans at different locations
    for count = 0:19
        widget.spawn([-11.000, 29.000, 1 + count*0.2], [0, 0, 0], [1, 1, 1], ...
            widget.METAL_CAN, [1, 1, 1], 0, 0, '', 1);
    end

    pause(1);

    % Create 20 plastic bottles of varying shades of blue
    for count = 0:19
        widget.spawn_degrees([-11.000, 29.000, 1 + count*0.2], [90, 0, 0], [1, 1, 1], ...
            widget.PLASTIC_BOTTLE, [count*0.01, count*0.02, 1], 0, 0, '', 1);
    end

    pause(1);

    % Create 10 spheres of red to yellow gradient
    for count = 0:9
        widget.spawn_degrees([-11.000, 31.000 + count*0.01, 1 + count*0.6], [90, 0, 0], [0.5, 0.5, 0.5], ...
            widget.SPHERE, [1, 0 + count*0.05, 0 + count*0.01], 1000, 0, '', 1);
    end

    pause(5);

    % Destroy all spawned widgets
    % widget.destroy_all_spawned_widgets(); % Uncomment this line if destroy function is defined
end

function main(qlabs)
    
    % Initialize desired camera location and rotation
    loc = [-18.783, 30.023, 2.757];
    rot = [0, 8.932, -2.312];

    % Create a camera in this qlabs instance
    camera = QLabsFreeCamera(qlabs);

    % Add a custom camera at a specified location and rotation using degrees
    camera.spawn_degrees(loc, rot);

    % Switch view to the new camera
    camera.possess();

    % Run the code for using widgets
    widgets(qlabs);

    % Close our connection to qlabs
    qlabs.close();
end

