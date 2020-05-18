from math import sqrt


def distance(x1, y1, x2, y2):
    catet = x2 - y2
    catet_2 = y1 - x1
    square = (catet * catet_2) / 2
    return round(square, 2)

print(distance(-27.421981390810785, 63.6331756176304, 83.33001016755915, 1.2648265646875103))