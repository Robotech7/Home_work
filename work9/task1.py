from django.db.models import Count
# модель называется не Pet, а Pets(Или указан related_name)
objects = Child.objects.annotate(counter=Count('pets'))
result = []
for object in objects:
    if object.counter == 1 or object.counter == 4:
        result.append(object.name)
result.sort(reverse=True)