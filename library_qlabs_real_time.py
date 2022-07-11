import math      
       
######################### MODULAR CONTAINER CLASS #########################

class QLabsRealTime:
        
    # Initialize class
    def __init__(self):

       return

    def start_real_time_model(self, modelName, actorNumber=0, QLabsHostName='localhost', additionalArguments=""):
        if platform.system() == "Windows":
            cmdString="start \"QLabs_{}_{}\" \"%QUARC_DIR%\quarc_run\" -D -r -t tcpip://localhost:17000 {}.rt-win64 -uri tcpip://localhost:{} -hostname {} -devicenum {} {}".format(modelName, actorNumber, modelName, self._URIPort, QLabsHostName, actorNumber, additionalArguments)
        elif platform.system() == "Linux":
            if platform.machine() == "armv7l":
                #Raspberry Pi 3, 4
                cmdString="quarc_run -D -r -t tcpip://localhost:17000 {}.rt-linux_pi_3 -uri tcpip://localhost:{} -hostname {} -devicenum {} {}".format(modelName, self._URIPort, QLabsHostName, actorNumber, additionalArguments)
            else:
                print("This Linux machine not supported for real-time model execution")
                return
        else:
            print("Platform not supported for real-time model execution")
            return
            
        os.system(cmdString)
        
        self._URIPort = self._URIPort + 1
        return cmdString            
          
    def terminate_real_time_model(self, modelName, additionalArguments=""):
        if platform.system() == "Windows":
            cmdString="start \"QLabs_Spawn_Model\" \"%QUARC_DIR%\quarc_run\" -q -Q -t tcpip://localhost:17000 {}.rt-win64 {}".format(modelName, additionalArguments)
        elif platform.system() == "Linux":
            if platform.machine() == "armv7l":
                cmdString="quarc_run -q -Q -t tcpip://localhost:17000 {}.rt-linux_pi_3 {}".format(modelName, additionalArguments)
            else:
                print("This Linux machine not supported for real-time model execution")
                return
            
        else:
            print("Platform not supported for real-time model execution")
            return
                    
        os.system(cmdString)
        return cmdString
        
    def terminate_all_real_time_models(self, additionalArguments=""):
        if platform.system() == "Windows":
            cmdString="start \"QLabs_Spawn_Model\" \"%QUARC_DIR%\quarc_run\" -q -Q -t tcpip://localhost:17000 *.rt-win64 {}".format(additionalArguments)
        elif platform.system() == "Linux":
            if platform.machine() == "armv7l":
                cmdString="quarc_run -q -Q -t tcpip://localhost:17000 *.rt-linux_pi_3 {}".format(additionalArguments)
            else:
                print("This Linux machine not supported for real-time model execution")
                return
            
        else:
            print("Platform not supported for real-time model execution")
            return
                    
        os.system(cmdString)
        return cmdString 