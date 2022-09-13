.. _base_shape:

Basic Shapes
------------

.. _basicshapeDescription: 

Description
^^^^^^^^^^^

Basic shapes are building blocks to modify and customize your environment.
All shapes are spawned by default as static objects complete with collision boundaries which
can be useful to create walls and other obstacles.  Dynamics can be enabled and
disabled to facilitate dynamic events that are triggered by actor locations such
as the sudden appearance of an obstacle crossing the path.
The physics properties can also be modified to tune the physics response depending
on the number of interacting actors and what they are colliding with.

Basic shapes include full support for parenting to build long kinematic chains
or simply to group multiple shapes together so they can be moved by manipulating 
a single parent actor. A special "empty" configuration is available to add additional
frames of reference that are not visible.

If you are using a large number of dynamic shapes, consider using :ref:`Widgets` instead.
They have both limitations and additional features, but are more efficient when spawning
large numbers of dynamic actors.

.. _basicshapelibrary:

Library
^^^^^^^

.. autoclass:: library_qlabs_basic_shape.QLabsBasicShape

.. _basicshapeConstants:

Constants
^^^^^^^^^

.. autoattribute:: library_qlabs_basic_shape.QLabsBasicShape.ID_BASIC_SHAPE
.. autoattribute:: library_qlabs_basic_shape.QLabsBasicShape.SHAPE_CUBE
.. autoattribute:: library_qlabs_basic_shape.QLabsBasicShape.SHAPE_CYLINDER
.. autoattribute:: library_qlabs_basic_shape.QLabsBasicShape.SHAPE_SPHERE

.. _basicshapeMethods:

Methods
^^^^^^^

.. automethod:: library_qlabs_basic_shape.QLabsBasicShape.spawn
.. automethod:: library_qlabs_basic_shape.QLabsBasicShape.spawn_degrees
.. automethod:: library_qlabs_basic_shape.QLabsBasicShape.spawn_and_parent_with_relative_transform
.. automethod:: library_qlabs_basic_shape.QLabsBasicShape.spawn_and_parent_with_relative_transform_degrees
.. automethod:: library_qlabs_basic_shape.QLabsBasicShape.set_material_properties
.. automethod:: library_qlabs_basic_shape.QLabsBasicShape.set_enable_dynamics
.. automethod:: library_qlabs_basic_shape.QLabsBasicShape.set_physics_properties
.. automethod:: library_qlabs_basic_shape.QLabsBasicShape.set_transform
.. automethod:: library_qlabs_basic_shape.QLabsBasicShape.set_transform_degrees
.. automethod:: library_qlabs_basic_shape.QLabsBasicShape.spawn_box_walls_from_end_points
.. automethod:: library_qlabs_basic_shape.QLabsBasicShape.spawn_box_walls_from_center
.. automethod:: library_qlabs_basic_shape.QLabsBasicShape.spawn_box_walls_from_center_degrees

.. _basicshapeConfig:

Configurations
^^^^^^^^^^^^^^

.. _basicshapeConnect:

Connection Points
^^^^^^^^^^^^^^^^^



.. _basicshapeTutorial:

Tutorial
^^^^^^^^

.. dropdown:: Example 1

.. dropdown:: Example 2

.. dropdown:: Example 3
