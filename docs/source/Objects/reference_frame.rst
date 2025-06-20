.. _Reference_Frame_Library:

*****************
Reference Frames
*****************

.. _referenceFrameDescription:

Description
============

The reference frame is an actor that, by default, is hidden, but can still be used to create parent-child
kinematic relationships, or simply for tracking points of interest that can be queried to get the world
location.

Optionally, reference frames can also be spawned with visible axes to aid understanding the current
transformation of child actors.

.. _referenceFrameLibrary:

Reference Frame Library
========================

.. autoclass:: qvl.reference_frame.QLabsReferenceFrame

.. _referenceFrameConstants:

Constants
============

.. autoattribute:: qvl.reference_frame.QLabsReferenceFrame.ID_REFERENCE_FRAME

.. _referenceFrameMemberVars:

Member Variables
=================

.. autoattribute:: qvl.reference_frame.QLabsReferenceFrame.actorNumber


.. _referenceFrameMethods:

Methods
========

.. automethod:: qvl.reference_frame.QLabsReferenceFrame.set_transform
.. automethod:: qvl.reference_frame.QLabsReferenceFrame.set_transform_degrees
.. automethod:: qvl.reference_frame.QLabsReferenceFrame.set_icon_scale


.. _referenceFrameParentMethods:

Parent Class (actor.py) Methods
================================

.. automethod:: qvl.reference_frame.QLabsReferenceFrame.__init__
.. automethod:: qvl.reference_frame.QLabsReferenceFrame.spawn
.. automethod:: qvl.reference_frame.QLabsReferenceFrame.spawn_degrees
.. automethod:: qvl.reference_frame.QLabsReferenceFrame.spawn_id
.. automethod:: qvl.reference_frame.QLabsReferenceFrame.spawn_id_degrees
.. automethod:: qvl.reference_frame.QLabsReferenceFrame.spawn_id_and_parent_with_relative_transform
.. automethod:: qvl.reference_frame.QLabsReferenceFrame.spawn_id_and_parent_with_relative_transform_degrees
.. automethod:: qvl.reference_frame.QLabsReferenceFrame.destroy
.. automethod:: qvl.reference_frame.QLabsReferenceFrame.destroy_all_actors_of_class
.. automethod:: qvl.reference_frame.QLabsReferenceFrame.ping
.. automethod:: qvl.reference_frame.QLabsReferenceFrame.get_world_transform
.. automethod:: qvl.reference_frame.QLabsReferenceFrame.get_world_transform_degrees
.. automethod:: qvl.reference_frame.QLabsReferenceFrame.parent_with_relative_transform
.. automethod:: qvl.reference_frame.QLabsReferenceFrame.parent_with_relative_transform_degrees
.. automethod:: qvl.reference_frame.QLabsReferenceFrame.parent_with_current_world_transform
.. automethod:: qvl.reference_frame.QLabsReferenceFrame.parent_break
    
.. _referenceFrameConfigs:

Configurations
===============

There are 3 configurations (0-2) for the reference actor class. 0 - Hidden, 1 - Axes arrows, 2 - Axes arrows with labels

.. _referenceFrameConnect:

Connection Points
==================

There are no connection points for the reference frame.

.. **See Also:**
