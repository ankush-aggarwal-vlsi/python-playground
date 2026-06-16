# 44 program CHECK RIGHT ANGLED TRIANGLE
a = float(input("ENTER THE FIRST SIDE OF A TRIANGLE (in cm) : "))
b = float(input("ENTER THE SECOND SIDE OF A TRIANGLE (in cm) : "))
c = float(input("ENTER THE THIRD SIDE OF A TRIANGLE (in cm) : "))
if a>0 and b>0 and c>0 and ((a+b)>c and (a+c)>b and (b+c)>a) :
    if ((a*a)+(b*b)==(c*c)) or ((a*a)+(c*c)==(b*b)) or ((b*b)+(c*c)==(a*a)) :
        print("THE GIVEN SIDE FORMS AN RIGHT ANGLED TRIANGLE")
    else :
        print("THE GIVEN SIDE DOESN'T FORM AN RIGHT ANGLED TRIANGLE")
else :
    print("ENTER VALID SIDES OF A TRAINGLE")