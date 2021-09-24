from library_qlabs import quanser_interactive_labs, comm_modular_container
from quanser.common import GenericError
import math

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class qlab_widget:

    CUBE = 0
    CYLINDER = 1
    SPHERE = 2
    AUTOCLAVE_CAGE = 3
        
    # Initilize class
    def __init__(self):

       return
       
    def spawn(self, qlabs, widget_type, location, rotation, scale, color, measured_mass=0, ID_tag=0, properties="", wait_for_confirmation=True):
        return qlabs.spawn_widget(widget_type, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2], color[0], color[1], color[2], measured_mass, ID_tag, properties, wait_for_confirmation)
 