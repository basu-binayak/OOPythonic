from geometry.point import Point 
from geometry.rectangle import Rectangle 
from game.game_logic import start_game

if __name__ == "__main__":
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
    
    # Create a rectangle instance and calculate area 
    lowleft = Point()
    upright = Point(4,4)
    rect_2 = Rectangle(lowleft, upright)
    
    print(f"The area of the rectangle is : {rect_2.area()}")
    
    # Let us now pley the game 
    start_game()

    