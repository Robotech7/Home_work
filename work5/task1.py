file = open('filename.txt', 'r')

lect = 0
pract = 0
lab = 0
for x in file:
    if 'лекц.' in x:
        lect += 1
    elif 'практ.' in x:
        pract += 1
    elif 'лаб.' in x:
        lab += 1
print(lect, pract, lab)

