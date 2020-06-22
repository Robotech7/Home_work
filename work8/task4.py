import os

files_heap = [
    'song.mp3',
    'film.avi',
    'film1.avi',
    'document.txt',
    'document.docx',
    'doc.docx'
]

path_map = {'.rtf': 'dir2/dir0/dir1', '.rty': 'dir2/dir0/dir1',
            '.waf': 'dir1/dir0', '.html': 'dir1/dir0', '.xml': 'dir0'}

result = []
for line in files_heap:
    ext = os.path.splitext(line)[1]
    result.append(os.path.join(path_map[ext], line))


