result = []
for item in pets_new:
    result.append(Pet(name=item['name'], type=item['type']))
Pet.objects.bulk_create(result)