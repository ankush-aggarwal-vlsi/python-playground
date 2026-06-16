# 60 program CHECK NUMBER IS 2-DIGIT OR NOT
x = int(input("ENTER A NUMBER : "))
if (x >= 10 and x <= 99) or (x <= -10 and x >= -99) :
    print("THE GIVEN NUMBER IS TWO DIGIT NUMBER.")
else :
    print("THE GIVEN NUMBER IS NOT TWO DIGIT NUMBER.")