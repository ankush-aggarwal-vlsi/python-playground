# 57 program CHECK PERFECT SQUARE

x = int(input("ENTER THE NUMBER : "))

if x >= 0:
    square_root = int(x ** 0.5)

    if square_root * square_root == x:
        print("THE GIVEN NUMBER IS A PERFECT SQUARE")
        print("SQUARE ROOT IS", square_root)
    else:
        print("THE GIVEN NUMBER IS NOT A PERFECT SQUARE")
else:
    print("NEGATIVE NUMBER CANNOT BE A PERFECT SQUARE")
