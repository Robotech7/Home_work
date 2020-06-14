import itertools as it

data_list_iter = ('a', 'b', 'c')
even_numbers = it.count(0, 2)
result = {next(even_numbers): value for value in data_list_iter}
print(result)


