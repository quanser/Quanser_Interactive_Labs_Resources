import math      
       
######################### MODULAR CONTAINER CLASS #########################

class QLabsWidget:
    """ This class is for the spawning of widgets. Widgets are special actors that cannot be addressed after they have been spawned so they do not support parenting. They are highly efficient so it is possible to spawn thousands of widgets while maintaining performance."""

    CUBE = 0
    """ """
    CYLINDER = 1
    """ """
    SPHERE = 2
    """ """
    AUTOCLAVE_CAGE = 3
    """ """
    PLASTIC_BOTTLE = 4
    """ """
    METAL_CAN = 5
    """ """
        
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
 