
class Fraction:
    """Объект дробь."""

    def __init__(self, top: int, bottom: int):
        k = Fraction.gcd(top, bottom)
        self.top = top / k
        if bottom == 0:
            raise ZeroDivisionError('Знаменатель не может быть равным 0')
        self.bottom = bottom / k

    @classmethod
    def gcd(cls, top, bottom):
        top = abs(top)
        bottom = abs(bottom)
        while bottom:
            top, bottom = bottom, top % bottom
        return top

    # def c(self):
    #     top = abs(self.top)
    #     bottom = abs(self.bottom)
    #     while bottom:
    #         top, bottom = bottom, top % bottom
    #     self.top = self.top / top
    #     self.bottom = self.bottom / top

    def __add__(self, other):
        new_top = self.top * other.bottom + self.bottom * other.top
        new_bottom = self.bottom * other.bottom
        deleting = Fraction.gcd(new_top, new_bottom)
        return Fraction(new_top / deleting, new_bottom / deleting)

    def __sub__(self, other):
        new_top = self.top * other.bottom - self.bottom * other.top
        new_bottom = self.bottom * other.bottom
        k = Fraction.gcd(new_top, new_bottom)
        return Fraction(new_top / k, new_bottom / k)

    def __mul__(self, other):
        new_top = self.top * other.top
        new_bottom = self.bottom * other.bottom
        k = Fraction.gcd(new_top, new_bottom)
        return Fraction(new_top / k, new_bottom / k)

    def __truediv__(self, other):
        new_top = self.top / other.top
        new_bottom = self.bottom / other.bottom
        k = Fraction.gcd(new_top, new_bottom)
        return Fraction(int(new_top / k), int(new_bottom / k))

    def __eq__(self, other):
        if self.top / self.bottom == other.top / other.bottom:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.top / self.bottom > other.top / other.bottom:
            return True
        else:
            return False

    def __le__(self, other):
        if self.top / self.bottom <= other.top / other.bottom:
            return True
        else:
            return False

    def __str__(self):
        return f'Fraction{int(self.top), int(self.bottom)}'


a = Fraction(5, 2)
b = Fraction(5, 2)

c = a / b
print(c)
