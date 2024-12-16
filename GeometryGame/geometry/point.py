import math

class Point:
    """
        Represents a point in two-dimensional geometric coordinates
        >>> p_0 = Point()
        >>> p_1 = Point(3, 4)
        >>> p_0.calculate_distance(p_1)
        5.0
    """
    def __init__(self, x:float = 0, y:float = 0) -> None:
        """
            Initialize the position of a new point. The x and y coordinates can be specified. If they are not, the point defaults to the origin.
            :param x: float x-coordinate
            :param y: float x-coordinate
        """
        self.move(x,y)
    
    def move(self, x:float, y:float) -> None:
        """
            Move the point to a new location in 2D space.
            :param x: float x-coordinate
            :param y: float x-coordinate
        """
        self.x = x
        self.y = y 
    
    def reset(self) -> None:
        """
            Resets the point to origin (0,0)
        """
        self.move(0,0)
    
    def calculate_distance(self, other: "Point") -> float:
        """
            Calculate the Euclidean distance from this point
            to a second point passed as a parameter.
            :param other: Point instance
            :return: float distance
        """
        if not isinstance(other, Point):
            raise TypeError("The 'other' parameter must be an instance of Point.")

        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    
    def is_inside_rectangle(self, rectangle:"Rectangle") -> bool:
        """
            Returns True if the point is inside the rectangle defined by leftpoint and rightpoint otherwise rturns False
            :param rectangle: Rectangle instance 
            :return: string 
        """
        # import late to avoid the circular Importerror 
        from .rectangle import Rectangle 
        
        condition_1 = rectangle.lowleft.x<self.x<rectangle.upright.x
        condition_2 = rectangle.lowleft.y<self.y<rectangle.upright.y
        
        if condition_1 and condition_2:
            return f"The point {self}, is inside the rectangle!"
        else:
            return f"The point {self}, is not inside the rectangle!"
    
    def __str__(self) -> str:
        """
            Returns a string representation of the point object
        """
        return f"({self.x},{self.y})"
    