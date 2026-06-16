# 29 program CHECK LEAP YEAR
x = int(input("ENTER THE YEAR : "))
if x % 400 == 0 :
    print("THE GIVEN YEAR IS A LEAP YEAR")
elif x % 100 == 0 and x % 400 != 0 :
    print("THE GIVEN YEAR IS NOT A LEAP YEAR")
elif x % 4 == 0 and x % 100 != 0 :
    print("THE GIVEN YEAR IS LEAP YEAR")
else :
    print("THE GIVEN YEAR IS NOT A LEAP YEAR")