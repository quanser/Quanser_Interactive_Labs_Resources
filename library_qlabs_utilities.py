from library_qlabs import QuanserInteractiveLabs, CommModularContainer
from quanser.common import GenericError
from library_qlabs_basic_shape import QLabsBasicShape
import math
import struct
        


def rotateVector2DDegrees(vector, angle):

    result = [0,0,vector[2]]

    result[0] = math.cos(angle)*vector[0] - math.sin(angle)*vector[1]
    result[1] = math.sin(angle)*vector[0] + math.cos(angle)*vector[1]
    
    return result


def spawnBoxWallsFromCenterDegrees(qlabs, deviceNumberStart, centerLocation, yaw, xSize, ySize, zHeight, wallThickness, floorThickness=0, wallColor=[1,1,1], floorColor=[1,1,1], waitForConfirmation=True):
    spawnBoxWallsFromCenter(qlabs, deviceNumberStart, centerLocation, yaw/180*math.pi, xSize, ySize, zHeight, wallThickness, floorThickness, wallColor, floorColor, waitForConfirmation)

def spawnBoxWallsFromCenter(qlabs, deviceNumberStart, centerLocation, yaw, xSize, ySize, zHeight, wallThickness, floorThickness=0, wallColor=[1,1,1], floorColor=[1,1,1], waitForConfirmation=True):

    location = rotateVector2DDegrees([centerLocation[0] + xSize/2 + wallThickness/2, centerLocation[1], centerLocation[2] + zHeight/2 + floorThickness], yaw)
    QLabsBasicShape().spawn(qlabs, deviceNumberStart+0, location, [0, 0, yaw], [wallThickness, ySize, zHeight], QLabsBasicShape().SHAPE_CUBE, waitForConfirmation)
    QLabsBasicShape().setMaterialProperties(qlabs, deviceNumberStart+0, wallColor, 1, False, waitForConfirmation)
    
    location = rotateVector2DDegrees([centerLocation[0] - xSize/2 - wallThickness/2, centerLocation[1], centerLocation[2] + zHeight/2 + floorThickness], yaw)
    QLabsBasicShape().spawn(qlabs, deviceNumberStart+1, location, [0, 0, yaw], [wallThickness, ySize, zHeight], QLabsBasicShape().SHAPE_CUBE, waitForConfirmation)
    QLabsBasicShape().setMaterialProperties(qlabs, deviceNumberStart+1, wallColor, 1, False, waitForConfirmation)
    
    location = rotateVector2DDegrees([centerLocation[0], centerLocation[1] + ySize/2 + wallThickness/2, centerLocation[2] + zHeight/2 + floorThickness], yaw)
    QLabsBasicShape().spawn(qlabs, deviceNumberStart+2, location, [0, 0, yaw], [xSize + wallThickness*2, wallThickness, zHeight], QLabsBasicShape().SHAPE_CUBE, waitForConfirmation)
    QLabsBasicShape().setMaterialProperties(qlabs, deviceNumberStart+2, wallColor, 1, False, waitForConfirmation)
    
    location = rotateVector2DDegrees([centerLocation[0], centerLocation[1] - ySize/2 - wallThickness/2, centerLocation[2] + zHeight/2 + floorThickness], yaw)
    QLabsBasicShape().spawn(qlabs, deviceNumberStart+3, location, [0, 0, yaw], [xSize + wallThickness*2, wallThickness, zHeight], QLabsBasicShape().SHAPE_CUBE, waitForConfirmation)
    QLabsBasicShape().setMaterialProperties(qlabs, deviceNumberStart+3, wallColor, 1, False, waitForConfirmation)
    
    
    if (floorThickness > 0):
        QLabsBasicShape().spawn(qlabs, deviceNumberStart+4, [centerLocation[0], centerLocation[1], centerLocation[2]+ floorThickness/2], [0, 0, yaw], [xSize+wallThickness*2, ySize+wallThickness*2, floorThickness], QLabsBasicShape().SHAPE_CUBE, waitForConfirmation)
        QLabsBasicShape().setMaterialProperties(qlabs, deviceNumberStart+4, floorColor, 1, False, waitForConfirmation)
    
        