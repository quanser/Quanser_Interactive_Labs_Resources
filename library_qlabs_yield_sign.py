import math     
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsYieldSign:

       
    ID_YIELD_SIGN = 10070
    
    # Initialize class
    def __init__(self):

       return
       
    def spawn(self, qlabs, actorNumber, location, rotation, scale, waitForConfirmation=True):
        return qlabs.spawn(actorNumber, self.ID_YIELD_SIGN, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2], 0, waitForConfirmation)
 
    def spawn_degrees(self, qlabs, actorNumber, location, rotation, scale, waitForConfirmation=True):
    
        return qlabs.spawn(actorNumber, self.ID_YIELD_SIGN, location[0], location[1], location[2], rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi, scale[0], scale[1], scale[2], 0, waitForConfirmation)
 


