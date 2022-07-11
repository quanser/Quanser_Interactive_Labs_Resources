from quanser.communications import Stream, StreamError, PollFlag, Timeout

import struct
import os
import platform
        
        
######################### MODULAR CONTAINER CLASS #########################

class CommModularContainer:

    """This class documents the Container used to send packets. This class is not typically used directly."""

    # Define class-level variables   
    containerSize = 0
    """The size of the packet in bytes. Container size (4 bytes) + class ID (4 bytes) + actor number (4 bytes) + actor function (1 byte) + payload (varies per function)"""
    classID = 0
    """See the ID_ variables in the respective library classes."""
    actorNumber = 0
    """An identifier that should be unique for a given class. """
    actorFunction = 0
    """See the FCN_ variables in the respective library classes."""
    payload = bytearray()
    """A variable sized payload depending on the actor function in use."""
       
    ID_GENERIC_ACTOR_SPAWNER = 135
    """The actor spawner is a special actor class that exists in open world environments that manages the spawning and destruction of dynamic actors."""
    FCN_GENERIC_ACTOR_SPAWNER_SPAWN = 10
    """ """
    FCN_GENERIC_ACTOR_SPAWNER_SPAWN_ACK = 11
    """ """
    FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ACTOR = 12
    """ """
    FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ACTOR_ACK = 13
    """ """
    FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ALL_SPAWNED_ACTORS = 14
    """ """
    FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ALL_SPAWNED_ACTORS_ACK = 15
    """ """
    FCN_GENERIC_ACTOR_SPAWNER_REGENERATE_CACHE_LIST = 16
    """ """
    FCN_GENERIC_ACTOR_SPAWNER_REGENERATE_CACHE_LIST_ACK = 17
    """ """
    FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ALL_SPAWNED_WIDGETS = 18
    """ """
    FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ALL_SPAWNED_WIDGETS_ACK = 19
    """ """
    FCN_GENERIC_ACTOR_SPAWNER_SPAWN_WIDGET = 20
    """ """
    FCN_GENERIC_ACTOR_SPAWNER_SPAWN_WIDGET_ACK = 21
    """ """
    FCN_GENERIC_ACTOR_SPAWNER_SPAWN_AND_PARENT_RELATIVE = 50
    """ """
    FCN_GENERIC_ACTOR_SPAWNER_SPAWN_AND_PARENT_RELATIVE_ACK = 51
    """ """
    FCN_GENERIC_ACTOR_SPAWNER_WIDGET_SPAWN_CONFIGURATION = 100
    """ """
    FCN_GENERIC_ACTOR_SPAWNER_WIDGET_SPAWN_CONFIGURATION_ACK = 101
    """ """
    
    
    ID_UNKNOWN = 0
    """Class ID 0 is reserved as an unknown class. QLabs may respond with a container with information it does not understand due to an unknown class, if data was improperly formatted, or if communication methods were executed in the wrong order."""
    
    # Common
    FCN_UNKNOWN = 0
    """Function ID is not recognized."""
    FCN_REQUEST_PING = 1
    """Request a response from an actor to test if it is present."""
    FCN_RESPONSE_PING = 2
    """Response from an actor to confirming it is present."""
    FCN_REQUEST_WORLD_TRANSFORM = 3
    """Request a world transform from the actor to read its current location, rotation, and scale."""
    FCN_RESPONSE_WORLD_TRANSFORM = 4
    """Response from an actor with its current location, rotation, and scale."""
    
    BASE_CONTAINER_SIZE = 13
    """Container size variable (4 bytes) + class ID (4 bytes) + actor number (4 bytes) + actor function (1 byte). Does not include the payload size which is variable per function."""

    # Initialize class
    def __init__(self):

       return

######################### COMMUNICATIONS #########################        
       
class QuanserInteractiveLabs:

    _stream = None
    #_client_connection = None
    _BUFFER_SIZE = 65537
        
    _readBuffer = bytearray(_BUFFER_SIZE)
    _sendBuffer = bytearray()

    _receivePacketBuffer = bytearray()
    _receivePacketSize = 0
    _receivePacketContainerIndex = 0  

    _URIPort = 17001

    # Initialize QLabs
    def __init__(self):
       """ Constructor Method """
        pass
    
    def open(self, address, timeout=10):
        """Open a connection to QLabs.

        :param address: The machine name or IP address of a local or remote copy of QLabs such as "localhost", or "192.168.1.123".
        :param timeout: (Optional) Period to attempt the connection for before aborting. Default 10s.
        :type address: string
        :type timeout: float
        :return: `True` if successful, `False` otherwise
        :rtype: boolean

        """

        address = "tcpip://" + address + ":18000"
        
        self._stream = Stream()

        result = self._stream.connect(address, True, self._BUFFER_SIZE, self._BUFFER_SIZE)
        if ((result < 0) and (result != -34)): # QERR_WOULD_BLOCK
            print("Connection failure.")
            return False

        pollResult = self._stream.poll(Timeout(1), PollFlag.CONNECT)

        while (((pollResult & PollFlag.CONNECT) != PollFlag.CONNECT) and (timeout > 0)):
            pollResult = self._stream.poll(Timeout(1), PollFlag.CONNECT)
            timeout = timeout - 1

        if pollResult & PollFlag.CONNECT == PollFlag.CONNECT:
            #print("Connection accepted")
            pass
        else:
            if (timeout == 0):
                print("Connection timeout")
        
            return False       
        
        return True
        
    def close(self):
        """Shutdown and close a connection to QLabs. Always close a connection when communications are finished.

        :return: No return. If an existing connection cannot be found, the function will fail silently.
        :rtype: none

        """
        try:
            self._stream.shutdown()
            self._stream.close()       
        except:
            pass
            
    # Pack data and send immediately
    def send_container (self, container):
        """Package a single container into a packet and transmit immediately

        :param container: CommModularContainer populated with the actor information.
        :type container: CommModularContainer object
        :return: `True` if successful, `False` otherwise
        :rtype: boolean

        """
        try:
            data = bytearray(struct.pack("<i", 1+container.containerSize)) + bytearray(struct.pack(">BiiiB", 123, container.containerSize, container.classID, container.actorNumber, container.actorFunction)) + container.payload
            numBytes = len(data)
            bytesWritten = self._stream.send(data, numBytes)
            self._stream.flush()
            return True
        except:
            return False      

    # Check if new data is available.  Returns true if a complete packet has been received.
    def receive_new_data(self):  
        """Poll for new data received from QLabs through the communications framework. If you are expecting large amounts of data such as video, this should be executed frequently to avoid overflowing internal buffers. Data split over multiple packets will be automatically reassembled before returning true. This method is non-blocking.

        :return: `True` if at least one complete container has been received, `False` otherwise
        :rtype: boolean

        """    
        bytesRead = 0
        
        try:
            bytesRead = self._stream.receive(self._readBuffer, self._BUFFER_SIZE)
        except StreamError as e:
            if e.error_code == -34:
                # would block
                bytesRead = 0
        newData = False
    
        while bytesRead > 0:
            self._receivePacketBuffer += bytearray(self._readBuffer[0:(bytesRead)])

            #while we're here, check if there are any more bytes in the receive buffer
            try:
                bytesRead = self._stream.receive(self._readBuffer, self._BUFFER_SIZE)
            except StreamError as e:
                if e.error_code == -34:
                    # would block
                    bytesRead = 0
                    
        # check if we already have data in the receive buffer that was unprocessed (multiple packets in a single receive)
        if len(self._receivePacketBuffer) > 5:
            if (self._receivePacketBuffer[4] == 123):
                
                # packet size
                self._receivePacketSize, = struct.unpack("<I", self._receivePacketBuffer[0:4])
                # add the 4 bytes for the size to the packet size
                self._receivePacketSize = self._receivePacketSize + 4          
            
                if len(self._receivePacketBuffer) >= self._receivePacketSize:
                    
                    self._receivePacketContainerIndex = 5
                    newData = True
                   
            else:
                print("Error parsing multiple packets in receive buffer.  Clearing internal buffers.")
                _receivePacketBuffer = bytearray()
                
        return newData

    # Parse out received containers
    def get_next_container(self):
        """If receive_new_data has returned true, use this method to receive the next container in the queue.

        :return: The data will be returned in a CommModularContainer object along with a flag to indicate if additional complete containers remain in the queue for extraction. If this method was used without checking for new data first and the queue is empty, the container will contain the default values with a class ID of ID_UNKNOWN.
        :rtype: CommModularContainer object, boolean

        """   

        c = CommModularContainer()
        isMoreContainers = False
    
        if (self._receivePacketContainerIndex > 0):
            c.containerSize, = struct.unpack(">I", self._receivePacketBuffer[self._receivePacketContainerIndex:(self._receivePacketContainerIndex+4)])
            c.classID, = struct.unpack(">I", self._receivePacketBuffer[(self._receivePacketContainerIndex+4):(self._receivePacketContainerIndex+8)])
            c.actorNumber, = struct.unpack(">I", self._receivePacketBuffer[(self._receivePacketContainerIndex+8):(self._receivePacketContainerIndex+12)])
            c.actorFunction = self._receivePacketBuffer[self._receivePacketContainerIndex+12]
            c.payload = bytearray(self._receivePacketBuffer[(self._receivePacketContainerIndex+c.BASE_CONTAINER_SIZE):(self._receivePacketContainerIndex+c.containerSize)])
            
            self._receivePacketContainerIndex = self._receivePacketContainerIndex + c.containerSize
            
            if (self._receivePacketContainerIndex >= self._receivePacketSize):
                
                isMoreContainers = False
                
                if len(self._receivePacketBuffer) == self._receivePacketSize:
                    # The data buffer contains only the one packet.  Clear the buffer.
                    self._receivePacketBuffer = bytearray()
                else:
                    # Remove the packet from the data buffer.  There is another packet in the buffer already.
                    self._receivePacketBuffer = self._receivePacketBuffer[(self._receivePacketContainerIndex):(len(self._receivePacketBuffer))]
                    
                self._receivePacketContainerIndex = 0
                
            else:
                isMoreContainers = True
                
    
        return c, isMoreContainers   

    def wait_for_container(self, classID, actorNumber, functionNumber):
        """Continually poll and parse incoming containers until a response from specific actor with a specific function response is received. Containers that do not match the class, actor number, and function number are discarded. This is a blocking function.

        :return: The data will be returned in a CommModularContainer object.
        :rtype: CommModularContainer object

        """   


       while(True):
            while (self.receive_new_data() == False):
                pass
                
            moreContainers = True
            
            while (moreContainers):
                c, moreContainers = self.get_next_container()
                
                if c.classID == classID:
                    if c.actorNumber == actorNumber:
                        if c.actorFunction == functionNumber:
                            return c
                            
    def flush_receive(self):
        """Flush receive buffers removing all unread data.

        :return: None
        :rtype: None

        """   
        try:
            bytesRead = self._stream.receive(self._readBuffer, self._BUFFER_SIZE)
        except StreamError as e:
            if e.error_code == -34:
                # would block
                bytesRead = 0
            
    def destroy_all_spawned_actors(self):
        """Find and destroy all spawned actors and widgets. This is a blocking operation.

        :return: `True` if successful, `False` otherwise
        :rtype: boolean

        .. danger::

            TODO: Confirm this does not block if the actor does not exist. Perhaps return integer for number of actors deleted.
        """   
        actorNumber = 0
        c = CommModularContainer()
        
        c.classID = CommModularContainer.ID_GENERIC_ACTOR_SPAWNER
        c.actorNumber = actorNumber
        c.actorFunction = CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ALL_SPAWNED_ACTORS
        c.payload = bytearray()
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)        

        if (self.send_container(c)):
            c = self.wait_for_container(CommModularContainer.ID_GENERIC_ACTOR_SPAWNER, actorNumber, CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ALL_SPAWNED_ACTORS_ACK)
            
            return True
        
        else:
            return False
            
    def destroy_spawned_actor(self, classID, actorNumber):
        """Find and destroy a specific actor. This is a blocking operation.
        
        :param classID: See the ID_ variables in the respective library classes for the class identifier
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :type classID: uint32
        :type actorNumber: uint32
        :return: `True` if successful, `False` otherwise
        :rtype: boolean

        .. danger::

            TODO: Change this to return the number of actors deleted

        """   
        c = CommModularContainer()
        
        c.classID = CommModularContainer.ID_GENERIC_ACTOR_SPAWNER
        c.actorNumber = 0
        c.actorFunction = CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ACTOR
        c.payload = bytearray(struct.pack(">II", classID, actorNumber))
        
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)        

        if (self.send_container(c)):
            c = self.wait_for_container(CommModularContainer.ID_GENERIC_ACTOR_SPAWNER, 0, CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ACTOR_ACK)
            
            return True
        
        else:
            return False            
            
    def spawn(self, actorNumber, classID, x, y, z, roll, pitch, yaw, sx, sy, sz, configuration=0, waitForConfirmation=True):
        """Spawns a new actor.

        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param classID: See the ID_ variables in the respective library classes for the class identifier
        :param x: Location in m
        :param y: Location in m
        :param z: Location in m
        :param roll: Angle in radians
        :param pitch: Angle in radians
        :param yaw: Angle in radians
        :param sx: Scale with 1.0 being full scale. Scale values of 0.0 should not be used.
        :param sy: Scale with 1.0 being full scale. Scale values of 0.0 should not be used.
        :param sz: Scale with 1.0 being full scale. Scale values of 0.0 should not be used.
        :param configuration: (Optional) Spawn configuration. See class library for configuration options.
        :param waitForConfirmation: (Optional) Make this operation blocking until confirmation of the spawn has occurred.
        :type actorNumber: uint32
        :type classID: uint32
        :type x: float
        :type y: float
        :type z: float
        :type roll: float
        :type pitch: float
        :type yaw: float
        :type sx: float
        :type sy: float
        :type sz: float
        :type configuration: uint32
        :type waitForConfirmation: boolean
        :return: `True` if spawn was successful, `False` otherwise
        :rtype: boolean

        """
        c = CommModularContainer()
        c.classID = CommModularContainer.ID_GENERIC_ACTOR_SPAWNER
        c.actorNumber = 0
        c.actorFunction = CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_SPAWN
        c.payload = bytearray(struct.pack(">IIfffffffffI", classID, actorNumber, x, y, z, roll, pitch, yaw, sx, sy, sz, configuration))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if waitForConfirmation:
            self.flush_receive()        
                
        if (self.send_container(c)):
        
            if waitForConfirmation:
                c = self.wait_for_container(CommModularContainer.ID_GENERIC_ACTOR_SPAWNER, 0, CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_SPAWN_ACK)
                return c
            
            return True
        else:
            return False 
            
    def spawn_and_parent_with_relative_transform(self, actorNumber, classID, x, y, z, roll, pitch, yaw, sx, sy, sz, configuration, parentClassID, parentActorNumber, parentComponent, waitForConfirmation=True):
        """Spawns a new actor relative to an existing actor and creates an kinematic relationship.

        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param classID: See the ID_ variables in the respective library classes for the class identifier
        :param x: Location in m
        :param y: Location in m
        :param z: Location in m
        :param roll: Angle in radians
        :param pitch: Angle in radians
        :param yaw: Angle in radians
        :param sx: Scale with 1.0 being full scale. Scale values of 0.0 should not be used.
        :param sy: Scale with 1.0 being full scale. Scale values of 0.0 should not be used.
        :param sz: Scale with 1.0 being full scale. Scale values of 0.0 should not be used.
        :param configuration: (Optional) Spawn configuration. See class library for configuration options.
        :param parentClassID: See the ID_ variables in the respective library classes for the class identifier
        :param parentActorNumber: User defined unique identifier for the class actor in QLabs
        :param parentComponent: `0` for the origin of the parent actor, see the parent class for additional reference frame options
        :param waitForConfirmation: (Optional) Make this operation blocking until confirmation of the spawn has occurred.
        :type actorNumber: uint32
        :type classID: uint32
        :type x: float
        :type y: float
        :type z: float
        :type roll: float
        :type pitch: float
        :type yaw: float
        :type sx: float
        :type sy: float
        :type sz: float
        :type configuration: uint32
        :type parentClassID: uint32
        :type parentActorNumber: uint32
        :type parentComponent: uint32
        :type waitForConfirmation: boolean
        :return: If waitForConfirmation = `False` then returns `True` if spawn was successful, `False` otherwise.  If waitForConfirmation = `True`, returns a container detailed response information if successful, otherwise `False`.
        :rtype: boolean

        """
        c = CommModularContainer()
        c.classID = CommModularContainer.ID_GENERIC_ACTOR_SPAWNER
        c.actorNumber = 0
        c.actorFunction = CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_SPAWN_AND_PARENT_RELATIVE
        c.payload = bytearray(struct.pack(">IIfffffffffIIII", classID, actorNumber, x, y, z, roll, pitch, yaw, sx, sy, sz, configuration, parentClassID, parentActorNumber, parentComponent))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if waitForConfirmation:
            self.flush_receive()        
                
        if (self.send_container(c)):
        
            if waitForConfirmation:
                c = self.wait_for_container(CommModularContainer.ID_GENERIC_ACTOR_SPAWNER, 0, CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_SPAWN_AND_PARENT_RELATIVE_ACK)
                return c
            
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
                  
            
    def ping(self):
        """Ping a specific actor. This is a blocking operation.
        
        :return: `True` if successful, `False` otherwise
        :rtype: boolean

        .. danger::

            TODO: This should not be a blocking function.  Re-write this with a timeout. If it can't find the actor, it will never return.
        """

        c = CommModularContainer()
        c.classID = CommModularContainer.ID_GENERIC_ACTOR_SPAWNER
        c.actorNumber = 0
        c.actorFunction = CommModularContainer.FCN_REQUEST_PING
        c.payload = bytearray()
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        self.flush_receive()        
                
        if (self.send_container(c)):
        
            c = self.wait_for_container(CommModularContainer.ID_GENERIC_ACTOR_SPAWNER, 0, CommModularContainer.FCN_RESPONSE_PING)
            return True
        else:
            return False 
    
    def regenerate_cache_list(self):
        """Advanced function for actor indexing.
        
        :return: `True` if successful, `False` otherwise
        :rtype: boolean

        .. danger::

            TODO: Improve this description.
        """
        c = CommModularContainer()
        c.classID = CommModularContainer.ID_GENERIC_ACTOR_SPAWNER
        c.actorNumber = 0
        c.actorFunction = CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_REGENERATE_CACHE_LIST
        c.payload = bytearray()
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)

        if (self.send_container(c)):
            c = self.wait_for_container(CommModularContainer.ID_GENERIC_ACTOR_SPAWNER, c.actorNumber, CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_REGENERATE_CACHE_LIST_ACK)
            
            return True
        
        else:
            return False
    
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
            
       
   
    def __del__(self):
        """ Destructor Method """
        self.close()