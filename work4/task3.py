class Complex:

    def __init__(self, real: int, imag: int):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        new_real = self.real + other.real
        new_imag = self.imag + other.imag
        return Complex(new_real, new_imag)

    def __sub__(self, other):
        new_real = self.real - other.real
        new_imag = self.imag - other.imag
        return Complex(new_real, new_imag)

    def __mul__(self, other):
        new_real = (self.real * other.real - self.imag * other.imag)
        new_imag = (self.real * other.imag + other.real * self.imag)
        return Complex(new_real, new_imag)

    def __truediv__(self, other):
        k = other.real * other.real + other.imag * other.imag
        new_real = (self.real * other.real + self.imag * other.imag) / k
        new_imag = (self.imag * other.real - self.real * other.imag) / k
        return Complex(new_real, new_imag)

    def __str__(self):
        return f'{self.real:.2f}{self.imag:+.2f}j'

a = Complex(70.90088491736537, -50.88769534913222)
b = Complex(74.99129783010608, -70.01206492985173)
print(a / b)