# 66 program SUM OF EVEN NUMBERS TILL N
n = int(input("ENTER THE VALUE TILL WHICH SUM OF EVEN NUMBER HAS TO BE CALCULATED : "))

total = 0

for i in range(1 , n + 1) :
    if i % 2 == 0 :
        total += i

print("SUM OF NUMBERS WILL BE :",total)