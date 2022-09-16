from library_qlabs_common import QLabsCommon
from library_qlabs_actor import QLabsActor

import math
import struct

class QLabsCrosswalk(QLabsActor):
    """This class is for spawning crosswalks."""
       
    ID_CROSSWALK = 10010
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
       self._classID = self.ID_CROSSWALK
       return

   