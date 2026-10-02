first_string = str(input())
second_string = str(input())

unique_string_checker = first_string

for _ in range(len(first_string)):
    left_side = second_string[:_ + 1]
    right_side = first_string[_ + 1:]
    whole_string = left_side + right_side
    if whole_string != unique_string_checker:
        print(whole_string)
        unique_string_checker = whole_string