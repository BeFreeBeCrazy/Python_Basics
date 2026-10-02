projection_type = str(input())
rows = int(input())
columns = int(input())  

if projection_type == 'Premiere':
    ticket = 12
elif projection_type == 'Normal':
    ticket = 7.50
elif projection_type == 'Discount':
    ticket = 5

seats = rows * columns

income = seats * ticket

print(f'{income:.2f} leva')