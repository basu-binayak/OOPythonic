import math
from geometry.point import Point 

class Rectangle:
    """
        Represents a rectangle defined by two points - one the leftmost point and the other the rightmost point 
    """
    def __init__(self, lowleft:"Point", upright:"Point") -> None:
        ''' 
            Initialize the rectangle by using the bottom leftmost point and the upper rightmost point.
            :param lowleft: Point instance 
            :param upright: Point instance
        '''
        self.lowleft = lowleft
        self.upright = upright

    def area(self):
        ''' 
            Calculates the area of the rectangle 
        '''
        length = self.upright.x - self.lowleft.x
        breadth = self.upright.y - self.lowleft.y
        area = abs(length*breadth)
        return area    

if __name__ == "__main__":
    
    # Create a rectangle instance and calculate area 
    lowleft = Point()
    upright = Point(4,4)
    rect_2 = Rectangle(lowleft, upright)
    
    print(f"The area of the rectangle is : {rect_2.area()}")
    