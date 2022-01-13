from quanser.communications import Stream, StreamError, PollFlag, Timeout
from quanser.common import GenericError

import struct
import os
import platform
        
        
######################### MODULAR CONTAINER CLASS #########################

class CommModularContainer:

    # Define class-level variables   
    containerSize = 0
    classID = 0       # What device type is this?
    deviceNumber = 0   # Increment if there are more than one of the same device ID
    deviceFunction = 0 # Command/reponse
    payload = bytearray()
    
       
    ID_GENERIC_ACTOR_SPAWNER = 135
    FCN_GENERIC_ACTOR_SPAWNER_SPAWN = 10
    FCN_GENERIC_ACTOR_SPAWNER_SPAWN_ACK = 11
    FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ACTOR = 12
    FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ACTOR_ACK = 13
    FCN_GENERIC_ACTOR_SPAWNER_destoryAllSpawnedActors = 14
    FCN_GENERIC_ACTOR_SPAWNER_destoryAllSpawnedActors_ACK = 15
    FCN_GENERIC_ACTOR_SPAWNER_REGENERATE_CACHE_LIST = 16
    FCN_GENERIC_ACTOR_SPAWNER_REGENERATE_CACHE_LIST_ACK = 17
    FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ALL_SPAWNED_WIDGETS = 18
    FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ALL_SPAWNED_WIDGETS_ACK = 19
    FCN_GENERIC_ACTOR_SPAWNER_SPAWN_WIDGET = 20
    FCN_GENERIC_ACTOR_SPAWNER_SPAWN_WIDGET_ACK = 21
    FCN_GENERIC_ACTOR_SPAWNER_SPAWN_AND_PARENT_RELATIVE = 50
    FCN_GENERIC_ACTOR_SPAWNER_SPAWN_AND_PARENT_RELATIVE_ACK = 51
    FCN_GENERIC_ACTOR_SPAWNER_WIDGET_SPAWN_CONFIGURATION = 100
    FCN_GENERIC_ACTOR_SPAWNER_WIDGET_SPAWN_CONFIGURATION_ACK = 101
    
    
    
    ID_UE4_SYSTEM = 1000
    FCN_UE4_SYSTEM_SET_TITLE_STRING = 10
    FCN_UE4_SYSTEM_SET_TITLE_STRING_ACK = 11
    
    ID_SIMULATION_CODE = 1001
    FCN_SIMULATION_CODE_RESET = 200
    
    ID_UNKNOWN = 0
    
    # Common
    FCN_UNKNOWN = 0
    FCN_REQUEST_PING = 1
    FCN_RESPONSE_PING = 2
    FCN_REQUEST_WORLD_TRANSFORM = 3
    FCN_RESPONSE_WORLD_TRANSFORM = 4
    
    BASE_CONTAINER_SIZE = 13

    
    # Initilize class
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

    # Initilize QLabs
    def __init__(self):
        pass
    
    def open(self, uri, timeout=10):
        
        self._stream = Stream()

        result = self._stream.connect(uri, True, self._BUFFER_SIZE, self._BUFFER_SIZE)
        if ((result < 0) and (result != -34)): # QERR_WOULD_BLOCK
            print("Connection failure.")
            return False

        poll_result = self._stream.poll(Timeout(1), PollFlag.CONNECT)

        while (((poll_result & PollFlag.CONNECT) != PollFlag.CONNECT) and (timeout > 0)):
            poll_result = self._stream.poll(Timeout(1), PollFlag.CONNECT)
            timeout = timeout - 1


        if poll_result & PollFlag.CONNECT == PollFlag.CONNECT:
            #print("Connection accepted")
            pass
        else:
            if (timeout == 0):
                print("Connection timeout")
        
            return False
        
        
        return True
        
    def close(self):
        try:
            self._stream.shutdown()
            self._stream.close()       
        except:
            pass
            
    # Pack data and send immediately
    def sendContainer (self, container):
        try:
            data = bytearray(struct.pack("<i", 1+container.containerSize)) + bytearray(struct.pack(">BiiiB", 123, container.containerSize, container.classID, container.deviceNumber, container.deviceFunction)) + container.payload
            numBytes = len(data)
            bytesWritten = self._stream.send(data, numBytes)
            self._stream.flush()
            return True
        except:
            return False      


    # Check if new data is available.  Returns true if a complete packet has been received.
    def receiveNewData(self):    
        bytesRead = 0
        
        try:
            bytesRead = self._stream.receive(self._readBuffer, self._BUFFER_SIZE)
        except StreamError as e:
            if e.error_code == -34:
                # would block
                bytesRead = 0
        #print("Bytes read: {}".format(bytesRead))
            
        new_data = False

    
        while bytesRead > 0:
            #print("Received {} bytes".format(bytesRead))
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
                    new_data = True
                   
            else:
                print("Error parsing multiple packets in receive buffer.  Clearing internal buffers.")
                _receivePacketBuffer = bytearray()
                
        return new_data



    # Parse out received containers
    def getNextContainer(self):
        c = CommModularContainer()
        isMoreContainers = False
    
        if (self._receivePacketContainerIndex > 0):
            c.containerSize, = struct.unpack(">I", self._receivePacketBuffer[self._receivePacketContainerIndex:(self._receivePacketContainerIndex+4)])
            c.classID, = struct.unpack(">I", self._receivePacketBuffer[(self._receivePacketContainerIndex+4):(self._receivePacketContainerIndex+8)])
            c.deviceNumber, = struct.unpack(">I", self._receivePacketBuffer[(self._receivePacketContainerIndex+8):(self._receivePacketContainerIndex+12)])
            c.deviceFunction = self._receivePacketBuffer[self._receivePacketContainerIndex+12]
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


    def waitForContainer(self, classID, deviceNumber, functionNumber):
       while(True):
            while (self.receiveNewData() == False):
                pass
                
            #print("DEBUG: Data received. Looking for class {}, device {}, function {}".format(classID, deviceNumber, functionNumber))
                
            more_containers = True
            
            while (more_containers):
                c, more_containers = self.getNextContainer()
                
                #print("DEBUG: Container class {}, device {}, function {}".format(c.classID, c.deviceNumber, c.deviceFunction))
                
                if c.classID == classID:
                    if c.deviceNumber == deviceNumber:
                        if c.deviceFunction == functionNumber:
                            return c
                            
    def flushReceive(self):
        try:
            bytesRead = self._stream.receive(self._readBuffer, self._BUFFER_SIZE)
        except StreamError as e:
            if e.error_code == -34:
                # would block
                bytesRead = 0
            
    def destroyAllSpawnedActors(self):
        deviceNumber = 0
        c = CommModularContainer()
        
        c.classID = CommModularContainer.ID_GENERIC_ACTOR_SPAWNER
        c.deviceNumber = deviceNumber
        c.deviceFunction = CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_destoryAllSpawnedActors
        c.payload = bytearray()
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)        

        if (self.sendContainer(c)):
            #print("DEBUG: Container sent")
            c = self.waitForContainer(CommModularContainer.ID_GENERIC_ACTOR_SPAWNER, deviceNumber, CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_destoryAllSpawnedActors_ACK)
            
            return True
        
        else:
            return False
            
    def destroySpawnedActor(self, ID, deviceNumber):
        c = CommModularContainer()
        
        c.classID = CommModularContainer.ID_GENERIC_ACTOR_SPAWNER
        c.deviceNumber = 0
        c.deviceFunction = CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ACTOR
        c.payload = bytearray(struct.pack(">II", ID, deviceNumber))
        
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)        

        if (self.sendContainer(c)):
            c = self.waitForContainer(CommModularContainer.ID_GENERIC_ACTOR_SPAWNER, 0, CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ACTOR_ACK)
            
            return True
        
        else:
            return False            
            
    def spawn(self, deviceNumber, classID, x, y, z, roll, pitch, yaw, sx, sy, sz, configuration=0, wait_for_confirmation=True):
        c = CommModularContainer()
        c.classID = CommModularContainer.ID_GENERIC_ACTOR_SPAWNER
        c.deviceNumber = 0
        c.deviceFunction = CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_SPAWN
        c.payload = bytearray(struct.pack(">IIfffffffffI", classID, deviceNumber, x, y, z, roll, pitch, yaw, sx, sy, sz, configuration))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if wait_for_confirmation:
            self.flushReceive()        
                
        if (self.sendContainer(c)):
        
            if wait_for_confirmation:
                c = self.waitForContainer(CommModularContainer.ID_GENERIC_ACTOR_SPAWNER, 0, CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_SPAWN_ACK)
                return c
            
            return True
        else:
            return False 
            
    def spawnAndParentWithRelativeTransform(self, deviceNumber, classID, x, y, z, roll, pitch, yaw, sx, sy, sz, configuration, parentClass, parentDeviceNum, parentComponent, wait_for_confirmation=True):
        c = CommModularContainer()
        c.classID = CommModularContainer.ID_GENERIC_ACTOR_SPAWNER
        c.deviceNumber = 0
        c.deviceFunction = CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_SPAWN_AND_PARENT_RELATIVE
        c.payload = bytearray(struct.pack(">IIfffffffffIIII", classID, deviceNumber, x, y, z, roll, pitch, yaw, sx, sy, sz, configuration, parentClass, parentDeviceNum, parentComponent))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if wait_for_confirmation:
            self.flushReceive()        
                
        if (self.sendContainer(c)):
        
            if wait_for_confirmation:
                c = self.waitForContainer(CommModularContainer.ID_GENERIC_ACTOR_SPAWNER, 0, CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_SPAWN_AND_PARENT_RELATIVE_ACK)
                return c
            
            return True
        else:
            return False            
            
    def spawnWidget(self, widgetType, x, y, z, roll, pitch, yaw, sx, sy, sz, color_r, color_g, color_b, measured_mass, ID_tag, properties, wait_for_confirmation=True):
        c = CommModularContainer()
        c.classID = CommModularContainer.ID_GENERIC_ACTOR_SPAWNER
        c.deviceNumber = 0
        c.deviceFunction = CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_SPAWN_WIDGET
        c.payload = bytearray(struct.pack(">IfffffffffffffBI", widgetType, x, y, z, roll, pitch, yaw, sx, sy, sz, color_r, color_g, color_b, measured_mass, ID_tag, len(properties)))
        c.payload = c.payload + bytearray(properties.encode('utf-8'))
        
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if wait_for_confirmation:
            self.flushReceive()        
                
        if (self.sendContainer(c)):
        
            if wait_for_confirmation:
                c = self.waitForContainer(CommModularContainer.ID_GENERIC_ACTOR_SPAWNER, 0, CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_SPAWN_WIDGET_ACK)
                return c
            
            return True
        else:
            return False      

    def setTitleString(self, titleString, wait_for_confirmation=True):
        c = CommModularContainer()
        c.classID = CommModularContainer.ID_UE4_SYSTEM
        c.deviceNumber = 0
        c.deviceFunction = CommModularContainer.FCN_UE4_SYSTEM_SET_TITLE_STRING
        c.payload = bytearray(struct.pack(">I", len(titleString)))
        c.payload = c.payload + bytearray(titleString.encode('utf-8'))
        
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if wait_for_confirmation:
            self.flushReceive()        
                
        if (self.sendContainer(c)):
        
            if wait_for_confirmation:
                c = self.waitForContainer(CommModularContainer.ID_UE4_SYSTEM, 0, CommModularContainer.FCN_UE4_SYSTEM_SET_TITLE_STRING_ACK)
                return c
            
            return True
        else:
            return False                  
            
    def ping(self):
        c = CommModularContainer()
        c.classID = CommModularContainer.ID_GENERIC_ACTOR_SPAWNER
        c.deviceNumber = 0
        c.deviceFunction = CommModularContainer.FCN_REQUEST_PING
        c.payload = bytearray()
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        self.flushReceive()        
                
        if (self.sendContainer(c)):
        
            c = self.waitForContainer(CommModularContainer.ID_GENERIC_ACTOR_SPAWNER, 0, CommModularContainer.FCN_RESPONSE_PING)
            return True
        else:
            return False 
    
    def regenerateCacheList(self):
        c = CommModularContainer()
        c.classID = CommModularContainer.ID_GENERIC_ACTOR_SPAWNER
        c.deviceNumber = 0
        c.deviceFunction = CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_REGENERATE_CACHE_LIST
        c.payload = bytearray()
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)

        if (self.sendContainer(c)):
            c = self.waitForContainer(CommModularContainer.ID_GENERIC_ACTOR_SPAWNER, c.deviceNumber, CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_REGENERATE_CACHE_LIST_ACK)
            
            return True
        
        else:
            return False
    
    def destroyAllSpawnedWidgets(self):
        deviceNumber = 0
        c = CommModularContainer()
        
        c.classID = CommModularContainer.ID_GENERIC_ACTOR_SPAWNER
        c.deviceNumber = deviceNumber
        c.deviceFunction = CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ALL_SPAWNED_WIDGETS
        c.payload = bytearray()
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)        

        if (self.sendContainer(c)):
            c = self.waitForContainer(CommModularContainer.ID_GENERIC_ACTOR_SPAWNER, deviceNumber, CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ALL_SPAWNED_WIDGETS_ACK)
            
            return True
        
        else:
            return False   
            

    def widgetSpawnConfiguration(self, EnableShadow=True):
        deviceNumber = 0
        c = CommModularContainer()
        
        c.classID = CommModularContainer.ID_GENERIC_ACTOR_SPAWNER
        c.deviceNumber = deviceNumber
        c.deviceFunction = CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_WIDGET_SPAWN_CONFIGURATION
        c.payload = bytearray(struct.pack(">B", EnableShadow))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)        

        if (self.sendContainer(c)):
            c = self.waitForContainer(CommModularContainer.ID_GENERIC_ACTOR_SPAWNER, deviceNumber, CommModularContainer.FCN_GENERIC_ACTOR_SPAWNER_WIDGET_SPAWN_CONFIGURATION_ACK)
            
            return True
        
        else:
            return False   
            
    def startRealTimeModel(self, modelName, deviceNum=0, QLabsHostName='localhost', additionalArguments=""):
        if platform.system() == "Windows":
            cmd_string="start \"QLabs_{}_{}\" \"%QUARC_DIR%\quarc_run\" -D -r -t tcpip://localhost:17000 {}.rt-win64 -uri tcpip://localhost:{} -hostname {} -devicenum {} {}".format(modelName, deviceNum, modelName, self._URIPort, QLabsHostName, deviceNum, additionalArguments)
        elif platform.system() == "Linux":
            if platform.machine() == "armv7l":
                #Raspberry Pi 3, 4
                cmd_string="quarc_run -D -r -t tcpip://localhost:17000 {}.rt-linux_pi_3 -uri tcpip://localhost:{} -hostname {} -devicenum {} {}".format(modelName, self._URIPort, QLabsHostName, deviceNum, additionalArguments)
            else:
                print("This Linux machine not supported for real-time model execution")
                return
        else:
            print("Platform not supported for real-time model execution")
            return
            
        os.system(cmd_string)
        
        self._URIPort = self._URIPort + 1
        return cmd_string            
          
    def terminateRealTimeModel(self, modelName, additionalArguments=""):
        if platform.system() == "Windows":
            cmd_string="start \"QLabs_Spawn_Model\" \"%QUARC_DIR%\quarc_run\" -q -Q -t tcpip://localhost:17000 {}.rt-win64 {}".format(modelName, additionalArguments)
        elif platform.system() == "Linux":
            if platform.machine() == "armv7l":
                cmd_string="quarc_run -q -Q -t tcpip://localhost:17000 {}.rt-linux_pi_3 {}".format(modelName, additionalArguments)
            else:
                print("This Linux machine not supported for real-time model execution")
                return
            
        else:
            print("Platform not supported for real-time model execution")
            return
                    
        os.system(cmd_string)
        return cmd_string
        
    def terminateAllRealTimeModels(self, additionalArguments=""):
        if platform.system() == "Windows":
            cmd_string="start \"QLabs_Spawn_Model\" \"%QUARC_DIR%\quarc_run\" -q -Q -t tcpip://localhost:17000 *.rt-win64 {}".format(additionalArguments)
        elif platform.system() == "Linux":
            if platform.machine() == "armv7l":
                cmd_string="quarc_run -q -Q -t tcpip://localhost:17000 *.rt-linux_pi_3 {}".format(additionalArguments)
            else:
                print("This Linux machine not supported for real-time model execution")
                return
            
        else:
            print("Platform not supported for real-time model execution")
            return
                    
        os.system(cmd_string)
        return cmd_string        
   
    def __del__(self):
        self.close()