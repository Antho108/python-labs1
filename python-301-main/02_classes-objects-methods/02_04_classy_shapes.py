# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.
# https://stackoverflow.com/questions/30958425/object-oriented-python-rectangle-using-classes-and-functions

import math 

class Rectangle(): 
 
    def __init__(self, name,  length, width) :  
        self.name = name
        self.length = length
        self.width = width 
     
    def perimeter_rectangle(self):
        return 2 * (self.length + self.width)
    
    def area(self):
        return self.width * self.length

    def __str__(self) :
        return f'{self.name}, have a perimeter of {self.perimeter_rectangle()}, and its area is {self.area()}'


rectangle_test = Rectangle("Rect", 2, 3)
print(rectangle_test)


class Circle(): 
             
    def __init__(self, name,  radius) :
        self.name = name
        self.ray = radius 
            
    def area(self):
        return math.pi * (self.ray*self.ray)

    def circumference(self): 
        return math.pi * (2*self.ray)
 
    def __str__(self) :
        return f'{self.name}, have an area of {self.area()}, and a circumference of {self.circumference(),}'


circle_test = Circle("Circle", 5)
print(circle_test)