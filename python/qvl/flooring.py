from qvl.qlabs import CommModularContainer
from qvl.actor import QLabsActor

import numpy as np
import math
import struct


######################### MODULAR CONTAINER CLASS #########################

class QLabsFlooring(QLabsActor):
    """ This class is for spawning static floors."""

    ID_FLOORING = 10090
    """Class ID"""

    FLOORING_QCAR_MAP_LARGE = 0
    FLOORING_QCAR_MAP_SMALL = 1

    FLOORING_QBOT_PLATFORM_0 = 2
    FLOORING_QBOT_PLATFORM_1 = 3
    FLOORING_QBOT_PLATFORM_2 = 4
    FLOORING_QBOT_PLATFORM_3 = 5
    FLOORING_QBOT_PLATFORM_4 = 6
    FLOORING_QBOT_PLATFORM_5 = 7


    def __init__(self, qlabs, verbose=False):
       """ Constructor Method

       :param qlabs: A QuanserInteractiveLabs object
       :param verbose: (Optional) Print error information to the console.
       :type qlabs: object
       :type verbose: boolean
       """

       self._qlabs = qlabs
       self._verbose = verbose
       self.classID = self.ID_FLOORING
       return