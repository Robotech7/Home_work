students = [
{'name': 'Ivanov', 'grade': 2.3},
{'name': 'Petrov', 'grade': 2.1},
{'name': 'Sidorov', 'grade': 3.5},
{'name': 'Smirnov', 'grade': 2.3}
]
rating = []
for item in students:
    rating.append(item.get('grade'))
rating.sort()
result = []
for item in students:
    if item['grade'] == rating[1]:
        result.append(item['name'])
print(result)