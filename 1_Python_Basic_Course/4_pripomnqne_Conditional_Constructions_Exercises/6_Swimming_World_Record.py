from math import floor

record_in_seconds = float(input())
destination_in_metres = float(input())
time_for_1_metre = float(input())

delay = (floor((destination_in_metres / 15)) * 12.5)
Ivan_time = destination_in_metres * time_for_1_metre + delay
last_calculations = Ivan_time - record_in_seconds

if Ivan_time >= record_in_seconds:
    print (f"No, he failed! He was {(last_calculations):.2f} seconds slower.")
else:
    print (f"Yes, he succeeded! The new world record is {Ivan_time:.2f} seconds.")