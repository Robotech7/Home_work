import collections
import itertools as it
from work7.data2 import activities_iter

n = 2

all_active = collections.Counter()
for item in activities_iter:
    all_active[item.user.username] += 1
group = it.groupby(sorted(activities_iter, key=lambda x: x.user.username),
                          key=lambda x: x.user.username)
active_days = {}
for x, y in group:
    gr = it.groupby(sorted(y, key=lambda x: x.activity_date),
                           key=lambda x: x.activity_date)
    active_days[x] = len(list(gr))
before_result = []
for x in all_active:
    score = all_active[x] / active_days[x]
    res_tuple = collections.namedtuple('Top', ['username', 'score'])
    before_result.append(res_tuple(x, score))
before_result.sort(key=lambda x: x[1], reverse=True)
result = []
for item in it.islice(before_result, n):
    result.append(item)



