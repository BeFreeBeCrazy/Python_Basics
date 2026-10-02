hour = int(input())
day = str(input())
state = ""

if (day == "Monday" 
    or day == "Tuesday" 
    or day == "Wednesday" 
    or day == "Thursday" 
    or day == "Friday"):
    if 10 <= hour <= 18:
        state = "open"

if state == "open":
    print("open")
else:
    print("closed")