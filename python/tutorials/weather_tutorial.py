"""
Weather Example
---------------

.. note::

    Make sure you have Quanser Interactive Labs open before running this
    example.  This example is designed to run in the QCar Cityscape.

"""

from qvl.qlabs import QuanserInteractiveLabs
from qvl.free_camera import QLabsFreeCamera
from qvl.environment_outdoors import QLabsEnvironmentOutdoors
from qvl.system import QLabsSystem

import time
import os

def main():

    # Clears the screen in Windows
    os.system('cls')

    print("\n\n------------------------------ Communications --------------------------------\n")

    # Creates a server connection with Quanser Interactive Labs and manages
    # the communications
    qlabs = QuanserInteractiveLabs()

    # Ensure that QLabs is running on your local machine
    print("Connecting to QLabs...")
    try:
        qlabs.open("localhost")
    except:
        print("Unable to connect to QLabs")
        return

    print("Connected")

    hSystem = QLabsSystem(qlabs)


    ### Outdoor Environment
    print("\n\n---Outdoor Environment---")

    hEnvironmentOutdoors2 = QLabsEnvironmentOutdoors(qlabs)
    hEnvironmentOutdoors2.set_outdoor_lighting(0)

    # Create a camera at spawn location to allow us to see the weather changes
    hCameraWeather = QLabsFreeCamera(qlabs)
    x = hCameraWeather.spawn(location=[0.075, -8.696, 1.576], rotation=[0, -0.141, 1.908])
    hCameraWeather.possess()

    time.sleep(2.5)

    # Run through different weather possibilities in QLabs
    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.CLEAR_SKIES)
    hSystem.set_title_string('Clear skies')
    time.sleep(2.5)

    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.PARTLY_CLOUDY)
    hSystem.set_title_string('Partly cloudy')
    time.sleep(2.5)

    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.CLOUDY)
    hSystem.set_title_string('Cloudy')
    time.sleep(2.5)

    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.OVERCAST)
    hEnvironmentOutdoors2.set_outdoor_lighting(1)
    hSystem.set_title_string('Overcast')
    time.sleep(2.5)

    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.FOGGY)
    hSystem.set_title_string('Foggy')
    time.sleep(2.5)

    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.LIGHT_RAIN)
    hEnvironmentOutdoors2.set_outdoor_lighting(0)
    hSystem.set_title_string('Light rain')
    time.sleep(2.5)

    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.RAIN)
    hEnvironmentOutdoors2.set_outdoor_lighting(1)
    hSystem.set_title_string('Rain')
    time.sleep(2.5)

    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.THUNDERSTORM)
    hSystem.set_title_string('Thunderstorm')
    time.sleep(2.5)

    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.LIGHT_SNOW)
    hEnvironmentOutdoors2.set_outdoor_lighting(0)
    hSystem.set_title_string('Light snow')
    time.sleep(2.5)

    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.SNOW)
    hEnvironmentOutdoors2.set_outdoor_lighting(1)
    hSystem.set_title_string('Snow')
    time.sleep(2.5)

    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.BLIZZARD)
    hSystem.set_title_string('Blizzard')
    time.sleep(2.5)

    hEnvironmentOutdoors2.set_weather_preset(hEnvironmentOutdoors2.PARTLY_CLOUDY)
    hEnvironmentOutdoors2.set_outdoor_lighting(0)
    hSystem.set_title_string('QLABS WEATHER')


    print("\n\n------------------------------ Communications --------------------------------\n")

    qlabs.close()
    print("Done!")

main()