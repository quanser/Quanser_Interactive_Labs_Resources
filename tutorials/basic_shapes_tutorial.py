"""
Basic Shape Library Example
---------------------------

.. note::

    Make sure you have Quanser Interactive Labs open before running this
    example.  This example is designed to best be run in QCar Cityscape.

"""
# imports to important libraries
import sys
import math
import time

from qvl.qlabs import QuanserInteractiveLabs
from qvl.free_camera import QLabsFreeCamera
from qvl.basic_shape import QLabsBasicShape
from qvl.system import QLabsSystem

def main():

    # creates a server connection with Quanser Interactive Labs and manages
    # the communications
    qlabs = QuanserInteractiveLabs()

    # initialize our desired variables
    # note that you can use the coordinate helper to pick locations for your camera.
    loc = [-17.801, 31.145, 1.783]
    rot = [0, -0.93, 6.9]

    # trying to connect to QLabs and open the instance we have created - program will end if this fails
    print("Connecting to QLabs...")
    if (not qlabs.open("localhost")):
        print("Unable to connect to QLabs")
        return    

    print("Connected")
    
    # Use hSystem to set the tutorial title in the upper left of the qlabs window 
    hSystem = QLabsSystem(qlabs)
    hSystem.set_title_string('Basic Shapes Tutorial')

    # destroy any spawned actors in our QLabs that currently exist
    qlabs.destroy_all_spawned_actors()
    # create a camera in this qlabs instance
    camera = QLabsFreeCamera(qlabs)
    # add a custom camera at a specified location and rotation using degrees
    camera.spawn_degrees(location=loc, rotation=rot)
    # to switch our view from our current camera to the new camera we just initialized
    camera.possess()

    # initialize 4 cubes in our qlabs instance
    cube0 = QLabsBasicShape(qlabs)
    cube1 = QLabsBasicShape(qlabs)
    cube2 = QLabsBasicShape(qlabs, True)
    cube3 = QLabsBasicShape(qlabs, True)

    # spawn one of the cubes using radians
    cube0.spawn_id(actorNumber=0, location=[-10.202, 36.005, 0.5], rotation=[0,0,math.pi/4], scale=[0.5,0.5,0.5], configuration=cube0.SHAPE_CUBE, waitForConfirmation=True)
    # ping this cube, expect True if cube does exist and the actorNumber hasn't been changed
    cube0.ping()
    # collecting the world transform coordinates of the cube
    x, loc, rot, scale = cube0.get_world_transform()
    print(x, loc, rot, scale)

    # spawn a second cube using degrees
    cube1.spawn_id_degrees(actorNumber=1, location=[-13.503, 33.677, 0.5], rotation=[0,0,45], scale=[0.5,0.5,0.5], configuration=cube1.SHAPE_CUBE, waitForConfirmation=True)
    # wait to see visualization
    time.sleep(1)
    # destroy this created block
    cube1.destroy()
    # spawn a third and fourth cube relative to another parent actor already created in our qlabs instance using radians and then degrees respectively
    cube2.spawn_id_and_parent_with_relative_transform(actorNumber=2, location=[0,2,0], rotation=[0,0,math.pi/4], scale=[1,1,1], configuration=cube2.SHAPE_CUBE, parentClassID=cube0.ID_BASIC_SHAPE, parentActorNumber=cube0.actorNumber, parentComponent=0, waitForConfirmation=True)
    cube3.spawn_id_and_parent_with_relative_transform_degrees(actorNumber=3, location=[0,-2,0], rotation=[0,0,45], scale=[1,1,1], configuration=cube3.SHAPE_CUBE, parentClassID=cube0.ID_BASIC_SHAPE, parentActorNumber=cube0.actorNumber, parentComponent=0, waitForConfirmation=True)
    # set the material properties to a metallic red and gold reflective surface
    cube2.set_material_properties(color=[1,0,0], roughness=0.0, metallic=True, waitForConfirmation=True)
    cube3.set_material_properties(color=[252/255,144/255,3/255], roughness=0.0, metallic=True, waitForConfirmation=True)
    # have child actors rotate around the parent actor as their scale grows in size simultaneously
    for y in range(51):
        cube0.set_transform(location=[-10.202, 36.005, 0.5], rotation=[0,0,math.pi/4+2*math.pi/50*y], scale=[0.5+0.5*y/50,0.5+0.5*y/50,0.5+0.5*y/50])
        cube2.set_transform(location=[0,2,0], rotation=[0,0,math.pi/4-math.pi/25*y], scale=[1,1,1])
        cube3.set_transform_degrees(location=[0,-2,0], rotation=[0,0,45-180/25*y], scale=[1,1,1])

    # initialize 6 spheres in our qlabs instance
    sphere10 = QLabsBasicShape(qlabs)
    sphere11 = QLabsBasicShape(qlabs)
    sphere12 = QLabsBasicShape(qlabs)

    sphere13 = QLabsBasicShape(qlabs)
    sphere14 = QLabsBasicShape(qlabs)
    sphere15 = QLabsBasicShape(qlabs)

    # for the three first spheres, spawns spheres increasing in size using radians
    sphere10.spawn_id(actorNumber=10, location=[-13.75, 32.5, 0.25], rotation=[0,0,0], scale=[0.5,0.5,0.5], configuration=sphere10.SHAPE_SPHERE, waitForConfirmation=True)
    sphere11.spawn_id(actorNumber=11, location=[-13.75, 31.5, 1], rotation=[0,0,0], scale=[0.6,0.6,0.6], configuration=sphere11.SHAPE_SPHERE, waitForConfirmation=True)
    sphere12.spawn_id(actorNumber=12, location=[-13.75, 30.5, 0.25], rotation=[0,0,0], scale=[0.7,0.7,0.7], configuration=sphere12.SHAPE_SPHERE, waitForConfirmation=True)

    # in qlabs, the color of shapes uses the RGB color space with 0 to 255 represented between 0 and 1.
    # if you know what color you'd like to set your shape in RGB simply divide the red, green and blue numbers by 255.
    # this script sets these spheres to red, green and blue respectively while increasing in roughness
    sphere10.set_material_properties(color=[1,0,0], roughness=0.0, metallic=False, waitForConfirmation=True)
    sphere11.set_material_properties(color=[0,1,0], roughness=0.5, metallic=False, waitForConfirmation=True)
    sphere12.set_material_properties(color=[0,0,1], roughness=1.0, metallic=False, waitForConfirmation=True)

    # we want to now look at physics properties that are available to us in qlabs
    # if we spawn three more spheres and set the properties of these spheres to
    sphere13.spawn_id(actorNumber=13, location=[-11.253, 28.614, 1], rotation=[0,0,0], scale=[0.6,0.6,0.6], configuration=sphere13.SHAPE_SPHERE, waitForConfirmation=True)
    sphere14.spawn_id(actorNumber=14, location=[-8.669, 26.631, 1], rotation=[0,0,0], scale=[0.6,0.6,0.6], configuration=sphere14.SHAPE_SPHERE, waitForConfirmation=True)
    sphere15.spawn_id(actorNumber=15, location=[-8.685, 25.751, 1], rotation=[0,0,0], scale=[0.6,0.6,0.6], configuration=sphere13.SHAPE_SPHERE, waitForConfirmation=True)
    sphere13.set_physics_properties(mass=10, linearDamping=0, angularDamping=0, enableDynamics=True, waitForConfirmation=True)
    sphere13.set_enable_collisions(enableCollisions=True, waitForConfirmation=True)
    sphere15.set_physics_properties(mass=0.5, linearDamping=0, angularDamping=0, enableDynamics=True, waitForConfirmation=True)
    sphere15.set_enable_collisions(enableCollisions=True, waitForConfirmation=True)

    sphere10.set_enable_dynamics(enableDynamics=True, waitForConfirmation=True)
    sphere11.set_enable_dynamics(enableDynamics=True, waitForConfirmation=True)
    sphere12.set_enable_dynamics(enableDynamics=True, waitForConfirmation=True)
    sphere13.set_enable_dynamics(enableDynamics=True, waitForConfirmation=True)



    boxSpawn = QLabsBasicShape(qlabs)
    boxSpawn.spawn_id_box_walls_from_center(actorNumbers=[210, 211, 212, 213, 214], centerLocation=[-9.35, 26.5, 0.005], yaw=math.pi/4, xSize=2, ySize=2, zHeight=0.5, wallThickness=0.1, floorThickness=0.1, wallColor=[1,0,0], floorColor=[0,0,0], waitForConfirmation=True)


    boxSpawn.spawn_id_box_walls_from_center_degrees(actorNumbers=[270, 271, 272, 273, 274], centerLocation=[-11.35, 28.5, 0.005], yaw=45, xSize=2, ySize=2, zHeight=0.5, wallThickness=0.1, floorThickness=0.1, wallColor=[1,0,0], floorColor=[0,0,0], waitForConfirmation=True)


    boxSpawn.spawn_id_box_walls_from_end_points(actorNumber=280, startLocation=[-10.5, 32.5, 0.005], endLocation=[-10.5, 30.5, 0.005], height=0.1, thickness=0.1, color=[0.2,0.2,0.2], waitForConfirmation=True)


    x, shapeHandle1 = boxSpawn.spawn(location=[-6.945, 31.5, 0.5], rotation=[0,0,math.pi/4], scale=[1,1,1], configuration=boxSpawn.SHAPE_CUBE, waitForConfirmation=True)
    x, shapeHandle2 = boxSpawn.spawn(location=[-6.945, 31.5, 1.375], rotation=[0,0,0], scale=[0.75,0.75,0.75], configuration=boxSpawn.SHAPE_CUBE, waitForConfirmation=True)
    x, shapeHandle3 = boxSpawn.spawn(location=[-6.945, 31.5, 2], rotation=[0,0,math.pi/4], scale=[0.5,0.5,0.5], configuration=boxSpawn.SHAPE_CUBE, waitForConfirmation=True)


    x, shapeHandle4 = boxSpawn.spawn_degrees(location=[-6.945, 31.5, 2.50], rotation=[0,0,0], scale=[0.5,0.5,0.5], configuration=boxSpawn.SHAPE_CUBE, waitForConfirmation=True)
    x, shapeHandle5 = boxSpawn.spawn_degrees(location=[-6.945, 31.5, 2.875], rotation=[0,0,45], scale=[0.25,0.25,0.25], configuration=boxSpawn.SHAPE_CUBE, waitForConfirmation=True)


    boxSpawn.actorNumber = shapeHandle1
    boxSpawn.set_material_properties(color=[0,0,0], roughness=0.0, metallic=False, waitForConfirmation=True)
    boxSpawn.actorNumber = shapeHandle2
    boxSpawn.set_material_properties(color=[1,1,1], roughness=0.0, metallic=False, waitForConfirmation=True)
    boxSpawn.actorNumber = shapeHandle3
    boxSpawn.set_material_properties(color=[0.5,0.5,0.5], roughness=0.0, metallic=False, waitForConfirmation=True)
    boxSpawn.actorNumber = shapeHandle4
    boxSpawn.set_material_properties(color=[0,0,0], roughness=0.0, metallic=False, waitForConfirmation=True)

    # Close qlabs
    qlabs.close()
    print('Done !')

if __name__ == "__main__":
    main()