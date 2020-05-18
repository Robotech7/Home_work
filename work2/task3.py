words = "The best thing about a boolean is even i you are wrong, you are only off by a bit."
number = words.count('f')
if number > 1:
    result = words.find('f') + words.rfind('f')
else:
    result = words.find('f')

print(result)