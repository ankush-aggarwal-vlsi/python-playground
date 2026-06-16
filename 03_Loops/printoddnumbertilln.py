# 64 program PRINT ODD NUMBERS TILL N 
n = int(input("ENTER THE VALUE TILL WHICH ODD NUMBERS NEED TO PRINT : "))

for i in range(1 , n + 1) :
    if i % 2 != 0 :
        print(i)
        