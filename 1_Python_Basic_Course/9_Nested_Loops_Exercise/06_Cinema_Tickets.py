movie_name = str(input())

count_tickets = 0
all_movies_tickets = 0

student_tickets = 0
standard_tickets = 0
kid_tickets = 0




while movie_name != "Finish":

    movie_name = str(movie_name)
    free_space = int(input())
    ticket_type = str(input())
    free_spaces_left = free_space

    while free_spaces_left > 0 and ticket_type != "End" and ticket_type != "Finish":
        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1

        free_spaces_left -= 1
        count_tickets += 1
        all_movies_tickets += 1

        if free_spaces_left > 0:
            ticket_type = input()
    print(f"{movie_name} - {count_tickets / free_space * 100:.2f}% full.")
    count_tickets = 0

    if ticket_type == "Finish":
        movie_name = ticket_type
    else:
        movie_name = str(input())


print(f"Total tickets: {all_movies_tickets}")
print(f"{student_tickets / all_movies_tickets * 100:.2f}% student tickets.")
print(f"{standard_tickets / all_movies_tickets * 100:.2f}% standard tickets.")
print(f"{kid_tickets / all_movies_tickets * 100:.2f}% kids tickets.")

