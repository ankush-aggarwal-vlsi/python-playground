# 55 program CHARACTER IS VOWEL USING IF
ch = input("ENTER A CHARACTER : ")
if ch.isalpha() :
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' :
        print("THE ENTERED CHARACTER IS A VOWEL")
    elif ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U' :
        print("THE ENTERED CHARACTER IS A VOWEL")
    else :
        print("THE ENTERED CHARACTER IS NOT A VOWEL")
else :
    print("PLEASE ENTER VALID CHARACTER.")