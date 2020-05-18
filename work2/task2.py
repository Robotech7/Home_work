words = 'А роза упала на лапу Азора.'
a = len(words)
middle = int((a + 1) / 2)
result = f'{words[middle:]}{words[:middle]}'
print(result)