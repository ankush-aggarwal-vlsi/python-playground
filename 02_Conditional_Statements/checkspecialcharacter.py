# 34 program CHECK SPECIAL CHARACTER
ch = input("ENTER A CHARACTER : ")
if ch.isalpha() :
    print("THE GIVEN CHARACTER IS AN ALPHABET")
elif ch.isdigit() :
    print("THE GIVEN CHARACTER IS A DIGIT")
else :
    print("THE GIVEN CHARACTER IS A SPECIAL CHARACTER")