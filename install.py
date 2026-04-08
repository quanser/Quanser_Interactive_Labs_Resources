import sys
import os
import platform
import tempfile
import shutil
import argparse
import subprocess
import site
from pathlib import Path
from importlib import reload

os.chdir(os.path.dirname(__file__))

#region: Check python version
pythonVersion = platform.python_version_tuple()
if (int(pythonVersion[0]) != 3) or (int(pythonVersion[1]) < 10):
    print('Error: Install requires python version 3.10 or newer.')
    print("We recommend one of the python versions here https://github.com/quanser/Quanser_Academic_Resources/blob/dev-windows/docs/pc_setup.md#if-you-are-using-python")
    print('Install unsuccessful.')
    sys.exit(1)
#endregion

#region: Check if QUARC or Quanser SDK is installed
try:
    import quanser  

except ImportError:
    # if quarc or quanser sdk is installed, install quanser python sdk just in case it wasn't installed before
    # for QUARC users, the files exist but are not installed by default
    # Define paths

    qsdk_dir = os.environ.get("QSDK_DIR")
    if not qsdk_dir:
        print('Error: Before running this installer, you must first install QUARC or the Quanser SDK.')
        sys.exit(1)
    
    qsdk_python_dir = Path(qsdk_dir) / "python"

    # Search for file starting with "quanser_api"
    quanser_files = list(qsdk_python_dir.glob("quanser_api*"))
    if not quanser_files:
        print("No quanser_api file found")
        sys.exit(1)

    filename = quanser_files[0]

    # Delete pip cache
    subprocess.run([sys.executable, "-m", "pip", "cache", "purge"], check=True)

    try:
        # Install Quanser Python API
        print(f"Installing Quanser Python API {filename.name}")
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--upgrade", 
            "--find-links", str(qsdk_python_dir), str(filename)],
            check=True
        )
    except:
        print("Error: Failed to install Quanser Python API.")
        print("Install unsuccessful.")
        sys.exit(1)

    print("Quanser's Python API installed successfully.")
    print('')
#endregion


# Default install location is Quanser folder in home directory
if (os.name == 'nt'):
    install_dir = os.environ['USERPROFILE'] + '/Documents/Quanser/'
elif (os.name == 'posix'):
    install_dir = os.environ['HOME'] + '/Quanser/'
else:
    print('Error: Unsupported OS')
    print('Install unsuccessful.')
    quit()

install_dir = os.path.normpath(install_dir)

if 'QAL_DIR' in os.environ:
    if install_dir != os.environ['QAL_DIR']:
        print('Error: QVL already installed in a different location.')
        print('Current location: ' + os.environ['QAL_DIR'])
        print('Attempted new location: ' + install_dir)
        print('Install unsuccessful.')
        quit()

    print('')
    confirmation = input(
        'Warning: QVL is already installed at "' + os.environ['QAL_DIR'] + '". '
        + 'Continuing with this installer will overwrite files from the '
        + 'current installation. Are you sure you want to continue? (y,[n])'
        )
    if 'y' not in confirmation.lower():
        print('Installation cancelled.')
        quit()

# Create install directory if it doesn't already exist
if not os.path.isdir(install_dir):
    try:
        os.mkdir(install_dir)
    except:
        print('Error: Invalid install location.')
        print('Install unsuccessful.')
        sys.exit(1)
        quit()
#endregion

# for future releases, we need to check for windows vs linux for pip vs aptget downloads.

#region: Install Dependencies
print('Installing required python packages...')

packages = [
    'numpy<2.4',
    'opencv-python',
    'pygit2',
]

try:
    subprocess.check_call([sys.executable,'-m','pip','install'] + packages)
    reload(site)
    import pygit2 # < must be placed here since it gets installed earlier in script
except:
    print('Error: Failed to install required python packages '
        + '(Note: this requires a valid internet connection).'
    )
    confirmation = input(
        'Would you like to skip installing dependencies for now '
        + 'and finish with the rest of the installation? (y,[n])'
    )
    if 'y' not in confirmation.lower():
        print('Installation cancelled.')
        sys.exit(1)
#endregion

#region: Install files from GitHub
print('Installing Quanser virtual libraries...')
try:
    tmpdir = tempfile.TemporaryDirectory()

    pygit2.clone_repository(
        'https://github.com/quanser/Quanser_Interactive_Labs_Resources.git',
        tmpdir.name
    )
    shutil.copytree(
        tmpdir.name + '/python/qvl/',
        os.path.join(install_dir,'0_libraries/python/qvl'),
        dirs_exist_ok=True,
        ignore=shutil.ignore_patterns('.*')
    )
    if (os.name == 'nt'):
        shutil.copytree(
            tmpdir.name + '/matlab/qvl/',
            os.path.join(install_dir,'0_libraries/matlab/qvl'),
            dirs_exist_ok=True,
            ignore=shutil.ignore_patterns('.*')
        )
    try:
        tmpdir.cleanup()
    except:
        pass
except:
    print('Error: Failed to install files from GitHub '
        + '(Note: this requires a valid internet connection).'
    )
    confirmation = input(
        'Would you like to skip this part for now '
        + 'and finish with the rest of the installation? (y,[n])'
    )
    if 'y' not in confirmation.lower():
        print('Installation cancelled.')
        sys.exit(1)
#endregion

#region: Setup Environment Variables
environmentVariablesSet = False

pythonPath = os.path.normpath(install_dir + '/0_libraries/python/')

if os.name == 'nt':
    if 'PYTHONPATH' not in os.environ:
        os.system('setx PYTHONPATH "' + pythonPath + '"')
        environmentVariablesSet = True

    elif pythonPath not in os.environ['PYTHONPATH']:
        pythonPath = os.environ['PYTHONPATH'] + ';' + pythonPath
        os.system('setx PYTHONPATH "' + pythonPath + '"')
        environmentVariablesSet = True

    if 'QAL_DIR' not in os.environ:
        os.system('setx QAL_DIR "' + install_dir + '"')
        environmentVariablesSet = True
elif os.name == 'posix':
    shell = os.environ.get('SHELL')
    if shell and 'bash' in shell:
        shellConfigFile = '.bashrc'
    elif shell and 'zsh' in shell:
        shellConfigFile = '.zshrc'
    else:
        print('Error: Unsupported shell interface. '
            +'Only bash and zsh supported.'
        )
        sys.exit(1)
        quit()
    configFilePath = os.path.join(os.environ['HOME'], shellConfigFile)

    alreadySetup = False
    if os.path.exists(configFilePath):
        with open(configFilePath, 'r') as config_file:
            for line in config_file.readlines():
                if 'QAL_DIR' in line.strip():
                    alreadySetup = True
                    break

    if not alreadySetup:
        msg = (
            '\n# Environment variables for Quanser Application Libraries'
            + '\nexport QAL_DIR="' + install_dir + '"'
            + '\nexport PYTHONPATH="${PYTHONPATH}:'+ pythonPath + '"'
        )
        with open(configFilePath, 'a') as config_file:
            config_file.write(msg)
        environmentVariablesSet = True
else:
    print('Error: unrecognized OS.')
    sys.exit(1)
    quit()
#endregion


print('')
print('Install Successful!')
print('Location: ' + install_dir)
print('')
if environmentVariablesSet:
    if (os.name == 'nt'):
        print('Windows must be reset in order '
            + 'to finish setup of environment variables.'
        )
    elif (os.name == 'posix'):
        print('Close this terminal and open a new one '
            + 'to finish setup of environment variables.'
        )
print('')