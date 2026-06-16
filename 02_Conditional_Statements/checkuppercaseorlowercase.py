# 31 program CHECK UPPERCASE OR LOWERCASE
ch = input("ENTER THE CHARACTER : ")
if ch.isalpha() :
    if ch == ch.lower() :
        print("THE GIVEN CHARACTER IS IN LOWERCASE")
    else :
        print("THE GIVEN CHARACTER IS IN UPPERCASE")
else :
    print("ENTER A VALID CHARACTER")
