from geometry import Point, Rectangle, Square, Cuboid

def test_Point():
    # Create a object from the Point class
    point_1 = Point(3,4)
    print(f"The first point is : {point_1}")
            
    point_2 = Point(8,15)
    print(f"The first point is : {point_2}")
        
    # Let us calculate the distance between the two 
    print(f"The distance between points {point_1} and {point_2} is: {point_1.calculate_distance(point_2)}")
            
    point_3 = Point(5,6)
    # Create a Rectangle instance and use it to find if the point ininside the rectangle
    rect_1 = Rectangle(point_1, point_2)
        
    print(point_3.is_inside_rectangle(rect_1))
    
def test_Rectangle():
    # Create a rectangle instance and calculate area 
    lowleft = Point()
    upright = Point(4,4)
    rect_2 = Rectangle(lowleft, upright)
    
    print(f"The area of the rectangle is : {rect_2.area()}")
    
def test_Square():
    # creata a square instance 
    square_1 = Square(Point(0,0),5)
    
    # calculate area 
    print(f"The are of the square is : {square_1.area()}")
    
    # calculate perimeter
    print(f"The perimeter of the square is {square_1.perimeter()}")

def test_Cuboid():
    # Create the bottom-left and upper-right points of the rectangle base
    lowleft = Point(0, 0)
    upright = Point(4, 3)

    # Create a Cuboid with height = 5
    cuboid = Cuboid(lowleft, upright, 5)

    print(f"Volume of cuboid: {cuboid.volume()}")            # Output: 60
    print(f"Surface area of cuboid: {cuboid.surface_area()}")  # Output: 94