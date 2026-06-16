# 52 program DAY NUMBER TO DAY NAME 
day_number = int(input("ENTER THE DAY NUMBER : "))
if day_number >= 1 and day_number <= 7 :
    if day_number == 1 :
        print("THE DAY WILL BE SUNDAY")
    elif day_number == 2 :
        print("THE DAY WILL BE MONDAY")
    elif day_number == 3 :
        print("THE DAY WILL BE TUESDAY")
    elif day_number == 4 :
        print("THE DAY WILL BE WEDNESDAY")
    elif day_number == 5 :
        print("THE DAY WILL BE THURSDAY")
    elif day_number == 6:
        print("THE DAY WILL BE FRIDAY")
    else :
        print("THE DAY WILL BE SATURDAY")
else :
    print("PLEASE ENTER THE DAY NUMBER IN BETWEEN 1 TO 7")
