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
    Download Quanser Interactive Labs

    .. note::
        All available content should be available to you on the main screen.
        If something is missing, try logging out and logging back in again.
    
    .. attention::
        Alternatively, the below installers are only needed for Python-only 
        Quanser Interactive Labs users, who do not intend to use Quanser 
        Interactive Labs with MATLAB® Simulink® and do not intend to use 
        Quanser virtual and physical systems on the same machine 
        (with QUARC). 

        Virtual-Only Python-Only Quanser Interactive Labs Download Links:
        | :download:`Windows Download <https://download.quanser.com/qlabs/latest/Install QLabs.exe>`
        | :download:`macOS Download <https://download.quanser.com/qlabs/latest/QLabs_Installer_mac64.zip>`

        On Linux computers, both the Quanser Interactive Labs for Linux and the Quanser SDK for Linux can be installed at the same time by running the commands shown on the Linux tab below.

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
    We have currently tested compatibility Python 3.11 or newer.  
    It is advised to not use an earlier version.

.. important::
    Ensure that you check the box that says 'Add Python to Path' when
    installing Python.

Python Package Update
^^^^^^^^^^^^^^^^^^^^^

For Quanser Interactive Labs to work with Python, certain base level Quanser
API libraries are required.

.. admonition:: Attention Windows, Linux & macOS Users

    On macOS computers, the required Quanser API libraries are included with 
    your Quanser Interactive Labs installation, and hence, you will need to have Quanser 
    Interactive Labs installed before running the commands shown on the macOS tab below.

    On Linux computers, the required Quanser API libraries are provided by installing  
    the Quanser SDK for Linux.
    For more information about the Quanser SDK for Linux, please visit its 
    `GitHub repository <https://github.com/quanser/quanser_sdk_linux>`__.     
    To install both the Quanser Interactive Labs for Linux and the Quanser SDK for Linux, run the commands shown on the Linux tab below.

    On Windows computers, the required Quanser API libraries are provided by installing  
    the Quanser SDK for Windows, if you have QUARC, it should have the necessary libraries too. 
    For more information about the Quanser SDK for Windows, please visit its 
    `GitHub repository <https://github.com/quanser/quanser_sdk_win64>`__.     
    To download the Quanser SDK for Windows installer, click on the following link  
    :download:`Download Quanser SDK for Windows <https://download.quanser.com/sdk/latest/install_quanser_sdk.exe>`. 
    After completing the installation, make sure the files in the "%QSDK_DIR%python" folder below have the same date (for example, 
    2024.3.8) as the date in the following code below before running it.  
    To check this, go to the "%QSDK_DIR%python" folder, which is typically under the "C:\\Program Files\\" directory.

.. tabs::
    .. code-tab:: console Windows

        # Type this into your Windows Command Prompt
        python -m pip install --upgrade pip
        python -m pip install --upgrade --find-links "%QSDK_DIR%python" "%QSDK_DIR%python\quanser_api-2024.3.8-py2.py3-none-any.whl"

    .. code-tab:: console Linux

        wget --no-cache https://repo.quanser.com/debian/release/config/configure_repo.sh
        chmod u+x configure_repo.sh
        ./configure_repo.sh
        rm -f ./configure_repo.sh
        sudo apt update
        sudo apt install qlabs-unreal quanser-sdk
    
    .. code-tab:: console macOS

        # Type this into your macOS Terminal
        python3 -m pip install --upgrade pip
        python3 -m pip install --upgrade --find-links /opt/quanser/python /opt/quanser/python/quanser_api-2024.3.8-py2.py3-none-any.whl

If you have trouble or for more information about our python APIs or 
installing individual python APIs check out the documentation here:
`click here <https://docs.quanser.com/quarc/documentation/python/getting_started.html>`__.

GitHub QLabs Libraries Download
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have purchased a product with us, the `Quanser Academic Resources`_ GitHub page 
includes instructions to download and set up your system to start using our resources. 
The Quanser Interactive Labs Libraries are downloaded and set up during the setup process. 
However, if you would like to only download the libraries by themselves you will 
need to follow the steps below.

.. _Quanser Academic Resources: https://github.com/quanser/Quanser_Academic_Resources/

Download our install.py script by entering the following command in your command prompt:

.. tabs::
    .. code-tab:: console
        
        # Navigate to your downloads or wherever you would like this file to be downloaded to, then run the below line 
        curl -L -o install.py https://raw.githubusercontent.com/quanser/Quanser_Interactive_Labs_Resources/main/install.py

Navigate to the **install.py** file and run this in the command window using the following code:

.. code-block:: console

    # cd to the directory where this install file is located
    python install.py

This install should work with Linux, macOS and Windows computers to install the qvl folders and files.

**At this point you should be ready to build and run a test script!**
