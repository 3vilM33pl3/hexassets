rotate(a = [0, 0, -90])
difference()
{
    color("Peru", 1.0)
    {
        // hexagon base
        linear_extrude(height = 4, center = false, convexity = 10, twist = 0)
        circle(r=15, $fn=6);
    }
    
    color("Blue", 1.0)
    {
        // canal shape
        rotate([90,0,0])
        linear_extrude(height=30, center=true, convexity = 10, twist = 0)
        polygon(points=[[-4.75,4.01],[4.75,4.01],[2.5,2], [-2.5,2]]);
    }
    
}
