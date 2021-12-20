import turtle

class Polygons:
    def __init__(self,name,sides,color = "red"):
        self.name = name
        self.no_of_sides = sides
        self.angles = ((self.no_of_sides-2)*180)/(self.no_of_sides)
        self.pensize = self.no_of_sides*2
        self.size = self.no_of_sides*50
        self.color = color
    
    def sum_angles(self):
        return (self.no_of_sides-2)*180
    
    def draw(self):
        turtle.pensize(self.pensize)
        turtle.color(self.color)
        for i in range(self.no_of_sides):
            turtle.forward(self.size)
            turtle.left(180-self.angles)
        turtle.done
        
class Square(Polygons):
    def __init__(self,color="green"):
        """A sub class which inherits attributes and methods from the parent"""
        super().__init__("square",4, color=color)
            
poly3 = Polygons("Triangle",3)
poly4 = Polygons("Square",4,)
poly5 = Polygons("Pentagon",5,"yellow")
poly6 = Polygons("Hexagon",6,"blue")


# draw_poly = [poly3.draw(),poly4.draw(),poly5.draw(),poly6.draw()]
square = Square()
print(square.sum_angles())
square.draw()