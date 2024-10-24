% Wall Maze Example
% -------------------------
% 
% .. note::
% 
%     Make sure you have Quanser Interactive Labs open before running this
%     example.  This example is designed to be run in the Plane, Studio,
%     or Warehouse environments.

% Define globals
global North;
global East;
global South;
global West;
global Unexplored;
global maze_data;
global maze_x;
global maze_y;

load_qvl_path()

% Do you want the walls to be able to fall over if hit? (Maze generatio will take slightly longer.)
dynamic_walls = true;

% Maze size
maze_x = 10;
maze_y = 10;

% Initialize constants and variables. We'll use a bit mask to efficiently store multiple
% pieces of information inside a single value.
North =      0b00001;
East =       0b00010;
South =      0b00100;
West =       0b01000;
Unexplored = 0b10000;
maze_data = uint8(ones(maze_x,maze_y)) * 0b11111; % (bit-or of N, E, S, W, and unexplored)


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
camera.spawn([-0.337, 3.205, 4.895], [-0, 0.59, -1.091]);
camera.possess();


% Initialize instances of walls 
wall = QLabsWalls(qlabs);

generate_maze();
draw_maze(qlabs, dynamic_walls);

% Closing qlabs
qlabs.close();
disp('Done!');




function load_qvl_path()

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
end

function generate_maze()
    global North;
    global East;
    global South;
    global West;
    global Unexplored;
    global maze_data;
    global maze_x;
    global maze_y;

    location = [1, 1];

    % Mark the first cell as explored and remove the North wall as the entrance to the maze
    maze_data(1,1) = bitand(bitand(maze_data(1,1), bitcmp(Unexplored)), bitcmp(North));

    % Start digging through the maze recursively
    remove_maze_wall(location);

    % Remove one wall on the South side of the maze
    maze_data(1,maze_y) = bitand(maze_data(1,maze_y), bitcmp(South));
end

function remove_maze_wall(location)
    global North;
    global East;
    global South;
    global West;
    global Unexplored;
    global maze_data;
    global maze_x;
    global maze_y;

    % first pick a random direction (N, S, W, E) (The order helps reduce "easy" solutions to the maze)
    first_direction = randi([1 4]);

    % Check all four compass directions for a valid travel path
    for direction = 1:4

        % Offset the direction count by the random direction
        current_direction = (direction + first_direction);
        if current_direction > 4
            current_direction = current_direction - 4;
        end

        if (current_direction == 1)
            if ((location(2) > 1) && (bitand(maze_data(location(1), location(2)-1), Unexplored)))
                % Remove North wall from the current cell and the South wall of the new cell and mark the new cell as explored
                maze_data(location(1), location(2)-1) = bitand(maze_data(location(1), location(2)-1), bitcmp(Unexplored));
                maze_data(location(1), location(2)-1) = bitand(maze_data(location(1), location(2)-1), bitcmp(South));
                maze_data(location(1), location(2))   = bitand(maze_data(location(1), location(2)), bitcmp(North));

                remove_maze_wall([location(1), location(2)-1]);
            end

        elseif (current_direction == 2)
            if ((location(2) < (maze_y)) && (bitand(maze_data(location(1), location(2)+1), Unexplored)))
                % Remove South wall from the current cell and the North wall of the new cell and mark the new cell as explored
                maze_data(location(1), location(2)+1) = bitand(maze_data(location(1), location(2)+1), bitcmp(Unexplored));
                maze_data(location(1), location(2)+1) = bitand(maze_data(location(1), location(2)+1), bitcmp(North));
                maze_data(location(1), location(2))   = bitand(maze_data(location(1), location(2)), bitcmp(South));

                remove_maze_wall([location(1), location(2)+1]);
            end

        elseif (current_direction == 3)
            if ((location(1) > 1) && (bitand(maze_data(location(1)-1, location(2)), Unexplored)))
                % Remove West wall from the current cell and the East wall of the new cell and mark the new cell as explored
                maze_data(location(1)-1, location(2)) = bitand(maze_data(location(1)-1, location(2)), bitcmp(Unexplored));
                maze_data(location(1)-1, location(2)) = bitand(maze_data(location(1)-1, location(2)), bitcmp(East));
                maze_data(location(1),   location(2)) = bitand(maze_data(location(1), location(2)), bitcmp(West));

                remove_maze_wall([location(1)-1, location(2)]);
            end

        else       
            if ((location(1) < (maze_x)) && (bitand(maze_data(location(1)+1, location(2)), Unexplored)))
                % Remove East wall from the current cell and the West wall of the new cell and mark the new cell as explored
                maze_data(location(1)+1, location(2)) = bitand(maze_data(location(1)+1, location(2)), bitcmp(Unexplored));
                maze_data(location(1)+1, location(2)) = bitand(maze_data(location(1)+1, location(2)), bitcmp(West));
                maze_data(location(1),   location(2)) = bitand(maze_data(location(1), location(2)), bitcmp(East));

                remove_maze_wall([location(1)+1, location(2)]);
            end
        end
    end
end            


function draw_maze(qlabs, dynamic_walls)
    global North;
    global East;
    global South;
    global West;
    global maze_data;
    global maze_x;
    global maze_y;

    % Initialize a wall object
    wall = QLabsWalls(qlabs);

    % add just the first top row
    for count_x = 1:maze_x
        if (bitand(maze_data(count_x, 1), North))
            place_wall(wall, count_x, 1, North, dynamic_walls);
        end
    end

    for count_y = 1:maze_y
        % left most wall of the maze
        if (bitand(maze_data(1, count_y), West))
            place_wall(wall, 1, count_y, West, dynamic_walls);
        end

        % all the rest of the walls
        for count_x = 1:maze_x
            if (bitand(maze_data(count_x, count_y), South))
                place_wall(wall, count_x, count_y, South, dynamic_walls);
            end

            if (bitand(maze_data(count_x, count_y), East))
                place_wall(wall, count_x, count_y, East, dynamic_walls);            
            end
        end
    end
end


function place_wall(wall, x, y, direction, dynamic_walls)
    global North;
    global East;
    global South;
    global West; %#ok<NUSED>

    % Length of a wall segment plus a bit of padding
    wall_length = 1.05;

    % Walls are static by default so we only need to wait for confirmation if the dynamic_walls flag is set.

    if direction == North
        wall.spawn_degrees([x*wall_length, -(y*wall_length), 0.001], [0, 0, 90], [1,1,1], 0, dynamic_walls);
    
    elseif direction == East
        wall.spawn_degrees([x*wall_length + wall_length/2, -(y*wall_length + wall_length/2), 0.001], [0, 0, 0], [1,1,1], 0, dynamic_walls);

    elseif direction == South
        wall.spawn_degrees([x*wall_length, -(y*wall_length + wall_length), 0.001], [0, 0, 90], [1,1,1], 0, dynamic_walls);
    else
        wall.spawn_degrees([x*wall_length-wall_length/2, -(y*wall_length + wall_length/2), 0.001], [0, 0, 0], [1,1,1], 0, dynamic_walls);
    end

    if (dynamic_walls)
        wall.set_enable_dynamics(dynamic_walls);
    end
end









