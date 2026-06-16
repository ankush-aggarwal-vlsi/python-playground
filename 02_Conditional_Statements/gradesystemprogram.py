# 35 program GRADE SYSTEM PROGRAM
x = int(input("ENTER THE MARKS OBTAINED (in %) : "))
if x <= 100 and x >= 0 :
    if x >= 90 and x <= 100 :
        print("YOUR GRADE WILL BE A+")
    elif x >= 80 and x < 90 :
        print("YOUR GRADE WILL BE A")
    elif x >= 70 and x < 80 :
        print("YOUR GRADE WILL BE B")
    elif x >= 60 and x < 70 :
        print("YOUR GRADE WILL BE C")
    elif x >= 50 and x < 60 :
        print("YOUR GRADE WILL BE D")
    else :
        print("YOUR ARE FAIL")
else :
    print("PLEASE ENTER A VALID SCORE")
