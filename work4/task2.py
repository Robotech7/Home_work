from itertools import zip_longest


class Polynome:
    """Операции с многочленами"""

    def __init__(self, array: list):
        self.array = array

    def __add__(self, other):
        result = [x + y for x, y in zip_longest(
            self.array, other.array, fillvalue=0)]
        return Polynome(result)

    def __sub__(self, other):
        result = [x - y for x, y in zip_longest(
            self.array, other.array, fillvalue=0)]
        return Polynome(result)

    def __mul__(self, other):
        result = [0] * (len(self.array) + len(other.array) - 1)
        for y1, item1 in enumerate(self.array):
            for y2, item2 in enumerate(other.array):
                result[y1 + y2] += item1 * item2
        return Polynome(result)

    def calc(self, x):
        result = 0
        for number, item in enumerate(self.array):
            result = result + item * x ** number
        return result

    def __str__(self):
        return f'Polynome{tuple([x for x in self.array])}'


a = Polynome([-12, -20])
b = Polynome([-11, 15, -1])

c = a * b
print(c.calc(-5))
