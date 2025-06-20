.. _Traffic_Light:

*****************
Traffic Light
*****************


.. _trafficlightdescription:

Description
============

A traffic light is considered an "actor" in Quanser Interactive Labs Open Worlds.
Traffic lights can be spawned anywhere in the Open Worlds.

See the :ref:`trafficlightTutorial` to get a better understanding of using road
signage in Quanser Interactive Labs.


.. _trafficlightlibrary:

Library
=========

.. autoclass:: qvl.traffic_light.QLabsTrafficLight

.. _trafficlightConstants:

Constants
===========

.. autoattribute:: qvl.traffic_light.QLabsTrafficLight.ID_TRAFFIC_LIGHT
.. autoattribute:: qvl.traffic_light.QLabsTrafficLight.COLOR_NONE
.. autoattribute:: qvl.traffic_light.QLabsTrafficLight.COLOR_RED
.. autoattribute:: qvl.traffic_light.QLabsTrafficLight.COLOR_YELLOW
.. autoattribute:: qvl.traffic_light.QLabsTrafficLight.COLOR_GREEN

.. _trafficlightVars:

Member Variables
==================

.. autoattribute:: qvl.traffic_light.QLabsTrafficLight.actorNumber

.. _trafficlightMethods:

Methods
=========

.. automethod:: qvl.traffic_light.QLabsTrafficLight.__init__
.. automethod:: qvl.traffic_light.QLabsTrafficLight.spawn
.. automethod:: qvl.traffic_light.QLabsTrafficLight.spawn_degrees
.. automethod:: qvl.traffic_light.QLabsTrafficLight.spawn_id
.. automethod:: qvl.traffic_light.QLabsTrafficLight.spawn_id_degrees
.. automethod:: qvl.traffic_light.QLabsTrafficLight.spawn_id_and_parent_with_relative_transform
.. automethod:: qvl.traffic_light.QLabsTrafficLight.spawn_id_and_parent_with_relative_transform_degrees
.. automethod:: qvl.traffic_light.QLabsTrafficLight.destroy
.. automethod:: qvl.traffic_light.QLabsTrafficLight.destroy_all_actors_of_class
.. automethod:: qvl.traffic_light.QLabsTrafficLight.ping
.. automethod:: qvl.traffic_light.QLabsTrafficLight.get_world_transform
.. automethod:: qvl.traffic_light.QLabsTrafficLight.get_world_transform_degrees
.. automethod:: qvl.traffic_light.QLabsTrafficLight.parent_with_relative_transform
.. automethod:: qvl.traffic_light.QLabsTrafficLight.parent_with_relative_transform_degrees
.. automethod:: qvl.traffic_light.QLabsTrafficLight.parent_with_current_world_transform
.. automethod:: qvl.traffic_light.QLabsTrafficLight.parent_break

.. automethod:: qvl.traffic_light.QLabsTrafficLight.set_color
.. automethod:: qvl.traffic_light.QLabsTrafficLight.get_color

.. _trafficlightConfig:

Configurations
===============

There are three configurations (0-2) for the traffic light actor class
generated in QLabs.

.. image:: ../pictures/configuration_trafficlight.png

.. _trafficlightConnect:

Connection Points
==================

There are no connection points for this actor class.

-------------------------------------------------------------------------------

.. _trafficlightTutorial:

Traffic Lights Tutorial
=========================

.. tabs::
    .. tab:: Python

        .. dropdown:: Python Tutorial

            Raw to download this tutorial: |traffic_lights_tutorial.py|.

            .. |traffic_lights_tutorial.py| replace::
                :download:`Traffic Lights Tutorial (.py) <../../../tutorials/traffic_lights_tutorial.py>`

            .. literalinclude:: ../../../tutorials/traffic_lights_tutorial.py
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

            Raw to download this tutorial: |traffic_lights_tutorial.m|.

            .. |traffic_lights_tutorial.m| replace::
                :download:`Traffic Lights Tutorial (.m) <../../../tutorials/traffic_lights_tutorial.m>`

            .. literalinclude:: ../../../tutorials/traffic_lights_tutorial.m
                :language: Matlab
                :linenos:

        .. dropdown:: Complete Road Signage Matlab Tutorial

            Raw to download this tutorial: |complete_road_signage_tutorial.m|.

            .. |complete_road_signage_tutorial.m| replace::
                :download:`Complete Road Signage Tutorial (.m) <../../../tutorials/complete_road_signage_tutorial.m>`

            .. literalinclude:: ../../../tutorials/complete_road_signage_tutorial.m
                :language: Matlab
                :linenos:

