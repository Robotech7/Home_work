array = [1, 2, 3]

def func(x):
    return x**2

def map(array, func):
    return array + func(array)

print(map(array,func))



