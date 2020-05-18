numbers = [626, 95, 987, 813, 247, 116, 239, 474, 264, 989, 85, 920, 884, 88, 324, 40, 957, 986, 630, 748, 486, 296, 342]
result = []
for x, item in enumerate(numbers):
    try:
        if numbers[x+1] > item:
            result.append(numbers[x+1])
    except IndexError:
        break
print(result)