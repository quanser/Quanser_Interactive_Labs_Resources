import math      
       
######################### MODULAR CONTAINER CLASS #########################

class QLabsWidget:

    CUBE = 0
    CYLINDER = 1
    SPHERE = 2
    AUTOCLAVE_CAGE = 3
    PLASTIC_BOTTLE = 4
    METAL_CAN = 5
        
    # Initialize class
    def __init__(self):

       return
       
    def spawn(self, qlabs, widgetType, location, rotation, scale, color, measuredMass=0, IDTag=0, properties="", waitForConfirmation=True):
        return qlabs.spawn_widget(widgetType, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2], color[0], color[1], color[2], measuredMass, IDTag, properties, waitForConfirmation)
 
    def spawn_degrees(self, qlabs, widgetType, location, rotation, scale, color, measuredMass=0, IDTag=0, properties="", waitForConfirmation=True):
        return qlabs.spawn_widget(widgetType, location[0], location[1], location[2], rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi, scale[0], scale[1], scale[2], color[0], color[1], color[2], measuredMass, IDTag, properties, waitForConfirmation)
 