from library_qlabs import QuanserInteractiveLabs, CommModularContainer
from quanser.common import GenericError
import math

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsConveyorStraight:

       
    ID_CONVEYOR_STRAIGHT = 210
    
    FCN_CONVEYOR_STRAIGHT_SET_SPEED = 10
    FCN_CONVEYOR_STRAIGHT_SET_SPEED_ACK = 11
    
    
    # Initialize class
    def __init__(self):

       return
       
       
    def spawn(self, qlabs, actorNumber, location, rotation, sections=0, waitForConfirmation=True):
        return qlabs.spawn(actorNumber, self.ID_CONVEYOR_STRAIGHT, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1, 1, 1, sections, waitForConfirmation)
 
    def spawn_degrees(self, qlabs, actorNumber, location, rotation, sections=0, waitForConfirmation=True):
        return qlabs.spawn(actorNumber, self.ID_CONVEYOR_STRAIGHT, location[0], location[1], location[2], rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi, 1, 1, 1, sections, waitForConfirmation)
 
    def set_speed(self, qlabs, actorNumber, speed):
        c = CommModularContainer()
        c.classID = self.ID_CONVEYOR_STRAIGHT
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_CONVEYOR_STRAIGHT_SET_SPEED
        c.payload = bytearray(struct.pack(">f", speed))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            c = qlabs.wait_for_container(self.ID_CONVEYOR_STRAIGHT, actorNumber, self.FCN_CONVEYOR_STRAIGHT_SET_SPEED_ACK)
                    
            return True
        else:
            return False    