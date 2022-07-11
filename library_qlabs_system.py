import math      
       
######################### MODULAR CONTAINER CLASS #########################

class QLabsSystem:
    """ This class documents the QLabs System methods."""

    ID_SYSTEM = 1000
    """The System is a special actor class that allows you to modify elements of the user interface and application."""
    FCN_SYSTEM_SET_TITLE_STRING = 10
    """ """
    FCN_SYSTEM_SET_TITLE_STRING_ACK = 11
    """ """
        
    # Initialize class
    def __init__(self):

       return

    def set_title_string(self, qlabs, titleString, waitForConfirmation=True):
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