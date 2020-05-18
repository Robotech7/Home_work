from math import sqrt, pow


def is_pow(x):
    for number in range(2, 1000):
        for y in range(2, 21):
            if number**y == x:
                return True
    return False

print(is_pow(169))
