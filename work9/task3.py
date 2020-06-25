for item in childs_with_cats:
    children, created = Child.objects.get_or_create(name=item['name'])
    for pet in item['pets']:
        Pet.objects.update_or_create(
            name=pet['name'], owner=children, defaults=pet)