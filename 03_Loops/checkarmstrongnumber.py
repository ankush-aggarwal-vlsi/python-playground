# 74 program CHECK ARMSTRONG NUMBER
n = int(input("ENTER THE NUMBER : "))

temp = n
sum = 0
digits = 0

# count number of digits
while temp > 0:
    digits += 1
    temp //= 10

temp = n

# calculate armstrong sum
while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10

if sum == n:
    print("THE GIVEN NUMBER IS AN ARMSTRONG NUMBER.")
else:
    print("THE GIVEN NUMBER IS NOT AN ARMSTRONG NUMBER.")
