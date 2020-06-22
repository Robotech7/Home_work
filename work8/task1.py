import os

press_result = []
for line in dir_list:
    press_result.append(os.path.abspath(line))
result = len(set(press_result))