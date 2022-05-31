from library_qlabs import QuanserInteractiveLabs, CommModularContainer
from quanser.common import GenericError
import math

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsBasicShape:
    
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
    
    # Initialize class
    def __init__(self):

       return
       
    def spawn(self, qlabs, deviceNumber, location, rotation, scale, configuration=SHAPE_CUBE, waitForConfirmation=True):
        return qlabs.spawn(deviceNumber, self.ID_BASIC_SHAPE, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2], configuration, waitForConfirmation)
 
    def spawn_degrees(self, qlabs, deviceNumber, location, rotation, scale, configuration=SHAPE_CUBE, waitForConfirmation=True):
    
        return qlabs.spawn(deviceNumber, self.ID_BASIC_SHAPE, location[0], location[1], location[2], rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi, scale[0], scale[1], scale[2], configuration, waitForConfirmation)
 
    def spawn_and_parent_with_relative_transform(self, qlabs, deviceNumber, location, rotation, scale, configuration, parentClass, parentDeviceNumber, parentComponent, waitForConfirmation=True):
        return qlabs.spawn_and_parent_with_relative_transform(deviceNumber, self.ID_BASIC_SHAPE, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2], configuration, parentClass, parentDeviceNumber, parentComponent, waitForConfirmation)
   
    def set_material_properties(self, qlabs, deviceNumber, color, roughness=0.4, metallic=False, waitForConfirmation=True):
        c = CommModularContainer()
        c.classID = self.ID_BASIC_SHAPE
        c.deviceNumber = deviceNumber
        c.deviceFunction = self.FCN_BASIC_SHAPE_SET_MATERIAL_PROPERTIES
        c.payload = bytearray(struct.pack(">ffffB", color[0], color[1], color[2], roughness, metallic))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if waitForConfirmation:
            qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            if waitForConfirmation:
                c = qlabs.wait_for_container(self.ID_BASIC_SHAPE, deviceNumber, self.FCN_BASIC_SHAPE_SET_MATERIAL_PROPERTIES_ACK)
                return True
                    
            return True
        else:
            return False    
            
    def set_physics_properties(self, qlabs, deviceNumber, mass, linearDampign, angularDamping, enableDynamics, waitForConfirmation=True):
        c = CommModularContainer()
        c.classID = self.ID_BASIC_SHAPE
        c.deviceNumber = deviceNumber
        c.deviceFunction = self.FCN_BASIC_SHAPE_SET_PHYSICS_PROPERTIES
        c.payload = bytearray(struct.pack(">fffB", mass, linearDampign, angularDamping, enableDynamics))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if waitForConfirmation:
            qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            if waitForConfirmation:
                c = qlabs.wait_for_container(self.ID_BASIC_SHAPE, deviceNumber, self.FCN_BASIC_SHAPE_SET_PHYSICS_PROPERTIES_ACK)
                return True
                    
            return True
        else:
            return False             
            
    def set_enable_dynamics(self, qlabs, deviceNumber, enableDynamics, waitForConfirmation=True):
        c = CommModularContainer()
        c.classID = self.ID_BASIC_SHAPE
        c.deviceNumber = deviceNumber
        c.deviceFunction = self.FCN_BASIC_SHAPE_ENABLE_DYNAMICS
        c.payload = bytearray(struct.pack(">B", enableDynamics))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if waitForConfirmation:
            qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            if waitForConfirmation:
                c = qlabs.wait_for_container(self.ID_BASIC_SHAPE, deviceNumber, self.FCN_BASIC_SHAPE_ENABLE_DYNAMICS_ACK)
                return True
                    
            return True
        else:
            return False       


    def set_transform(self, qlabs, deviceNumber, location, rotation, scale, waitForConfirmation=True):
        c = CommModularContainer()
        c.classID = self.ID_BASIC_SHAPE
        c.deviceNumber = deviceNumber
        c.deviceFunction = self.FCN_BASIC_SHAPE_SET_TRANSFORM
        c.payload = bytearray(struct.pack(">fffffffff", location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2]))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if waitForConfirmation:
            qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            if waitForConfirmation:
                c = qlabs.wait_for_container(self.ID_BASIC_SHAPE, deviceNumber, self.FCN_BASIC_SHAPE_SET_TRANSFORM_ACK)
                return c
                    
            return True
        else:
            return False        

    def set_transform_degrees(self, qlabs, deviceNumber, location, rotation, scale, waitForConfirmation=True):
    
        return self.set_transform(qlabs, deviceNumber, location, [x/180*math.pi for x in rotation], scale, waitForConfirmation)   
