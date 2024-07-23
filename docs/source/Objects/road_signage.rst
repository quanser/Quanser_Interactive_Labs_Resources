.. _Road_Signage:


#############
Road Signage
#############


.. _roadsignagedescription:

******************
Description
******************

Road signage is considered an "actor" in Quanser Interactive Labs Open Worlds.
The road signage library controls the road signage available to be placed in
the QLabs environment.
Road signage can be spawned anywhere in the Open Worlds.

See the :ref:`roadsignageTutorial` to get a better understanding of using road
signage in Quanser Interactive Labs.


.. contents:: Table of Contents
    :backlinks: none
    :depth: 2



-------------------------------------------------------------------------------

****************
Roundabout Sign
****************

.. _roundaboutlibrary:

Library
========

.. autoclass:: qvl.roundabout_sign.QLabsRoundaboutSign

.. _roundaboutConstants:

Constants
==========

.. autoattribute:: qvl.roundabout_sign.QLabsRoundaboutSign.ID_ROUNDABOUT_SIGN

.. _roundaboutVars:

Member Variables
=================

.. autoattribute:: qvl.roundabout_sign.QLabsRoundaboutSign.actorNumber

.. _roundaboutMethods:

Methods
========

.. automethod:: qvl.roundabout_sign.QLabsRoundaboutSign.spawn
.. automethod:: qvl.roundabout_sign.QLabsRoundaboutSign.spawn_degrees
.. automethod:: qvl.roundabout_sign.QLabsRoundaboutSign.spawn_id
.. automethod:: qvl.roundabout_sign.QLabsRoundaboutSign.spawn_id_degrees
.. automethod:: qvl.roundabout_sign.QLabsRoundaboutSign.spawn_id_and_parent_with_relative_transform
.. automethod:: qvl.roundabout_sign.QLabsRoundaboutSign.spawn_id_and_parent_with_relative_transform_degrees
.. automethod:: qvl.roundabout_sign.QLabsRoundaboutSign.destroy
.. automethod:: qvl.roundabout_sign.QLabsRoundaboutSign.destroy_all_actors_of_class
.. automethod:: qvl.roundabout_sign.QLabsRoundaboutSign.ping
.. automethod:: qvl.roundabout_sign.QLabsRoundaboutSign.get_world_transform
.. automethod:: qvl.roundabout_sign.QLabsRoundaboutSign.get_world_transform_degrees
.. automethod:: qvl.roundabout_sign.QLabsRoundaboutSign.parent_with_relative_transform
.. automethod:: qvl.roundabout_sign.QLabsRoundaboutSign.parent_with_relative_transform_degrees
.. automethod:: qvl.roundabout_sign.QLabsRoundaboutSign.parent_with_current_world_transform
.. automethod:: qvl.roundabout_sign.QLabsRoundaboutSign.parent_break


.. _roundaboutConfig:

Configurations
===============

There is only one configuration (0) of the roundabout sign actor generated in
QLabs.

.. image:: ../pictures/roundaboutsign.png

.. _roundaboutConnect:

Connection Points
==================

There are no connection points for this actor class.

-------------------------------------------------------------------------------

***********
Stop Sign
***********

.. _stopsignlibrary:

Library
========

.. autoclass:: qvl.stop_sign.QLabsStopSign

.. _stopsignConstants:

Constants
==========

.. autoattribute:: qvl.stop_sign.QLabsStopSign.ID_STOP_SIGN

.. _stopsignVars:

Member Variables
==================

.. autoattribute:: qvl.stop_sign.QLabsStopSign.actorNumber

.. _stopsignMethods:

Methods
========

.. automethod:: qvl.stop_sign.QLabsStopSign.spawn
.. automethod:: qvl.stop_sign.QLabsStopSign.spawn_degrees
.. automethod:: qvl.stop_sign.QLabsStopSign.spawn_id
.. automethod:: qvl.stop_sign.QLabsStopSign.spawn_id_degrees
.. automethod:: qvl.stop_sign.QLabsStopSign.spawn_id_and_parent_with_relative_transform
.. automethod:: qvl.stop_sign.QLabsStopSign.spawn_id_and_parent_with_relative_transform_degrees
.. automethod:: qvl.stop_sign.QLabsStopSign.destroy
.. automethod:: qvl.stop_sign.QLabsStopSign.destroy_all_actors_of_class
.. automethod:: qvl.stop_sign.QLabsStopSign.ping
.. automethod:: qvl.stop_sign.QLabsStopSign.get_world_transform
.. automethod:: qvl.stop_sign.QLabsStopSign.get_world_transform_degrees
.. automethod:: qvl.stop_sign.QLabsStopSign.parent_with_relative_transform
.. automethod:: qvl.stop_sign.QLabsStopSign.parent_with_relative_transform_degrees
.. automethod:: qvl.stop_sign.QLabsStopSign.parent_with_current_world_transform
.. automethod:: qvl.stop_sign.QLabsStopSign.parent_break

.. _stopsignConfig:

Configurations
================

There is only one configuration (0) of the stop sign actor generated in QLabs.

.. image:: ../pictures/stopsign.png

.. _stopsignConnect:

Connection Points
====================

There are no connection points for this actor class.


-------------------------------------------------------------------------------

***********
Yield Sign
***********

.. _yieldsignlibrary:

Library
========

.. autoclass:: qvl.yield_sign.QLabsYieldSign

.. _yieldsignConstants:

Constants
==========

.. autoattribute:: qvl.yield_sign.QLabsYieldSign.ID_YIELD_SIGN

.. _yieldsignVars:

Member Variables
==================

.. autoattribute:: qvl.yield_sign.QLabsYieldSign.actorNumber

.. _yieldsignMethods:

Methods
========

.. automethod:: qvl.yield_sign.QLabsYieldSign.spawn
.. automethod:: qvl.yield_sign.QLabsYieldSign.spawn_degrees
.. automethod:: qvl.yield_sign.QLabsYieldSign.spawn_id
.. automethod:: qvl.yield_sign.QLabsYieldSign.spawn_id_degrees
.. automethod:: qvl.yield_sign.QLabsYieldSign.spawn_id_and_parent_with_relative_transform
.. automethod:: qvl.yield_sign.QLabsYieldSign.spawn_id_and_parent_with_relative_transform_degrees
.. automethod:: qvl.yield_sign.QLabsYieldSign.destroy
.. automethod:: qvl.yield_sign.QLabsYieldSign.destroy_all_actors_of_class
.. automethod:: qvl.yield_sign.QLabsYieldSign.ping
.. automethod:: qvl.yield_sign.QLabsYieldSign.get_world_transform
.. automethod:: qvl.yield_sign.QLabsYieldSign.get_world_transform_degrees
.. automethod:: qvl.yield_sign.QLabsYieldSign.parent_with_relative_transform
.. automethod:: qvl.yield_sign.QLabsYieldSign.parent_with_relative_transform_degrees
.. automethod:: qvl.yield_sign.QLabsYieldSign.parent_with_current_world_transform
.. automethod:: qvl.yield_sign.QLabsYieldSign.parent_break



.. _yieldsignConfig:

Configurations
===============

There is only one configuration (0) of the yield sign actor generated in QLabs.

.. image:: ../pictures/yieldsign.png

.. _yieldsignConnect:

Connection Points
==================

There are no connection points for this actor class.

-------------------------------------------------------------------------------

.. _roadsignageTutorial:

**********************
Road Signage Tutorial
**********************

.. tabs::
    .. tab:: Python

        .. dropdown:: Python Tutorial

            Raw to download this tutorial: |road_signage_tutorial.py|.

            .. |road_signage_tutorial.py| replace::
                :download:`Road Signage Tutorial (.py) <../../../tutorials/road_signage_tutorial.py>`

            .. literalinclude:: ../../../tutorials/road_signage_tutorial.py
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

            Raw to download this tutorial: |road_signage_tutorial.m|.

            .. |road_signage_tutorial.m| replace::
                :download:`Road Signage Tutorial (.m) <../../../tutorials/road_signage_tutorial.m>`

            .. literalinclude:: ../../../tutorials/road_signage_tutorial.m
                :language: Matlab
                :linenos:

        .. dropdown:: Complete Road Signage Matlab Tutorial

            Raw to download this tutorial: |complete_road_signage_tutorial.m|.

            .. |complete_road_signage_tutorial.m| replace::
                :download:`Complete Road Signage Tutorial (.m) <../../../tutorials/complete_road_signage_tutorial.m>`

            .. literalinclude:: ../../../tutorials/complete_road_signage_tutorial.m
                :language: Matlab
                :linenos: