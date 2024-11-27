'''
WAP to define a class Point with coordinates x and y as attributes. Create relevant
methods and print the objects. Also define a method distance to calculate the distance
between any two point objects.
'''
import math 
class point:
    def __init__(self,x,y) -> None:
        """Initialize a Point object with x and y coordinates."""
        self.x = x
        self.y = y
        
    def __str__(self):
        """Provide a string representation of the Point object."""
        return f"Point({self.x}, {self.y})"
    
    def distance(self,other):
        """
        Calculate the distance between this point and another point.
        
        Args:
            other (Point): Another Point object to calculate the distance to.
        
        Returns:
            float: The distance between the two points.
        """
        return math.sqrt((other.x-self.x)**2 + (other.y-self.y)**2)
    
# Example usage
if __name__ == "__main__":
    point1 = point(3, 4)
    point2 = point(7, 1)
    
    print("Point 1:", point1)
    print("Point 2:", point2)
    print("Distance between Point 1 and Point 2:", point1.distance(point2))    