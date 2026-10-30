from qvl.qlabs import QuanserInteractiveLabs, CommModularContainer
from quanser.common import GenericError
from qvl.actor import QLabsActor
import math

import struct


######################### MODULAR CONTAINER CLASS #########################

class QLabsSmartConveyor(QLabsActor):


    ID_SMART_CONVEYOR = 260

    FCN_SMART_CONVEYOR_SET_SPEED = 10
    FCN_SMART_CONVEYOR_SET_SPEED_ACK = 11
    FCN_SMART_CONVEYOR_SET_LED_MODE_AND_COLOR = 12
    FCN_SMART_CONVEYOR_SET_LED_MODE_AND_COLOR_ACK = 13
    FCN_SMART_CONVEYOR_SET_INDIVIDUAL_LED_COLORS = 14
    FCN_SMART_CONVEYOR_SET_INDIVIDUAL_LED_COLORS_ACK = 15

    LED_MODE_CUSTOM = 0
    LED_MODE_SOLID = 1
    LED_MODE_BIG_ANT = 2
    LED_MODE_LITTLE_ANT = 3
    LED_MODE_RAINBOW = 4
    


    # Initialize class
    def __init__(self, qlabs, verbose=False):
        """ Constructor Method

        :param qlabs: A QuanserInteractiveLabs object
        :param verbose: (Optional) Print error information to the console.
        :type qlabs: object
        :type verbose: boolean
        """

        self._qlabs = qlabs
        self._verbose = verbose
        self.classID = self.ID_SMART_CONVEYOR
        return

    def set_speed(self, speed):
        c = CommModularContainer()
        c.classID = self.ID_SMART_CONVEYOR
        c.actorNumber = self.actorNumber
        c.actorFunction = self.FCN_SMART_CONVEYOR_SET_SPEED
        c.payload = bytearray(struct.pack(">f", speed))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)

        self._qlabs.flush_receive()

        if (self._qlabs.send_container(c)):
            c = self._qlabs.wait_for_container(self.ID_SMART_CONVEYOR, self.actorNumber, self.FCN_SMART_CONVEYOR_SET_SPEED_ACK)

            return True
        else:
            return False

    def set_led_mode_and_color(self, mode, color):
        c = CommModularContainer()
        c.classID = self.ID_SMART_CONVEYOR
        c.actorNumber = self.actorNumber
        c.actorFunction = self.FCN_SMART_CONVEYOR_SET_LED_MODE_AND_COLOR
        c.payload = bytearray(struct.pack(">ifff", mode, color[0], color[1], color[2]))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)

        self._qlabs.flush_receive()

        if (self._qlabs.send_container(c)):
            c = self._qlabs.wait_for_container(self.ID_SMART_CONVEYOR, self.actorNumber, self.FCN_SMART_CONVEYOR_SET_LED_MODE_AND_COLOR_ACK)

            return True
        else:
            return False

    def set_individual_led_colors(self, colors):
        c = CommModularContainer()
        c.classID = self.ID_SMART_CONVEYOR
        c.actorNumber = self.actorNumber
        c.actorFunction = self.FCN_SMART_CONVEYOR_SET_INDIVIDUAL_LED_COLORS
        c.payload = bytearray(struct.pack(">300f", *[colors[row][col] for col in range(100) for row in range(3)]))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)

        self._qlabs.flush_receive()

        if (self._qlabs.send_container(c)):
            c = self._qlabs.wait_for_container(self.ID_SMART_CONVEYOR, self.actorNumber, self.FCN_SMART_CONVEYOR_SET_INDIVIDUAL_LED_COLORS_ACK)

            return True
        else:
            return False
