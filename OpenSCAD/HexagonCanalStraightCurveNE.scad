difference()
{
    color("Peru", 1.0)
    {
        // hexagon base
        linear_extrude(height = 4, center = false, convexity = 10, twist = 0)
        circle(r=15, $fn=6);
    }
    
    color("DogerBlue", 1.0)
    {
        // canal shape
        rotate([90,0,0])
        linear_extrude(height=30, center=true, convexity = 10, twist = 0)
        polygon(points=[[-4.75,4.01],[4.75,4.01],[2.5,2], [-2.5,2]]);
    }
    
    color("DogerBlue", 1.0)
    {
        // canal shape
        translate([22.5,-12.99,0])
        rotate_extrude(angle=360, convexity=10, $fn=90)
        translate([-22.5,0,0])
        polygon(points=[[-4.75,4.01],[4.75,4.01],[2.5,2], [-2.5,2]]);
    }
    
}
