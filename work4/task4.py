from math import pi


class Figure:
    """Класс фигур"""

    def __init__(self, *args):
        self.args = args

    def area(self, *args):
        pass

    def perimeter(self, *args):
        pass


class Triangle(Figure):
    """Класс треугольник"""

    def area(self):
        p = sum(self.args) / 2
        area = (p * (p - self.args[0]) * (p - self.args[1])
                * (p - self.args[2])) ** 0.5
        return area

    def perimeter(self):
        return sum(self.args)


class Rectangle(Figure):
    """Класс прямоугольник"""

    def area(self):
        area = self.args[0] * self.args[1]
        return area

    def perimeter(self):
        return sum(self.args)


class Circle(Figure):
    """Класс круг"""

    def perimeter(self):
        return self.args[0] * 2 * pi

    def area(self):
        return self.args[0] ** 2 * pi


a = Triangle(93.70222348950283, 50.77844960729303, 55.56273091185004)

print(a.perimetr())
print(a.area())
