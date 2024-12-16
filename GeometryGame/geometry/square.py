from geometry.rectangle import Rectangle 
from geometry.point import Point 

class Square(Rectangle):
    """
        Represents a square, which is a special case of a rectangle 
        where all sides are of equal length.
        Hence, Square is a subclass of Rectangle. It inherits all the properties of a Rectangle. 
    """
    def __init__(self, lowleft:"Point", sidelength:float) -> None:
        '''
            Initialize the square by using the bottom-left point 
            and the length of one side.
            :param lowleft: Point instance (bottom-left corner of square)
            :param side_length: Length of the square's sides
            
            Here is a clearer order of events:

                Square's __init__ starts.
                Compute upright Point.
                Call Rectangle's __init__ via super() to initialize lowleft and upright.
                Return to Square's __init__ to set self.side_length.
                Object creation is complete.
        '''
        # Compute the upright point based on the side_length
        upright = Point(lowleft.x+sidelength, lowleft.y+sidelength)
        
        # call the parent class constructor 
        """
            The line super().__init__(lowleft, upright) is used to call the parent class's constructor in Python. It allows a child class to reuse or initialize the attributes of its parent class without rewriting the code.
            
            What is super()?
                super() returns a proxy object that represents the parent class of the current class. It allows you to call methods or access attributes in the parent class.
        """
        super().__init__(lowleft, upright)
        self.sidelength = sidelength
    
    # def area(self):
    #     """
    #         Calculates the area of the square instance
    #     """
    #     return super().area()
        
    """
    Python will look for the area method in the Square class.
    Since it is not defined there, Python will search the parent class (Rectangle) for the method.
    The Rectangle.area() method will be called, and it will calculate the area correctly because the lowleft and upright attributes are already set appropriately for a square.
    """
    
    def perimeter(self):
        """
            Calculates the perimeter of the Square 
        """
        return 4*self.sidelength
    
if __name__=="__main__":
    # creata a square instance 
    square_1 = Square(Point(0,0),5)
    
    # calculate area 
    print(f"The are of the square is : {square_1.area()}")
    
    # calculate perimeter
    print(f"The perimeter of the square is {square_1.perimeter()}")