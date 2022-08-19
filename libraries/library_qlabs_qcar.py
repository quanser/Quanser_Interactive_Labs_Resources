from library_qlabs_common import QLabsCommon
from library_qlabs import CommModularContainer

import math
import struct
import cv2
import numpy as np
        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsQCar:
    """This class is for spawning QCars."""
    
       
    ID_QCAR = 160 
    """ Class ID """
    FCN_QCAR_SET_VELOCITY_AND_REQUEST_STATE = 10
    FCN_QCAR_VELOCITY_STATE_RESPONSE = 11
    FCN_QCAR_SET_TRANSFORM_AND_REQUEST_STATE = 12
    FCN_QCAR_TRANSFORM_STATE_RESPONSE = 13
    FCN_QCAR_POSSESS = 20
    FCN_QCAR_POSSESS_ACK = 21
    FCN_QCAR_GHOST_MODE = 22
    FCN_QCAR_GHOST_MODE_ACK = 23
    FCN_QCAR_CAMERA_DATA_REQUEST = 100
    FCN_QCAR_CAMERA_DATA_RESPONSE = 101
    FCN_QCAR_LIDAR_DATA_REQUEST = 110
    FCN_QCAR_LIDAR_DATA_RESPONSE = 111
    
    
    CAMERA_CSI_RIGHT = 0
    CAMERA_CSI_BACK = 1
    CAMERA_CSI_LEFT = 2
    CAMERA_CSI_FRONT = 3
    CAMERA_RGB = 4
    CAMERA_DEPTH = 5
    CAMERA_OVERHEAD = 6
    """ Note: The mouse scroll wheel can be used to zoom in and out in this mode. """
    CAMERA_TRAILING = 7
    """ Note: The mouse scroll wheel can be used to zoom in and out in this mode. """
    
    # Initialize class
    def __init__(self):
        """ Constructor Method """
        return
       
    def spawn(self, qlabs, actorNumber, location, rotation, waitForConfirmation=True):
        """Spawns a QCar in an instance of QLabs at a specific location and rotation using radians.  Note that dynamics are enabled by default. Use set_transform_and_request_state to disable dynamics.

        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param location: An array of floats for x, y and z coordinates in full-scale units. Multiply physical QCar locations by 10 to get full scale locations.
        :param rotation: An array of floats for the roll, pitch, and yaw in radians
        :param waitForConfirmation: (Optional) Wait for confirmation of the spawn before proceeding. This makes the method a blocking operation.
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :type location: float array[3]
        :type rotation: float array[3]
        :type waitForConfirmation: boolean
        :return: 0 if successful, 1 class not available, 2 actor number not available or already in use, 3 unknown error, -1 communications error
        :rtype: int32


        """
        return QLabsCommon().spawn(qlabs, actorNumber, self.ID_QCAR, location, rotation, [1.0, 1.0, 1.0], 0, waitForConfirmation)
    
    def spawn_degrees(self, qlabs, actorNumber, location, rotation, waitForConfirmation=True):
        """Spawns a QCar in an instance of QLabs at a specific location and rotation using degrees. Note that dynamics are enabled by default. Use set_transform_and_request_state to disable dynamics.

        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param location: An array of floats for x, y and z coordinates in full-scale units. Multiply physical QCar locations by 10 to get full scale locations.
        :param rotation: An array of floats for the roll, pitch, and yaw in degrees
        :param waitForConfirmation: (Optional) Wait for confirmation of the spawn before proceeding. This makes the method a blocking operation.
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :type location: float array[3]
        :type rotation: float array[3]
        :type waitForConfirmation: boolean
        :return: 0 if successful, 1 class not available, 2 actor number not available or already in use, 3 unknown error, -1 communications error
        :rtype: int32


        """        
        return QLabsCommon().spawn(qlabs, actorNumber, self.ID_QCAR,  location, [rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi], [1.0, 1.0, 1.0], 0, waitForConfirmation)
    
    
    def set_transform_and_request_state(self, qlabs, actorNumber, location, rotation, enableDynamics, headlights, leftTurnSignal, rightTurnSignal, brakeSignal, reverseSignal, waitForConfirmation=True):
        """Sets the location, rotation, and other car properties. Note that setting the location ignores collisions so ensure that the location is free of obstacles that may trap the actor if it is subsequently used in a dynamic mode. This transform can also be used to "playback" previously recorded position data without the need for a full dynamic model.

        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param location: An array of floats for x, y and z coordinates in full-scale units. Multiply physical QCar locations by 10 to get full scale locations.
        :param rotation: An array of floats for the roll, pitch, and yaw in radians
        :param enableDynamics: (default True) Enables or disables gravity for set transform requests.
        :param headlights: Enable the headlights
        :param leftTurnSignal: Enable the left turn signal
        :param rightTurnSignal: Enable the right turn signal
        :param brakeSignal: Enable the brake lights (does not affect the motion of the vehicle)
        :param reverseSignal: Play a honking sound
        :param waitForConfirmation: (Optional) Wait for confirmation of the spawn before proceeding. This makes the method a blocking operation.
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :type location: float array[3]
        :type rotation: float array[3]
        :type enableDynamics: boolean
        :type headlights: boolean
        :type leftTurnSignal: boolean
        :type rightTurnSignal: boolean
        :type brakeSignal: boolean
        :type reverseSignal: boolean
        :type waitForConfirmation: boolean
        :return: True if successful or False otherwise, location in full scale, rotation in radians, unit forward vector, unit up vector, front bumper hit, rear bumper hit. Data only valid if waitForConfirmation=True.
        :rtype: boolean, float array[3], float array[3], float array[3], float array[3], boolean, boolean

        """ 
        c = CommModularContainer()
        c.classID = self.ID_QCAR
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_QCAR_SET_TRANSFORM_AND_REQUEST_STATE
        c.payload = bytearray(struct.pack(">ffffffBBBBBB", location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], enableDynamics, headlights, leftTurnSignal, rightTurnSignal, brakeSignal, reverseSignal))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        

        location = [0,0,0]
        rotation = [0,0,0]
        forward_vector = [0,0,0]
        up_vector = [0,0,0]
        frontHit = False
        rearHit = False

        if waitForConfirmation:
            qlabs.flush_receive()

        if (qlabs.send_container(c)):
            if waitForConfirmation:
                c = qlabs.wait_for_container(self.ID_QCAR, actorNumber, self.FCN_QCAR_TRANSFORM_STATE_RESPONSE)
                if len(c.payload) == 50:
                    
                    location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], forward_vector[0], forward_vector[1], forward_vector[2], up_vector[0], up_vector[1], up_vector[2], frontHit, rearHit, = struct.unpack(">ffffffffffff??", c.payload[0:50])
                    return True, location, rotation, forward_vector, up_vector, frontHit, rearHit  
                else:
                    return False, location, rotation, forward_vector, up_vector, frontHit, rearHit 
            else:
                return True, location, rotation, forward_vector, up_vector, frontHit, rearHit  
        else:
            return False, location, rotation, forward_vector, up_vector, frontHit, rearHit  

    def set_transform_and_request_state_degrees(self, qlabs, actorNumber, location, rotation, enableDynamics, headlights, leftTurnSignal, rightTurnSignal, brakeSignal, reverseSignal, waitForConfirmation=True):
        """Sets the location, rotation, and other car properties. Note that setting the location ignores collisions so ensure that the location is free of obstacles that may trap the actor if it is subsequently used in a dynamic mode. This transform can also be used to "playback" previously recorded position data without the need for a full dynamic model.

        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param location: An array of floats for x, y and z coordinates in full-scale units. Multiply physical QCar locations by 10 to get full scale locations.
        :param rotation: An array of floats for the roll, pitch, and yaw in degrees
        :param enableDynamics: (default True) Enables or disables gravity for set transform requests.
        :param headlights: Enable the headlights
        :param leftTurnSignal: Enable the left turn signal
        :param rightTurnSignal: Enable the right turn signal
        :param brakeSignal: Enable the brake lights (does not affect the motion of the vehicle)
        :param reverseSignal: Play a honking sound
        :param waitForConfirmation: (Optional) Wait for confirmation of the spawn before proceeding. This makes the method a blocking operation.
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :type location: float array[3]
        :type rotation: float array[3]
        :type enableDynamics: boolean
        :type headlights: boolean
        :type leftTurnSignal: boolean
        :type rightTurnSignal: boolean
        :type brakeSignal: boolean
        :type reverseSignal: boolean
        :type waitForConfirmation: boolean
        :return: True if successful or False otherwise, location in full scale, rotation in degrees, unit forward vector, unit up vector, front bumper hit, rear bumper hit. Data only valid if waitForConfirmation=True.
        :rtype: boolean, float array[3], float array[3], float array[3], float array[3], boolean, boolean

        """ 
        success, location, rotation, forward_vector, up_vector, frontHit, rearHit = self.set_transform_and_request_state(qlabs, actorNumber, location, [rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi], enableDynamics, headlights, leftTurnSignal, rightTurnSignal, brakeSignal, reverseSignal, waitForConfirmation)
        rotation_deg = [rotation[0]/math.pi*180, rotation[1]/math.pi*180, rotation[2]/math.pi*180]

        return success, location, rotation_deg, forward_vector, up_vector, frontHit, rearHit
            
    def set_velocity_and_request_state(self, qlabs, actorNumber, forward, turn, headlights, leftTurnSignal, rightTurnSignal, brakeSignal, reverseSignal):
        """Sets the location, rotation, and other car properties. Note that setting the location ignores collisions so ensure that the location is free of obstacles that may trap the actor. This transform can also be used to "playback" previously recorded position data without the need for a full dynamic model.

        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param forward: Speed in m/s of a full-scale car. Multiply physical QCar speeds by 10 to get full scale speeds.
        :param turn: Turn angle in radians. Positive values turn right.
        :param headlights: Enable the headlights
        :param leftTurnSignal: Enable the left turn signal
        :param rightTurnSignal: Enable the right turn signal
        :param brakeSignal: Enable the brake lights (does not affect the motion of the vehicle)
        :param reverseSignal: Play a honking sound
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :type actorNumber: float
        :type turn: float
        :type enableDynamics: boolean
        :type headlights: boolean
        :type leftTurnSignal: boolean
        :type rightTurnSignal: boolean
        :type brakeSignal: boolean
        :type reverseSignal: boolean
        :return: True or False if successful, location, rotation in radians, front bumper hit, rear bumper hit
        :rtype: boolean, float array[3], float array[3], boolean, boolean


        """ 
        c = CommModularContainer()
        c.classID = self.ID_QCAR
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_QCAR_SET_VELOCITY_AND_REQUEST_STATE
        c.payload = bytearray(struct.pack(">ffBBBBB", forward, turn, headlights, leftTurnSignal, rightTurnSignal, brakeSignal, reverseSignal))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        location = [0,0,0]
        rotation = [0,0,0]
        frontHit = False
        rearHit = False
        

        qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            c = qlabs.wait_for_container(self.ID_QCAR, actorNumber, self.FCN_QCAR_VELOCITY_STATE_RESPONSE)
            if len(c.payload) == 26:
                location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], frontHit, rearHit, = struct.unpack(">ffffff??", c.payload[0:26])
                return True, location, rotation, frontHit, rearHit  
            else:
                return False, location, rotation, frontHit, rearHit  
        else:
            return False, location, rotation, frontHit, rearHit  
            

    def set_velocity_and_request_state_degrees(self, qlabs, actorNumber, forward, turn, headlights, leftTurnSignal, rightTurnSignal, brakeSignal, reverseSignal):
        """Sets the location, rotation, and other car properties. Note that setting the location ignores collisions so ensure that the location is free of obstacles that may trap the actor. This transform can also be used to "playback" previously recorded position data without the need for a full dynamic model.

        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param forward: Speed in m/s of a full-scale car. Multiply physical QCar speeds by 10 to get full scale speeds.
        :param turn: Turn angle in degrees. Positive values turn right.
        :param headlights: Enable the headlights
        :param leftTurnSignal: Enable the left turn signal
        :param rightTurnSignal: Enable the right turn signal
        :param brakeSignal: Enable the brake lights (does not affect the motion of the vehicle)
        :param reverseSignal: Play a honking sound
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :type actorNumber: float
        :type turn: float
        :type enableDynamics: boolean
        :type headlights: boolean
        :type leftTurnSignal: boolean
        :type rightTurnSignal: boolean
        :type brakeSignal: boolean
        :type reverseSignal: boolean
        :return: True or False if successful, location, rotation in degrees, front bumper hit, rear bumper hit
        :rtype: boolean, float array[3], float array[3], boolean, boolean


        """ 
        success, location, rotation, frontHit, rearHit = self.set_velocity_and_request_state(qlabs, actorNumber, forward, turn/180*math.pi, headlights, leftTurnSignal, rightTurnSignal, brakeSignal, reverseSignal)

        rotation_deg = [rotation[0]/math.pi*180, rotation[1]/math.pi*180, rotation[2]/math.pi*180]
        return success, location, rotation_deg, frontHit, rearHit 
            
    def possess(self, qlabs, actorNumber, camera=CAMERA_TRAILING):
        """
        Possess (take control of) a QCar in QLabs with the selected camera.
        
        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param camera: Pre-defined camera constant. See CAMERA constants for available options. Default is the trailing camera.
        :type qlabs: object
        :type actorNumber: uint32
        :type camera: uint32
        :return: `True` if possessing the camera was successful, `False` otherwise
        :rtype: boolean

        """

        c = CommModularContainer()
        c.classID = self.ID_QCAR
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_QCAR_POSSESS
        c.payload = bytearray(struct.pack(">B", camera))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            c = qlabs.wait_for_container(self.ID_QCAR, actorNumber, self.FCN_QCAR_POSSESS_ACK)
                    
            return True
        else:
            return False    

    def ghost_mode(self, qlabs, actorNumber, enable=True, colour=[0,1,0]):
        """
        Ghost mode changes the selected QCar actor into a transparent coloured version. This can be useful as a reference actor or indicating a change in state.
        
        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param enable: Set the QCar to the defined transparent colour, otherwise revert to the solid color scheme.
        :param colour: Red, Green, Blue components of the RGB color on a 0.0 to 1.0 scale.
        :type qlabs: object
        :type actorNumber: uint32
        :type camera: uint32
        :type enable: boolean
        :type colour: float array[3]
        :return: `True` if successful, `False` otherwise
        :rtype: boolean

        """

        c = CommModularContainer()
        c.classID = self.ID_QCAR
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_QCAR_GHOST_MODE
        c.payload = bytearray(struct.pack(">Bfff", enable, colour[0], colour[1], colour[2]))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            c = qlabs.wait_for_container(self.ID_QCAR, actorNumber, self.FCN_QCAR_GHOST_MODE_ACK)
                    
            return True
        else:
            return False             

    def get_image(self, qlabs, actorNumber, camera):   
        """
        Request a JPG image from one of the QCar cameras.
        
        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param camera: Pre-defined camera constant. See CAMERA constants for available options. Trailing and Overhead cameras cannot be selected.
        :type qlabs: object
        :type actorNumber: uint32
        :type camera: uint32
        :return: `True` and image data if successful, `False` and empty otherwise
        :rtype: boolean, byte array with jpg data

        """        
    
        c = CommModularContainer()
        c.classID = self.ID_QCAR
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_QCAR_CAMERA_DATA_REQUEST
        c.payload = bytearray(struct.pack(">I", camera))
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            c = qlabs.wait_for_container(self.ID_QCAR, actorNumber, self.FCN_QCAR_CAMERA_DATA_RESPONSE)
            jpg_buffer = cv2.imdecode(np.frombuffer(bytearray(c.payload[8:len(c.payload)]), dtype=np.uint8, count=-1, offset=0), 1)
            
            
            return True, jpg_buffer
        else:
            return False, None
            
    def get_lidar(self, qlabs, actorNumber, samplePoints=400):   
        """
        Request LIDAR data from a QCar.
        
        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :param samplePoints: (Optional) Change the number of points per revolution of the LIDAR.
        :type qlabs: object
        :type actorNumber: uint32
        :type samplePoints: uint32
        :return: `True`, angles in radians, and distances in m if successful, `False`, none, and none otherwise
        :rtype: boolean, float array, float array

        """        
        LIDAR_SAMPLES = 4096
        LIDAR_RANGE = 80
        
        # The LIDAR is simulated by using 4 orthogonal virtual cameras that are 1 pixel high. The
        # lens distortion of these cameras must be removed to accurately calculate the XY position
        # of the depth samples.
        quarter_angle = np.linspace(0, 45, int(LIDAR_SAMPLES/8))
        lens_curve = -0.0077*quarter_angle*quarter_angle + 1.3506*quarter_angle
        lens_curve_rad = lens_curve/180*np.pi
    
        angles = np.concatenate((np.pi*4/2-1*np.flip(lens_curve_rad), \
                                 lens_curve_rad, \
                                 (np.pi/2 - 1*np.flip(lens_curve_rad)), \
                                 (np.pi/2 + lens_curve_rad), \
                                 (np.pi - 1*np.flip(lens_curve_rad)), \
                                 (np.pi + lens_curve_rad), \
                                 (np.pi*3/2 - 1*np.flip(lens_curve_rad)), \
                                 (np.pi*3/2 + lens_curve_rad)))


   
        c = CommModularContainer()
        c.classID = self.ID_QCAR
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_QCAR_LIDAR_DATA_REQUEST
        c.payload = bytearray()
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            c = qlabs.wait_for_container(self.ID_QCAR, actorNumber, self.FCN_QCAR_LIDAR_DATA_RESPONSE)
            
            if ((len(c.payload)-4)/2 != LIDAR_SAMPLES):
                print("Received {} bytes, expected {}".format(len(c.payload), LIDAR_SAMPLES*2))
                return False, None, None

            distance = np.linspace(0,0,LIDAR_SAMPLES)
            
            LidarAngle = np.linspace(-math.pi/4,math.pi/4, int(LIDAR_SAMPLES/4));

            
            for count in range(LIDAR_SAMPLES-1):
                distance[count] = (c.payload[4+count*2] * 256 + c.payload[5+count*2] )/65535*LIDAR_RANGE             


            # Resample the data using a linear radial distribution to the desired number of points
            # and realign the first index to be 0 (forward)
            sampled_angles = np.linspace(0,2*np.pi, num=samplePoints, endpoint=False)
            sampled_distance = np.linspace(0,0, samplePoints)
            
            index_raw = 512
            for count in range(samplePoints):
                while (angles[index_raw] < sampled_angles[count]):
                    index_raw = (index_raw + 1) % 4096
                
                    
                if index_raw != 0:
                    if (angles[index_raw]-angles[index_raw-1]) == 0:
                        sampled_distance[count] = distance[index_raw]
                    else:
                        sampled_distance[count] = (distance[index_raw]-distance[index_raw-1])*(sampled_angles[count]-angles[index_raw-1])/(angles[index_raw]-angles[index_raw-1]) + distance[index_raw-1]
                        
                    
                else:
                    sampled_distance[count] = distance[index_raw]
                    
                    
            return True, sampled_angles, sampled_distance
        else:
            return False, None, None            
            

    def destroy(self, qlabs, actorNumber):
        """Destroys a QCar in an instance of QLabs.

        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :return: The number of actors destroyed. -1 if failed.
        :rtype: int32

        """
        return QLabsCommon().destroy_spawned_actor(qlabs, self.ID_QCAR, actorNumber)


    def ping(self, qlabs, actorNumber):
        """Checks if a QCar of the corresponding actor number exists in the QLabs environment.

        :param qlabs: A QuanserInteractiveLabs object
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :return: `True` if actor is present, `False` otherwise
        :rtype: boolean

        """
        return QLabsCommon().ping_actor(qlabs, actorNumber, self.ID_QCAR)

    def get_world_transform(self, qlabs, actorNumber):
        """Get the location, rotation, and scale in world coordinates of the QCar
        
        :param qlabs: A QuanserInteractiveLabs object.
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :return: success, location, rotation in radians
        :rtype: boolean, float array[3], float array[3]
        """    
        success, location, rotation, scale = QLabsCommon().get_world_transform(qlabs, actorNumber, self.ID_QCAR)

        return  success, location, rotation

    def get_world_transform_degrees(self, qlabs, actorNumber):
        """Get the location, rotation, and scale in world coordinates of the QCar
        
        :param qlabs: A QuanserInteractiveLabs object.
        :param actorNumber: User defined unique identifier for the class actor in QLabs
        :type qlabs: QuanserInteractiveLabs object
        :type actorNumber: uint32
        :return: success, location, rotation in degrees
        :rtype: boolean, float array[3], float array[3]
        """    
        success, location, rotation, scale = QLabsCommon().get_world_transform(qlabs, actorNumber, self.ID_QCAR)
        rotation_deg = rotation_deg = [rotation[0]/math.pi*180, rotation[1]/math.pi*180, rotation[2]/math.pi*180]

        return  success, location, rotation_deg
        