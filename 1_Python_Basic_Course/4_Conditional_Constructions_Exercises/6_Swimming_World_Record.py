from math import floor
record_seconds = float(input())
metres = float(input())
time_for_1m = float(input())

resistence = floor(metres / 15)
seconds_after_resistence = resistence * 12.5

Ivan_time = metres * time_for_1m
Ivan_time_after_resistence = Ivan_time + seconds_after_resistence
Ivan_time_minus_record = Ivan_time_after_resistence - record_seconds
Ivan_record = Ivan_time + seconds_after_resistence

if Ivan_record >= record_seconds:
    print(f"No, he failed! He was {Ivan_time_minus_record:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {Ivan_record:.2f} seconds.")