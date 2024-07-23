% Shredder Library Example
% -------------------------
% 
% .. note::
% 
%     Make sure you have Quanser Interactive Labs open before running this
%     example.  This example is designed to best be run in any of the open
%     world environments.

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

main();


function createCylinder(cylinder,location)

    color = [0, 1, 0; 0, 0, 1; 1, 0, 0];
    position = randi(3);

    cylinder.spawn(location, [0, 0, 0.5], [0.05, 0.05, 0.05], cylinder.CYLINDER, color(position,:));
       
end

function main()

    fprintf('\n\n----------------- Communications -------------------\n\n');

    qlabs = QuanserInteractiveLabs();
    connection_established = qlabs.open('localhost');
    
    if connection_established == false
        disp("Failed to open connection.")
        return
    end
    
    disp('Connected')
    num_destroyed = qlabs.destroy_all_spawned_actors();
    fprintf('%d actors destroyed\n', num_destroyed);

    % Use hSystem to set the tutorial title in the upper left of the qlabs window 
    hSystem = QLabsSystem(qlabs);
    hSystem.set_title_string('Shredder Tutorial')

    % create the widget instance
    cylinder = QLabsWidget(qlabs);

    % destroy any spawned actors (this is useful if you are running the same script over and over)
    qlabs.destroy_all_spawned_actors()

    % create a camera in this qlabs instance
    camera = QLabsFreeCamera(qlabs);

    % place the custom camera at a specified location and rotation using radians
    camera.spawn([0.39, -11.2, 1.8], [0, 0.8, -1.581])

    % to switch our view from our current camera to the new camera we just initialized to
    % be able to view where our people will spawn
    camera.possess()

    %%% Shredder
    % Create the shredder instance
    shredder = QLabsShredder(qlabs);

    % Spawn the first shredder, configuration = 2 indicates the color is blue
    shredder.spawn([0, -12, 0], [0, 0, 0], [1, 1, 1], 2)

    % Spawn the second shredder that is larger, controlled by the scale argument
    shredder.spawn([0.5, -12, 0], [0, 0, 0], [1.7, 1.7, 1.7], shredder.RED)
    pause(2)

    % Spawn 20 widgets and drop them into the shredders
    for i = 1:20

        % Adding noise to the spawn location of the widgets
        noiseX = rand() / 20;
        noiseY = rand() / 20;
        
        % Spawn one cylindrical widget for each shredder
        createCylinder(cylinder, [0 + noiseX, -12 - noiseY, 1]);
        createCylinder(cylinder, [0.5 - noiseX, -12 + noiseY, 1]);
        
        pause(0.7);  % Pause for 0.7 seconds
    end

end