# 68 program MULTIPLICATION TABLE 
n = int(input("ENTER THE NUMBER FOR WHICH MULTIPLICATION TABLE IS NEEDED : "))

multiply = 0

for i in range(1,11) :
    multiply = n * i
    print(n,"x",i,"=",multiply)
