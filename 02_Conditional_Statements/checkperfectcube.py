# 58 program CHECK PERFECT CUBE 
x = int(input("ENTER THE NUMBER : "))
if x >= 0 :
    cube_root = int(x**(1/3))

    if cube_root * cube_root * cube_root == x :
        print("THE GIVEN NUMBER IS A PERFECT CUBE")
        print("THE CUBE ROOT IS :",cube_root)
    else :
        print("THE GIVEN NUMBER IS NOT A PERFECT CUBE")
else :
    print("PLEASE ENTER A VALID NUMBER.")
    