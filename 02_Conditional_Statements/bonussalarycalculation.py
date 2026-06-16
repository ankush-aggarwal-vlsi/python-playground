# 41 program BONUS SALARY CALCULATION
salary = int(input("ENTER YOUR SALARY (in Rs) : "))
if salary >= 50000 :
    bonus = (salary * 10)/100
    new_salary = salary + bonus
elif salary < 50000 and salary >= 0 :
    bonus = (salary * 5)/100
    new_salary = salary + bonus
else :
    print("ENTER A VALID SALARY AMOUNT")
    bonus = None
    new_salary = None
if bonus is not None and salary is not None :
    print("THE BONUS AMOUNT WILL BE",bonus)
    print("THE SALARY WITH BONUS WILL BE",new_salary)
    