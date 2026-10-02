hour = int(input())
minute = int(input())
arrive_hour = int(input())
arrive_minutes = int(input())
result = ""
printing = ""

transformation_minutes = hour * 60 + minute
transformation_arrival = arrive_hour * 60 + arrive_minutes
final_transformation = transformation_arrival - transformation_minutes

if -30 <= final_transformation <= 0:
    result = "On time"
elif final_transformation < -30:
    result = "Early"
elif final_transformation > 0:
    result = "Late"


if -59 <= final_transformation <= 0:
    printing = (f"{(final_transformation * -1)} minutes before the start")
elif -60 >= final_transformation:
    final_transformation *= -1
    if final_transformation >= 60:
        hh = final_transformation // 60
        mm = final_transformation % 60
    printing = (f"{hh}:{mm:02d} hours before the start")
elif 59 >= final_transformation >= 0:
    printing = (f"{final_transformation} minutes after the start")
elif final_transformation >= 60:
    hh = final_transformation // 60
    mm = final_transformation % 60
    printing =(f"{hh}:{mm:02d} hours after the start")

print(result)
print(printing)