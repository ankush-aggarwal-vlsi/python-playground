#9th program FIND REMAINDER
x = int(input("ENTER THE FIRST NUMBER : "))
y = int(input("ENTER THE SECOND NUMBER :"))
if x > y :
    remainder = x % y
else :
    remainder = y % x
print("THE REMAINDER WILL BE : ",float(remainder))
