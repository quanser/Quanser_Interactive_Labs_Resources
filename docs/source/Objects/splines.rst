.. _Spline_Base:

*****************
Splines
*****************

.. _splineDescription:

Description
============

The spline actor can be used to create both curves and straight lines.
Line color can be set for the entire line, and line width can be set on a
per-control point basis.
Splines are created by first spawning a spline actor and then adding control
points.
Depending on the configuration used when spawned, you can get variations on the
curve shape or straight lines.

See the :ref:`splineTutorial` to get a better understanding of using splines in
Quanser Interactive Labs.

.. _splinelibrary:

Library
========

.. autoclass:: qvl.spline_line.QLabsSplineLine

.. _splineConstants:

Constants
============

.. autoattribute:: qvl.spline_line.QLabsSplineLine.ID_SPLINE_LINE
.. autoattribute:: qvl.spline_line.QLabsSplineLine.LINEAR
.. autoattribute:: qvl.spline_line.QLabsSplineLine.CURVE
.. autoattribute:: qvl.spline_line.QLabsSplineLine.CONSTANT
.. autoattribute:: qvl.spline_line.QLabsSplineLine.CLAMPED_CURVE


.. _splineMemberVars:

Member Variables
=================

.. autoattribute:: qvl.spline_line.QLabsSplineLine.actorNumber

.. _splineMethods:

Methods
========

.. automethod:: qvl.spline_line.QLabsSplineLine.__init__
.. automethod:: qvl.spline_line.QLabsSplineLine.spawn
.. automethod:: qvl.spline_line.QLabsSplineLine.spawn_degrees
.. automethod:: qvl.spline_line.QLabsSplineLine.spawn_id
.. automethod:: qvl.spline_line.QLabsSplineLine.spawn_id_degrees
.. automethod:: qvl.spline_line.QLabsSplineLine.spawn_id_and_parent_with_relative_transform
.. automethod:: qvl.spline_line.QLabsSplineLine.spawn_id_and_parent_with_relative_transform_degrees
.. automethod:: qvl.spline_line.QLabsSplineLine.destroy
.. automethod:: qvl.spline_line.QLabsSplineLine.destroy_all_actors_of_class
.. automethod:: qvl.spline_line.QLabsSplineLine.ping
.. automethod:: qvl.spline_line.QLabsSplineLine.get_world_transform
.. automethod:: qvl.spline_line.QLabsSplineLine.get_world_transform_degrees
.. automethod:: qvl.spline_line.QLabsSplineLine.set_points
.. automethod:: qvl.spline_line.QLabsSplineLine.circle_from_center
.. automethod:: qvl.spline_line.QLabsSplineLine.arc_from_center
.. automethod:: qvl.spline_line.QLabsSplineLine.arc_from_center_degrees
.. automethod:: qvl.spline_line.QLabsSplineLine.rounded_rectangle_from_center
.. automethod:: qvl.spline_line.QLabsSplineLine.parent_with_relative_transform
.. automethod:: qvl.spline_line.QLabsSplineLine.parent_with_relative_transform_degrees
.. automethod:: qvl.spline_line.QLabsSplineLine.parent_with_current_world_transform
.. automethod:: qvl.spline_line.QLabsSplineLine.parent_break

.. _splineConfig:

Configurations
================

.. image:: ../pictures/configuration_spline_types.png
    :scale: 75%
    :align: center

Configurations 0 to 3 are shown from top to bottom in the above image using the
same set of control points.

.. table::
    :widths: 10, 10, 80
    :align: center

    ============= ============= ===========
    Configuration Mode          Description
    ============= ============= ===========
    0             Linear        The tangent of the curve at each control point is set to match the tangent of the start of each line segment.
    1             Curve         The tangent of the curve at each control point is an average of the two adjacent line segments and matched to the start and end tangents.
    2             Constant      Straight line segments
    3             Clamped Curve As angles become more acute, the curve will transition from a smooth change to a sharp point.
    ============= ============= ===========

.. _splineConnect:

Connection Points
====================

There are no connection points for this actor class.

.. _splineTutorial:

Splines Tutorial
====================

.. tabs::
    .. tab:: Python

        .. dropdown:: Python Tutorial

            Raw to download this tutorial: |splines_tutorial.py|.

            .. |splines_tutorial.py| replace::
                :download:`Splines Tutorial (.py) <../../../tutorials/splines_tutorial.py>`

            .. literalinclude:: ../../../tutorials/splines_tutorial.py
                :language: python
                :linenos:

    .. tab:: Matlab

        .. dropdown:: Matlab Tutorial

            Raw to download this tutorial: |splines_tutorial.m|.

            .. |splines_tutorial.m| replace::
                :download:`Splines tutorial (.m) <../../../tutorials/splines_tutorial.m>`

            .. literalinclude:: ../../../tutorials/splines_tutorial.m
                :language: Matlab
                :linenos:
    
