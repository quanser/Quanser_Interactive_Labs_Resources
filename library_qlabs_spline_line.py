from library_qlabs import quanser_interactive_labs, comm_modular_container
from quanser.common import GenericError
import math

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class qlab_spline_line:

    # Define class-level variables   
    container_size = 0
    class_id = 0       # What device type is this?
    device_number = 0   # Increment if there are more than one of the same device ID
    device_function = 0 # Command/reponse
    payload = bytearray()
    
       
    ID_SPLINE_LINE = 180
    
    FCN_SPLINE_LINE_SET_POINTS = 10
    FCN_SPLINE_LINE_SET_POINTS_ACK = 11
    
        
    # Initilize class
    def __init__(self):

       return
       
    def spawn(self, qlabs, device_num, location, rotation, scale, configuration=0, wait_for_confirmation=True):
        return qlabs.spawn(device_num, self.ID_SPLINE_LINE, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2], configuration, wait_for_confirmation)
   
    def spawn_degrees(self, qlabs, device_num, location, rotation, scale, configuration=0, wait_for_confirmation=True):
        rotation[0] = rotation[0]/180*math.pi
        rotation[1] = rotation[1]/180*math.pi
        rotation[2] = rotation[2]/180*math.pi
    
        return qlabs.spawn(device_num, self.ID_SPLINE_LINE, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2], configuration, wait_for_confirmation)
   
    def set_points(self, qlabs, device_num, color, align_end_point_tangents, point_list, wait_for_confirmation=True):
        c = comm_modular_container()
        c.class_id = self.ID_SPLINE_LINE
        c.device_number = device_num
        c.device_function = self.FCN_SPLINE_LINE_SET_POINTS
        c.payload = bytearray(struct.pack(">fffB", color[0], color[1], color[2], align_end_point_tangents))
        
        for point in point_list:
            c.payload = c.payload + bytearray(struct.pack(">ffff", point[0], point[1], point[2], point[3]))
        
                
        c.container_size = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if wait_for_confirmation:
            qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            if wait_for_confirmation:
                c = qlabs.wait_for_container(self.ID_SPLINE_LINE, device_num, self.FCN_SPLINE_LINE_SET_POINTS_ACK)
                return c
                    
            return True
        else:
            return False    