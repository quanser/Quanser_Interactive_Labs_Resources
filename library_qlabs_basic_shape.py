from library_qlabs import quanser_interactive_labs, comm_modular_container
from quanser.common import GenericError
import math

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class qlab_basic_shape:

    # Define class-level variables   
    container_size = 0
    class_id = 0       # What device type is this?
    device_number = 0   # Increment if there are more than one of the same device ID
    device_function = 0 # Command/reponse
    payload = bytearray()
    
    SHAPE_CUBE = 0
    SHAPE_CYLINDER = 1
    SHAPE_SPHERE = 2
       
    ID_BASIC_SHAPE = 200
    
    FCN_BASIC_SHAPE_SET_MATERIAL_PROPERTIES = 10
    FCN_BASIC_SHAPE_SET_MATERIAL_PROPERTIES_ACK = 11
    FCN_BASIC_SHAPE_SET_PHYSICS_PROPERTIES = 12
    FCN_BASIC_SHAPE_SET_PHYSICS_PROPERTIES_ACK = 13
    FCN_BASIC_SHAPE_ENABLE_DYNAMICS = 14
    FCN_BASIC_SHAPE_ENABLE_DYNAMICS_ACK = 15
    FCN_BASIC_SHAPE_SET_TRANSFORM = 16
    FCN_BASIC_SHAPE_SET_TRANSFORM_ACK = 17
    
    # Initilize class
    def __init__(self):

       return
       
    def spawn(self, qlabs, device_num, location, rotation, scale, configuration=SHAPE_CUBE, wait_for_confirmation=True):
        return qlabs.spawn(device_num, self.ID_BASIC_SHAPE, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2], configuration, wait_for_confirmation)
 
    def spawn_degrees(self, qlabs, device_num, location, rotation, scale, configuration=SHAPE_CUBE, wait_for_confirmation=True):
        rotation[0] = rotation[0]/180*math.pi
        rotation[1] = rotation[1]/180*math.pi
        rotation[2] = rotation[2]/180*math.pi
    
        return qlabs.spawn(device_num, self.ID_BASIC_SHAPE, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2], configuration, wait_for_confirmation)
 
 
    def set_material_properties(self, qlabs, device_num, color, roughness=0.4, metallic=False, wait_for_confirmation=True):
        c = comm_modular_container()
        c.class_id = self.ID_BASIC_SHAPE
        c.device_number = device_num
        c.device_function = self.FCN_BASIC_SHAPE_SET_MATERIAL_PROPERTIES
        c.payload = bytearray(struct.pack(">ffffB", color[0], color[1], color[2], roughness, metallic))
        c.container_size = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if wait_for_confirmation:
            qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            if wait_for_confirmation:
                c = qlabs.wait_for_container(self.ID_BASIC_SHAPE, device_num, self.FCN_BASIC_SHAPE_SET_MATERIAL_PROPERTIES_ACK)
                return True
                    
            return True
        else:
            return False    
            
    def set_physics_properties(self, qlabs, device_num, mass, linear_damping, angular_damping, enable_dynamics, wait_for_confirmation=True):
        c = comm_modular_container()
        c.class_id = self.ID_BASIC_SHAPE
        c.device_number = device_num
        c.device_function = self.FCN_BASIC_SHAPE_SET_PHYSICS_PROPERTIES
        c.payload = bytearray(struct.pack(">fffB", mass, linear_damping, angular_damping, enable_dynamics))
        c.container_size = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if wait_for_confirmation:
            qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            if wait_for_confirmation:
                c = qlabs.wait_for_container(self.ID_BASIC_SHAPE, device_num, self.FCN_BASIC_SHAPE_SET_PHYSICS_PROPERTIES_ACK)
                return True
                    
            return True
        else:
            return False             
            
    def set_enable_dynamics(self, qlabs, device_num, enable_dynamics, wait_for_confirmation=True):
        c = comm_modular_container()
        c.class_id = self.ID_BASIC_SHAPE
        c.device_number = device_num
        c.device_function = self.FCN_BASIC_SHAPE_ENABLE_DYNAMICS
        c.payload = bytearray(struct.pack(">B", enable_dynamics))
        c.container_size = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if wait_for_confirmation:
            qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            if wait_for_confirmation:
                c = qlabs.wait_for_container(self.ID_BASIC_SHAPE, device_num, self.FCN_BASIC_SHAPE_ENABLE_DYNAMICS_ACK)
                return True
                    
            return True
        else:
            return False       


    def set_transform(self, qlabs, device_num, location, rotation, scale, wait_for_confirmation=True):
        c = comm_modular_container()
        c.class_id = self.ID_BASIC_SHAPE
        c.device_number = device_num
        c.device_function = self.FCN_BASIC_SHAPE_SET_TRANSFORM
        c.payload = bytearray(struct.pack(">fffffffff", location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2]))
        c.container_size = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if wait_for_confirmation:
            qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            if wait_for_confirmation:
                c = qlabs.wait_for_container(self.ID_BASIC_SHAPE, device_num, self.FCN_BASIC_SHAPE_SET_TRANSFORM_ACK)
                return c
                    
            return True
        else:
            return False        

    def set_transform_degrees(self, qlabs, device_num, location, rotation, scale, wait_for_confirmation=True):
    
        rotation[0] = rotation[0]/180*math.pi
        rotation[1] = rotation[1]/180*math.pi
        rotation[2] = rotation[2]/180*math.pi
    
        return self.set_transform(qlabs, device_num, location, rotation, scale, wait_for_confirmation)   
