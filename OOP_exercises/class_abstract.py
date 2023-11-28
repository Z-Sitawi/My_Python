from abc import *


class Form(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def surface(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Form):
    def __init__(self, r, color):
        Form.__init__(self, color)
        self.rayon = r

    def surface(self):
        return self.rayon ** 2 * 3.14

    def perimeter(self):
        return self.rayon * 2 * 3.14

    def __str__(self):
        return (f"La coleur de cercle: {self.color}\nLa surface de cercle: {self.surface()} m²\n"
                f"Le périmétre de cercle: {self.perimeter()} m\n")


class Carree(Form):
    def __init__(self, cout, color):
        Form.__init__(self, color)
        self.cout = cout

    def surface(self):
        return self.cout ** 2

    def perimeter(self):
        return self.cout * 4

    def __str__(self):
        return (f"La coleur de carrée: {self.color}\nLa surface de carrée: {self.surface()} m²\n"
                f"Le périmétre de carrée: {self.perimeter()} m\n")


class Rectangle(Form):
    def __init__(self, lon, lar, color):
        Form.__init__(self, color)
        self.lon = lon
        self.lar = lar

    def surface(self):
        return self.lon * self.lar

    def perimeter(self):
        return (self.lar + self.lon) * 2

    def __str__(self):
        return (f"La coleur de rectangle: {self.color}\nLa surface de rectangle: {self.surface()} m²\n"
                f"Le périmétre de rectangle: {self.perimeter()} m\n")


circle = Circle(3, "rouge")
square = Carree(4, "Blue")
rectangle = Rectangle(4, 5, "Noir")

print(circle, square, rectangle, sep="\n-------------------------\n", )