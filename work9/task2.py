result = []
for item in childs_new:
    children = Child.objects.create(name=item['name'])
    for pet in item['pets']:
        object = Pet(name=pet['name'], type=pet['type'], owner=children)
        result.append(object)
Pet.objects.bulk_create(result)