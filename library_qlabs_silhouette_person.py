from library_qlabs import QuanserInteractiveLabs, CommModularContainer
from quanser.common import GenericError
import math

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsSilhouettePerson:
    
       
    ID_SILHOUETTE_PERSON = 10030
    FCN_SILHOUETTE_PERSON_MOVE_TO = 10
    FCN_SILHOUETTE_PERSON_MOVE_TO_ACK = 11
    
    # Initialize class
    def __init__(self):

       return
       
    def spawn(self, qlabs, deviceNumber, location, rotation, scale, configuration=0, waitForConfirmation=True):
        # To put the spawn point at the feet, offset z by 1m
        return qlabs.spawn(deviceNumber, self.ID_SILHOUETTE_PERSON, location[0], location[1], location[2]+1.0, rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2], configuration, waitForConfirmation)

    def spawn_degrees(self, qlabs, deviceNumber, location, rotation, scale, configuration=0, waitForConfirmation=True):
    
        # To put the spawn point at the feet, offset z by 1m
        return qlabs.spawn(deviceNumber, self.ID_SILHOUETTE_PERSON, location[0], location[1], location[2]+1.0, rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi, scale[0], scale[1], scale[2], configuration, waitForConfirmation)
    

        
    def move_to(self, qlabs, deviceNumber, location, speed, waitForConfirmation=True):
        c = CommModularContainer()
        c.classID = self.ID_SILHOUETTE_PERSON
        c.deviceNumber = deviceNumber
        c.deviceFunction = self.FCN_SILHOUETTE_PERSON_MOVE_TO
        c.payload = bytearray(struct.pack(">ffff", location[0], location[1], location[2], speed))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if waitForConfirmation:
            qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            if waitForConfirmation:
                c = qlabs.wait_for_container(self.ID_SILHOUETTE_PERSON, deviceNumber, self.FCN_SILHOUETTE_PERSON_MOVE_TO_ACK)
                    
            return True
        else:
            return False    

