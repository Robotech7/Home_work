import re

word = 'better'
file = open('filename.txt', 'r').read()
result = file.lower().count(word)
print(result)
result = len((re.findall(word, file)))