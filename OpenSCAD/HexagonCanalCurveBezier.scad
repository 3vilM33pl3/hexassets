// resolution bezier curve
deltat = 0.02;

// cubic bexier curve function
function cubic_bezier(p0,p1,p2,p3) = [for (t=[0:deltat:1+deltat]) pow(1-t,3)*p0+3*pow((1-t),2)*t*p1+3*(1-t)*pow(t,2)*p2+pow(t,3)*p3];
    
function reverse(v) = [for (i=[len(v)-1:-1:0]) v[i]];
function delete_first(v) = [for (i=[1:len(v)-1]) v[i]]; 


p10 = [-4.75,4.0 + 1/128];
p11 = [-2.75,4.0];
p12 = [-4.8,2.2];
p13 = [0.0,2.0 + 1/128];

p20 = [4.75,4.0 + 1/128];
p21 = [2.75,4.0];
p22 = [4.8,2.2];
p23 = [0.0,2.0 + 1/128];



// bezier curve for cx
points_left = cubic_bezier(p10, p11, p12, p13);
points_right = reverse(cubic_bezier(p20, p21, p22, p23));
points = concat(points_left, points_right);

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
        translate([22.5,-12.99,0])
        rotate_extrude(angle=360, convexity=10, $fn=90)
        translate([-22.5,0,0])
        polygon(points);
    }
    
}
