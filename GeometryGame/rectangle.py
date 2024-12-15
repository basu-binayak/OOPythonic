import math
from point import Point 

class Rectangle:
    """
        Represents a rectangle defined by two points - one the leftmost point and the other the rightmost point 
    """
    def __init__(self, point_1:"Point", point_2:"Point") -> None:
        ''' 
            Initialize the rectangle by using the bottom leftmost point and the upper rightmost point.
            :param point_1: Point instance 
            :param point_2: Point instance
        '''
        self.point_1 = point_1
        self.point_2 = point_2

    def area(self):
        ''' 
            Calculates the area of the rectangle 
        '''
        length = self.point_2.x - self.point_1.x
        breadth = self.point_2.y - self.point_1.y
        area = abs(length*breadth)
        return (f'The area of the rectangle is {area}')

if __name__=="__main__":
    point_1 = Point()
    point_2 = Point(4,4)
    rect_1 = Rectangle(point_1, point_2)
    
    print(rect_1.area())