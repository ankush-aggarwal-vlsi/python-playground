# 42 program TRIANGLE VALIDITY
a = float(input("ENTER THE FIRST SIDE OF TRIANGLE (in cm) : "))
b = float(input("ENTER THE SECOND SIDE OF TRIANGLE (in cm) : "))
c = float(input("ENTER THE THIRD SIDE OF TRIANGLE (in cm) : "))
if a > 0 and b > 0 and c > 0 :
    if (a+b)>c and (a+c)>b and (b+c)>a :
        print("VALID TRIANGLE")
    else :
        print("INVALID TRIANGLE")
else :
    print("ENTER THE VALID SIDES OF A TRIANGLE")