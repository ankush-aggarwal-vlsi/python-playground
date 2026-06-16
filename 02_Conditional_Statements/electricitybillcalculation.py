# 40 program ELECTRICITY BILL CALCULATION
unit = int(input("ENTER THE UNIT TAKEN FROM ELECTRICITY METER : "))
if unit <= 100 and unit >= 0 :
    bill = 1.5 * unit
elif unit > 100 and unit <= 200 :
    bill = (1.5*100)+(2.5*(unit-100))
elif unit > 200 :
    bill  = (1.5*100)+(2.5*100)+(4*(unit-200))
else :
    print("ENTER VALID UNIT , UNIT CANNOT BE NEGATIVE")
    bill = None
if bill is not None :
    print("YOUR ELECTRICITY BILL WILL BE",bill)

