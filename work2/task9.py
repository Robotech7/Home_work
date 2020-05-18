numbers = [5, -2, 5, -1, 4, -8, -10, -8, 9, -9, -8, 6, -6, -8, 5]
for x in range(1, len(numbers)):
    if (numbers[x-1] > 0 and numbers[x] > 0) \
            or (numbers[x-1] < 0 and numbers[x] < 0):
        result = numbers[x-1] + numbers[x]
        break
print(result)