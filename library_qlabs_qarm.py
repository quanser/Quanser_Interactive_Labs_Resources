from library_qlabs import QuanserInteractiveLabs, CommModularContainer
from quanser.common import GenericError
import math

import sys
import struct
import os
        
sys.path.append('../Common/')
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsQArm:

       
    ID_QARM = 10
    
    # Initialize class
    def __init__(self):

       return
       
    def spawn(self, qlabs, deviceNumber, location, rotation, configuration=0, waitForConfirmation=True):
        return qlabs.spawn(deviceNumber, self.ID_QARM, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], 1.0, 1.0, 1.0, configuration, waitForConfirmation)
   
    def spawnDegrees(self, qlabs, deviceNumber, location, rotation, configuration=0, waitForConfirmation=True):
        
        return qlabs.spawn(deviceNumber, self.ID_QARM, location[0], location[1], location[2], rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi, 1.0, 1.0, 1.0, configuration, waitForConfirmation)
 
    def start_RT_model(self, device_num=0, RT_hostname='localhost', UE_hostname='localhost'):
        #cmd_string="quarc_run -D -r -t tcpip://localhost:17000 QArm_Spawn.rt-linux_pi_3 -uri tcpip://localhost:17002 -hostname {} -devicenum {}".format(QLabs_hostname, device_num)
        cmd_string=f'start "QArm_Spawn_Model" "%QUARC_DIR%\quarc_run" -D -r -t tcpip://{RT_hostname}:17000 QArm_Spawn.rt-win64 -hostname {UE_hostname} -devicenum {device_num}'
        os.system(cmd_string)
        return cmd_string
        
    def terminate_RT_model(self, RT_hostname='localhost'):
        #cmd_string="quarc_run -q -Q -t tcpip://localhost:17000 QArm_Spawn.rt-linux_pi_3".format()
        cmd_string=f'start "QArm_Spawn_Model" "%QUARC_DIR%\quarc_run" -q -t tcpip://{RT_hostname}:17000 QArm_Spawn.rt-win64'
        os.system(cmd_string)
        return cmd_string
        