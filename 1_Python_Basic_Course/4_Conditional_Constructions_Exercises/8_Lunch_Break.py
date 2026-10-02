from math import ceil
serial_name = str(input())
episode_duration = int(input())
break_duration = int(input())

lunch_duration = break_duration * 0.125
chill_duration = break_duration * 0.25

time_left = break_duration - lunch_duration - chill_duration - episode_duration

if time_left >= 0:
    print(f"You have enough time to watch {serial_name} and left with {ceil(time_left)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {ceil(time_left * -1)} more minutes.")