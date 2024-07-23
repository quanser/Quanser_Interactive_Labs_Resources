.. _Basic_Shapes:

*************
Basic Shapes
*************

.. _basicshapeDescription:

Description
=============

Basic shapes are building blocks to modify and customize your environment.
All shapes are spawned by default as static objects complete with collision
boundaries which can be useful to create walls and other obstacles.
Dynamics can be enabled and disabled to facilitate dynamic events that are
triggered by actor locations such as the sudden appearance of an obstacle
crossing the path.
The physics properties can also be modified to tune the physics response
depending 9on the number of interacting actors and what they are colliding with
.

Basic shapes include full support for parenting to build long kinematic chains
or simply to group multiple shapes together so they can be moved by
manipulating a single parent actor.

If you are using a large number of dynamic shapes, consider using
:ref:`Widgets` instead.
They have both limitations and additional features, but are more efficient when
spawning large numbers of dynamic actors.

See the :ref:`basicshapesTutorial` to get a better understanding of using basic 
shapes in Quanser Interactive Labs.

.. _basicshapelibrary:

Library
=============

.. autoclass:: python.qvl.basic_shape.QLabsBasicShape

.. _basicshapeConstants:

Constants
=============

.. autoattribute:: python.qvl.basic_shape.QLabsBasicShape.ID_BASIC_SHAPE
.. autoattribute:: python.qvl.basic_shape.QLabsBasicShape.SHAPE_CUBE
.. autoattribute:: python.qvl.basic_shape.QLabsBasicShape.SHAPE_CYLINDER
.. autoattribute:: python.qvl.basic_shape.QLabsBasicShape.SHAPE_SPHERE
.. autoattribute:: python.qvl.basic_shape.QLabsBasicShape.SHAPE_CONE

.. autoattribute:: python.qvl.basic_shape.QLabsBasicShape.COMBINE_AVERAGE
.. autoattribute:: python.qvl.basic_shape.QLabsBasicShape.COMBINE_MIN
.. autoattribute:: python.qvl.basic_shape.QLabsBasicShape.COMBINE_MULTIPLY
.. autoattribute:: python.qvl.basic_shape.QLabsBasicShape.COMBINE_MAX


.. _basicshapeMemberVars:

Member Variables
=================

.. autoattribute:: python.qvl.basic_shape.QLabsBasicShape.actorNumber

.. _basicshapeMethods:

Methods
=============

.. automethod:: python.qvl.basic_shape.QLabsBasicShape.__init__
.. automethod:: python.qvl.basic_shape.QLabsBasicShape.spawn
.. automethod:: python.qvl.basic_shape.QLabsBasicShape.spawn_degrees
.. automethod:: python.qvl.basic_shape.QLabsBasicShape.spawn_id
.. automethod:: python.qvl.basic_shape.QLabsBasicShape.spawn_id_degrees
.. automethod:: python.qvl.basic_shape.QLabsBasicShape.spawn_id_and_parent_with_relative_transform
.. automethod:: python.qvl.basic_shape.QLabsBasicShape.spawn_id_and_parent_with_relative_transform_degrees
.. automethod:: python.qvl.basic_shape.QLabsBasicShape.set_material_properties
.. automethod:: python.qvl.basic_shape.QLabsBasicShape.get_material_properties
.. automethod:: python.qvl.basic_shape.QLabsBasicShape.set_enable_dynamics
.. automethod:: python.qvl.basic_shape.QLabsBasicShape.set_enable_collisions
.. automethod:: python.qvl.basic_shape.QLabsBasicShape.set_physics_properties
.. automethod:: python.qvl.basic_shape.QLabsBasicShape.set_transform
.. automethod:: python.qvl.basic_shape.QLabsBasicShape.set_transform_degrees
.. automethod:: python.qvl.basic_shape.QLabsBasicShape.spawn_id_box_walls_from_end_points
.. automethod:: python.qvl.basic_shape.QLabsBasicShape.spawn_id_box_walls_from_center
.. automethod:: python.qvl.basic_shape.QLabsBasicShape.spawn_id_box_walls_from_center_degrees
.. automethod:: python.qvl.basic_shape.QLabsBasicShape.destroy
.. automethod:: python.qvl.basic_shape.QLabsBasicShape.destroy_all_actors_of_class
.. automethod:: python.qvl.basic_shape.QLabsBasicShape.get_world_transform
.. automethod:: python.qvl.basic_shape.QLabsBasicShape.get_world_transform_degrees
.. automethod:: python.qvl.basic_shape.QLabsBasicShape.ping
.. automethod:: python.qvl.basic_shape.QLabsBasicShape.parent_with_relative_transform
.. automethod:: python.qvl.basic_shape.QLabsBasicShape.parent_with_relative_transform_degrees
.. automethod:: python.qvl.basic_shape.QLabsBasicShape.parent_with_current_world_transform
.. automethod:: python.qvl.basic_shape.QLabsBasicShape.parent_break
.. automethod:: python.qvl.basic_shape.QLabsBasicShape.set_custom_properties
.. automethod:: python.qvl.basic_shape.QLabsBasicShape.get_custom_properties



.. _basicshapeConfig:

Configurations
===============
There are four configurations (0-3) for the basic shape actor class.

    * 0 - Cube
    * 1 - Cylinder
    * 2 - Sphere
    * 3 - Cone


.. image:: ../pictures/configuration_basicshapes.png

.. _basicshapeConnect:

Connection Points
====================

There are no connection points for this actor class.

-------------------------------------------------------------------------------

.. _basicshapesTutorial:

Basic Shapes Tutorial
=======================

.. tabs::
    .. tab:: Python

        .. dropdown:: Python Tutorial

            Raw to download this tutorial: |basic_shapes_tutorial.py|.

            .. |basic_shapes_tutorial.py| replace::
                :download:`Basic Shapes Tutorial (.py) <../../../tutorials/basic_shapes_tutorial.py>`

            .. literalinclude:: ../../../tutorials/basic_shapes_tutorial.py
                :language: python
                :linenos:

    .. tab:: Matlab

        .. dropdown:: Matlab Tutorial

            Raw to download this tutorial: |basic_shapes_tutorial.m|.

            .. |basic_shapes_tutorial.m| replace::
                :download:`Basic Shapes Tutorial (.m) <../../../tutorials/basic_shapes_tutorial.m>`

            .. literalinclude:: ../../../tutorials/basic_shapes_tutorial.m
                :language: Matlab
                :linenos:

