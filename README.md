# Core set of hexagons for HexWorld
## Hexagon Base
![](./Images/HexagonBase.png)
## Hexagon Canal Straight Bezier
![](./Images/HexagonCanalStraightBezier.png)
## Hexagon Canal Curve Bezier
![](./Images/HexagonCanalCurveBezier.png)
## Hexagon Canal Split Bezier
![](./Images/HexagonCanalSplitBezier.png)
## Hexagon Canal Strtaight Curve North East Bezier
![](./Images/HexagonCanalStraightCurveNEBezier.png)
## Hexagon Canal Strtaight Curve North West Bezier
![](./Images/HexagonCanalStraightCurveNWBezier.png)


Convert OpenSCAD to STL -> Blender -> FBX run:
```shell script
blender -b -P ./ConvertOpenSCAD2FBX.py
```
Or
```shell script
blender --background --python ./ConvertOpenSCAD2FBX.py
```
On Ubuntu (snap script ignores --background):
```shell script
 /snap/blender/current/blender --background --python ConvertOpenSCAD2FBX.py
```

