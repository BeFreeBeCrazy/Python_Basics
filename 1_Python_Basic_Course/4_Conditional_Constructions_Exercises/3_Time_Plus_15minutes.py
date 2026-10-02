hours = int(input())
minutes = int(input())

added_minutes = minutes + 15

if added_minutes >= 60:
    hours += 1
    added_minutes -= 60

if hours == 24:
    hours = 0

if added_minutes > 10:
    print(f'{hours}:{added_minutes}')
else:
    print(f'{hours}:{added_minutes:02d}')

# print(f'{added_minutes:02d}')