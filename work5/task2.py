import math

file = open('filename.txt', 'r')
dot_array = []
for line in file:
    dot_line = line.split()
    dot_array.append(list(map(int, dot_line)))
distance = []
for p in dot_array:
    k = math.hypot(p[0] - p[2], p[1] - p[3])
    distance.append(k)
print(min(distance))
