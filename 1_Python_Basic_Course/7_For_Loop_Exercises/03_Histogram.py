number_count = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0



for _ in range(number_count):
    new_number = int(input())
    if new_number < 200:
        p1 += 1
    elif new_number <= 399:
        p2 += 1
    elif new_number <= 599:
        p3 += 1
    elif new_number <= 799:
        p4 += 1
    elif new_number <= 1000:
        p5 += 1

p1_calculation = p1 / number_count * 100
p2_calculation = p2 / number_count * 100
p3_calculation = p3 / number_count * 100
p4_calculation = p4 / number_count * 100
p5_calculation = p5 / number_count * 100

print(f"{p1_calculation:.2f}%")
print(f"{p2_calculation:.2f}%")
print(f"{p3_calculation:.2f}%")
print(f"{p4_calculation:.2f}%")
print(f"{p5_calculation:.2f}%")
