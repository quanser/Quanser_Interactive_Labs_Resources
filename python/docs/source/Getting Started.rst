.. _Getting Started:

***************
Getting Started
***************

Installation / Set Up
=====================

#. 
    Create an account on `Portal <https://portal.quanser.com/Accounts/Login?returnUrl=/>`__ with your school email.

    .. tip:: Check the box "Remember Me" for QLabs to remember your account

#. 
    Download Quanser Interactive Lab on the `Portal <https://portal.quanser.com/Accounts/Login?returnUrl=/>`__

    .. note:: All available content should be available to you on the main screen. If something is missing, try logging out and logging back in again.

#. 
    Scroll using a mouse wheel or the arrow keys on either side of the screen to the QCar studio. 
    Alternatively you can also right-click and drag left/right to scroll through available modules.

#. 
    Click on the QCar studio and select the workspace of choice.

Running a Python Script for QLabs SDCS
======================================

In order to run a python script in QLabs to control the environment and its objects, a few things will be required.

.. Note that this will need to change when we agree what info will be where for customers.

Prerequisites
-------------

GitHub QLabs Libraries Download
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Download the common library off Github which will be needed in order to run the objects in your python script for QLabs `Virtual QCar Libraries <https://github.com/quanser/virtual_qcar_libraries>`__.

Download Python
^^^^^^^^^^^^^^^

If you don't already have python installed on your computer, you can download it from `here <https://Python.org/downloads/>`__.

We have currently tested compatibility with Python 3.

.. important:: Ensure that you check the box that says 'Add Python to Path' when installing python.

Download OpenCV-Python
^^^^^^^^^^^^^^^^^^^^^^

In the command terminal running as an admin (or in Linux running "sudo"), paste and run this code to install opencv on the computer.

.. code-block:: python

    pip install opencv-python

Python Package Update
^^^^^^^^^^^^^^^^^^^^^

For Quanser Interactive Labs to work with Python, certain base level Quanser API libraries are 
required.

.. admonition:: Attention Windows Users
    
    On Windows, the required Quanser API libraries are included with your QUARC installation, and 
    hence, you will need to have QUARC installed before running the following command. Make sure 
    the files in the QUARC python folder below have the same date as the date in the following code
    below before running it.

.. admonition:: Attention Linux Users
    
    On Linux, the required Quanser API libraries will be installed by the following command.


.. tabs::
    .. code-tab:: console Windows

        # Type this into your Windows Command Prompt
        python -m pip install --upgrade --find-links "%QUARC_DIR%\python" "%QUARC_DIR%\python\quanser_api-2022.4.29-py2.py3-none-any.whl"
    
    .. code-tab:: console Linux

        # Type this into your Linux Terminal
        sudo apt update
        sudo apt-get install python3-quanser-apis

If you have trouble or for more information about this `click here <https://docs.quanser.com/quarc/documentation/python/hardware/Getting%20Started/getting_started.html#:~:text=Installing%20Quanser%20Hardware%20Python%20Package,29%2Dpy2>`__.

**At this point you should be ready to build and run a test script!**

.. The following test script will test your capabilities in a simple script to get you up and running.

.. Tutorial - Getting Started

.. ==========================

.. I think there should be a tutorial script to walk someone through a simple python file in here.
