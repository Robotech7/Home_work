from functools import reduce

array = [1, 2, 3, 4, 5]

def func(x, y):
    return x + y


def reduce(array, func, init=None):
    it = iter(array)
    if init is None:
        init = next(it)
    accum = init
    for x in it:
        accum = func(accum, x)
    return accum


print(reduce(array, func,))