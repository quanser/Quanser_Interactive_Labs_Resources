from library_qlabs_basic_shape import QLabsBasicShape
from library_qlabs_spline_line import QLabsSplineLine
import math

def rotate_vector_2d_degrees(vector, angle):

    result = [0,0,vector[2]]

    result[0] = math.cos(angle)*vector[0] - math.sin(angle)*vector[1]
    result[1] = math.sin(angle)*vector[0] + math.cos(angle)*vector[1]
    
    return result

def spawn_box_walls_from_end_points(qlabs, deviceNumber, startLocation, endLocation, height, wallThickness, wallColor=[1,1,1], waitForConfirmation=True):
    length = math.sqrt(pow(startLocation[0] - endLocation[0],2) + pow(startLocation[1] - endLocation[1],2) + pow(startLocation[2] - endLocation[2],2))
    location = [(startLocation[0] + endLocation[0])/2, (startLocation[1] + endLocation[1])/2, (startLocation[2] + endLocation[2])/2]
    
    yRotation = -math.asin( (endLocation[2] - startLocation[2])/(length) )
    zRotation = math.atan2( (endLocation[1] - startLocation[1]), (endLocation[0] - startLocation[0]))
    
    shiftedLocation = [location[0]+math.sin(yRotation)*math.cos(zRotation)*height/2, location[1]+math.sin(yRotation)*math.sin(zRotation)*height/2, location[2]+math.cos(yRotation)*height/2]
    
    QLabsBasicShape().spawn(qlabs, deviceNumber, shiftedLocation, [0, yRotation, zRotation], [length, wallThickness, height], QLabsBasicShape().SHAPE_CUBE, waitForConfirmation)
    QLabsBasicShape().set_material_properties(qlabs, deviceNumber, wallColor, 1, False, waitForConfirmation)
    
def spawn_box_walls_from_center_degrees(qlabs, deviceNumberStart, centerLocation, yaw, xSize, ySize, zHeight, wallThickness, floorThickness=0, wallColor=[1,1,1], floorColor=[1,1,1], waitForConfirmation=True):
    spawn_box_walls_from_center(qlabs, deviceNumberStart, centerLocation, yaw/180*math.pi, xSize, ySize, zHeight, wallThickness, floorThickness, wallColor, floorColor, waitForConfirmation)

def spawn_box_walls_from_center(qlabs, deviceNumberStart, centerLocation, yaw, xSize, ySize, zHeight, wallThickness, floorThickness=0, wallColor=[1,1,1], floorColor=[1,1,1], waitForConfirmation=True):

    location = rotate_vector_2d_degrees([centerLocation[0] + xSize/2 + wallThickness/2, centerLocation[1], centerLocation[2] + zHeight/2 + floorThickness], yaw)
    QLabsBasicShape().spawn(qlabs, deviceNumberStart+0, location, [0, 0, yaw], [wallThickness, ySize, zHeight], QLabsBasicShape().SHAPE_CUBE, waitForConfirmation)
    QLabsBasicShape().set_material_properties(qlabs, deviceNumberStart+0, wallColor, 1, False, waitForConfirmation)
    
    location = rotate_vector_2d_degrees([centerLocation[0] - xSize/2 - wallThickness/2, centerLocation[1], centerLocation[2] + zHeight/2 + floorThickness], yaw)
    QLabsBasicShape().spawn(qlabs, deviceNumberStart+1, location, [0, 0, yaw], [wallThickness, ySize, zHeight], QLabsBasicShape().SHAPE_CUBE, waitForConfirmation)
    QLabsBasicShape().set_material_properties(qlabs, deviceNumberStart+1, wallColor, 1, False, waitForConfirmation)
    
    location = rotate_vector_2d_degrees([centerLocation[0], centerLocation[1] + ySize/2 + wallThickness/2, centerLocation[2] + zHeight/2 + floorThickness], yaw)
    QLabsBasicShape().spawn(qlabs, deviceNumberStart+2, location, [0, 0, yaw], [xSize + wallThickness*2, wallThickness, zHeight], QLabsBasicShape().SHAPE_CUBE, waitForConfirmation)
    QLabsBasicShape().set_material_properties(qlabs, deviceNumberStart+2, wallColor, 1, False, waitForConfirmation)
    
    location = rotate_vector_2d_degrees([centerLocation[0], centerLocation[1] - ySize/2 - wallThickness/2, centerLocation[2] + zHeight/2 + floorThickness], yaw)
    QLabsBasicShape().spawn(qlabs, deviceNumberStart+3, location, [0, 0, yaw], [xSize + wallThickness*2, wallThickness, zHeight], QLabsBasicShape().SHAPE_CUBE, waitForConfirmation)
    QLabsBasicShape().set_material_properties(qlabs, deviceNumberStart+3, wallColor, 1, False, waitForConfirmation)
        
    if (floorThickness > 0):
        QLabsBasicShape().spawn(qlabs, deviceNumberStart+4, [centerLocation[0], centerLocation[1], centerLocation[2]+ floorThickness/2], [0, 0, yaw], [xSize+wallThickness*2, ySize+wallThickness*2, floorThickness], QLabsBasicShape().SHAPE_CUBE, waitForConfirmation)
        QLabsBasicShape().set_material_properties(qlabs, deviceNumberStart+4, floorColor, 1, False, waitForConfirmation)
        
def spawn_spline_circle_from_center(qlabs, deviceNumber, centerLocation, rotation, radius, lineWidth=1, color=[1,0,0], numSplinePoints=4, waitForConfirmation=True):
    # Place the spawn point of the spline at the global origin so we can use world coordinates for the points
    QLabsSplineLine().spawn(qlabs, deviceNumber, centerLocation, rotation, [1, 1, 1], 0, waitForConfirmation)

    points = []

    for angle in range(0, numSplinePoints):
        points.append([radius*math.sin(angle/numSplinePoints*math.pi*2), radius*math.cos(angle/numSplinePoints*math.pi*2), 0, lineWidth])
        
    points.append(points[0])
    
    QLabsSplineLine().set_points(qlabs, deviceNumber, color, alignEndPointTangents=True, pointList=points)
        
def spawn_spline_circle_from_centerDegrees(qlabs, deviceNumber, centerLocation, rotation, radius, lineWidth=1, color=[1,0,0], numSplinePoints=4, waitForConfirmation=True):

    spawn_spline_circle_from_center(qlabs, deviceNumber, centerLocation, [x/180*math.pi for x in rotation], radius, lineWidth, color, numSplinePoints, waitForConfirmation)
     
def spawn_spline_arc_from_center(qlabs, deviceNumber, centerLocation, rotation, radius, startAngle=0, endAngle=math.pi/2, lineWidth=1, color=[1,0,0], numSplinePoints=4, waitForConfirmation=True):
    # Place the spawn point of the spline at the global origin so we can use world coordinates for the points
    QLabsSplineLine().spawn(qlabs, deviceNumber, centerLocation, rotation, [1, 1, 1], 0, waitForConfirmation)

    points = []

    for angle in range(0, numSplinePoints+1):
        points.append([radius*math.sin(angle/numSplinePoints*(endAngle-startAngle)+startAngle), radius*math.cos(angle/numSplinePoints*(endAngle-startAngle)+startAngle), 0, lineWidth])
        
    QLabsSplineLine().set_points(qlabs, deviceNumber, color, alignEndPointTangents=False, pointList=points)
    
def spawn_spline_arc_from_centerDegrees(qlabs, deviceNumber, centerLocation, rotation, radius, startAngle=0, endAngle=90, lineWidth=1, color=[1,0,0], numSplinePoints=4, waitForConfirmation=True):

    spawn_spline_arc_from_center(qlabs, deviceNumber, centerLocation, rotation, radius, startAngle/180*math.pi, endAngle/180*math.pi, lineWidth, color, numSplinePoints, waitForConfirmation)

def spawn_spline_line_two_point(qlabs, deviceNumber, p1, p2, lineWidth=1, color=[1,0,0], waitForConfirmation=True):
    # Place the spawn point of the spline at the global origin so we can use world coordinates for the points
    QLabsSplineLine().spawn(qlabs, deviceNumber, [0,0,0], [0,0,0], [1, 1, 1], 0, waitForConfirmation)

    points = [[p1[0], p1[1], p1[2], lineWidth], [p2[0], p2[1], p2[2], lineWidth]]
        
    QLabsSplineLine().set_points(qlabs, deviceNumber, color, alignEndPointTangents=False, pointList=points)
        
def spawn_spline_rounded_rectangle_from_center(qlabs, deviceNumber, centerLocation, rotation, cornerRadius, xWidth, yLength, lineWidth=1, color=[1,0,0], waitForConfirmation=True):
    # Place the spawn point of the spline at the global origin so we can use world coordinates for the points
    QLabsSplineLine().spawn(qlabs, deviceNumber, centerLocation, rotation, [1, 1, 1], 0, waitForConfirmation)

    points = spawn_spline_rounded_rectangle_from_center_point_list(centerLocation, rotation, cornerRadius, xWidth, yLength, lineWidth)
        
    QLabsSplineLine().set_points(qlabs, deviceNumber, color, alignEndPointTangents=True, pointList=points)
    
    
    # index = 2000
    # for pt in points:
        # QLabsBasicShape().spawn(qlabs, index, [pt[0], pt[1], pt[2]], [0, 0, 0], [0.05+0.001*(index-2000), 0.05+0.001*(index-2000), 0.05+0.001*(index-2000)], QLabsBasicShape().SHAPE_SPHERE, waitForConfirmation)
        # index = index + 1
        
    

    #QLabsBasicShape().spawn(qlabs, index, centerLocation, [0, 0, 0], [xWidth, yLength, 0.5], QLabsBasicShape().SHAPE_CUBE, waitForConfirmation)    
    
def spawn_spline_rounded_rectangle_from_center_point_list(centerLocation, rotation, cornerRadius, xWidth, yLength, lineWidth=1):
    if (xWidth <= cornerRadius*2):
        xWidth = cornerRadius*2
        
    if (yLength <= cornerRadius*2):
        yLength = cornerRadius*2
        
    circleSegmentLength = math.pi*cornerRadius*2/8
    
    xCount = math.ceil((xWidth - 2*cornerRadius)/circleSegmentLength)
    yCount = math.ceil((yLength - 2*cornerRadius)/circleSegmentLength)
    
    # Y
    # ▲
    # │
    # ┼───► X
    #
    #   4───────3
    #   │       │
    #   │   ┼   │
    #   │       │
    #   1───────2
    
    offset225deg = cornerRadius-cornerRadius*math.sin(math.pi/8)
    offset45deg = cornerRadius-cornerRadius*math.sin(math.pi/8*2) 
    offset675deg = cornerRadius-cornerRadius*math.sin(math.pi/8*3)
    
    # corner 1
    points = []
    points.append([-xWidth/2, -yLength/2+cornerRadius, 0, lineWidth])
    points.append([-xWidth/2+offset675deg, -yLength/2+offset225deg, 0, lineWidth])
    points.append([-xWidth/2+offset45deg, -yLength/2+offset45deg, 0, lineWidth])
    points.append([-xWidth/2+offset225deg, -yLength/2+offset675deg, 0, lineWidth])
    points.append([-xWidth/2+cornerRadius,-yLength/2, 0, lineWidth])
    
    # x1
    if (xWidth > cornerRadius*2):
        sideSegmentLength = (xWidth - 2*cornerRadius)/xCount
       
        for sideCount in range(1,xCount):
             points.append([-xWidth/2+cornerRadius + sideCount*sideSegmentLength,-yLength/2, 0, lineWidth])
    
        points.append([xWidth/2-cornerRadius,-yLength/2, 0, lineWidth])

    # corner 2
    points.append([xWidth/2-offset225deg, -yLength/2+offset675deg, 0, lineWidth])
    points.append([xWidth/2-offset45deg, -yLength/2+offset45deg, 0, lineWidth])
    points.append([xWidth/2-offset675deg, -yLength/2+offset225deg, 0, lineWidth])
    points.append([xWidth/2, -yLength/2+cornerRadius, 0, lineWidth])
 
    # y1
    if (yLength > cornerRadius*2):
        sideSegmentLength = (yLength - 2*cornerRadius)/yCount
       
        for sideCount in range(1,yCount):
            points.append([xWidth/2, -yLength/2+cornerRadius  + sideCount*sideSegmentLength, 0, lineWidth])
        
        points.append([xWidth/2, yLength/2-cornerRadius, 0, lineWidth])

    # corner 3
    points.append([xWidth/2-offset675deg, yLength/2-offset225deg, 0, lineWidth])
    points.append([xWidth/2-offset45deg, yLength/2-offset45deg, 0, lineWidth])
    points.append([xWidth/2-offset225deg, yLength/2-offset675deg, 0, lineWidth])
    points.append([xWidth/2-cornerRadius, yLength/2, 0, lineWidth])
    
    # x2
    if (xWidth > cornerRadius*2):
        sideSegmentLength = (xWidth - 2*cornerRadius)/xCount
        
        for sideCount in range(1,xCount):
            points.append([xWidth/2-cornerRadius - sideCount*sideSegmentLength, yLength/2, 0, lineWidth])
    
        points.append([-xWidth/2+cornerRadius, yLength/2, 0, lineWidth])  
        
    # corner 4     
    points.append([-xWidth/2+offset225deg, yLength/2-offset675deg, 0, lineWidth])
    points.append([-xWidth/2+offset45deg, yLength/2-offset45deg, 0, lineWidth])
    points.append([-xWidth/2+offset675deg, yLength/2-offset225deg, 0, lineWidth])
    points.append([-xWidth/2, yLength/2-cornerRadius, 0, lineWidth])
    
    # y2
    if (yLength > cornerRadius*2):
        sideSegmentLength = (yLength - 2*cornerRadius)/yCount
       
        for sideCount in range(1,yCount):
            points.append([-xWidth/2, yLength/2-cornerRadius - sideCount*sideSegmentLength, 0, lineWidth])

        points.append(points[0])
        
    return points