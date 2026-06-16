# 30 program CHECK VOWEL OR CONSONANT
ch = input("ENTER THE CHARACTER : ").lower()
if ch.isalpha() :
    if ch in ('a','e','i','o','u') :
        print("THE GIVEN CHARACTER IS A VOWEL")
    else :
        print("THE GIVEN CHARACTER IS A CONSONANT")
else :
    print("ENTER A VALID CHARACTER")
    