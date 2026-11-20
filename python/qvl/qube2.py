from qvl.actor import QLabsActor

class QLabsQube2(QLabsActor):
    """This class is for spawning Qube 2 actors."""

    ID_QUBE2 = 60
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
       self.classID = self.ID_QUBE2
       return

