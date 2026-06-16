# 46 program INSURANCE ELIGIBILITY
age = input("ENTER YOUR AGE (in yrs) ")
if age.isdigit() :
    age = int(age)
    if age >= 18 and age <= 60 :
        print("YOU ARE ELIGIBLE FOR THE INSURANCE.")
    else :
        print("YOU ARE NOT ELIGIBLE FOR THE INSURANCE.")
else :
    print("PLEASE ENTER VALID AGE.")
    