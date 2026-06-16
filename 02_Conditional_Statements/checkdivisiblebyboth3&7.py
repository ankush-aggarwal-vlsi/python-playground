# 59 program CHECK DIVISIBLE BY BOTH 3 & 7
x = int(input("ENTER THE NUMBER : "))
if x % 3 == 0 and x % 7 == 0 :
    print("THE GIVEN NUMBER IS DIVISIBLE BY BOTH 3 & 7.")
elif x % 3 == 0 and x % 7 != 0 :
    print("THE GIVEN NUMBER IS DIVISBLE BY 3 BUT NOT DIVISIBLE BY 7.")
elif x % 3 != 0 and x % 7 == 0 :
    print("THE GIVEN NUMBER IS DIVISBLE BY 7 BUT NOT DIVISIBLE BY 3.")
else :
    print("THE GIVEN NUMBER IS NOT DIVISIBLE BY BOTH 3 & 7.")

 