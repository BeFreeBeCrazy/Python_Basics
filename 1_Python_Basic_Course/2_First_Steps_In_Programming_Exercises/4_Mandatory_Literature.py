number_of_pages = int(input())
pages_per_hour = int(input())
days = int(input())


hours_per_day_needed = (number_of_pages / pages_per_hour) / days

print(round(hours_per_day_needed))