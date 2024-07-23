.. _Shredder:

*****************
Shredder
*****************


.. image:: ../pictures/configuration_shredder.png

.. _shredderDescription:

Description
============

Shredders are considered an "actor" in Quanser Interactive Labs Open Worlds.
They can be spawned anywhere in the Open Worlds and will delete widgets
when they fall into the shredder. 

Shredders should always use the same scale for x,y,z so they can function properly.

See the :ref:`shredderTutorial` to get a better understanding of using shredders
in Quanser Interactive Labs.

.. _shredderlibrary:

Library
========

.. autoclass:: python.qvl.shredder.QLabsShredder

.. _shredderConstants:

Constants
============

.. autoattribute:: python.qvl.shredder.QLabsShredder.ID_SHREDDER
.. autoattribute:: python.qvl.shredder.QLabsShredder.RED
.. autoattribute:: python.qvl.shredder.QLabsShredder.GREEN
.. autoattribute:: python.qvl.shredder.QLabsShredder.BLUE
.. autoattribute:: python.qvl.shredder.QLabsShredder.WHITE



.. _shredderMemberVars:

Member Variables
==================

.. autoattribute:: python.qvl.shredder.QLabsShredder.actorNumber

.. _shredderMethods:

Methods
========

.. automethod:: python.qvl.shredder.QLabsShredder.__init__
.. automethod:: python.qvl.shredder.QLabsShredder.spawn
.. automethod:: python.qvl.shredder.QLabsShredder.spawn_degrees
.. automethod:: python.qvl.shredder.QLabsShredder.spawn_id
.. automethod:: python.qvl.shredder.QLabsShredder.spawn_id_degrees
.. automethod:: python.qvl.shredder.QLabsShredder.spawn_id_and_parent_with_relative_transform
.. automethod:: python.qvl.shredder.QLabsShredder.spawn_id_and_parent_with_relative_transform_degrees
.. automethod:: python.qvl.shredder.QLabsShredder.destroy
.. automethod:: python.qvl.shredder.QLabsShredder.destroy_all_actors_of_class
.. automethod:: python.qvl.shredder.QLabsShredder.get_world_transform
.. automethod:: python.qvl.shredder.QLabsShredder.get_world_transform_degrees
.. automethod:: python.qvl.shredder.QLabsShredder.ping
.. automethod:: python.qvl.shredder.QLabsShredder.parent_with_relative_transform
.. automethod:: python.qvl.shredder.QLabsShredder.parent_with_relative_transform_degrees
.. automethod:: python.qvl.shredder.QLabsShredder.parent_with_current_world_transform
.. automethod:: python.qvl.shredder.QLabsShredder.parent_break
.. automethod:: python.qvl.shredder.QLabsShredder.set_custom_properties
.. automethod:: python.qvl.shredder.QLabsShredder.get_custom_properties


.. _shredderConfig:

Configurations
================

There are four configurations (0-3) for the shredder actor class.

    * 0 or shredder.RED
    * 1 or shredder.GREEN
    * 2 or shredder.BLUE
    * 3 or shredder.WHITE

.. image:: ../pictures/configuration_shredder.png

.. _shredderConnect:

Connection Points
====================

There are no connection points for this actor class.

-------------------------------------------------------------------------------

.. _shredderTutorial:

Shredder Tutorial
====================

.. tabs::
    .. tab:: Python

        .. dropdown:: Python Tutorial

            Raw to download this tutorial: |shredder_tutorial.py|.

            .. |shredder_tutorial.py| replace::
                :download:`Shredder Tutorial (.py) <../../../tutorials/shredder_tutorial.py>`

            .. literalinclude:: ../../../tutorials/shredder_tutorial.py
                :language: python
                :linenos:

    .. tab:: Matlab

        .. dropdown:: Matlab Tutorial

            Raw to download this tutorial: |shredder_tutorial.m|.

            .. |shredder_tutorial.m| replace::
                :download:`Shredder Tutorial (.m) <../../../tutorials/shredder_tutorial.m>`

            .. literalinclude:: ../../../tutorials/shredder_tutorial.m
                :language: Matlab
                :linenos:


