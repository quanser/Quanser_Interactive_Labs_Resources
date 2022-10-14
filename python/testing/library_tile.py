import numpy as np
from library_qlabs_basic_shape import QLabsBasicShape
from library_qlabs_spline_line import QLabsSplineLine

# XXX use enum for tile types?

class TileMap():
    def __init__(self, qlabs, position, rotation):
        self._qlabs = qlabs
        Tile._qlabs = qlabs

        self._pos = position
        self._rot = rotation

        self.tiles = []

    def add_tile(self,x,y,th,type):
        cTh = np.cos(self._rot)
        sTh = np.sin(self._rot)
        xOffset = cTh*x*Tile.width - sTh*y*Tile.width
        yOffset = sTh*x*Tile.width + cTh*y*Tile.width

        pos = [
            self._pos[0]+xOffset,
            self._pos[1]+yOffset,
            self._pos[2]
        ]
        self.tiles.append(Tile(pos,self._rot+th*np.pi/2,type))


class Tile():
    # Handles shared by all tiles
    _qlabs = None
    _hSpline = None
    _hShape = None

    # Tile Dimensions (meters)
    width = 1.2192
    height = 0.001 
    lineWidth = 0.0127
    markerWidth = 0.0254
    edgeMarkerDepth = 0.01905
    lineHeightOffset = height/2 + 0.001
    markerHeightOffset = height/2 + 0.002

    # Material Properties
    roughness = 0.4
    matColor = [0.0, 0.0, 0.0]
    lineColor = [1.0, 1.0, 1.0]
    markerColor = [0.925, 0.110, 0.141, 1]
    edgeMarkerColor = [0.537, 0.537, 0.537]

    def __init__(self, position, rotation, type=0):
        self._pos = position
        self._rot = rotation
        self._compute_R()
        self.type = type

        self._createHandles()
        self._generate_basic_tile()
        self._generate_type_specific_elements()

    def _createHandles(self):
        if Tile._qlabs is not None and Tile._hShape is None:
            Tile._hShape = QLabsBasicShape(Tile._qlabs)
            Tile._hSpline = QLabsSplineLine(Tile._qlabs)

    def _compute_R(self):
        self._R = [
            [np.cos(self._rot), -np.sin(self._rot)],
            [np.sin(self._rot), np.cos(self._rot)]
        ]

    def transform_marker(self,marker):
        p = [
            self._pos[0] + self._R[0][0]*marker[0] + self._R[0][1]*marker[1],
            self._pos[1] + self._R[1][0]*marker[0] + self._R[1][1]*marker[1],
            self._pos[2] + Tile.markerHeightOffset
        ]
        th = self._rot + marker[2]
        return p, th


    def _generate_basic_tile(self):
        # Spawn floor mat
        Tile._hShape.spawn(
            self._pos,
            [0, 0, self._rot],
            [Tile.width, Tile.width, Tile.height],
            waitForConfirmation=True
        )
        Tile._hShape.set_material_properties(
            Tile.matColor,
            roughness=Tile.roughness,
            metallic=False,
            waitForConfirmation=False
        )

        # Spawn Edge Markers
        markers = [
            [-Tile.width/4, Tile.width/2-Tile.edgeMarkerDepth/2, np.pi/2],
            [Tile.width/4, Tile.width/2-Tile.edgeMarkerDepth/2, np.pi/2],
            [Tile.width/2-Tile.edgeMarkerDepth/2, Tile.width/4, 0],
            [Tile.width/2-Tile.edgeMarkerDepth/2, -Tile.width/4, 0],
            [Tile.width/4, -Tile.width/2+Tile.edgeMarkerDepth/2, -np.pi/2],
            [-Tile.width/4, -Tile.width/2+Tile.edgeMarkerDepth/2, -np.pi/2],
            [-Tile.width/2+Tile.edgeMarkerDepth/2, -Tile.width/4, np.pi],
            [-Tile.width/2+Tile.edgeMarkerDepth/2, Tile.width/4, np.pi]
        ]
        points = [
            [-Tile.edgeMarkerDepth/2, 0, 0, Tile.markerWidth],
            [Tile.edgeMarkerDepth/2, 0, 0, Tile.markerWidth],
        ]
        for marker in markers:
            p, th = self.transform_marker(marker)
            Tile._hSpline.spawn(
                location=p,
                rotation=[0, 0, th],
                scale=[1, 1, 1],
                configuration=1,
            )
            Tile._hSpline.set_points(
                colour=Tile.edgeMarkerColor,
                pointList=points,
                alignEndPointTangents=False,
                waitForConfirmation=False
            )

    def _generate_line(self,p1,p2):
        points = [
            [p1[0], p1[1], Tile.lineHeightOffset, Tile.lineWidth],
            [p2[0], p2[1], Tile.lineHeightOffset, Tile.lineWidth],
        ]

        Tile._hSpline.spawn(
            location=self._pos,
            rotation=[0, 0, self._rot],
            scale=[1, 1, 1],
            configuration=1
        )
        Tile._hSpline.set_points(
            colour=Tile.lineColor,
            pointList=points,
            alignEndPointTangents=False,
            waitForConfirmation=False
        )

    def _generate_arc(self,c,p1,p2):
        v1 = [p1[0]-c[0], p1[1]-c[1]]
        v2 = [p2[0]-c[0], p2[1]-c[1]]

        r = np.linalg.norm(v1)
        th1 = np.arctan2(v1[1], v1[0])
        th2 = np.arctan2(v2[1], v2[0]) - th1
        th2 = np.mod(np.mod(th2,np.pi*2)+np.pi*2, np.pi*2)

        p, th = self.transform_marker([c[0], c[1], th1])
        p[2] = self._pos[2] + self.lineHeightOffset

        Tile._hSpline.spawn(
            location=p,
            rotation=[0, 0, th],
            scale=[1, 1, 1],
            configuration=1
        )
        Tile._hSpline.arc_from_center(
            r,
            startAngle=0,
            endAngle=th2 , 
            lineWidth=Tile.lineWidth,
            colour=Tile.lineColor,
            numSplinePoints=8,
            waitForConfirmation=False
        )

    def _generate_marker(self,p):
        p, th = self.transform_marker([p[0],p[1],0])
        points = [
            [-Tile.markerWidth/2, 0, 0, Tile.markerWidth],
            [Tile.markerWidth/2, 0, 0, Tile.markerWidth],
        ]
        Tile._hSpline.spawn(
            location=p,
            rotation=[0, 0, th],
            scale=[1, 1, 1],
            configuration=1
        )
        Tile._hSpline.set_points(
            colour=Tile.markerColor,
            pointList=points,
            alignEndPointTangents=False,
            waitForConfirmation=False
        )


    def _generate_type_specific_elements(self):
        if self.type == 0:
            self._generate_line(
                [-Tile.width/4, -Tile.width/2],
                [-Tile.width/4, Tile.width/2]
            )
            self._generate_line(
                [Tile.width/4, -Tile.width/2],
                [Tile.width/4, Tile.width/2]
            )
            self._generate_line(
                [-Tile.width/2, -Tile.width/4],
                [Tile.width/2, -Tile.width/4]
            )
            self._generate_line(
                [-Tile.width/2, Tile.width/4],
                [Tile.width/2, Tile.width/4]
            )
            self._generate_marker([-Tile.width/4, Tile.width/4])
            self._generate_marker([Tile.width/4, Tile.width/4])
            self._generate_marker([-Tile.width/4, -Tile.width/4])
            self._generate_marker([Tile.width/4, -Tile.width/4])
        elif self.type == 1:
            self._generate_line(
                [-Tile.width/4, -Tile.width/2],
                [-Tile.width/4, Tile.width/4]
            )
            self._generate_line(
                [Tile.width/4, -Tile.width/2],
                [Tile.width/4, Tile.width/4]
            )
            self._generate_line(
                [-Tile.width/2, -Tile.width/4],
                [Tile.width/2, -Tile.width/4]
            )
            self._generate_line(
                [-Tile.width/2, Tile.width/4],
                [Tile.width/2, Tile.width/4]
            )
            self._generate_marker([-Tile.width/4, Tile.width/4])
            self._generate_marker([Tile.width/4, Tile.width/4])
            self._generate_marker([-Tile.width/4, -Tile.width/4])
            self._generate_marker([Tile.width/4, -Tile.width/4])
        elif self.type == 2:
            self._generate_arc(
                [Tile.width/2, Tile.width/2],
                [Tile.width/4, Tile.width/2],
                [Tile.width/2, Tile.width/4]
            )
            self._generate_arc(
                [Tile.width/2, Tile.width/2],
                [-Tile.width/4, Tile.width/2],
                [Tile.width/2, -Tile.width/4]
            )
            self._generate_marker([-Tile.width/4, -Tile.width/4])
        elif self.type == 3:
            self._generate_arc(
                [0, Tile.width/2],
                [-Tile.width/4, Tile.width/2],
                [Tile.width/4, Tile.width/2]
            )
            self._generate_arc(
                [Tile.width/2, 0],
                [Tile.width/2, Tile.width/4],
                [Tile.width/2, -Tile.width/4]
            )
            self._generate_arc(
                [0, -Tile.width/2],
                [Tile.width/4, -Tile.width/2],
                [-Tile.width/4, -Tile.width/2]
            )
            self._generate_arc(
                [-Tile.width/2, 0],
                [-Tile.width/2, -Tile.width/4],
                [-Tile.width/2, Tile.width/4]
            )
            self._generate_marker([0,0])
        elif self.type == 4:
            self._generate_arc(
                [-Tile.width/2, Tile.width/2],
                [-Tile.width/2, Tile.width/4],
                [-Tile.width/4, Tile.width/2]
            )
            self._generate_arc(
                [Tile.width/2, Tile.width/2],
                [Tile.width/4, Tile.width/2],
                [Tile.width/2, Tile.width/4]
            )
            self._generate_arc(
                [Tile.width/2, -Tile.width/2],
                [Tile.width/2, -Tile.width/4],
                [Tile.width/4, -Tile.width/2]
            )
            self._generate_arc(
                [-Tile.width/2, -Tile.width/2],
                [-Tile.width/4, -Tile.width/2],
                [-Tile.width/2, Tile.width/4]
            )
            self._generate_marker([0, 0])
        
        else:
            # Invalid tile type
            pass