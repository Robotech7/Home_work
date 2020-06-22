import os
import collections


path_list = [
    '/path/path/1.txt',
    '/path/path/1.py',
    '/path/path/1.txt',
    '/path/path/1.py',
    '/path/path/1.txt',
    '/path/path/1.docx',
    '/path/path/1.txt',
]


result = collections.defaultdict(int)

for line in path_list:
    ext = os.path.splitext(line)[1]
    result[ext] += 1