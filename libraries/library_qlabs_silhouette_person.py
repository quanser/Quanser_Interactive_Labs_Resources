from library_qlabs import QuanserInteractiveLabs, CommModularContainer
from quanser.common import GenericError
import math

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsSilhouettePerson:
    
       
    ID_SILHOUETTE_PERSON = 10030
    """Class ID"""
    FCN_SILHOUETTE_PERSON_MOVE_TO = 10
    """ """
    FCN_SILHOUETTE_PERSON_MOVE_TO_ACK = 11
    """ """

    def __init__(self):
        """ Constructor Method """
        return
       
    def spawn(self, qlabs, actorNumber, location, rotation, scale, configuration=0, waitForConfirmation=True):
        # To put the spawn point at the feet, offset z by 1m
        return qlabs.spawn(actorNumber, self.ID_SILHOUETTE_PERSON, location[0], location[1], location[2]+1.0, rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2], configuration, waitForConfirmation)

    def spawn_degrees(self, qlabs, actorNumber, location, rotation, scale, configuration=0, waitForConfirmation=True):
    
        # To put the spawn point at the feet, offset z by 1m
        return qlabs.spawn(actorNumber, self.ID_SILHOUETTE_PERSON, location[0], location[1], location[2]+1.0, rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi, scale[0], scale[1], scale[2], configuration, waitForConfirmation)
    

        
    def move_to(self, qlabs, actorNumber, location, speed, waitForConfirmation=True):
        c = CommModularContainer()
        c.classID = self.ID_SILHOUETTE_PERSON
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_SILHOUETTE_PERSON_MOVE_TO
        c.payload = bytearray(struct.pack(">ffff", location[0], location[1], location[2], speed))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if waitForConfirmation:
            qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            if waitForConfirmation:
                c = qlabs.wait_for_container(self.ID_SILHOUETTE_PERSON, actorNumber, self.FCN_SILHOUETTE_PERSON_MOVE_TO_ACK)
                    
            return True
        else:
            return False    

