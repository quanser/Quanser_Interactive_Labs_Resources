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

.. autoclass:: python.qvl.crosswalk.QLabsCrosswalk

.. _crosswalkConstants:

Constants
==========

.. autoattribute:: python.qvl.crosswalk.QLabsCrosswalk.ID_CROSSWALK

.. _crosswalkVars:

Member Variables
=================

.. autoattribute:: python.qvl.crosswalk.QLabsCrosswalk.actorNumber


.. _crosswalkMethods:

Methods
========

.. automethod:: python.qvl.crosswalk.QLabsCrosswalk.spawn
.. automethod:: python.qvl.crosswalk.QLabsCrosswalk.spawn_degrees
.. automethod:: python.qvl.crosswalk.QLabsCrosswalk.spawn_id
.. automethod:: python.qvl.crosswalk.QLabsCrosswalk.spawn_id_degrees
.. automethod:: python.qvl.crosswalk.QLabsCrosswalk.spawn_id_and_parent_with_relative_transform
.. automethod:: python.qvl.crosswalk.QLabsCrosswalk.spawn_id_and_parent_with_relative_transform_degrees
.. automethod:: python.qvl.crosswalk.QLabsCrosswalk.destroy
.. automethod:: python.qvl.crosswalk.QLabsCrosswalk.destroy_all_actors_of_class
.. automethod:: python.qvl.crosswalk.QLabsCrosswalk.ping
.. automethod:: python.qvl.crosswalk.QLabsCrosswalk.get_world_transform
.. automethod:: python.qvl.crosswalk.QLabsCrosswalk.get_world_transform_degrees
.. automethod:: python.qvl.crosswalk.QLabsCrosswalk.parent_with_relative_transform
.. automethod:: python.qvl.crosswalk.QLabsCrosswalk.parent_with_relative_transform_degrees
.. automethod:: python.qvl.crosswalk.QLabsCrosswalk.parent_with_current_world_transform
.. automethod:: python.qvl.crosswalk.QLabsCrosswalk.parent_break

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

            Raw to download this tutorial: |crosswalk_tutorial.py|.

            .. |crosswalk_tutorial.py| replace::
                :download:`Crosswalk Tutorial (.py) <../../../tutorials/crosswalk_tutorial.py>`

            .. literalinclude:: ../../../tutorials/crosswalk_tutorial.py
                :language: python
                :linenos:

        .. dropdown:: Complete Road Signage Python Tutorial

            Raw to download this tutorial: |complete_road_signage_tutorial.py|.

            .. |complete_road_signage_tutorial.py| replace::
                :download:`Complete Road Signage Tutorial (.py) <../../../tutorials/complete_road_signage_tutorial.py>`

            .. literalinclude:: ../../../tutorials/complete_road_signage_tutorial.py
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

        .. dropdown:: Complete Road Signage Matlab Tutorial

            Raw to download this tutorial: |complete_road_signage_tutorial.m|.

            .. |complete_road_signage_tutorial.m| replace::
                :download:`Complete Road Signage Tutorial (.m) <../../../tutorials/complete_road_signage_tutorial.m>`

            .. literalinclude:: ../../../tutorials/complete_road_signage_tutorial.m
                :language: Matlab
                :linenos:

