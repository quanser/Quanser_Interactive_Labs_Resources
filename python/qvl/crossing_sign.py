from qvl.actor import QLabsActor
import math
import struct

class QLabsCrossingSign(QLabsActor):
    """This class is for spawning crossing signs."""

    ID_CROSSING_SIGN = 10210
    """Class ID"""

    def __init__(self, qlabs, verbose=False):
       """ Constructor Method

       :param qlabs: A QuanserInteractiveLabs object
       :param verbose: (Optional) Print error information to the console.
       :type qlabs: object
       :type verbose: boolean
       """

       self._qlabs = qlabs
       self._verbose = verbose
       self.classID = self.ID_CROSSING_SIGN
       return

