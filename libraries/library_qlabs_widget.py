from library_qlabs import QuanserInteractiveLabs, CommModularContainer
import math      
       
######################### MODULAR CONTAINER CLASS #########################

class QLabsWidget:
    """ This class is for the spawning of widgets. Widgets are special actors that cannot be addressed after they have been spawned so they do not support parenting. They are highly efficient so it is possible to spawn thousands of widgets while maintaining performance."""

    FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ALL_SPAWNED_WIDGETS = 18
    FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ALL_SPAWNED_WIDGETS_ACK = 19
    FCN_GENERIC_ACTOR_SPAWNER_SPAWN_WIDGET = 20
    FCN_GENERIC_ACTOR_SPAWNER_SPAWN_WIDGET_ACK = 21
    FCN_GENERIC_ACTOR_SPAWNER_SPAWN_AND_PARENT_RELATIVE = 50
    FCN_GENERIC_ACTOR_SPAWNER_SPAWN_AND_PARENT_RELATIVE_ACK = 51
    FCN_GENERIC_ACTOR_SPAWNER_WIDGET_SPAWN_CONFIGURATION = 100
    FCN_GENERIC_ACTOR_SPAWNER_WIDGET_SPAWN_CONFIGURATION_ACK = 101


    CUBE = 0
    CYLINDER = 1
    SPHERE = 2
    AUTOCLAVE_CAGE = 3
    PLASTIC_BOTTLE = 4
    METAL_CAN = 5
        
    # Initialize class
    def __init__(self):
        """ Constructor Method """
        return
       
    def spawn(self, qlabs, widgetType, location, rotation, scale, color, measuredMass=0, IDTag=0, properties="", waitForConfirmation=True):
        """Spawns a widget in an instance of QLabs at a specific location and rotation using radians.

        :param qlabs: A QuanserInteractiveLabs object.
        :param widgetType: See QLabsWidget class
        :param location: An array of floats for x, y and z coordinates.
        :param rotation: An array of floats for the roll, pitch, and yaw in radians.
        :param scale: An array of floats for the scale in the x, y, and z directions.
        :param color: Red, Green, Blue components of the RGB color on a 0.0 to 1.0 scale.
        :param measuredMass: A float value for use with mass sensor instrumented actors. This does not alter the dynamic properties.
        :param IDTag: An integer value for use with IDTag sensor instrumented actors.
        :param properties: A string for use with properties sensor instrumented actors. This can contain any string that is available for use to parse out user-customized parameters.
        :param waitForConfirmation: (Optional) Make this operation blocking until confirmation of the spawn has occurred.
        :type qlabs: QuanserInteractiveLabs object
        :type widgetType: uint32
        :type location: float array[3]
        :type rotation: float array[3]
        :type scale: float array[3]
        :type color: float array[3]
        :type measuredMass: float
        :type IDTag: uint8
        :type properties: string
        :type waitForConfirmation: boolean
        :return: If waitForConfirmation = `False` then returns `True` if spawn was successful, `False` otherwise.  If waitForConfirmation = `True`, returns a container detailed response information if successful, otherwise `False`.
        :rtype: boolean or CommModularContainer object

        """
        return qlabs.spawn_widget(widgetType, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2], color[0], color[1], color[2], measuredMass, IDTag, properties, waitForConfirmation)
 
    def spawn_degrees(self, qlabs, widgetType, location, rotation, scale, color, measuredMass=0, IDTag=0, properties="", waitForConfirmation=True):
        """Spawns a widget in an instance of QLabs at a specific location and rotation using degrees.

        :param qlabs: A QuanserInteractiveLabs object.
        :param widgetType: See QLabsWidget class
        :param location: An array of floats for x, y and z coordinates.
        :param rotation: An array of floats for the roll, pitch, and yaw in degrees.
        :param scale: An array of floats for the scale in the x, y, and z directions.
        :param color: Red, Green, Blue components of the RGB color on a 0.0 to 1.0 scale.
        :param measuredMass: A float value for use with mass sensor instrumented actors. This does not alter the dynamic properties.
        :param IDTag: An integer value for use with IDTag sensor instrumented actors.
        :param properties: A string for use with properties sensor instrumented actors. This can contain any string that is available for use to parse out user-customized parameters.
        :param waitForConfirmation: (Optional) Make this operation blocking until confirmation of the spawn has occurred.
        :type widgetType: uint32
        :type location: float array[3]
        :type rotation: float array[3]
        :type scale: float array[3]
        :type color: float array[3]
        :type measuredMass: float
        :type IDTag: uint8
        :type properties: string
        :type waitForConfirmation: boolean
        :return: If waitForConfirmation = `False` then returns `True` if spawn was successful, `False` otherwise.  If waitForConfirmation = `True`, returns a container detailed response information if successful, otherwise `False`.
        :rtype: boolean or CommModularContainer object

        """
        return qlabs.spawn_widget(widgetType, location[0], location[1], location[2], rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi, scale[0], scale[1], scale[2], color[0], color[1], color[2], measuredMass, IDTag, properties, waitForConfirmation)
 

    def destroy_all_spawned_widgets(self):
        """Destroys all spawned widgets, but does not destroy actors.
        
        :return: `True` if successful, `False` otherwise
        :rtype: boolean

        """
        actorNumber = 0
        c = CommModularContainer()
        
        c.classID = CommModularContainer.ID_GENERIC_ACTOR_SPAWNER
        c.actorNumber = actorNumber
        c.actorFunction = CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ALL_SPAWNED_WIDGETS
        c.payload = bytearray()
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)        

        if (self.send_container(c)):
            c = self.wait_for_container(CommModularContainer.ID_GENERIC_ACTOR_SPAWNER, actorNumber, CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ALL_SPAWNED_WIDGETS_ACK)
            
            return True
        
        else:
            return False   

            
    def widget_spawn_configuration(self, enableShadow=True):
        """If spawning a large number of widgets causes performance degradation, you can try disabling the widget shadows. This function must be called in advance of widget spawning and all subsequence widgets will be spawned with the specified shadow setting.
        
        :param enableShadow: (Optional) Show (`True`) or hide (`False`) widget shadows.
        :type enableShadow: boolean
        :return: `True` if successful, `False` otherwise
        :rtype: boolean

        """
        actorNumber = 0
        c = CommModularContainer()
        
        c.classID = CommModularContainer.ID_GENERIC_ACTOR_SPAWNER
        c.actorNumber = actorNumber
        c.actorFunction = CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_WIDGET_SPAWN_CONFIGURATION
        c.payload = bytearray(struct.pack(">B", enableShadow))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)        

        if (self.send_container(c)):
            c = self.wait_for_container(CommModularContainer.ID_GENERIC_ACTOR_SPAWNER, actorNumber, CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_WIDGET_SPAWN_CONFIGURATION_ACK)
            
            return True
        
        else:
            return False 

       
    def spawn_widget(self, widgetType, x, y, z, roll, pitch, yaw, sx, sy, sz, colorR, colorG, colorB, measuredMass, IDTag, properties, waitForConfirmation=True):
        """Spawns a new widget. It is recommended that you use the methods implemented in the QLabsWidget class instead.

        :param widgetType: See QLabsWidget class
        :param x: Location in m
        :param y: Location in m
        :param z: Location in m
        :param roll: Angle in radians
        :param pitch: Angle in radians
        :param yaw: Angle in radians
        :param sx: Scale with 1.0 being full scale. Scale values of 0.0 should not be used.
        :param sy: Scale with 1.0 being full scale. Scale values of 0.0 should not be used.
        :param sz: Scale with 1.0 being full scale. Scale values of 0.0 should not be used.
        :param colorR: Red component of the color on a 0.0 to 1.0 scale.
        :param colorG: Green component of the color on a 0.0 to 1.0 scale.
        :param colorB: Blue component of the color on a 0.0 to 1.0 scale.
        :param measuredMass: A float value for use with mass sensor instrumented actors. This does not alter the dynamic properties.
        :param IDTag: An integer value for use with IDTag sensor instrumented actors.
        :param properties: A string for use with properties sensor instrumented actors. This can contain any string that is available for use to parse out user-customized parameters.
        :param waitForConfirmation: (Optional) Make this operation blocking until confirmation of the spawn has occurred.
        :type widgetType: uint32
        :type x: float
        :type y: float
        :type z: float
        :type roll: float
        :type pitch: float
        :type yaw: float
        :type sx: float
        :type sy: float
        :type sz: float
        :type colorR: float
        :type colorG: float
        :type colorB: float
        :type measuredMass: float
        :type IDTag: uint8
        :type properties: string
        :type waitForConfirmation: boolean
        :return: If waitForConfirmation = `False` then returns `True` if spawn was successful, `False` otherwise.  If waitForConfirmation = `True`, returns a container detailed response information if successful, otherwise `False`.
        :rtype: boolean

        """
        c = CommModularContainer()
        c.classID = CommModularContainer.ID_GENERIC_ACTOR_SPAWNER
        c.actorNumber = 0
        c.actorFunction = CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_SPAWN_WIDGET
        c.payload = bytearray(struct.pack(">IfffffffffffffBI", widgetType, x, y, z, roll, pitch, yaw, sx, sy, sz, colorR, colorG, colorB, measuredMass, IDTag, len(properties)))
        c.payload = c.payload + bytearray(properties.encode('utf-8'))
        
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if waitForConfirmation:
            self.flush_receive()        
                
        if (self.send_container(c)):
        
            if waitForConfirmation:
                c = self.wait_for_container(CommModularContainer.ID_GENERIC_ACTOR_SPAWNER, 0, CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_SPAWN_WIDGET_ACK)
                return c
            
            return True
        else:
            return False  