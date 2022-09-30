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
    FCN_SET_TIME_OF_DAY_ACK = 11

    _qlabs = None
    _verbose = False
   
    def __init__(self, qlabs, verbose=False):
       """ Constructor method

       :param qlabs: A QuanserInteractiveLabs object
       :param verbose: (Optional) Print error information to the console.
       :type qlabs: object
       :type verbose: boolean
       """

       self._qlabs = qlabs
       self._verbose = verbose
       return
       

    def set_time_of_day(self, time):
        """
        Set the time of day for an outdoor environment.
        
        :param time: A value from 0 to 24. Midnight is a value 0 or 24. Noon is a value of 12.
        :type time: float
        :return: `True` if setting the time was successful, `False` otherwise
        :rtype: boolean

        """
        c = CommModularContainer()
        c.classID = self.ID_ENVIRONMENT_OUTDOORS
        c.actorNumber = 0
        c.actorFunction = self.FCN_SET_TIME_OF_DAY
        c.payload = bytearray(struct.pack(">f", time))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        self._qlabs.flush_receive()  
        
        if (self._qlabs.send_container(c)):
            c = self._qlabs.wait_for_container(self.ID_ENVIRONMENT_OUTDOORS, 0, self.FCN_SET_TIME_OF_DAY_ACK)
            if (c == None):
                return False
            else:                
                return True
        else:
            return False  