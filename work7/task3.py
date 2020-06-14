from collections import defaultdict
from itertools import chain
from work7.data import responses
data = chain.from_iterable(responses)
iterator = sorted(data, key=lambda x: x['time'])
result = defaultdict(str)
for item in iterator:
    result[item['hash']] = item['log']
print(result)

