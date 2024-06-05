.. _Conveyors:

*********
Conveyors
*********

.. _conveyorDescription:

Conveyors are considered an "actor" in Quanser Interactive Labs Open Worlds.
The conveyor library controls the conveyors available to be placed in
the QLabs environment.
Conveyors can be straight or curved and can be spawned anywhere in the Open Worlds.

See the :ref:`conveyorTutorial` to get a better understanding of using 
conveyors in Quanser Interactive Labs.

.. contents:: Table of Contents
    :depth: 1
    :local:
    :backlinks: none

-------------------------------------------------------------------------------

Straight Conveyor
-----------------

.. _straightconveyorlibrary:

Library
^^^^^^^

.. autoclass:: qvl.conveyor_straight.QLabsConveyorStraight

.. _straightconveyorConstants:

Constants
^^^^^^^^^

.. autoattribute:: qvl.conveyor_straight.QLabsConveyorStraight.ID_CONVEYOR_STRAIGHT

.. _straightconveyorMemberVars:

Member Variables
^^^^^^^^^^^^^^^^

.. autoattribute:: qvl.conveyor_straight.QLabsConveyorStraight.actorNumber

.. _straightconveyorMethods:

Methods
^^^^^^^

.. automethod:: qvl.conveyor_straight.QLabsConveyorStraight.__init__
.. automethod:: qvl.conveyor_straight.QLabsConveyorStraight.spawn
.. automethod:: qvl.conveyor_straight.QLabsConveyorStraight.spawn_degrees
.. automethod:: qvl.conveyor_straight.QLabsConveyorStraight.spawn_id
.. automethod:: qvl.conveyor_straight.QLabsConveyorStraight.spawn_id_degrees
.. automethod:: qvl.conveyor_straight.QLabsConveyorStraight.set_speed
.. automethod:: qvl.conveyor_straight.QLabsConveyorStraight.spawn_id_and_parent_with_relative_transform
.. automethod:: qvl.conveyor_straight.QLabsConveyorStraight.spawn_id_and_parent_with_relative_transform_degrees
.. automethod:: qvl.conveyor_straight.QLabsConveyorStraight.destroy
.. automethod:: qvl.conveyor_straight.QLabsConveyorStraight.destroy_all_actors_of_class
.. automethod:: qvl.conveyor_straight.QLabsConveyorStraight.get_world_transform
.. automethod:: qvl.conveyor_straight.QLabsConveyorStraight.get_world_transform_degrees
.. automethod:: qvl.conveyor_straight.QLabsConveyorStraight.ping
.. automethod:: qvl.conveyor_straight.QLabsConveyorStraight.parent_with_relative_transform
.. automethod:: qvl.conveyor_straight.QLabsConveyorStraight.parent_with_relative_transform_degrees
.. automethod:: qvl.conveyor_straight.QLabsConveyorStraight.parent_with_current_world_transform
.. automethod:: qvl.conveyor_straight.QLabsConveyorStraight.parent_break
.. automethod:: qvl.conveyor_straight.QLabsConveyorStraight.set_custom_properties
.. automethod:: qvl.conveyor_straight.QLabsConveyorStraight.get_custom_properties

.. _straightconveyorConfig:

Configurations
^^^^^^^^^^^^^^
A spawned straight conveyor with configuration set to 0 will create a conveyor
of 0.5 m in length. For each number you increase the configuration the length
will increase by .25m. 
For example, a configuration of 3 will create a 1.25m conveyor.
The configuration number accepts whole number between 0 and 20. 

All types of conveyors can be connected to make a setup of your choosing.

.. image:: ../pictures/configuration_straightConveyor.png

.. _straightconveyorConnect:

Connection Points
^^^^^^^^^^^^^^^^^

There are no connection points for this actor class.


-------------------------------------------------------------------------------

Curved Conveyor
-----------------

.. _curvedconveyorlibrary:

Library
^^^^^^^

.. autoclass:: qvl.conveyor_curved.QLabsConveyorCurved

.. _curvedconveyorConstants:

Constants
^^^^^^^^^

.. autoattribute:: qvl.conveyor_curved.QLabsConveyorCurved.ID_CONVEYOR_CURVED

.. _curvedconveyorVars:

Member Variables
^^^^^^^^^^^^^^^^

.. autoattribute:: qvl.conveyor_curved.QLabsConveyorCurved.actorNumber


.. _curvedconveyorMethods:

Methods
^^^^^^^

.. automethod:: qvl.conveyor_curved.QLabsConveyorCurved.__init__
.. automethod:: qvl.conveyor_curved.QLabsConveyorCurved.spawn
.. automethod:: qvl.conveyor_curved.QLabsConveyorCurved.spawn_degrees
.. automethod:: qvl.conveyor_curved.QLabsConveyorCurved.spawn_id
.. automethod:: qvl.conveyor_curved.QLabsConveyorCurved.spawn_id_degrees
.. automethod:: qvl.conveyor_curved.QLabsConveyorCurved.set_speed
.. automethod:: qvl.conveyor_curved.QLabsConveyorCurved.spawn_id_and_parent_with_relative_transform
.. automethod:: qvl.conveyor_curved.QLabsConveyorCurved.spawn_id_and_parent_with_relative_transform_degrees
.. automethod:: qvl.conveyor_curved.QLabsConveyorCurved.destroy
.. automethod:: qvl.conveyor_curved.QLabsConveyorCurved.destroy_all_actors_of_class
.. automethod:: qvl.conveyor_curved.QLabsConveyorCurved.get_world_transform
.. automethod:: qvl.conveyor_curved.QLabsConveyorCurved.get_world_transform_degrees
.. automethod:: qvl.conveyor_curved.QLabsConveyorCurved.ping
.. automethod:: qvl.conveyor_curved.QLabsConveyorCurved.parent_with_relative_transform
.. automethod:: qvl.conveyor_curved.QLabsConveyorCurved.parent_with_relative_transform_degrees
.. automethod:: qvl.conveyor_curved.QLabsConveyorCurved.parent_with_current_world_transform
.. automethod:: qvl.conveyor_curved.QLabsConveyorCurved.parent_break
.. automethod:: qvl.conveyor_curved.QLabsConveyorCurved.set_custom_properties
.. automethod:: qvl.conveyor_curved.QLabsConveyorCurved.get_custom_properties

.. _curvedconveyorConfig:

Configurations
^^^^^^^^^^^^^^
By default, the curved conveyor is spawned from the center and has a radius of 0.5m.
When configuration is set to 1, it will create a 15 degree conveyor. 
For each number you increase the configuration the length will increase by 15 degrees. 

For example, a configuration of 3 will create a 45 degree conveyor.
The configuration number accepts whole numbers between 1 and 24. 

Using a configuration number of 24 will create a circular conveyor.

All types of conveyors can be connected to make a setup of your choosing.


.. image:: ../pictures/configuration_curvedConveyor.png

.. _curvedconveyorConnect:

Connection Points
^^^^^^^^^^^^^^^^^

There are no connection points for this actor class.

-------------------------------------------------------------------------------

.. _conveyorTutorial:

Conveyors Tutorial
--------------------

.. tabs::
    .. tab:: Python

        .. dropdown:: Python Tutorial

            Raw to download this tutorial: |conveyor_tutorial.py|.

            .. |conveyor_tutorial.py| replace::
                :download:`Conveyor Tutorial (.py) <../../../tutorials/conveyor_tutorial.py>`

            .. literalinclude:: ../../../tutorials/conveyor_tutorial.py
                :language: python
                :linenos:

    .. tab:: Matlab

        .. dropdown:: Matlab Tutorial

            Raw to download this tutorial: |conveyor_tutorial.m|.

            .. |conveyor_tutorial.m| replace::
                :download:`Conveyor Tutorial (.m) <../../../tutorials/conveyor_tutorial.m>`

            .. literalinclude:: ../../../tutorials/conveyor_tutorial.m
                :language: guess
                :linenos:

