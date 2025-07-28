from .point import Point
from .rectangle import Rectangle

class Cuboid(Rectangle):
    """
        Represents a cuboid, which extends a rectangle
        into three dimensions by adding height.
    """
    def __init__(self, lowleft: "Point", upright: "Point", height: float) -> None:
        '''
            Initialize the cuboid using the bottom-left and upper-right
            points for the rectangle base, and a height for the 3D dimension.
            :param lowleft: Point instance (bottom-left corner of base)
            :param upright: Point instance (upper-right corner of base)
            :param height: Height of the cuboid
        '''
        # Initialize the rectangle part using parent class
        super().__init__(lowleft, upright)
        
        # Add the cuboid-specific attribute: height
        self.height = height

    def volume(self):
        '''
            Calculates the volume of the cuboid.
        '''
        base_area = super().area()  # Reuse Rectangle's area method
        return base_area * self.height

    def surface_area(self):
        '''
            Calculates the surface area of the cuboid.
        '''
        length = self.upright.x - self.lowleft.x
        breadth = self.upright.y - self.lowleft.y
        base_area = length * breadth
        side_area = 2 * (length * self.height + breadth * self.height)
        return 2 * base_area + side_area


