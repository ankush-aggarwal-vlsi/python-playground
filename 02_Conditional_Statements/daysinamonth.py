# 54 program DAYS IN A MONTH
month_name = ["JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE","JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER"]
month_number = int(input("ENTER THE MONTH NUMBER : "))
if month_number <= 12 and month_number >= 1 :
    month_name = month_name[month_number - 1]
    if month_number == 1 or month_number == 3 or month_number == 5 or month_number == 7 or month_number == 8 or month_number == 10 or month_number == 12 :
        print("THE CURRENT MONTH IS",month_name,"HAS 31 DAYS")
    elif month_number == 4 or month_number == 6 or month_number == 9 or month_number == 11:
        print("THE CURRENT MONTH IS",month_name,"HAS 30 DAYS")
    else :
        print("THE CURRENT MONTH IS",month_name,"HAS 28 DAYS")
else :
    print("PLEASE ENTER CORRECT MONTH NUMBER BETWEEN 1 TO 12.")
