from functools import partial

rsorted = partial(sorted, reverse=True)
a = [1,2,3,4,5]
b = rsorted(a)
print(b)