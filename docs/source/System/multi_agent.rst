.. _MultiAgent_Library:

*********************
Multi Agent Class
*********************

.. _multiAgentDescription:

Description
=============

This class is for spawning multiple agents in Quanser Interactive Labs that will then
be controlled by the user not through the QLabs interface but through the HIL interface.
For this to work, the user must have Quanser's teaching or research content installed in
their computer so that the necessary RT models can run. The class will create a new folder in the
RTMODELS_DIR directory called MultiAgent where it will store the necessary files to run the
agents. 
The class will also create a JSON file called RobotAgents.json that will store the
information of the agents that were spawned. This JSON file will be used by the user to
initialize the robots using python or simulink as it has all the necessary port numbers used 
for each robot.

See the :ref:`MultiAgentTutorial` to get a better understanding of using QCars in
Quanser Interactive Labs.

.. _multiAgentLibrary:

Library
=========

.. autoclass:: qvl.multiAgent.MultiAgent


.. _multiAgentMemberVars:

Member Variables
=================

.. autoattribute:: qvl.multiAgent.MultiAgent.robotActors
.. autoattribute:: qvl.multiAgent.MultiAgent.robotsDict

.. _multiAgentMethods:

Methods
=========

.. automethod:: qvl.multiAgent.MultiAgent.__init__
.. automethod:: qvl.multiAgent.readRobots


-------------------------------------------------------------------------------

.. _MultiAgentTutorial:

MultiAgent Tutorial
=====================

.. tabs::
    .. tab:: Python

        .. dropdown:: Python Tutorial

            Raw to download this tutorial: |multiAgent_tutorial.py|.

            .. |multiAgent_tutorial.py| replace::
                :download:`Multi Agent Tutorial (.py) <../../../tutorials/multiAgent_tutorial.py>`

            .. literalinclude:: ../../../tutorials/multiAgent_tutorial.py
                :language: python
                :linenos:

    .. tab:: Matlab

        Coming Soon!

        ..
            .. dropdown:: Matlab Tutorial

            Raw to download this tutorial: |qcar2_tutorial.m|.

            .. |qcar2_tutorial.m| replace::
                :download:`QCar 2 Tutorial (.m) <../../../tutorials/qcar2_tutorial.m>`

            .. literalinclude:: ../../../tutorials/qcar2_tutorial.m
                :language: Matlab
                :linenos: