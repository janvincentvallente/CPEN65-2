#Finding the Area of the circle using OOP Concepts
#Using Polymorphism

class Circle:
  def __init__(self, side):
    self.side = side

class Radius(Circle):
  def area(self):
    return (3.14 * (self.side * self.side))

class Diameter(Circle):
  def area(self):
    return ((3.14 * (self.side * self.side)) / 4)

print("Area of the Circle")
print()

object = Radius(4)
print("Radius=", object.side, "\nArea =", object.area())

object2 = Diameter(4)
print("\nDiameter=", object2.side, "\nArea =", object2.area())