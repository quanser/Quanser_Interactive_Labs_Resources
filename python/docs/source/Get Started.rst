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

.. admonition:: Attention Windows & MacOS Users

    On Windows and MACOS computers, the required Quanser API libraries are included with 
    your Quanser Interactive Labs installation, and hence, you will need to have Quanser 
    Interactive Labs installed before running the following command.

    Make sure the files in the QUARC python folder below have the same date (for example 
    2022.4.29) as the date in the following code below before running it.  
    To find this go to program files and find the Quanser/QUARC/python directory.

.. tabs::
    .. code-tab:: console Windows

        # Type this into your Windows Command Prompt
        python -m pip install --upgrade --find-links "%QUARC_DIR%\python"
        "%QUARC_DIR%\python\quanser_api-2022.4.29-py2.py3-none-any.whl"

    .. code-tab:: console Linux

        # Type this into your Linux Terminal
        wget --no-cache https://repo.quanser.com/debian/release/config/configure_repo.sh
        chmod u+x configure_repo.sh
        ./configure_repo.sh
        rm -f ./configure_repo.sh
        sudo apt update
        sudo apt-get install python3-quanser-apis
    
    .. code-tab:: console MacOS

        # Type this into your Linux Terminal
        sudo apt update
        sudo apt-get install python3-quanser-apis

If you have trouble or for more information about our python APIs or 
installing individual python APIs check out the documentation here:
`click here <https://docs.quanser.com/quarc/documentation/python/getting_started.html>`__.

GitHub QLabs Libraries Download
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have purchased a hardware product with us, the Research Resources.zip file should 
automatically include Quanser Interactive Labs Libraries in its setup file and you can skip this step.  
However, if you would like to only download the libraries by themselves you will 
need to follow the steps below.

Download our install.py script by entering the following in your command prompt:
.. tabs::
    .. code-tab:: console Windows
        
        # Navigate to your downloads or where ever you would like this file to be downloaded to then run the below line 
        curl -L -o install.py https://raw.githubusercontent.com/quanser/Quanser_Interactive_Labs_Resources/main/install.py

Navigate to the **install.py** file and run this in the command window using the following code:

.. code-block:: console

    # cd to the directory where this install file is located
    python install.py

This install should work with Linux, MacOS and Windows computers to install the qvl folders and files.

**At this point you should be ready to build and run a test script!**

.. The following test script will test your capabilities in a simple script to
.. get you up and running.

.. Tutorial - Getting Started

.. ==========================

.. I think there should be a tutorial script to walk someone through a simple
.. python file in here.
