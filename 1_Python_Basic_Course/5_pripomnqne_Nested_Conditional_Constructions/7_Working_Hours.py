hour = int(input())
day = str(input())
state = ""

if (day == "Monday" 
    or day == "Tuesday" 
    or day == "Wednesday" 
    or day == "Thursday" 
    or day == "Friday"
    or day == "Saturday"):
    if 10 <= hour <= 18:
        state = "open"
    else:
        state = "closed"
else:
    state = "closed"

print (state)
