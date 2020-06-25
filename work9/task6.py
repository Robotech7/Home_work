from django.db.models import Q

item = Pet.objects.filter(name__iexact='Max')
item.filter(Q(type='cat') | Q(type='fish')).delete()