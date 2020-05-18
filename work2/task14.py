list_one = ['apple', 1, 'banana', 5, 2]
list_two = ['apple', 2, 2, 'peach']

result = list(set(list_one) & set(list_two))
print(result)