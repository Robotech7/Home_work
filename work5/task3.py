import re

file = open('filename.txt', 'r').read()

rows = len(file.split('\n'))
words = len((re.findall(r'\w+', file)))
letters = len(re.findall('[a-zA-Z]', file))

print(rows, words, letters)