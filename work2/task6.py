words = "The quick brown fox jumps over the lazy dog"
result = len(set(words.replace(' ', '').lower())) == 26

print(result)