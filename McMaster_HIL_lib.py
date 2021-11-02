from quanser.communications import Stream, StreamError, PollFlag, Timeout
from quanser.common import GenericError
from quanser.hardware import HIL, HILError, PWMMode, MAX_STRING_LENGTH
import math
import numpy as np
import sys
import time
import cv2
import os
sys.path.append('../Common/')



########################################################################
######################### VIRTUAL QBOT CLASSES ######################### 
########################################################################





########################################################################
####################### (VIRTUAL) QARM CLASSES ######################### 
########################################################################

############################## NEW QARM ################################
class QArm:

    # Define class-level variables 
    base = 0
    shoulder = 0
    elbow = 0
    wrist = 0
    gripper = 0
    contact = 0
    contact_id = 0
    static_environment_collision = 0
    finger_pad_detection_right_proximal = 0
    finger_pad_detection_right_distal = 0
    finger_pad_detection_left_proximal = 0
    finger_pad_detection_left_distal = 0
    
    _dev_num = 0

    # Manipulator parameters in meters:
    _L1 = 0.127
    _L2 = 0.3556
    _L3 = 0.4064

    # Define joint angle (in deg) and gripper limits
    _qarm_base_upper_lim = 175
    _qarm_base_lower_lim = -175
    _qarm_shoulder_upper_limit = 90
    _qarm_shoulder_lower_limit = -90
    _qarm_elbow_upper_limit = 90
    _qarm_elbow_lower_limit = -80
    _qarm_wrist_upper_limit = 170
    _qarm_wrist_lower_limit = -170
    _qarm_gripper_upper_limit = 1
    _qarm_gripper_lower_limit = 0
    
    # Define base LED color
    _base_color_r = 1
    _base_color_g = 0
    _base_color_b = 0
        
    _arm_brightness = 1 
    
    _err_lim = 0.05
        
    image_rgb = None
    image_depth = None
    
    #region: Channel and Buffer definitions
    # Other Writes 
    write_other_channels = np.array([1000, 1001, 1002, 1003, 1004, 11000, 11001, 11002, 11003], dtype=np.int32)
    write_other_buffer = np.zeros(9, dtype=np.float64)
    write_LED_channels = np.array([11005, 11006, 11007], dtype=np.int32)
    write_LED_buffer = np.array([1,0,0], dtype=np.float64)

    # Other Reads
    read_other_channels = np.array([1000, 1001, 1002, 1003, 1004, 3000, 3001, 3002, 3003, 3004, 10000, 10001, 10002, 10003, 10004, 11000, 11001, 11002, 11003, 11004], dtype=np.int32)
    read_other_buffer = np.zeros(20, dtype=np.float64)
    
    # User LEDs Write Only - Other channel 11004:11007 are User LEDs
    read_analog_channels = np.array([5, 6, 7, 8, 9], dtype=np.int32)
    read_analog_buffer = np.zeros(5, dtype=np.float64)

    measJointCurrent = np.zeros(5, dtype=np.float64)
    measJointPosition = np.zeros(5, dtype=np.float64)
    measJointSpeed = np.zeros(5, dtype=np.float64)
    measJointPWM= np.zeros(5, dtype=np.float64)
    measJointTemperature = np.zeros(5, dtype=np.float64)    
    status = False
    #endregion
    
    # Initilize QuanserSim
    def __init__(self, device_num, QArm_hostname, hardware = False):
    
        self._dev_num = device_num
        self.mode = 0 # Only Position Mode is tested and available in Python
        self.card = HIL()
        
        print("HIL initialized")

        board_identifier = "{}@tcpip://{}:18900?nagle='off'".format(int(self._dev_num), QArm_hostname)

        if (hardware==True):
            board_identifier = str(self._dev_num)

        board_specific_options = "j0_mode=0;j1_mode=0;j2_mode=0;j3_mode=0;gripper_mode=0;"

        try:
            # Open the Card
            self.card.open("qarm_usb", board_identifier)
            if self.card.is_valid():
                self.card.set_card_specific_options(board_specific_options, MAX_STRING_LENGTH)
                self.status = True

                print('QArm configured in Position Mode.')
        
        except HILError as h:
            print(h.get_error_message())  
        print ("QArm initialized")

    # Set base LED color; color is an array of 3 elements of [r, g, b]; element values from 0-1
    def set_base_color (self, color=[1, 0, 0]):
        
        self.write_LED_buffer = np.array(color, dtype=np.float64)
       
        # IO
        try:
            if True:
                #Writes: Analog Channel, Num Analog Channel, PWM Channel, Num PWM Channel, Digital Channel, Num Digital Channel, Other Channel, Num Other Channel, Analog Buffer, PWM Buffer, Digital Buffer, Other Buffer           
                self.card.write(None, 0, None, 0, None, 0, self.write_LED_channels, 3, 
                                None, None, None, self.write_LED_buffer)  

        except HILError as h:
            print(h.get_error_message())

        finally:
            pass     
        
    def return_home(self):
        self.qarm_move(0, 0, 0, 0, 0)
    
    # All angles in rads
    def qarm_move(self, base, shoulder, elbow, wrist, gripper, wait = True):
        
        self.write_other_buffer[0:4] = np.array([base, shoulder, elbow, wrist], dtype=np.float64)
        grpCMD = np.maximum(0.1, np.minimum(gripper, 0.9))
        self.write_other_buffer[4] = grpCMD
        
        self.write_all_arm_joints() 
        
        if (wait == True):
            reached = False
            count = 0
            while not reached and not count > 100:
                b, s, e, w, g = self.read_all_arm_joints()
                #errors = (abs(b - base), abs(s - shoulder), abs(e - elbow), abs(w - wrist), abs(g - grpCMD))
                if ((abs(b - base) < self._err_lim) and (abs(s - shoulder) < self._err_lim) and (abs(e - elbow) < self._err_lim) and (abs(w - wrist) < self._err_lim) and (abs(g - grpCMD) < self._err_lim)):
                    reached = True
                else:
                    time.sleep(0.1)
                    count = count + 1
                    #print(errors)
            return b, s, e, w, g 
        return 0
        
    def qarm_move_gripper(self, gripper, wait = True):
        grpCMD = np.maximum(0.1, np.minimum(gripper, 0.9))
        self.write_other_buffer[4] = grpCMD
        
        self.write_all_arm_joints() 
        
        if (wait == True):
            reached = False
            while not reached:
                b, s, e, w, g = self.read_all_arm_joints()
                if ((abs(g - grpCMD) < self._err_lim)):
                    reached = True
                else:
                    time.sleep(0.1)
            return g        
        return 0

    def read_all_arm_joints(self):
        self.card.read(None, 0, None, 0, None, 0, self.read_other_channels, 20, None, None, None, self.read_other_buffer)
        b, s, e, w, g = self.read_other_buffer[0:5]
        return b, s, e, w, g
        
    def write_all_arm_joints(self):
        try:
            self.card.write(None, 0, None, 0, None, 0, self.write_other_channels, 9, 
                    None, None, None, self.write_other_buffer)
                
        except HILError as h:
            print(h.get_error_message())   
        
        finally: 
            pass

    def terminate(self):
        ''' This function terminates the QArm card after setting final values for home position and 0 pwm.'''
        
        self.set_base_color([1, 0, 0]) 
        self.write_other_buffer = np.zeros(9, dtype=np.float64)
        
        try:    
            self.card.write(None, 0, None, 0, None, 0, self.write_other_channels, 9, 
                                 None, None, None, self.write_other_buffer)
            self.card.close()
            print('QArm terminated successfully.')
            
        except HILError as h:
            print(h.get_error_message())
            
    def close(self):
        self.terminate()
     
    # Check if given joint angles and gripper value are within acceptable limit
    # Return 1 if withing bound, 0 otherwise
    def angles_within_bound (self, qarm_base, qarm_shoulder, qarm_elbow, qarm_wrist, qarm_gripper):
        if qarm_base > self._qarm_base_upper_lim or qarm_base < self._qarm_base_lower_lim or \
                qarm_shoulder > self._qarm_shoulder_upper_limit or qarm_shoulder < self._qarm_shoulder_lower_limit or \
                qarm_elbow > self._qarm_elbow_upper_limit or qarm_elbow < self._qarm_elbow_lower_limit or \
                qarm_wrist > self._qarm_wrist_upper_limit or qarm_wrist < self._qarm_wrist_lower_limit or \
                qarm_gripper > self._qarm_gripper_upper_limit or qarm_gripper < self._qarm_gripper_lower_limit:
            return 0
        else:
            return 1

    # Check if given end-effector coordinates are within bounds
    # Return 1 if withing bound, 0 otherwise
    def coordinates_within_bound(self, p_x, p_y, p_z):
        R = math.sqrt(p_x ** 2 + p_y ** 2)

        # Vertical offset within the verical plane from Frame 1 to End-Effector
        # Note: Frame 1 y-axis points downward (negative global Z-axis direction)
        Z = self._L1 - p_z

        # Distance from Frame 1 to End-Effector Frame
        Lambda = math.sqrt(R ** 2 + Z ** 2)

        if Lambda > (self._L2 + self._L3) or p_z < 0:
            return 0
        else:
            return 1


        
        
########################################################################
######################## VIRTUAL EMG CLASSES ########################### 
########################################################################

######################### EMG SIM #############################

class EMGSim:

    # Define class-level variables 
    
    image_width = 700
    image_height = 224
    
    _emgLeft = 0.0
    _emgRight = 0.0
    _imgHead = cv2.imread('../Common/HeadOutline.png')
    _imgFlexSheet = cv2.imread('../Common/FlexAnimSpriteSheet.png')
    _imgFlexArray = np.zeros((200, 300, 3, 13), dtype=np.uint8)
    _imgBGnd = np.full((image_height, image_width, 3), (255, 255, 255), dtype=np.uint8)
    
    
    ##--------------- VIRTUAL EMG METHODS ----------------------- 
    
    # Callback fcn for left slider
    def _on_change_Left(self, left):
        self._emgLeft = left / 100.0
        self._updateEMGImage()
        
    # Callback fcn for right slider
    def _on_change_Right(self, right):
        self._emgRight = right / 100.0
        self._updateEMGImage()
    
    # Read EMG values and check for inputs
    def readEMG(self):
        cv2.waitKey(1)
        return (self._emgLeft, self._emgRight)
        
    def EMG_right(self):
        cv2.waitKey(1)
        return self._emgRight
        
    def EMG_left(self):
        cv2.waitKey(1)
        return self._emgLeft
    
    # Draw the flexing guy
    def _updateEMGImage(self):
        imgComp = self._imgBGnd
        imgComp[24:224, :300, :] = self._imgFlexArray[:, :, :, int(self._emgLeft * 12)]
        imgComp[24:224, (self.image_width - 300):, :] = cv2.flip(self._imgFlexArray[:, :, :, int(self._emgRight * 12)], 1)
        imgComp[:170, 268:438, :] = cv2.bitwise_and(imgComp[:170, 268:438, :], self._imgHead)
        cv2.imshow("Myo Sim", imgComp)
        return None
    
    # Close window
    def close(self):
        cv2.destroyWindow("Myo Sim")
        return None
                
    # Initilize EMG sensor
    def __init__(self):
        for i in range(13):
            self._imgFlexArray[:, :, :, i] = self._imgFlexSheet[(200*i):(200*(i+1)), :300, :]
        cv2.imshow("Myo Sim", self._imgBGnd)
        cv2.createTrackbar("Left (%)", "Myo Sim", 0, 100, self._on_change_Left)
        cv2.createTrackbar("Right (%)", "Myo Sim", 0, 100, self._on_change_Right)
        self._updateEMGImage()
        cv2.waitKey(1)
        print ("Virtual EMG initialized")
        return None

