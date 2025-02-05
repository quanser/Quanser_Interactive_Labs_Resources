.. _MultiAgent_Library:

*********************
Multi Agent Class
*********************

.. _multiAgentDescription:

.. note::
    This class is for advanced users wanting to control multiple robots through QUARC or Quanser SDK.
    Make sure you have installed the academic resources from the Quanser website.
    It will only work with Quanser robots that you have a valid Quanser Interactive Labs license for.

    This class is still under development. 

    For any questions, please contact Quanser Support at tech@quanser.com 

Description
=============

This class can be utilized for spawning multiple robot agents in 
Quanser Interactive Labs for user control directly via QUARC or Quanser SDK. 
This library requires a complete installation of Quanser's academic resources (available through www.quanser.com) 
for associated real-time application modules and other supporting libraries.

The class copies and creates all necessary files to run multiple robots at the same time.
It will also create a JSON file called RobotAgents.json that will store the information 
of the agents that were spawned as well as its port and URI numbers.

See the :ref:`MultiAgentTutorial` to get a better understanding of using 
the MultiAgent class to spawn multiple agents.

.. _multiAgentLibrary:

Library
=========

.. autoclass:: qvl.multi_agent.MultiAgent


.. _multiAgentMemberVars:

Member Variables
=================

.. autoattribute:: qvl.multi_agent.MultiAgent.robotActors
.. autoattribute:: qvl.multi_agent.MultiAgent.robotsDict

.. _multiAgentMethods:

Methods
=========

.. automethod:: qvl.multi_agent.MultiAgent.__init__

.. note::
    The dictionaries can have the following keys (one per robot that will be spawned):
        - "RobotType": string - can be "QC2", "QCar2", "QBP", "QArm", "QA", "QDrone2", or "QD2"
        - "Location": float array[3] - for spawning in x, y, z of the QLabs environment
        - "Rotation": (Optional) float array[3] - for spawning in x, y, z. Can be in Degrees or Radians. If it is radians, set the "Radians" key to True. If not defined, will spawn with [0, 0, 0] rotation
        - "Radians": (Optional) boolean - defaults to False. Only needed if rotation is in Radians
        - "Scale": (Optional) float - if you want to change the scaling of the spawned object. If not defined, will spawn with scaling of 1. The scaling will apply in x, y, and z
        - "actorNumber": (Optional) int - set only if you want a predefined actor number for your robot. If not, it will use the next available number for the type of robot. If the number is already in use, it will overwrite it. We do not recommend using it unless tracking of actors is done manually by the user.
        


.. automethod:: qvl.multi_agent.readRobots


-------------------------------------------------------------------------------

.. _MultiAgentTutorial:

MultiAgent Tutorial
=====================

.. tabs::
    .. tab:: Python

        .. dropdown:: Python Tutorial

            Raw to download this tutorial: |multiagent_tutorial.py|.

            .. |multiagent_tutorial.py| replace::
                :download:`Multi Agent Tutorial (.py) <../../../tutorials/multiagent_tutorial.py>`

            .. literalinclude:: ../../../tutorials/multiagent_tutorial.py
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