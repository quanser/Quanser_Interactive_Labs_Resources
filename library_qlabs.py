from quanser.communications import Stream, StreamError, PollFlag, Timeout
from quanser.common import GenericError

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class comm_modular_container:

    # Define class-level variables   
    container_size = 0
    class_id = 0       # What device type is this?
    device_number = 0   # Increment if there are more than one of the same device ID
    device_function = 0 # Command/reponse
    payload = bytearray()
    
       
    ID_GENERIC_ACTOR_SPAWNER = 135
    FCN_GENERIC_ACTOR_SPAWNER_SPAWN = 10
    FCN_GENERIC_ACTOR_SPAWNER_SPAWN_ACK = 11
    FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ACTOR = 12
    FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ACTOR_ACK = 13
    FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ALL_SPAWNED_ACTORS = 14
    FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ALL_SPAWNED_ACTORS_ACK = 15
    FCN_GENERIC_ACTOR_SPAWNER_REGENERATE_CACHE_LIST = 16
    FCN_GENERIC_ACTOR_SPAWNER_REGENERATE_CACHE_LIST_ACK = 17
    FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ALL_SPAWNED_WIDGETS = 18
    FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ALL_SPAWNED_WIDGETS_ACK = 19
    FCN_GENERIC_ACTOR_SPAWNER_SPAWN_WIDGET = 20
    FCN_GENERIC_ACTOR_SPAWNER_SPAWN_WIDGET_ACK = 21
    
    
    
    ID_UE4_SYSTEM = 1000
    
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
       
class quanser_interactive_labs:

    _stream = None
    #_client_connection = None
    _BUFFER_SIZE = 65537
        
    _read_buffer = bytearray(_BUFFER_SIZE)
    _send_buffer = bytearray()

    _receive_packet_buffer = bytearray()
    _receive_packet_size = 0
    _receive_packet_container_index = 0   

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
    def send_container (self, container):
        try:
            data = bytearray(struct.pack("<i", 1+container.container_size)) + bytearray(struct.pack(">BiiiB", 123, container.container_size, container.class_id, container.device_number, container.device_function)) + container.payload
            num_bytes = len(data)
            bytes_written = self._stream.send(data, num_bytes)
            self._stream.flush()
            return True
        except:
            return False      


    # Check if new data is available.  Returns true if a complete packet has been received.
    def receive_new_data(self):    
        bytes_read = 0
        
        try:
            bytes_read = self._stream.receive(self._read_buffer, self._BUFFER_SIZE)
        except StreamError as e:
            if e.error_code == -34:
                # would block
                bytes_read = 0
        #print("Bytes read: {}".format(bytes_read))
            
        new_data = False

    
        while bytes_read > 0:
            #print("Received {} bytes".format(bytes_read))
            self._receive_packet_buffer += bytearray(self._read_buffer[0:(bytes_read)])

            #while we're here, check if there are any more bytes in the receive buffer
            try:
                bytes_read = self._stream.receive(self._read_buffer, self._BUFFER_SIZE)
            except StreamError as e:
                if e.error_code == -34:
                    # would block
                    bytes_read = 0
                    
        # check if we already have data in the receive buffer that was unprocessed (multiple packets in a single receive)
        if len(self._receive_packet_buffer) > 5:
            if (self._receive_packet_buffer[4] == 123):
                
                # packet size
                self._receive_packet_size, = struct.unpack("<I", self._receive_packet_buffer[0:4])
                # add the 4 bytes for the size to the packet size
                self._receive_packet_size = self._receive_packet_size + 4
            
            
                if len(self._receive_packet_buffer) >= self._receive_packet_size:
                    
                    self._receive_packet_container_index = 5
                    new_data = True
                   
            else:
                print("Error parsing multiple packets in receive buffer.  Clearing internal buffers.")
                _receive_packet_buffer = bytearray()
                
        return new_data



    # Parse out received containers
    def get_next_container(self):
        c = comm_modular_container()
        is_more_containers = False
    
        if (self._receive_packet_container_index > 0):
            c.container_size, = struct.unpack(">I", self._receive_packet_buffer[self._receive_packet_container_index:(self._receive_packet_container_index+4)])
            c.class_id, = struct.unpack(">I", self._receive_packet_buffer[(self._receive_packet_container_index+4):(self._receive_packet_container_index+8)])
            c.device_number, = struct.unpack(">I", self._receive_packet_buffer[(self._receive_packet_container_index+8):(self._receive_packet_container_index+12)])
            c.device_function = self._receive_packet_buffer[self._receive_packet_container_index+12]
            c.payload = bytearray(self._receive_packet_buffer[(self._receive_packet_container_index+c.BASE_CONTAINER_SIZE):(self._receive_packet_container_index+c.container_size)])
            
            self._receive_packet_container_index = self._receive_packet_container_index + c.container_size
            
            if (self._receive_packet_container_index >= self._receive_packet_size):
                
                is_more_containers = False
                
                if len(self._receive_packet_buffer) == self._receive_packet_size:
                    # The data buffer contains only the one packet.  Clear the buffer.
                    self._receive_packet_buffer = bytearray()
                else:
                    # Remove the packet from the data buffer.  There is another packet in the buffer already.
                    self._receive_packet_buffer = self._receive_packet_buffer[(self._receive_packet_container_index):(len(self._receive_packet_buffer))]
                    
                self._receive_packet_container_index = 0
                
            else:
                is_more_containers = True
                
    
        return c, is_more_containers   


    def wait_for_container(self, class_id, device_num, function_num):
       while(True):
            while (self.receive_new_data() == False):
                pass
                
            #print("DEBUG: Data received. Looking for class {}, device {}, function {}".format(class_id, device_num, function_num))
                
            more_containers = True
            
            while (more_containers):
                c, more_containers = self.get_next_container()
                
                #print("DEBUG: Container class {}, device {}, function {}".format(c.class_id, c.device_number, c.device_function))
                
                if c.class_id == class_id:
                    if c.device_number == device_num:
                        if c.device_function == function_num:
                            return c
                            
    def flush_receive(self):
        try:
            bytes_read = self._stream.receive(self._read_buffer, self._BUFFER_SIZE)
        except StreamError as e:
            if e.error_code == -34:
                # would block
                bytes_read = 0
            
    def destroy_all_spawned_actors(self):
        device_num = 0
        c = comm_modular_container()
        
        c.class_id = comm_modular_container.ID_GENERIC_ACTOR_SPAWNER
        c.device_number = device_num
        c.device_function = comm_modular_container.FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ALL_SPAWNED_ACTORS
        c.payload = bytearray()
        c.container_size = c.BASE_CONTAINER_SIZE + len(c.payload)        

        if (self.send_container(c)):
            #print("DEBUG: Container sent")
            c = self.wait_for_container(comm_modular_container.ID_GENERIC_ACTOR_SPAWNER, device_num, comm_modular_container.FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ALL_SPAWNED_ACTORS_ACK)
            
            return True
        
        else:
            return False
            
    def destroy_spawned_actor(self, ID, device_num):
        device_num = 0
        c = comm_modular_container()
        
        c.class_id = comm_modular_container.ID_GENERIC_ACTOR_SPAWNER
        c.device_number = device_num
        c.device_function = comm_modular_container.FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ACTOR
        c.payload = bytearray(struct.pack(">II", ID, device_num))
        
        c.container_size = c.BASE_CONTAINER_SIZE + len(c.payload)        

        if (self.send_container(c)):
            c = self.wait_for_container(comm_modular_container.ID_GENERIC_ACTOR_SPAWNER, device_num, comm_modular_container.FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ACTOR_ACK)
            
            return True
        
        else:
            return False            
            
    def spawn(self, device_num, ID, x, y, z, roll, pitch, yaw, sx, sy, sz, configuration=0, wait_for_confirmation=True):
        c = comm_modular_container()
        c.class_id = comm_modular_container.ID_GENERIC_ACTOR_SPAWNER
        c.device_number = 0
        c.device_function = comm_modular_container.FCN_GENERIC_ACTOR_SPAWNER_SPAWN
        c.payload = bytearray(struct.pack(">IIfffffffffI", ID, device_num, x, y, z, roll, pitch, yaw, sx, sy, sz, configuration))
        c.container_size = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if wait_for_confirmation:
            self.flush_receive()        
                
        if (self.send_container(c)):
        
            if wait_for_confirmation:
                c = self.wait_for_container(comm_modular_container.ID_GENERIC_ACTOR_SPAWNER, 0, comm_modular_container.FCN_GENERIC_ACTOR_SPAWNER_SPAWN_ACK)
                return c
            
            return True
        else:
            return False 
            
    def spawn_widget(self, widget_type, x, y, z, roll, pitch, yaw, sx, sy, sz, color_r, color_g, color_b, measured_mass, ID_tag, properties, wait_for_confirmation=True):
        c = comm_modular_container()
        c.class_id = comm_modular_container.ID_GENERIC_ACTOR_SPAWNER
        c.device_number = 0
        c.device_function = comm_modular_container.FCN_GENERIC_ACTOR_SPAWNER_SPAWN_WIDGET
        c.payload = bytearray(struct.pack(">IfffffffffffffBI", widget_type, x, y, z, roll, pitch, yaw, sx, sy, sz, color_r, color_g, color_b, measured_mass, ID_tag, len(properties)))
        c.payload = c.payload + bytearray(properties.encode('utf-8'))
        
        c.container_size = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if wait_for_confirmation:
            self.flush_receive()        
                
        if (self.send_container(c)):
        
            if wait_for_confirmation:
                c = self.wait_for_container(comm_modular_container.ID_GENERIC_ACTOR_SPAWNER, 0, comm_modular_container.FCN_GENERIC_ACTOR_SPAWNER_SPAWN_WIDGET_ACK)
                return c
            
            return True
        else:
            return False             
            
    def ping(self):
        c = comm_modular_container()
        c.class_id = comm_modular_container.ID_GENERIC_ACTOR_SPAWNER
        c.device_number = 0
        c.device_function = comm_modular_container.FCN_REQUEST_PING
        c.payload = bytearray()
        c.container_size = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        self.flush_receive()        
                
        if (self.send_container(c)):
        
            c = self.wait_for_container(comm_modular_container.ID_GENERIC_ACTOR_SPAWNER, 0, comm_modular_container.FCN_RESPONSE_PING)
            return True
        else:
            return False 
    
    def regenerate_cache_list(self):
        c = comm_modular_container()
        c.class_id = comm_modular_container.ID_GENERIC_ACTOR_SPAWNER
        c.device_number = 0
        c.device_function = comm_modular_container.FCN_GENERIC_ACTOR_SPAWNER_REGENERATE_CACHE_LIST
        c.payload = bytearray()
        c.container_size = c.BASE_CONTAINER_SIZE + len(c.payload)

        if (self.send_container(c)):
            c = self.wait_for_container(comm_modular_container.ID_GENERIC_ACTOR_SPAWNER, c.device_number, comm_modular_container.FCN_GENERIC_ACTOR_SPAWNER_REGENERATE_CACHE_LIST_ACK)
            
            return True
        
        else:
            return False
    
    def destroy_all_spawned_widgets(self):
        device_num = 0
        c = comm_modular_container()
        
        c.class_id = comm_modular_container.ID_GENERIC_ACTOR_SPAWNER
        c.device_number = device_num
        c.device_function = comm_modular_container.FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ALL_SPAWNED_WIDGETS
        c.payload = bytearray()
        c.container_size = c.BASE_CONTAINER_SIZE + len(c.payload)        

        if (self.send_container(c)):
            c = self.wait_for_container(comm_modular_container.ID_GENERIC_ACTOR_SPAWNER, device_num, comm_modular_container.FCN_GENERIC_ACTOR_SPAWNER_DESTROY_ALL_SPAWNED_WIDGETS_ACK)
            
            return True
        
        else:
            return False   
   
    def __del__(self):
        self.close()