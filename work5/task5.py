file = open('filename.txt', 'r')
file_2 = open('outfilename.txt', 'w')

data = file.read()
word_dict = {}
for letter in data:
    if letter in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
        if letter in word_dict:
            word_dict[letter] += 1
        else:
            word_dict[letter] = 1
for key in word_dict:
  if word_dict[key] >= 1:
    file_2.write(f'{key} {word_dict[key]}\n')
file_2.close()



