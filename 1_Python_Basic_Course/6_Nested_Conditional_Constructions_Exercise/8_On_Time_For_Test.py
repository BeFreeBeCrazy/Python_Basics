hour_test_time = int(input())
minute_test_time = int(input())
hour_arrival_time = int(input())
minute_arrival_time = int(input())

on_time_or_not = ''

test_time_in_mins = hour_test_time * 60
arrival_time_in_mins = hour_arrival_time * 60

exam_total_time = test_time_in_mins + minute_test_time
atanas_total_time = arrival_time_in_mins + minute_arrival_time

difference_in_time = exam_total_time - atanas_total_time
reversed_difference_in_time = atanas_total_time - exam_total_time

total_hour_time = hour_test_time - hour_arrival_time
total_minute_time = minute_test_time - minute_arrival_time
reversed_total_hour_time = hour_arrival_time - hour_test_time
reversed_total_minute_time = minute_arrival_time - minute_test_time

if difference_in_time < 0:
    on_time_or_not = 'Late'
elif difference_in_time <= 30:
    on_time_or_not = 'On Time'
elif difference_in_time > 30:
    on_time_or_not = 'Early'


if difference_in_time != 0:
    if difference_in_time > 0:
        diff = difference_in_time  # early
    else:
        diff = -difference_in_time  # late

    hours = diff // 60
    minutes = diff % 60


if 0 < difference_in_time < 60:
    printing = f"{minutes} minutes before the start"
elif difference_in_time >= 60:
    if difference_in_time < 0:
        total_minute_time = total_minute_time * -1
    printing = f"{hours}:{minutes:02d} hours before the start"
# "mm minutes after the start" за закъснение под час
elif 0 > difference_in_time >= -59:
    printing = f"{minutes} minutes after the start"
elif difference_in_time <= -60:
    printing = f"{hours}:{(minutes):02d} hours after the start"

# "hh:mm hours after the start" за закъснение от 1 час или повече. Минутите винаги печатайте с 2 цифри, например "1:03”.

if difference_in_time == 0:
    print(on_time_or_not)
else: 
    print(on_time_or_not)
    print(printing)



# hour_test_time = int(input())
# minute_test_time = int(input())
# hour_arrival_time = int(input())
# minute_arrival_time = int(input())

# exam_total_time = hour_test_time * 60 + minute_test_time
# arrival_total_time = hour_arrival_time * 60 + minute_arrival_time

# difference = exam_total_time - arrival_total_time  # positive = early, negative = late

# # Determine status
# if difference < 0:
#     status = "Late"
# elif difference <= 30:
#     status = "On time"
# else:
#     status = "Early"

# print(status)

# # Print time difference if not exactly on time
# if difference != 0:
#     if difference > 0:
#         diff = difference  # early
#     else:
#         diff = -difference  # late

#     hours = diff // 60
#     minutes = diff % 60

#     if difference > 0:  # early
#         if diff < 60:
#             print(f"{minutes} minutes before the start")
#         else:
#             print(f"{hours}:{minutes:02d} hours before the start")
#     else:  # late
#         if diff < 60:
#             print(f"{minutes} minutes after the start")
#         else:
#             print(f"{hours}:{minutes:02d} hours after the start")

# print(hours)
# print(minutes)
