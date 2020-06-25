from django.db.models import Count

objects = Pet.objects.values_list('type').annotate(
    total=Count('type')).order_by('-total')
Pet.objects.filter(type=objects[0][0]).update(type='horse')