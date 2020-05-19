from itertools import zip_longest


class Polynome:
    """Операции с многочленами"""

    def __init__(self, array: list):
        self.array = array

    def __add__(self, other):
        result = [x + y for x, y in zip_longest(self.array, other.array, fillvalue=0)]
        return Polynome(result)

    def __sub__(self, other):
        result = [x - y for x, y in zip_longest(self.array, other.array, fillvalue=0)]
        return Polynome(result)

    def __mul__(self, other):
        result = [x - y for x, y in zip_longest(self.array, other.array, fillvalue=0)]
        return Polynome(result)

    def calc(self, x):
        result = 0
        for number, item in enumerate(self.array):
            result = result + item * x ** number
        # y = 0
        # while y < len(self.array):
        #     result = result + self.array[y] * x ** y
        #     y += 1
        return result


a = Polynome([-5, 15, -16, 11])
b = Polynome([1, -5, 2, 23])

c = a + b
print(a.calc(5))
