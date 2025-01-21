import json
import sys
import os
import time
import numpy as np
from quanser.hardware import HIL, HILError, MAX_STRING_LENGTH, Clock
from pal.utilities.vision import Camera3D
from qvl.actor import QLabsActor
import shutil
from qvl.real_time import QLabsRealTime
from qvl.qlabs import QuanserInteractiveLabs
from qvl.qarm import QLabsQArm
from qvl.qcar2 import QLabsQCar2
from qvl.qbot_platform import QLabsQBotPlatform
from qvl.qdrone2 import QLabsQDrone2


class MultiAgent():

    # location of RT models and creation of new MultiAgent folder
    __qalDirPath = os.environ['RTMODELS_DIR']
    
    _QArmDir = os.path.normpath(
        os.path.join(__qalDirPath, 'QArm'))
    _QCar2Dir = os.path.normpath(
        os.path.join(__qalDirPath, 'QCar2'))
    _QBPDir = os.path.normpath(
        os.path.join(__qalDirPath, 'QBotPlatform'))
    _QBPDriverDir = os.path.normpath(
        os.path.join(__qalDirPath, 'QBotPlatforms'))
    _QD2Dir = os.path.normpath(
        os.path.join(__qalDirPath, 'QDrone2'))
    _directory = os.path.normpath(
        os.path.join(__qalDirPath, 'MultiAgent'))

    def __init__(self, agentList, spawnAfter = False, sendActor = False):

        # agentList is a list of dictionaries with the following keys
        #"RobotType": (string, can be "QC2"or"QCar2" /"QBP"/ "QArm"or"QA" /"QDrone2"or"QD2") 
        #"Location": for spawning in x,y,z of the QLabs environment
        #"Rotation": for spawning, in x,y,z. Can be in Degrees or Radians, if it is radians, set the "Radians" key to true. If not defined, will spawn with [0, 0, 0] rotation
        #"Radians" : True  # Only needed if rotation is in Radians
        #"Scale": (float) if you want to change the scaling of the spawned object, if not defined, will spawn with scaling of 1
        #"actorNumber" : 9 , set only if you want a predefined actor number for your robot. If not, it will use the next available number for the type of robot. If the number 
        # is already in use, it will overwrite it. We recommend not using it unless tracking of actors is done manually by the user.

        self.qlabs = QuanserInteractiveLabs()
        print("Connecting to QLabs...")
        if (not self.qlabs.open("localhost")):
            print("Unable to connect to QLabs")   

        print("Connected")

        cmd = QLabsRealTime().terminate_all_real_time_models()
        print(cmd)
        time.sleep(1)
        cmd = QLabsRealTime().terminate_all_real_time_models()
        print(cmd)
        time.sleep(1)
        # QLabsRealTime().terminate_all_real_time_models()
        # time.sleep(1)

        #self.qlabs.destroy_all_spawned_actors()

        QLabsQArm(self.qlabs).destroy_all_actors_of_class()
        QLabsQCar2(self.qlabs).destroy_all_actors_of_class()
        QLabsQBotPlatform(self.qlabs).destroy_all_actors_of_class()
        QLabsQDrone2(self.qlabs).destroy_all_actors_of_class()
        
        # x = self.qlabs.destroy_all_spawned_actors()

        # print(x)
        

        self._fileType = '.rt-win64' # will need a check once we have multiple OS support
        self._portNumber = 18799
        self._uriPortNumber = 17010
        self._driverPortNumber = 18949 

        created = self._createMultiAgentDir()

        time.sleep(.5)
        # if not created:
        #     print ('Directory not created successfully. Aborting.')
        #     return []
        
        if not sendActor:
            # remove robot if not RobotType or Location defined
            for robot in agentList[:]:
                if "RobotType" not in robot:
                    agentList.remove(robot)
                    print("Removed the following entry due to no RobotType defined:")
                    print(robot)
                if "Location" not in robot:
                    agentList.remove(robot)
                    print("Removed the following entry due to no Location defined:")
                    print(robot)

            # fill empty rotation, radians and scaling if not defined
            for robot in agentList:
                if "Rotation" not in robot:
                    # If "Rotation" is not defined, set it to the default value
                    robot["Rotation"] = [0,0,0]
                if "Radians" not in robot:
                    # If "Radians" is not defined, set it to the default value of False
                    robot["Radians"] = False
                if "Scale" not in robot:
                    # If "Scaling" is not defined, set it to the default value
                    robot["Scale"] = 1
            
            robotActors = self._spawnRobots(agentList)

            #print("FinishSpawn")

        self.robotActors = robotActors

        robotsDict = {}

        for robot in robotActors:
            name, robotDict = self.createRobot(robot)
            #print(robotDict)
            robotsDict[name] = robotDict

        filePath = os.path.join(MultiAgent._directory,"RobotAgents.json")
        with open(filePath, "w") as outfile: 
            json.dump(robotsDict, outfile)

        
    def _createMultiAgentDir(self):
        try:
            os.mkdir(MultiAgent._directory)
            print(f"Directory '{MultiAgent._directory}' created successfully.")
            return True
        except FileExistsError:
            print(f"Deleting existing directory '{MultiAgent._directory}'...")
            shutil.rmtree(MultiAgent._directory)
            os.mkdir(MultiAgent._directory)
            print(f"Directory '{MultiAgent._directory}' created successfully.")
            return True
        except PermissionError:
            print(f"Permission denied: Unable to create '{MultiAgent._directory}'.")
            return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
      
    def _spawnRobots(self, agentList):
        robotActors = [0] * len(agentList)
        x = 0
        for robot in agentList:
            qlabsRobot = 0

            if robot["RobotType"] == "QArm" or robot["RobotType"] == "QA":
                qlabsRobot = QLabsQArm(self.qlabs)
            if robot["RobotType"] == "QCar2" or robot["RobotType"] == "QC2":
                qlabsRobot = QLabsQCar2(self.qlabs)
            if robot["RobotType"] == "QBotPlatform" or robot["RobotType"] == "QBP":
                qlabsRobot = QLabsQBotPlatform(self.qlabs)
            if robot["RobotType"] == "QDrone2" or robot["RobotType"] == "QD2":
                qlabsRobot = QLabsQDrone2(self.qlabs)
            
            location = robot["Location"]
            rotation = robot["Rotation"]
            scale = [robot["Scale"], robot["Scale"], robot["Scale"]]
            
            if "ActorNumber" not in robot: # spawn degrees or spawn
                if robot["Radians"] == True:
                    qlabsRobot.spawn(location=location, rotation=rotation, scale=scale)
                else:
                    qlabsRobot.spawn_degrees(location=location, rotation=rotation, scale=scale)
            else: # spawn id or spawn ID degrees
                actorNumber = robot["ActorNumber"]
                if robot["Radians"] == True:
                    qlabsRobot.spawn_id(actorNumber=actorNumber,location=location, rotation=rotation, scale=scale)
                else:
                    qlabsRobot.spawn_id_degrees(actorNumber=actorNumber, location=location, rotation=rotation, scale=scale)

            robotActors[x] = qlabsRobot 
        
            x = x + 1

        return robotActors

    def createRobot(self, QLabsActor):
        classID = QLabsActor.classID
        actorNumber = QLabsActor.actorNumber
        if classID == 10: #QArm
            name, robotDict = self._createQArm(actorNumber)
        if classID == 23: # QBP
            name, robotDict = self._createQBP(actorNumber)
        if classID == 161: #QCar2
            name, robotDict = self._createQC2(actorNumber)
        if classID == 231: #QDrone2
            name, robotDict = self._createQD2(actorNumber)
        
        return name, robotDict

    def _createQArm(self, actorNumber):
        path = self._copyQArm_files(actorNumber)
        path, ext = os.path.splitext(path)

        hilPort = self._nextNumber()
        videoPort = self._nextNumber()
        uriPort = self._nextURINumber()

        arguments = '-uri_hil tcpip://localhost:' + str(hilPort) + ' ' + \
                    '-uri_video tcpip://localhost:' + str(videoPort)
        
        display = 'QArm ' + str(actorNumber) + ' spawned as ' + arguments
        print(display)

        #Start spawn model
        QLabsRealTime().start_real_time_model(path, actorNumber=actorNumber, uriPort = uriPort, additionalArguments=arguments)

        name = 'QA_' + str(actorNumber)
        robotDict = {
            "robotType": "QArm",
            "actorNumber": actorNumber,
            "classID": 10,
            "hilPort" : hilPort,
            "videoPort" : videoPort
        }

        return name, robotDict

    def _createQBP(self, actorNumber):
        workspacePath, driverPath = self._copyQBP_files(actorNumber)

        workspacePath, ext = os.path.splitext(workspacePath)

        driverPath, ext = os.path.splitext(driverPath)

        videoPort = self._nextNumber()
        video3dPort = self._nextNumber()
        lidarPort = self._nextNumber()
        uriPort = self._nextURINumber()

        # hilPort, driverPort = self._nextDriverNumber()
        hilPort = 18950 + actorNumber
        driverPort = 18970 + actorNumber
        uriPortDriver = self._nextURINumber()
    
        arguments = '-uri_hil tcpip://localhost:'    + str(hilPort) + ' ' + \
                    '-uri_video tcpip://localhost:' + str(videoPort) + ' ' + \
                    '-uri_video3d tcpip://localhost:'+ str(video3dPort) + ' ' + \
                    '-uri_lidar tcpip://localhost:'  + str(lidarPort)  
        
        display = 'QBP ' + str(actorNumber) + ' spawned as ' + arguments
        print(display)

        #Start spawn model
        QLabsRealTime().start_real_time_model(workspacePath, actorNumber=actorNumber, uriPort = uriPort, additionalArguments=arguments)

        arguments = '-uri tcpip://localhost:'+ str(uriPortDriver) 
        QLabsRealTime().start_real_time_model(driverPath, actorNumber=actorNumber, userArguments=False, additionalArguments= arguments)

        name = 'QBP_' + str(actorNumber)
        robotDict = {
            "robotType": "QBP",
            "actorNumber": actorNumber,
            "classID": 23,
            "hilPort" : hilPort,
            "videoPort" : videoPort,
            "video3dPort" : video3dPort,
            "lidarPort" : lidarPort,
            "driverPort" : driverPort
        }

        return name, robotDict

    def _createQC2(self, actorNumber):
        path = self._copyQC2_files(actorNumber)
        path, ext = os.path.splitext(path)

        hilPort = self._nextNumber()
        video0Port = self._nextNumber()
        video1Port = self._nextNumber()
        video2Port = self._nextNumber()
        video3Port = self._nextNumber()
        video3dPort = self._nextNumber()
        lidarPort = self._nextNumber()
        gpsPort = self._nextNumber()
        lidarIdealPort = self._nextNumber()
        ledPort = self._nextNumber()

        uriPort = self._nextURINumber()
    
        arguments = '-uri_hil tcpip://localhost:'    + str(hilPort) + ' ' + \
                    '-uri_video0 tcpip://localhost:' + str(video0Port) + ' ' + \
                    '-uri_video1 tcpip://localhost:' + str(video1Port) + ' ' + \
                    '-uri_video2 tcpip://localhost:' + str(video2Port) + ' ' + \
                    '-uri_video3 tcpip://localhost:' + str(video3Port) + ' ' + \
                    '-uri_video3d tcpip://localhost:'+ str(video3dPort) + ' ' + \
                    '-uri_lidar tcpip://localhost:'  + str(lidarPort) + ' ' + \
                    '-uri_gps tcpip://localhost:'    + str(gpsPort) + ' ' + \
                    '-uri_lidar_ideal tcpip://localhost:'  + str(lidarIdealPort) + ' ' + \
                    '-uri_led tcpip://localhost:'    + str(ledPort)
        
        display = 'QCar ' + str(actorNumber) + ' spawned as ' + arguments
        print(display)

        #Start spawn model
        QLabsRealTime().start_real_time_model(path, actorNumber=actorNumber, uriPort = uriPort, additionalArguments=arguments)

        name = 'QC2_' + str(actorNumber)
        robotDict = {
            "robotType": "QC2",
            "actorNumber": actorNumber,
            "classID": 161,
            "hilPort" : hilPort,
            "videoPort" : video0Port,
            "video3dPort" : video3dPort,
            "lidarPort" : lidarPort,
            "gpsPort" : gpsPort,
            "lidarIdealPort" : lidarIdealPort,
            "ledPort" : ledPort
        }

        return name, robotDict
  
    def _createQD2(self, actorNumber):
        path = self._copyQD2_files(actorNumber)
        path, ext = os.path.splitext(path)

        hilPort = self._nextNumber()
        video0Port = self._nextNumber()
        video1Port = self._nextNumber()
        video2Port = self._nextNumber()
        video3Port = self._nextNumber()
        video3dPort = self._nextNumber()
        posePort = self._nextNumber()

        uriPort = self._nextURINumber()

        arguments = '-uri_hil tcpip://localhost:'    + str(hilPort) + ' ' + \
                    '-uri_video0 tcpip://localhost:' + str(video0Port) + ' ' + \
                    '-uri_video1 tcpip://localhost:' + str(video1Port) + ' ' + \
                    '-uri_video2 tcpip://localhost:' + str(video2Port) + ' ' + \
                    '-uri_video3 tcpip://localhost:' + str(video3Port) + ' ' + \
                    '-uri_video3d tcpip://localhost:'+ str(video3dPort) + ' ' + \
                    '-uri_pose tcpip://localhost:'  + str(posePort) 
    
        
        display = 'QDrone ' + str(actorNumber) + ' spawned as ' + arguments
        print(display)

        #Start spawn model
        QLabsRealTime().start_real_time_model(path, actorNumber=actorNumber, uriPort = uriPort, additionalArguments=arguments)

        name = 'QD2_' + str(actorNumber)
        robotDict = {
            "robotType": "QD2",
            "actorNumber": actorNumber,
            "classID": 231,
            "hilPort" : hilPort,
            "videoPort" : video0Port,
            "video3dPort" : video3dPort,
            "posePort" : posePort
        }

        return name, robotDict

    def _copyQArm_files(self,actorNumber):
        rtFile = 'QArm_Spawn'

        # create copy of rt file workspace
        originalFile = rtFile + self._fileType
        originalPath = os.path.join(MultiAgent._QArmDir,originalFile)
        newFile = rtFile + str(actorNumber) + self._fileType
        newPath = os.path.join(MultiAgent._directory,newFile)
        shutil.copy(originalPath, newPath)

        time.sleep(0.2)
        return newPath

    def _copyQBP_files(self,actorNumber):
        rtFile = 'QBotPlatform_Workspace_debug'
        driverFile = 'qbot_platform_driver_virtual' + str(actorNumber)

        # create copy of rt file workspace
        originalFile = rtFile + self._fileType
        originalPath = os.path.join(MultiAgent._QBPDir,originalFile)
        newFile = rtFile + str(actorNumber) + self._fileType
        newPathWorkspace = os.path.join(MultiAgent._directory,newFile)
        shutil.copy(originalPath, newPathWorkspace)

        # create copy of driver _QBPDriverDir
        originalFile = driverFile + self._fileType
        originalPath = os.path.join(MultiAgent._QBPDriverDir,originalFile)
        newFile = driverFile + self._fileType
        newPathDriver = os.path.join(MultiAgent._directory,newFile)
        shutil.copy(originalPath, newPathDriver)

        time.sleep(2) # change! back to 0.2
        return newPathWorkspace, newPathDriver

    def _copyQC2_files(self, actorNumber):
        rtFile = 'QCar2_Workspace'

        # create copy of rt file workspace
        originalFile = rtFile + self._fileType
        originalPath = os.path.join(MultiAgent._QCar2Dir,originalFile)
        newFile = rtFile + str(actorNumber) + self._fileType
        newPath = os.path.join(MultiAgent._directory,newFile)
        shutil.copy(originalPath, newPath)

        time.sleep(0.2)
        return newPath
    
    def _copyQD2_files(self,actorNumber):
        rtFile = 'QDrone2_Workspace'

        # create copy of rt file workspace
        originalFile = rtFile + self._fileType
        originalPath = os.path.join(MultiAgent._QD2Dir,originalFile)
        newFile = rtFile + str(actorNumber) + self._fileType
        newPath = os.path.join(MultiAgent._directory,newFile)
        shutil.copy(originalPath, newPath)

        time.sleep(0.2)
        return newPath
    
    def _nextNumber(self):
        self._portNumber = self._portNumber + 1
        return self._portNumber
    
    def _nextURINumber(self):
        self._uriPortNumber = self._uriPortNumber + 1
        return self._uriPortNumber
    
    def _nextDriverNumber(self):
        self._driverPortNumber = self._driverPortNumber + 1
        driverPort = self._driverPortNumber + 20
        return self._driverPortNumber, driverPort
    
    
def readRobots():
    directory = os.path.normpath(
        os.path.join(os.environ['RTMODELS_DIR'], 'MultiAgent'))
    
    filePath = os.path.join(directory,"RobotAgents.json")
    tmpPath = os.path.join(directory,"tmp.csv")
    
    
    wait = True

    while wait:
        tmpExists = os.path.isfile(tmpPath)
        
        if not tmpExists: 
            open(tmpPath, 'a').close() # temporary file to prevent robotJSON from opening if its already used by someone else
            with open(filePath, 'r') as file:
                robotsDict = json.load(file)
            os.remove(tmpPath)
            wait = False
        
        else:
            time.sleep(0.05)
        
    return robotsDict