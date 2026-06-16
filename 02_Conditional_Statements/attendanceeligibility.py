# 48 program ATTENDANCE ELIGIBLITY 
attendance = input("ENTER THE NUMBER OF DAYS STUDENT PRESENT (out of 365 days) : ")
if attendance.isdigit() :
    attendance = int(attendance)
    attendance_percentage = ( attendance * 100 ) / 365
    if 0 <= attendance <= 365 :
        if attendance_percentage >= 75 :
            print("THE STUDENT IS ELIGIBLE TO APPEAR IN EXAM")
        else :
            print("THE STUDENT IS NOT ELIGIBLE TO APPEAR IN EXAM")
    else :
        print("PLEASE , ENTER NUMBER OF DAYS IN BETWEEN 0 to 365.")
else : 
    print("ENTER VALID NUMBER OF DAYS.")