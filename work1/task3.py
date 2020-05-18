number = 8
time_lesson = number * 45
number_break = number + 1
time_break = (number_break // 2) * 15 + (number_break % 2) * 5
all_time = time_lesson + time_break
hours = all_time // 60 + 9
minute = all_time % 60
if hours < 10:
    hours = f'0{hours}'
if minute < 10:
    minute = f'0{minute}'
print(f'{hours}:{minute}')
