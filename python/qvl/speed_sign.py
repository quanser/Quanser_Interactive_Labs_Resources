from qvl.qlabs import CommModularContainer
from qvl.actor import QLabsActor

import struct

class QLabsSpeedSign(QLabsActor):
    """This class is for spawning speed signs."""

    ID_SPEED_SIGN = 10240

    FCN_SPEED_SIGN_SET_SPEED = 10
    FCN_SPEED_SIGN_SET_SPEED_ACK = 11

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
       self.classID = self.ID_SPEED_SIGN
       return

    def set_speed(self, speed, waitForConfirmation=True):
        """Sets the speed on the sign post.

        :param speed: Speed value
        :param waitForConfirmation: (Optional) Wait for confirmation of the before proceeding. This makes the method a blocking operation.
        :type enable: int32
        :type waitForConfirmation: boolean
        :return: `True` if successful, `False` otherwise.
        :rtype: boolean
        """
        c = CommModularContainer()
        c.classID = self.ID_SPEED_SIGN
        c.actorNumber = self.actorNumber
        c.actorFunction = self.FCN_SPEED_SIGN_SET_SPEED
        c.payload = bytearray(struct.pack(">I", speed))

        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)

        if waitForConfirmation:
            self._qlabs.flush_receive()

        if (self._qlabs.send_container(c)):

            if waitForConfirmation:
                c = self._qlabs.wait_for_container(self.ID_SPEED_SIGN, self.actorNumber, self.FCN_SPEED_SIGN_SET_SPEED_ACK)
                if (c == None):
                    return False
                else:
                    return True

            return True
        else:
            return False