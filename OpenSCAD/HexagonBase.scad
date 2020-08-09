color("Peru", 1.0)
{
    rotate(a = [0, 0, -90])
    linear_extrude(height = 4, center = false, convexity = 10, twist = 0)
    circle(r=15, $fn=6);
}