.. _Office_Objects:


#################
Office Objects
#################

.. image:: ../pictures/banner_office.png
    :width: 800px
    :align: center


.. _officedescription:

******************
Description
******************

Office objects are considered "actors" in Quanser Interactive Labs Open Worlds.
The office objects library controls the office objects available to be placed in
the QLabs environment.
Office objects can be spawned anywhere in the Open Worlds.

See the :ref:`officeTutorial` to get a better understanding of 
using office objects in Quanser Interactive Labs.


.. contents:: Table of Contents
    :backlinks: none
    :depth: 2

-------------------------------------------------------------------------------

.. important::
    All of the office objects have the same methods and member variables. 
    To simplify this documentation, the methods and member variables are documented
    only once, see :ref:`officeShared` and the :ref:`officeTutorial`.
    No office object has connection points or different configurations.

****************
Desk
****************

.. _desklibrary:

Library
========

.. autoclass:: qvl.desk.QLabsDesk

.. _deskConstants:

Constants
==========

.. autoattribute:: qvl.desk.QLabsDesk.ID_DESK

.. image:: ../pictures/desk.png

-------------------------------------------------------------------------------

***********
Chair
***********

.. _chairlibrary:

Library
========

.. autoclass:: qvl.chair.QLabsChair

.. _chairConstants:

Constants
==========

.. autoattribute:: qvl.chair.QLabsChair.ID_CHAIR

.. image:: ../pictures/chair.png

-------------------------------------------------------------------------------

***********
Computer
***********

.. _computerlibrary:

Library
========

.. autoclass:: qvl.computer.QLabsComputer

.. _computerConstants:

Constants
==========

.. autoattribute:: qvl.computer.QLabsComputer.ID_COMPUTER

.. image:: ../pictures/computer.png

-------------------------------------------------------------------------------


*****************
Computer Monitor
*****************

.. _monitorlibrary:

Library
========

.. autoclass:: qvl.computer_monitor.QLabsComputerMonitor

.. _monitorConstants:

Constants
==========

.. autoattribute:: qvl.computer_monitor.QLabsComputerMonitor.ID_COMPUTER_MONITOR

.. image:: ../pictures/monitor.png

-------------------------------------------------------------------------------

*******************
Computer Keyboard
*******************

.. _keyboardlibrary:

Library
========

.. autoclass:: qvl.computer_keyboard.QLabsComputerKeyboard

.. _keyboardConstants:

Constants
==========

.. autoattribute:: qvl.computer_keyboard.QLabsComputerKeyboard.ID_COMPUTER_KEYBOARD

.. image:: ../pictures/keyboard.png

-------------------------------------------------------------------------------

*******************
Computer Mouse
*******************

.. _mouselibrary:

Library
========

.. autoclass:: qvl.computer_mouse.QLabsComputerMouse

.. _mouseConstants:

Constants
==========

.. autoattribute:: qvl.computer_mouse.QLabsComputerMouse.ID_COMPUTER_MOUSE

.. image:: ../pictures/mouseActor.png
    
-------------------------------------------------------------------------------

.. _officeShared:

******************************
Shared Variables and Methods
******************************

.. _officeVars:

Member Variables
=================

.. autoattribute:: qvl.actor.QLabsActor.actorNumber
    :noindex:

.. _officeMethods:

Parent Class (actor.py) Methods
================================

.. automethod:: qvl.actor.QLabsActor.spawn
    :noindex:
.. automethod:: qvl.actor.QLabsActor.spawn_degrees
    :noindex:
.. automethod:: qvl.actor.QLabsActor.spawn_id
    :noindex:
.. automethod:: qvl.actor.QLabsActor.spawn_id_degrees
    :noindex:
.. automethod:: qvl.actor.QLabsActor.spawn_id_and_parent_with_relative_transform
    :noindex:
.. automethod:: qvl.actor.QLabsActor.spawn_id_and_parent_with_relative_transform_degrees
    :noindex:
.. automethod:: qvl.actor.QLabsActor.destroy
    :noindex:
.. automethod:: qvl.actor.QLabsActor.destroy_all_actors_of_class
    :noindex:
.. automethod:: qvl.actor.QLabsActor.ping
    :noindex:
.. automethod:: qvl.actor.QLabsActor.get_world_transform
    :noindex:
.. automethod:: qvl.actor.QLabsActor.get_world_transform_degrees
    :noindex:
.. automethod:: qvl.actor.QLabsActor.parent_with_relative_transform
    :noindex:
.. automethod:: qvl.actor.QLabsActor.parent_with_relative_transform_degrees
    :noindex:
.. automethod:: qvl.actor.QLabsActor.parent_with_current_world_transform
    :noindex:
.. automethod:: qvl.actor.QLabsActor.parent_break
    :noindex:


Configurations
===============

There is only one configuration (0) for the office actors generated in
QLabs.


Connection Points
==================

There are no connection points for any of these actor classes.

-------------------------------------------------------------------------------
    
.. _officeTutorial:

*************************
Office Objects Tutorial
*************************

.. tabs::
    .. tab:: Python

        .. dropdown:: Python Tutorial

            Raw to download this tutorial: |office_tutorial.py|.

            .. |office_tutorial.py| replace::
                :download:`Office Objects Tutorial (.py) <../../../tutorials/office_tutorial.py>`

            .. literalinclude:: ../../../tutorials/office_tutorial.py
                :language: python
                :linenos:

        .. dropdown:: Python Tutorial Multiple Desks 

            Raw to download this tutorial: |office_tutorial2.py|.

            This tutorial uses a function to simplify creating multiple desks set up the same way. 

            .. |office_tutorial2.py| replace::
                :download:`Office Objects Tutorial (.py) <../../../tutorials/office_tutorial2.py>`

            .. literalinclude:: ../../../tutorials/office_tutorial2.py
                :language: python
                :linenos:


    .. tab:: Matlab

        .. dropdown:: Matlab Tutorial

           Coming Soon!
