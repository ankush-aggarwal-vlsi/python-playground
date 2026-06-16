# 67 program SUM OF ODD NUMBERS TILL N 
n = int(input("ENTER THE NUMBER TILL WHICH ODD SUM IS CALCULATED : "))

total_odd = 0

i = 1
while i <= n :
    if i % 2 != 0 :
        total_odd += i 
    i += 1
    
print("SUM OF TOTAL ODD NUMBERS TILL N WILL BE :",total_odd)