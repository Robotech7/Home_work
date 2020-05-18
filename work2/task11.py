numbers = [323, 132, 323, 313, 333, 321, 311, 132, 312, 311, 123]
result = []
for item in numbers:
    if numbers.count(item) == 1:
        result.append(item)
result.sort()
print(result)