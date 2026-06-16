# 45 program AGE ELIGIBILITY FOR VOTE
age = input("ENTER YOUR AGE (in yrs) : ")
if age.isdigit() :
    age = int(age)
    
    if age >= 18 :
        print("THE CANDIDATE IS ELIGIBLE TO VOTE")
    else :
        print("THE CANDIDATE IS NOT ELIGIBLE TO VOTE ")
else :
    print("PLEASE ENTER VALID AGE (in yrs)")
