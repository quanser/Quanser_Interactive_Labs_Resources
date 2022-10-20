.. _Animal_Library:

Animals
-------

.. _animalDescription: 

Description
^^^^^^^^^^^

Animals are considered "actors" in the open world workspaces.  
The animal library controls the animals placed in Quanser Interactive Labs. 

Animal actors can be spawned anywhere in the open worlds, but to use the
move_to methods to allow the people to self-navigate around the environment,
they must originate and travel to a connected valid nav area.

For the best visual animation, it is recommended that you use the speed
constants defining different gait styles. A character will accurately travel 
at any specified speed up to 6m/s, but the visual animation may give the
impression of "slipping" at certain speeds outside the recommended values.

.. See the tutorial to get a better understanding of using cameras in the Quanser Interactive Labs.

.. _animalLibrary:

Library
^^^^^^^

.. autoclass:: library_qlabs_animal.QLabsAnimal

.. _animalConstants:

Constants
^^^^^^^^^

.. autoattribute:: library_qlabs_animal.QLabsAnimal.ID_ANIMAL
.. autoattribute:: library_qlabs_animal.QLabsAnimal.GOAT
.. autoattribute:: library_qlabs_animal.QLabsAnimal.SHEEP
.. autoattribute:: library_qlabs_animal.QLabsAnimal.COW
.. autoattribute:: library_qlabs_animal.QLabsAnimal.GOAT_STANDING
.. autoattribute:: library_qlabs_animal.QLabsAnimal.GOAT_WALK
.. autoattribute:: library_qlabs_animal.QLabsAnimal.GOAT_RUN
.. autoattribute:: library_qlabs_animal.QLabsAnimal.SHEEP_STANDING
.. autoattribute:: library_qlabs_animal.QLabsAnimal.SHEEP_WALK
.. autoattribute:: library_qlabs_animal.QLabsAnimal.SHEEP_RUN
.. autoattribute:: library_qlabs_animal.QLabsAnimal.COW_STANDING
.. autoattribute:: library_qlabs_animal.QLabsAnimal.COW_WALK
.. autoattribute:: library_qlabs_animal.QLabsAnimal.COW_RUN

.. _animalMemberVars:

Member Variables
^^^^^^^^^^^^^^^^

.. autoattribute:: library_qlabs_animal.QLabsAnimal.actorNumber

.. _animalMethods:

Methods
^^^^^^^

.. automethod:: library_qlabs_animal.QLabsAnimal.__init__
.. automethod:: library_qlabs_animal.QLabsAnimal.spawn
.. tip::
    The origin of the animal is in the center of the body so by default, it will be spawned 1m 
    above the surface of the target. An additional vertical offset may be required if the surface 
    is sloped to prevent the actor from falling through the world ground surface.
.. tip::
    If you would like to use the `move_to` method, the actor must be spawned in a valid nav area.

.. automethod:: library_qlabs_animal.QLabsAnimal.spawn_degrees
.. tip::
    The origin of the animal is in the center of the body so by default, it will be spawned 1m above the surface of the target. An additional vertical offset may be required if the surface is sloped to prevent the actor from falling through the world ground surface.
.. tip::
    If you would like to use the `move_to` method, the actor must be spawned in a valid nav area.

.. automethod:: library_qlabs_animal.QLabsAnimal.spawn_id
.. tip::
    The origin of the animal is in the center of the body so by default, it will be spawned 1m above the surface of the target. An additional vertical offset may be required if the surface is sloped to prevent the actor from falling through the world ground surface.
.. tip::
    If you would like to use the `move_to` method, the actor must be spawned in a valid nav area.

.. automethod:: library_qlabs_animal.QLabsAnimal.spawn_id_degrees
.. tip::
    The origin of the animal is in the center of the body so by default, it will be spawned 1m above the surface of the target. An additional vertical offset may be required if the surface is sloped to prevent the actor from falling through the world ground surface.
.. tip::
    If you would like to use the `move_to` method, the actor must be spawned in a valid nav area.

.. automethod:: library_qlabs_animal.QLabsAnimal.move_to
.. automethod:: library_qlabs_animal.QLabsAnimal.destroy
.. automethod:: library_qlabs_animal.QLabsAnimal.destroy_all_actors_of_class
.. automethod:: library_qlabs_animal.QLabsAnimal.ping
.. automethod:: library_qlabs_animal.QLabsAnimal.get_world_transform
.. automethod:: library_qlabs_animal.QLabsAnimal.get_world_transform_degrees

.. _animalConfig:

Configurations
^^^^^^^^^^^^^^

There are 3 configurations (0-2) for a animal generated in QLabs.

.. TODO: Add image of 3 configurations

.. _animalConnect:

Connection Points
^^^^^^^^^^^^^^^^^

There are no connection points for the animal actor.

.. .. _animalTutorial:

.. Tutorial
.. ^^^^^^^^

.. .. dropdown:: Example 1
.. 
.. .. dropdown:: Example 2

.. .. dropdown:: Example 3

.. **See Also:**
