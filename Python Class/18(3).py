from abc import ABC, abstractclassmethod


class Polygon(ABC):
    @abstractclassmethod
    def noofsides(self):
        pass


class Triangle(Polygon):
    def noofsides(self):
        print('I have 3 sides')


class Pentagon(Polygon):
    def noofsides(self):
        print('I have 5 sides')


class Hexagon(Polygon):
    def noofsides(self):
        print('I have 6 sides')


class Quadrilateral(Polygon):
    def noofsides(self):
        print('I have 4 sides')


k = Polygon()
