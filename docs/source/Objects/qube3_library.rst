.. _Qube3:

*****************
Qube-Servo 3
*****************

.. _qube3Description:

Description
============

The Qube-Servo 3 is considered an "actor" in Quanser Interactive Labs.
It can be spawned in the workspaces that support it and controlled through its
HIL ports. See :ref:`spawnableactorsWorkspaces` for the workspaces where this
actor is available.

.. _qube3Library:

Library
========

.. autoclass:: qvl.qube3.QLabsQube3

.. _qube3Constants:

Constants
============

.. autoattribute:: qvl.qube3.QLabsQube3.ID_QUBE3

.. _qube3MemberVars:

Member Variables
==================

.. autoattribute:: qvl.qube3.QLabsQube3.actorNumber

.. _qube3ParentMethods:

Parent Class (actor.py) Methods
================================

.. automethod:: qvl.qube3.QLabsQube3.__init__
.. automethod:: qvl.qube3.QLabsQube3.spawn
.. automethod:: qvl.qube3.QLabsQube3.spawn_degrees
.. automethod:: qvl.qube3.QLabsQube3.spawn_id
.. automethod:: qvl.qube3.QLabsQube3.spawn_id_degrees
.. automethod:: qvl.qube3.QLabsQube3.spawn_id_and_parent_with_relative_transform
.. automethod:: qvl.qube3.QLabsQube3.spawn_id_and_parent_with_relative_transform_degrees
.. automethod:: qvl.qube3.QLabsQube3.destroy
.. automethod:: qvl.qube3.QLabsQube3.destroy_all_actors_of_class
.. automethod:: qvl.qube3.QLabsQube3.get_world_transform
.. automethod:: qvl.qube3.QLabsQube3.get_world_transform_degrees
.. automethod:: qvl.qube3.QLabsQube3.ping
.. automethod:: qvl.qube3.QLabsQube3.parent_with_relative_transform
.. automethod:: qvl.qube3.QLabsQube3.parent_with_relative_transform_degrees
.. automethod:: qvl.qube3.QLabsQube3.parent_with_current_world_transform
.. automethod:: qvl.qube3.QLabsQube3.parent_break
.. automethod:: qvl.qube3.QLabsQube3.set_custom_properties
.. automethod:: qvl.qube3.QLabsQube3.get_custom_properties

.. _qube3Config:

Configurations
================

There are three configurations (0-2) for the Qube-Servo 3 actor class.

    * 0 - Hub only
    * 1 - Inertial disc
    * 2 - Pendulum

.. image:: ../pictures/configuration_qube3.png

.. _qube3Connect:

Connection Points
====================
.. |conn0| image:: ../pictures/connection_qube3_0.png
   :height: 50pt

.. |conn1| image:: ../pictures/connection_qube3_1.png
   :height: 50pt


.. table::
    :widths: 20, 11, 11, 11, 53
    :align: center

    =============================== ====================== ============ ====================================================== ===========
    Image (Click for enlarged view) Reference Frame Number Parent Frame Relative Transform to Parent (Location, Rotation)      Description
    =============================== ====================== ============ ====================================================== ===========
    |conn0|                         0                                                                                          The base frame is located on the center between the four feet.
    |conn1|                         1                      0            [0,0,0.116] [0,0,0]                                    Top of the hub mounting surface.
    =============================== ====================== ============ ====================================================== ===========


