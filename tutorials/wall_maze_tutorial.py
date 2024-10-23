"""
Maze Example
---------------

.. note::

    Make sure you have Quanser Interactive Labs open before running this
    example. This example is designed to be run in the Plane or Warehouse
    environment.

"""

from qvl.qlabs import QuanserInteractiveLabs
from qvl.free_camera import QLabsFreeCamera 
from qvl.system import QLabsSystem

import numpy as np
import random

from qvl.walls import QLabsWalls

# Use the ramdom seed if you want the same maze every time (uncomment the following line)
#random.seed(12)

# Do you want the walls to be able to fall over if hit? (Maze generatio will take slightly longer.)
dynamic_walls = False

# Maze size
maze_x = 10
maze_y = 10

# Initialize constants and variables. We'll use a bit mask to efficiently store multiple
# pieces of information inside a single value.
North =      0b00001
East =       0b00010
South =      0b00100
West =       0b01000
Unexplored = 0b10000
maze_data = np.ones(shape=(maze_x,maze_y), dtype=int) * (North | East | South | West | Unexplored)

# Length of a wall segment plus a bit of padding
wall_length = 1.05



def generate_maze():
    location = [0, 0]

    # Mark the first cell as explored and remove the North wall as the entrance to the maze
    maze_data[0,0] = maze_data[0,0] & (~Unexplored) & (~North)

    # Start digging through the maze recursively
    remove_maze_wall(location)

    # Remove one wall on the South side of the maze
    maze_data[0,maze_y-1] = maze_data[0,maze_y-1] & (~South)


def remove_maze_wall(location):
    
    # first pick a random direction (N, S, W, E) (The order helps reduce "easy" solutions to the maze)
    first_direction = random.randint(0,3)
    
    # Check all four compass directions for a valid travel path
    for direction in range(4):

        # Offset the direction count by the random direction
        current_direction = (direction + first_direction) % 4

        if (current_direction == 0):
            if ((location[1] > 0) and (maze_data[location[0], location[1]-1] & Unexplored)):
                # Remove North wall from the current cell and the South wall of the new cell and mark the new cell as explored
                maze_data[location[0], location[1]-1] = maze_data[location[0], location[1]-1] & (~Unexplored)
                maze_data[location[0], location[1]-1] = maze_data[location[0], location[1]-1] & (~South)
                maze_data[location[0], location[1]]   = maze_data[location[0], location[1]] & (~North)

                remove_maze_wall([location[0], location[1]-1])

        elif (current_direction == 1):
            if ((location[1] < (maze_y-1)) and (maze_data[location[0], location[1]+1] & Unexplored)):
                # Remove South wall from the current cell and the North wall of the new cell and mark the new cell as explored
                maze_data[location[0], location[1]+1] = maze_data[location[0], location[1]+1] & (~Unexplored)
                maze_data[location[0], location[1]+1] = maze_data[location[0], location[1]+1] & (~North)
                maze_data[location[0], location[1]]   = maze_data[location[0], location[1]] & (~South)

                remove_maze_wall([location[0], location[1]+1])   

        elif (current_direction == 2):
            if ((location[0] > 0) and (maze_data[location[0]-1, location[1]] & Unexplored)):
                # Remove West wall from the current cell and the East wall of the new cell and mark the new cell as explored
                maze_data[location[0]-1, location[1]] = maze_data[location[0]-1, location[1]] & (~Unexplored)
                maze_data[location[0]-1, location[1]] = maze_data[location[0]-1, location[1]] & (~East)
                maze_data[location[0],   location[1]] = maze_data[location[0], location[1]] & (~West)

                remove_maze_wall([location[0]-1, location[1]])   

        else:            
            if ((location[0] < (maze_x-1)) and (maze_data[location[0]+1, location[1]] & Unexplored)):
                # Remove East wall from the current cell and the West wall of the new cell and mark the new cell as explored
                maze_data[location[0]+1, location[1]] = maze_data[location[0]+1, location[1]] & (~Unexplored)
                maze_data[location[0]+1, location[1]] = maze_data[location[0]+1, location[1]] & (~West)
                maze_data[location[0],   location[1]] = maze_data[location[0], location[1]] & (~East)

                remove_maze_wall([location[0]+1, location[1]])            

              


def draw_maze(qlabs):
    # Initialize a wall object
    wall = QLabsWalls(qlabs)
    
    # add just the first top row
    for count_x in range(maze_x):
        if (maze_data[count_x, 0] & North):
            place_wall(wall, count_x, 0, North)
    
    for count_y in range(maze_y):
        # left most wall of the maze
        if (maze_data[0, count_y] & West):
            place_wall(wall, 0, count_y, West)

        # all the rest of the walls
        for count_x in range(maze_x):
            if (maze_data[count_x, count_y] & South):
                place_wall(wall, count_x, count_y, South)

            if (maze_data[count_x, count_y] & East):
                place_wall(wall, count_x, count_y, East)             

        
def place_wall(wall, x, y, direction):
    # Walls are static by default so we only need to wait for confirmation if the dynamic_walls flag is set.

    if direction == North:
        wall.spawn_degrees(location=[x*wall_length, -(y*wall_length), 0.001], rotation=[0, 0, 90], waitForConfirmation=dynamic_walls)

    elif direction == East:
        wall.spawn_degrees(location=[x*wall_length + wall_length/2, -(y*wall_length + wall_length/2), 0.001], rotation=[0, 0, 0], waitForConfirmation=dynamic_walls)

    elif direction == South:
        wall.spawn_degrees(location=[x*wall_length, -(y*wall_length + wall_length), 0.001], rotation=[0, 0, 90], waitForConfirmation=dynamic_walls)
    else:
        wall.spawn_degrees(location=[x*wall_length-wall_length/2, -(y*wall_length + wall_length/2), 0.001], rotation=[0, 0, 0], waitForConfirmation=dynamic_walls)
        
    if (dynamic_walls):
        wall.set_enable_dynamics(dynamic_walls)




def main():

    # Creates a server connection with Quanser Interactive Labs and manages
    # the communications
    qlabs = QuanserInteractiveLabs()

    # Ensure that QLabs is running on your local machine
    print("Connecting to QLabs...")
    if (not qlabs.open("localhost")):
        print("Unable to connect to QLabs")
        return    

    print("Connected")

    # Set the window title
    hSystem = QLabsSystem(qlabs)
    hSystem.set_title_string('Walls Tutorial')

    num_destroyed = qlabs.destroy_all_spawned_actors()

    # Initialize an instance of a camera 
    camera = QLabsFreeCamera(qlabs)

    # Set the spawn of the camera in a specific location 
    camera.spawn([-0.337, 3.205, 4.895], [-0, 0.59, -1.091], [1, 1, 1], 0, 1)
    camera.possess()
       
    generate_maze()
    draw_maze(qlabs)

    # Closing qlabs
    qlabs.close()
    print('Done!')

if __name__ == "__main__":
    main()