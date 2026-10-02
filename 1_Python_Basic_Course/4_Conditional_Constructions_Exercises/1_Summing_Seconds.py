first_runner = int(input())
second_runner = int(input())
third_runner = int(input())
hours = 0

summed_seconds = first_runner + second_runner + third_runner

if summed_seconds >= 60:
    hours += 1
    summed_seconds -= 60
if hours >= 1 and summed_seconds >=60:
    hours += 1
    summed_seconds -= 60

print(f'{hours}:{summed_seconds:02d}')



# first_runner = int(input())
# second_runner = int(input())
# third_runner = int(input())
# total_time = first_runner + second_runner + third_runner

# minutes = total_time // 60
# seconds = total_time % 60

# if seconds < 10:
#     print(f'{minutes}:0{seconds}')
# else:
#     print(f'{minutes}:{seconds}')