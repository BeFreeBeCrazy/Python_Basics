from math import ceil

serial_name = str(input())
duration_of_episode = float(input())
break_duration = float(input())

lunchtime = 0.125 * break_duration
relax_time = 0.25 * break_duration

last_calculations = break_duration - lunchtime - relax_time - duration_of_episode

if last_calculations >= 0:
    print (f"You have enough time to watch {serial_name} and left with {(ceil(last_calculations))} minutes free time.")
elif last_calculations < 0:
    print (f"You don't have enough time to watch {serial_name}, you need {(ceil(last_calculations * -1))} more minutes.")