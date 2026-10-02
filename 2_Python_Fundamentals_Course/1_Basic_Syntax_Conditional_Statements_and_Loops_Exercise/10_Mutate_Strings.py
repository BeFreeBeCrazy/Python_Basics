first_string = str(input())
second_string = str(input())

unique_string_checker = first_string

for _ in range (len(first_string)):
    for __ in second_string:
        right_side = (first_string[_ + 1:])
        left_side = (second_string[:_ + 1])
        whole_string = left_side + right_side
        if unique_string_checker != whole_string:
            print(whole_string)
        unique_string_checker = whole_string