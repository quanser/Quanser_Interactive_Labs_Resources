from library_qlabs import QuanserInteractiveLabs, CommModularContainer
from quanser.common import GenericError
import math

import struct
        
        
######################### MODULAR CONTAINER CLASS #########################

class QLabsSplineLine:

       
    ID_SPLINE_LINE = 180
    
    FCN_SPLINE_LINE_SET_POINTS = 10
    FCN_SPLINE_LINE_SET_POINTS_ACK = 11
    
        
    # Initialize class
    def __init__(self):

       return
       
    def spawn_id(self, qlabs, actorNumber, location, rotation, scale, configuration=0, waitForConfirmation=True):
        return qlabs.spawn(actorNumber, self.ID_SPLINE_LINE, location[0], location[1], location[2], rotation[0], rotation[1], rotation[2], scale[0], scale[1], scale[2], configuration, waitForConfirmation)
   
    def spawn_id_degrees(self, qlabs, actorNumber, location, rotation, scale, configuration=0, waitForConfirmation=True):
    
        return qlabs.spawn(actorNumber, self.ID_SPLINE_LINE, location[0], location[1], location[2], rotation[0]/180*math.pi, rotation[1]/180*math.pi, rotation[2]/180*math.pi, scale[0], scale[1], scale[2], configuration, waitForConfirmation)
   
    def set_points(self, qlabs, actorNumber, colour, alignEndPointTangents, pointList, waitForConfirmation=True):
        c = CommModularContainer()
        c.classID = self.ID_SPLINE_LINE
        c.actorNumber = actorNumber
        c.actorFunction = self.FCN_SPLINE_LINE_SET_POINTS
        c.payload = bytearray(struct.pack(">fffB", colour[0], colour[1], colour[2], alignEndPointTangents))
        
        for point in pointList:
            c.payload = c.payload + bytearray(struct.pack(">ffff", point[0], point[1], point[2], point[3]))
        
                
        c.containerSize = c.BASE_CONTAINER_SIZE + len(c.payload)
        
        if waitForConfirmation:
            qlabs.flush_receive()  
        
        if (qlabs.send_container(c)):
            if waitForConfirmation:
                c = qlabs.wait_for_container(self.ID_SPLINE_LINE, actorNumber, self.FCN_SPLINE_LINE_SET_POINTS_ACK)
                return c
                    
            return True
        else:
            return False    

    def spawn_spline_circle_from_center(qlabs, actorNumber, centerLocation, rotation, radius, lineWidth=1, colour=[1,0,0], numSplinePoints=4, waitForConfirmation=True):
        # Place the spawn point of the spline at the global origin so we can use world coordinates for the points
        QLabsSplineLine().spawn(qlabs, actorNumber, centerLocation, rotation, [1, 1, 1], 0, waitForConfirmation)

        points = []

        for angle in range(0, numSplinePoints):
            points.append([radius*math.sin(angle/numSplinePoints*math.pi*2), radius*math.cos(angle/numSplinePoints*math.pi*2), 0, lineWidth])
        
        points.append(points[0])
    
        QLabsSplineLine().set_points(qlabs, actorNumber, colour, alignEndPointTangents=True, pointList=points)
        
    def spawn_spline_circle_from_center_degrees(qlabs, actorNumber, centerLocation, rotation, radius, lineWidth=1, colour=[1,0,0], numSplinePoints=4, waitForConfirmation=True):

        spawn_spline_circle_from_center(qlabs, actorNumber, centerLocation, [x/180*math.pi for x in rotation], radius, lineWidth, colour, numSplinePoints, waitForConfirmation)
     
    def spawn_spline_arc_from_center(qlabs, actorNumber, centerLocation, rotation, radius, startAngle=0, endAngle=math.pi/2, lineWidth=1, colour=[1,0,0], numSplinePoints=4, waitForConfirmation=True):
        # Place the spawn point of the spline at the global origin so we can use world coordinates for the points
        QLabsSplineLine().spawn(qlabs, actorNumber, centerLocation, rotation, [1, 1, 1], 0, waitForConfirmation)

        points = []

        for angle in range(0, numSplinePoints+1):
            points.append([radius*math.sin(angle/numSplinePoints*(endAngle-startAngle)+startAngle), radius*math.cos(angle/numSplinePoints*(endAngle-startAngle)+startAngle), 0, lineWidth])
        
        QLabsSplineLine().set_points(qlabs, actorNumber, colour, alignEndPointTangents=False, pointList=points)
    
    def spawn_spline_arc_from_center_degrees(qlabs, actorNumber, centerLocation, rotation, radius, startAngle=0, endAngle=90, lineWidth=1, colour=[1,0,0], numSplinePoints=4, waitForConfirmation=True):

        spawn_spline_arc_from_center(qlabs, actorNumber, centerLocation, rotation, radius, startAngle/180*math.pi, endAngle/180*math.pi, lineWidth, colour, numSplinePoints, waitForConfirmation)

    def spawn_spline_line_two_point(qlabs, actorNumber, p1, p2, lineWidth=1, colour=[1,0,0], waitForConfirmation=True):
        # Place the spawn point of the spline at the global origin so we can use world coordinates for the points
        QLabsSplineLine().spawn(qlabs, actorNumber, [0,0,0], [0,0,0], [1, 1, 1], 0, waitForConfirmation)

        points = [[p1[0], p1[1], p1[2], lineWidth], [p2[0], p2[1], p2[2], lineWidth]]
        
        QLabsSplineLine().set_points(qlabs, actorNumber, colour, alignEndPointTangents=False, pointList=points)
        
    def spawn_spline_rounded_rectangle_from_center(qlabs, actorNumber, centerLocation, rotation, cornerRadius, xWidth, yLength, lineWidth=1, colour=[1,0,0], waitForConfirmation=True):
        # Place the spawn point of the spline at the global origin so we can use world coordinates for the points
        QLabsSplineLine().spawn(qlabs, actorNumber, centerLocation, rotation, [1, 1, 1], 0, waitForConfirmation)

        points = spawn_spline_rounded_rectangle_from_center_point_list(centerLocation, rotation, cornerRadius, xWidth, yLength, lineWidth)
        
        QLabsSplineLine().set_points(qlabs, actorNumber, colour, alignEndPointTangents=True, pointList=points)
    
    
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