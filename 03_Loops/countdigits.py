# 70 program COUNT DIGITS
n = int(input("ENTER THE NUMBER WHOSE LENGTH NEED TO FIND : "))

count = 0

while n > 0:
    count += 1
    n = n // 10

print("LENGTH OF THE GIVEN NUMBER WILL BE :", count)
