words = "Measuring programming progress by lines of code is like measuring aircraft building progress by weight."
# result = ''.join([words[x] for x in range(len(words)) if x % 3 != 0])
word_list = list(words)
del word_list[2::3]
result = ''.join(word_list)
print(result)