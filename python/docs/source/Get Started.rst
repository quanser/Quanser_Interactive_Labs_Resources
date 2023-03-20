.. _Get Started:

***********
Get Started
***********

Installation / Set Up
=====================

#.
    Create an account on
    `Portal <https://portal.quanser.com/Accounts/Login?returnUrl=/>`__ with
    the email from your institution.

    .. tip:: Check the box "Remember Me" for QLabs to remember your account

#.
    Download Quanser Interactive Labs on
    `Portal <https://portal.quanser.com/Accounts/Login?returnUrl=/>`__

    .. note::
        All available content should be available to you on the main screen.
        If something is missing, try logging out and logging back in again.
#.  
    Open Quanser Interactive Labs and log in.
#.
    Scroll using a mouse wheel or the arrow keys on either side of the screen
    to the product of choice.
    Alternatively you can also right-click and drag left/right to scroll
    through available modules.

#.
    Click on the product of choice and select the workspace of choice. Note
    that not all products have an open world workspace.

Running a Python Script for QLabs Open Worlds
=============================================

In order to run a python script in QLabs to control the environment and its
objects, a few things will be required.

Prerequisites
-------------

Download Python
^^^^^^^^^^^^^^^

If you don't already have python installed on your computer, you can download
it from `here <https://Python.org/downloads/>`__.

.. important::
    We have currently tested compatibility Python 3.8 or newer.  
    It is advised to not use an earlier version.

.. important::
    Ensure that you check the box that says 'Add Python to Path' when
    installing Python.

Python Package Update
^^^^^^^^^^^^^^^^^^^^^

For Quanser Interactive Labs to work with Python, certain base level Quanser
API libraries are required.

.. admonition:: Attention Windows Users

    On Windows, the required Quanser API libraries are included with your QUARC
    installation, and hence, you will need to have QUARC installed before
    running the following command.
    Make sure the files in the QUARC python folder below have the same date as
    the date in the following code below before running it.

.. tabs::
    .. code-tab:: console Windows

        # Type this into your Windows Command Prompt
        python -m pip install --upgrade --find-links "%QUARC_DIR%\python"
        "%QUARC_DIR%\python\quanser_api-2022.4.29-py2.py3-none-any.whl"

    .. code-tab:: console Linux

        # Type this into your Linux Terminal
        sudo apt update
        sudo apt-get install python3-quanser-apis

If you have trouble or for more information about this
`click here <https://docs.quanser.com/quarc/documentation/python/hardware/Getting%20Started/getting_started.html#:~:text=Installing%20Quanser%20Hardware%20Python%20Package,29%2Dpy2>`__.

GitHub QLabs Libraries Download
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have purchased a hardware product with us, the Research Resources.zip file should 
automatically include Quanser Interactive Labs Libraries in its setup file and you can skip this step.  
However, if you would like to only download the libraries by themselves you will 
need to follow the steps below.

Download our install.py script `here <https://raw.githubusercontent.com/quanser/Quanser_Interactive_Labs_Private/main/install.py>__`.
Open the folder and run the **install.py** file to download all the requirements and the qvl library.
You can run this in the command window using the following code:

.. code-block:: console

    # cd to the directory where this install file is located
    python install.py

This install should work with both Linux and Windows computers.

**At this point you should be ready to build and run a test script!**

.. The following test script will test your capabilities in a simple script to
.. get you up and running.

.. Tutorial - Getting Started

.. ==========================

.. I think there should be a tutorial script to walk someone through a simple
.. python file in here.
