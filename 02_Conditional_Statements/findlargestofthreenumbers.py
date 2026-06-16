# 28 program FIND LARGEST OF THREE NUMBERS
x = int(input("ENTER THE FIRST NUMBER : "))
y = int(input("ENTER THE SECOND NUMBER : "))
z = int(input("ENTER THE THIRD NUMBER : "))
if x > y and x > z :
    print("THE LARGEST OUT OF THREE NUMBERS WILL BE :",x)
elif y > x and y > z :
    print("THE LARGEST OUT OF THREE NUMBERS WILL BE :",y)
else :
    print("THE LARGEST OUT OF THREE NUMBERS WILL BE :",z)
    