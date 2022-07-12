import math      
       
######################### MODULAR CONTAINER CLASS #########################

class QLabsSystem:
    """The System is a special actor class that allows you to modify elements of the user interface and application."""

    ID_SYSTEM = 1000
    """Class ID."""
    FCN_SYSTEM_SET_TITLE_STRING = 10
    """ """
    FCN_SYSTEM_SET_TITLE_STRING_ACK = 11
    """ """
        
    # Initialize class
    def __init__(self):
        """ Constructor Method """
        return

    def set_title_string(self, qlabs, titleString, waitForConfirmation=True):
        """Sets the title string in the upper left of the window to custom text. This can be useful when doing screen recordings or labeling experiment configurations.

        :param qlabs: A QuanserInteractiveLabs object.
        :param titleString: User defined string to replace the default title text
        :param waitForConfirmation: (Optional) Wait for confirmation of the before proceeding. This makes the method a blocking operation.
        :type qlabs: QuanserInteractiveLabs object
        :type titleString: string
        :type waitForConfirmation: boolean
        :return: If waitForConfirmation = `False` then returns `True` if spawn was successful, `False` otherwise.  If waitForConfirmation = `True`, returns a container detailed response information if successful, otherwise `False`.
        :rtype: boolean or CommModularContainer object
        """
        c = CommModularContainer()
        c.classID = CommModularContainer.ID_SYSTEM
        c.actorNumber = 0
        c.actorFunction = CommModularContainer.FCN_SYSTEM_SET_TITLE_STRING
        c.payload = bytearray(struct.pack(">I", len(titleString)))
        c.payload = c.payload + bytearray(titleString.encode('utf-8'))
        
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if waitForConfirmation:
            qlabs.flush_receive()        
                
        if (qlabs.send_container(c)):
        
            if waitForConfirmation:
                c = qlabs.wait_for_container(CommModularContainer.ID_SYSTEM, 0, CommModularContainer.FCN_SYSTEM_SET_TITLE_STRING_ACK)
                return c
            
            return True
        else:
            return False