import operator

user = {
    'first_name': 'Ivanov',
    'second_name': 'Sidorov',
    'middle_name': 'popov'
}

result = operator.itemgetter('first_name', 'second_name', 'middle_name')(user)
print(result)
