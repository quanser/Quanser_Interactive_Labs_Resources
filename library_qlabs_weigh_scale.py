from library_qlabs import CommModularContainer
import math
import struct      
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsWeighScale:

       
    ID_WEIGH_SCALE = 120
    
    FCN_WEIGH_SCALE_REQUEST_LOAD_MASS = 91
    FCN_WEIGH_SCALE_RESPONSE_LOAD_MASS = 92
    
    # Initialize class
    def __init__(self):

       return
       
    def spawn(self, qlabs, deviceNumber, location, rotation, waitForConfirmation=True):
        return qlabs.spawn(deviceNumber, self.ID_WEIGH_SCALE, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1, 1, 1, 0, waitForConfirmation)
 
    def spawn_degrees(self, qlabs, deviceNumber, location, rotation, waitForConfirmation=True):
    
        return qlabs.spawn(deviceNumber, self.ID_WEIGH_SCALE, location[0], location[1], location[2], rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi, 1, 1, 1, 0, waitForConfirmation)
        
    def spawn_and_parent_with_relative_transform(self, qlabs, deviceNumber, location, rotation, parentClass, parentDeviceNum, parentComponent, waitForConfirmation=True):
        return qlabs.spawn_and_parent_with_relative_transform(deviceNumber, self.ID_WEIGH_SCALE, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1, 1, 1, 0, parentClass, parentDeviceNum, parentComponent, waitForConfirmation)
           
    def get_measured_mass(self, qlabs, deviceNumber):
        c = CommModularContainer()
        c.classID = self.ID_WEIGH_SCALE
        c.deviceNumber = deviceNumber
        c.deviceFunction = self.FCN_WEIGH_SCALE_REQUEST_LOAD_MASS
        c.payload = bytearray()
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            c = qlabs.wait_for_container(self.ID_WEIGH_SCALE, deviceNumber, self.FCN_WEIGH_SCALE_RESPONSE_LOAD_MASS)
            
            if (len(c.payload) == 4):
                mass,  = struct.unpack(">f", c.payload)
                return mass
            else:
                return -1.0
        else:
            return -1.0
