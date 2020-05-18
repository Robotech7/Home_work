moment = 12555
hours = moment // 60
minutes = moment % 60

if hours > 24:
    hours = hours % 24
if hours < 10:
    hours = f'0{hours}'
if minutes < 10:
    minute = f'0{minutes}'
result = f'{hours}:{minutes}'
