# 76 program PRINT PALINDROME NUMBER IN RANGE
n = int(input("ENTER THE RANGE : "))

for num in range(1, n + 1):
    temp = num
    rev = 0

    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp //= 10

    if rev == num:
        print(num)
