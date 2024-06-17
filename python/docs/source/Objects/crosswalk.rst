.. _Crosswalk:


***********
Crosswalk
***********

.. _crosswalkdescription:

Description
===============

Crosswalks are considered an "actor" in Quanser Interactive Labs Open Worlds.
Crosswalks can be spawned anywhere in the Open Worlds.

See the :ref:`crosswalkTutorial` to get a better understanding of using road
signage in Quanser Interactive Labs.



.. _crosswalklibrary:

Library
========

.. autoclass:: qvl.crosswalk.QLabsCrosswalk

.. _crosswalkConstants:

Constants
==========

.. autoattribute:: qvl.crosswalk.QLabsCrosswalk.ID_CROSSWALK

.. _crosswalkVars:

Member Variables
=================

.. autoattribute:: qvl.crosswalk.QLabsCrosswalk.actorNumber


.. _crosswalkMethods:

Methods
========

.. automethod:: qvl.crosswalk.QLabsCrosswalk.spawn
.. automethod:: qvl.crosswalk.QLabsCrosswalk.spawn_degrees
.. automethod:: qvl.crosswalk.QLabsCrosswalk.spawn_id
.. automethod:: qvl.crosswalk.QLabsCrosswalk.spawn_id_degrees
.. automethod:: qvl.crosswalk.QLabsCrosswalk.spawn_id_and_parent_with_relative_transform
.. automethod:: qvl.crosswalk.QLabsCrosswalk.spawn_id_and_parent_with_relative_transform_degrees
.. automethod:: qvl.crosswalk.QLabsCrosswalk.destroy
.. automethod:: qvl.crosswalk.QLabsCrosswalk.destroy_all_actors_of_class
.. automethod:: qvl.crosswalk.QLabsCrosswalk.ping
.. automethod:: qvl.crosswalk.QLabsCrosswalk.get_world_transform
.. automethod:: qvl.crosswalk.QLabsCrosswalk.get_world_transform_degrees
.. automethod:: qvl.crosswalk.QLabsCrosswalk.parent_with_relative_transform
.. automethod:: qvl.crosswalk.QLabsCrosswalk.parent_with_relative_transform_degrees
.. automethod:: qvl.crosswalk.QLabsCrosswalk.parent_with_current_world_transform
.. automethod:: qvl.crosswalk.QLabsCrosswalk.parent_break

.. _crosswalkConfig:

Configurations
================
There are 3 different configurations (0-2) available for crosswalks generated
in QLabs.

.. image:: ../pictures/configuration_crosswalk.png

.. _crosswalkConnect:

Connection Points
===================

There are no connection points for this actor class.

-------------------------------------------------------------------------------

.. _crosswalkTutorial:

Crosswalk Tutorial
===================

.. tabs::
    .. tab:: Python

        .. dropdown:: Python Tutorial

            Raw to download this tutorial: |road_signage_tutorial.py|.

            .. |road_signage_tutorial.py| replace::
                :download:`Crosswalk Tutorial (.py) <../../../tutorials/road_signage_tutorial.py>`

            .. literalinclude:: ../../../tutorials/road_signage_tutorial.py
                :language: python
                :linenos:

    .. tab:: Matlab

        .. dropdown:: Matlab Tutorial

            Raw to download this tutorial: |crosswalks_tutorial.m|.

            .. |crosswalks_tutorial.m| replace::
                :download:`Crosswalks Tutorial (.m) <../../../tutorials/crosswalks_tutorial.m>`

            .. literalinclude:: ../../../tutorials/crosswalks_tutorial.m
                :language: Matlab
                :linenos:
