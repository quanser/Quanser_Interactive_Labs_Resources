from library_qlabs import QuanserInteractiveLabs, CommModularContainer
from quanser.common import GenericError
import math

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsSplineLine:

       
    ID_SPLINE_LINE = 180
    
    FCN_SPLINE_LINE_SET_POINTS = 10
    FCN_SPLINE_LINE_SET_POINTS_ACK = 11
    
        
    # Initialize class
    def __init__(self):

       return
       
    def spawn(self, qlabs, actorNumber, location, rotation, scale, configuration=0, waitForConfirmation=True):
        return qlabs.spawn(actorNumber, self.ID_SPLINE_LINE, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2], configuration, waitForConfirmation)
   
    def spawn_degrees(self, qlabs, actorNumber, location, rotation, scale, configuration=0, waitForConfirmation=True):
    
        return qlabs.spawn(actorNumber, self.ID_SPLINE_LINE, location[0], location[1], location[2], rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi, scale[0], scale[1], scale[2], configuration, waitForConfirmation)
   
    def set_points(self, qlabs, actorNumber, colour, alignEndPointTangents, pointList, waitForConfirmation=True):
        c = CommModularContainer()
        c.classID = self.ID_SPLINE_LINE
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_SPLINE_LINE_SET_POINTS
        c.payload = bytearray(struct.pack(">fffB", colour[0], colour[1], colour[2], alignEndPointTangents))
        
        for point in pointList:
            c.payload = c.payload + bytearray(struct.pack(">ffff", point[0], point[1], point[2], point[3]))
        
                
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if waitForConfirmation:
            qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            if waitForConfirmation:
                c = qlabs.wait_for_container(self.ID_SPLINE_LINE, actorNumber, self.FCN_SPLINE_LINE_SET_POINTS_ACK)
                return c
                    
            return True
        else:
            return False    