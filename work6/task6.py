
lib = {}
for item in history:
    dt = item['access_date']
    if dt not in lib:
        lib[dt] = {}
    if item['access_type'] in lib[dt]:
        lib[dt][item['access_type']] += 1
    else:
        lib[dt][item['access_type']] = 1
result = {}
for item in sorted(lib):
    result[item] = lib[item]

print(result)
print(lib, sep='\n')






