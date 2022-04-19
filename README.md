# Core set of hexagons for HexWorld
All files are modelled in [OpenSCAD](https://openscad.org/), a paremetric CAD modelling program.

### Slope
The slope of the canal is done with a bezier curve:

`function cubic_bezier(p0,p1,p2,p3) = [for (t=[0:deltat:1+deltat]) pow(1-t,3)*p0+3*pow((1-t),2)*t*p1+3*(1-t)*pow(t,2)*p2+pow(t,3)*p3];`

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

## Conversion 
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

