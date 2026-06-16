# 36 program PASS OR FAIL PROGRAM
x = int(input("ENTER THE SCORE : "))
if x <= 100 and x >= 0 :
    if x >= 35 :
        print("YOU PASSED THE EXAM")
    else :
        print("YOU FAILED THE EXAM")
else :
    print("ENTER A VALID SCORE")
    