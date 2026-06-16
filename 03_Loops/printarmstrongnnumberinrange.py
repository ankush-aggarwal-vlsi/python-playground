# 75 program PRINT ARMSTRONG NUMBER IN RANGE
n = int(input("ENTER THE RANGE : "))

for num in range(1, n + 1):
    temp = num
    digits = 0
    sum = 0

    # count digits
    while temp > 0:
        digits += 1
        temp //= 10

    temp = num

    # calculate armstrong sum
    while temp > 0:
        digit = temp % 10
        sum += digit ** digits
        temp //= 10

    if sum == num:
        print(num)
