from library_qlabs import CommModularContainer
from quanser.common import GenericError
import math
import os
import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsEnvironmentOutdoors:
    """ This class modifies QLabs open worlds with outdoor environments."""

    ID_ENVIRONMENT_OUTDOORS = 1100 
    """Class ID"""

    FCN_SET_TIME_OF_DAY = 10
    """ """
    FCN_SET_TIME_OF_DAY_ACK = 11
    """ """
   
    def __init__(self):
       """ Constructor Method """
       return

    def set_time_of_day(self, qlabs, time):
        """
        Set the time of day for an outdoor environment
        
        :param qlabs: A QuanserInteractiveLabs object
        :param time: A value from 0 to 24
        :type qlabs: object
        :type float: float
        :return: `True` if setting the time was successful, `False` otherwise
        :rtype: boolean

        """
        c = CommModularContainer()
        c.classID = self.ID_ENVIRONMENT_OUTDOORS
        c.actorNumber = 0
        c.actorFunction = self.FCN_SET_TIME_OF_DAY
        c.payload = bytearray(struct.pack(">f", time))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            c = qlabs.wait_for_container(self.ID_ENVIRONMENT_OUTDOORS, 0, self.FCN_SET_TIME_OF_DAY_ACK)
                    
            return True
        else:
            return False  