# 53 program MONTH NUMBER TO MONTH NAME
month_name = ["JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE","JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER"]
month_number = int(input("ENTER THE MONTH NUMBER : "))
print(month_name[month_number - 1] if 1 <= month_number <= 12 else "INVALID")
