# 43 program TRIANGLE TYPE
a= float(input("ENTER THE FIRST SIDE OF A TRIANGLE : "))
b = float(input("ENTER THE SECOND SIDE OF A TRIANGLE : "))
c = float(input("ENTER THE THIRD SIDE OF A TRIANGLE : "))
if a > 0 and b > 0 and c > 0 and ((a+b)>c and (a+c)>b and (b+c)>a):
    if a==b and b==c and c==a :
        print("THE GIVEN TRIANGLE IS EQUILATERAL TRIANGLE")
    elif (a!=b and (c==b or a==c)) or (a!=c and(a==b or b==c)) or (b!=c and (b==a or c==a)) :
        print("THE GIVEN TRIANGLE IS ISOCELES TRIANGLE")
    elif a!=b and b!=c and c!=a :
        print("THE GIVEN TRIANGLE IS SCALENE TRIANGLE")
    else :
        print("INVALID TRIANGLE")
else :
    print("ENTER THE VALID SIDE OF A TRIANGLE")