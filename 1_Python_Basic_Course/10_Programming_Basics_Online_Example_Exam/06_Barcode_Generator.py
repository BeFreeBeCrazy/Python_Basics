number1 = int(input())
number2 = int(input())


x = str(number1)
y = str(number2)

integer1_1 = int(x[0])
integer2_1= int(x[1])
integer3_1= int(x[2])
integer4_1= int(x[3])

integer1_2 = int(y[0])
integer2_2= int(y[1])
integer3_2= int(y[2])
integer4_2= int(y[3])

for x1 in range(integer1_1, integer1_2 + 1):
    if x1 % 2 != 0:
        for x2 in range(integer2_1, integer2_2 + 1):
            if x2 % 2 != 0:
                for x3 in range(integer3_1, integer3_2 + 1):
                    if x3 % 2 != 0:
                        for x4 in range(integer4_1, integer4_2 + 1):
                            if x4 % 2 != 0:
                                print(f"{x1}{x2}{x3}{x4}", end = " ")
                            if x4 % 2 == 0 or x1 == 0:
                                continue
                    if x3 % 2 == 0 or x1 == 0:
                        continue
            if x2 % 2 == 0 or x1 == 0:
                continue
    if x1 % 2 == 0 or x1 == 0:
        continue

























# count = 0

# for x in range(number1, number2 + 1):
#     x = str(x)
#     for char in x:
#         # count += 1
#         integer = int(char)
#         if integer % 2 == 0 or integer == 0:
#             count = 0
#             break
#         if count == 4:
#             print(x, end = " ")

