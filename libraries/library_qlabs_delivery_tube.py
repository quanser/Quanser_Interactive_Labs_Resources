from library_qlabs import QuanserInteractiveLabs, CommModularContainer
from quanser.common import GenericError
import math

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsDeliveryTube:

       
    ID_DELIVERY_TUBE = 80
    
    FCN_DELIVERY_TUBE_SPAWN_BLOCK = 10
    FCN_DELIVERY_TUBE_SPAWN_BLOCK_ACK = 11
    FCN_DELIVERY_TUBE_SET_HEIGHT = 12
    FCN_DELIVERY_TUBE_SET_HEIGHT_ACK = 13
    
    BLOCK_CUBE = 0
    BLOCK_CYLINDER = 1
    BLOCK_SPHERE = 2
    BLOCK_GEOSPHERE = 3
    
    CONFIG_HOVER = 0
    CONFIG_NO_HOVER = 1
    
    # Initialize class
    def __init__(self):

       return
       
    def spawn(self, qlabs, actorNumber, location, rotation, configuration=0, waitForConfirmation=True):
        return qlabs.spawn(actorNumber, self.ID_DELIVERY_TUBE, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1, 1, 1, configuration, waitForConfirmation)
 
    def spawn_degrees(self, qlabs, actorNumber, location, rotation, configuration=0, waitForConfirmation=True):
    
        return qlabs.spawn(actorNumber, self.ID_DELIVERY_TUBE, location[0], location[1], location[2], rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi, 1, 1, 1, configuration, waitForConfirmation)
  
    def spawn_block(self, qlabs, actorNumber, blockType, mass, yawRotation, color):
        c = CommModularContainer()
        c.classID = self.ID_DELIVERY_TUBE
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_DELIVERY_TUBE_SPAWN_BLOCK
        c.payload = bytearray(struct.pack(">Ifffff", blockType, mass, yawRotation, color[0], color[1], color[2]))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            c = qlabs.wait_for_container(self.ID_DELIVERY_TUBE, actorNumber, self.FCN_DELIVERY_TUBE_SPAWN_BLOCK_ACK)
                    
            return True
        else:
            return False 
            
    def set_height(self, qlabs, actorNumber, height):
        c = CommModularContainer()
        c.classID = self.ID_DELIVERY_TUBE
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_DELIVERY_TUBE_SET_HEIGHT
        c.payload = bytearray(struct.pack(">f", height))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            c = qlabs.wait_for_container(self.ID_DELIVERY_TUBE, actorNumber, self.FCN_DELIVERY_TUBE_SET_HEIGHT_ACK)
                    
            return True
        else:
            return False             
            
            
class QLabsDeliveryTubeBottles:

       
    ID_DELIVERY_TUBE_BOTTLES = 81
    
    FCN_DELIVERY_TUBE_SPAWN_CONTAINER = 10
    FCN_DELIVERY_TUBE_SPAWN_CONTAINER_ACK = 11
    FCN_DELIVERY_TUBE_SET_HEIGHT = 12
    FCN_DELIVERY_TUBE_SET_HEIGHT_ACK = 13
    
    PLASTIC_BOTTLE = 4
    METAL_CAN = 5
    
    CONFIG_HOVER = 0
    CONFIG_NO_HOVER = 1
    
    # Initialize class
    def __init__(self):

       return
       
    def spawn(self, qlabs, actorNumber, location, rotation, configuration=0, waitForConfirmation=True):
        return qlabs.spawn(actorNumber, self.ID_DELIVERY_TUBE_BOTTLES, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1, 1, 1, configuration, waitForConfirmation)
 
    def spawn_degrees(self, qlabs, actorNumber, location, rotation, configuration=0, waitForConfirmation=True):
    
        return qlabs.spawn(actorNumber, self.ID_DELIVERY_TUBE_BOTTLES, location[0], location[1], location[2], rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi, 1, 1, 1, configuration, waitForConfirmation)
  
    
    
    def spawn_container(self, qlabs, actorNumber, metallic, color, mass, propertyString="", height = 0.1, diameter = 0.65, roughness = 0.65):
        c = CommModularContainer()
        c.classID = self.ID_DELIVERY_TUBE_BOTTLES
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_DELIVERY_TUBE_SPAWN_CONTAINER
        c.payload = bytearray(struct.pack(">ffBffffffI", height, diameter, metallic, color[0], color[1], color[2], 1.0, roughness, mass, len(propertyString)))
        c.payload = c.payload + bytearray(propertyString.encode('utf-8'))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            c = qlabs.wait_for_container(self.ID_DELIVERY_TUBE_BOTTLES, actorNumber, self.FCN_DELIVERY_TUBE_SPAWN_CONTAINER_ACK)
                    
            return True
        else:
            return False 
            
                      
            
    def set_height(self, qlabs, actorNumber, height):
        c = CommModularContainer()
        c.classID = self.ID_DELIVERY_TUBE_BOTTLES
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_DELIVERY_TUBE_SET_HEIGHT
        c.payload = bytearray(struct.pack(">f", height))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            c = qlabs.wait_for_container(self.ID_DELIVERY_TUBE_BOTTLES, actorNumber, self.FCN_DELIVERY_TUBE_SET_HEIGHT_ACK)
                    
            return True
        else:
            return False     

    