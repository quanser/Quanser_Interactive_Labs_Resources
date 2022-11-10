.. _Getting Started:

***************
Getting Started
***************

Installation / Set Up
=====================

#. Create an account on `Portal <https://portal.quanser.com/Accounts/Login?returnUrl=/>`__ with your school email.

    .. tip:: Check the box "Remember Me" for QLabs to remember your account

#. Download Quanser Interactive Lab on the `Portal <https://portal.quanser.com/Accounts/Login?returnUrl=/>`__

    .. note:: All available content should be available to you on the main screen. If something is missing, try logging out and logging back in again.

#. Scroll using a mouse wheel or the arrow keys on either side of the screen to the QCar studio.  

#. Click on the QCar studio and select the workspace of choice.

Running a Python Script for QLabs SDCS
======================================

In order to run a python script in QLabs to control the enviroment and its objects, a few things that will need to be installed first.

.. Note that this will need to change when we agree what info will be where for customers.

Prerequisites
-------------

GitHub QLabs Libraries Download
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Download the common library off Github which will be needed in order to run the objects in your python script for QLabs `Virtual QCar Public Libraries <https://github.com/quanser/virtual_qcar_libraries>`__.

Download OpenCV-Python
^^^^^^^^^^^^^^^^^^^^^^
In the command terminal running as an admin (or in Linux running "sudo"), paste and run this code to install opencv on the computer.

.. code-block:: python

    pip install opencv-python

Python Package Update
^^^^^^^^^^^^^^^^^^^^^

Quanser has a set of python packages that need to be installed as well to run with your QUARC.
In order to do this, navigate to your QUARC python folder.

.. note:: You will need to have QUARC installed for this to work.
 
.. important:: Make sure the files in the QUARC python folder below have the same date as the date in the following code below before running it!

.. tabs::
    .. code-tab:: console Windows

        cd C:\Program Files\Quanser\QUARC\python
        python -m pip install --upgrade --find-links "%QUARC_DIR%\python" "%QUARC_DIR%\python\quanser_api-2022.4.29-py2.py3-none-any.whl"
    
    .. code-tab:: console Linux

        cd /opt/quanser/python
        python3 -m pip install --upgrade --find-links /opt/quanser/python /opt/quanser/python/quanser_api-2022.4.29-py2.py3-none-any.whl

If you have trouble or for more information about this `click here <https://docs.quanser.com/quarc/documentation/python/hardware/Getting%20Started/getting_started.html#:~:text=Installing%20Quanser%20Hardware%20Python%20Package,29%2Dpy2>`__.

**At this point you should be ready to build and run a test script!**

..The following test script will test your capabilities in a simple script to get you up and running.

..Tutorial - Getting Started
..==========================

.. I think there should be a tutorial script to walk someone through a simple python file in here.
