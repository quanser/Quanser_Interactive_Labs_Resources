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

.. important::
    All of the office objects have the same methods and member variables. 
    To simplify this documentation, the methods and member variables are documented
    only once, see :ref:`roadSignsShared` and the :ref:`roadsignageTutorial`.
    No office object has connection points or different configurations.

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


.. image:: ../pictures/roundaboutsign.png

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


.. image:: ../pictures/stopsign.png


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


.. image:: ../pictures/yieldsign.png

-------------------------------------------------------------------------------

.. _roadSignsShared:

******************************
Shared Variables and Methods
******************************

.. _roadSignsVars:

Member Variables
=================

.. autoattribute:: qvl.actor.QLabsActor.actorNumber

.. _roadSignsMethods:

Methods
========

.. automethod:: qvl.actor.QLabsActor.spawn
.. automethod:: qvl.actor.QLabsActor.spawn_degrees
.. automethod:: qvl.actor.QLabsActor.spawn_id
.. automethod:: qvl.actor.QLabsActor.spawn_id_degrees
.. automethod:: qvl.actor.QLabsActor.spawn_id_and_parent_with_relative_transform
.. automethod:: qvl.actor.QLabsActor.spawn_id_and_parent_with_relative_transform_degrees
.. automethod:: qvl.actor.QLabsActor.destroy
.. automethod:: qvl.actor.QLabsActor.destroy_all_actors_of_class
.. automethod:: qvl.actor.QLabsActor.ping
.. automethod:: qvl.actor.QLabsActor.get_world_transform
.. automethod:: qvl.actor.QLabsActor.get_world_transform_degrees
.. automethod:: qvl.actor.QLabsActor.parent_with_relative_transform
.. automethod:: qvl.actor.QLabsActor.parent_with_relative_transform_degrees
.. automethod:: qvl.actor.QLabsActor.parent_with_current_world_transform
.. automethod:: qvl.actor.QLabsActor.parent_break


Configurations
===============

There is only one configuration (0) for the road sign actors generated in
QLabs.


Connection Points
==================

There are no connection points for any of these actor classes.

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