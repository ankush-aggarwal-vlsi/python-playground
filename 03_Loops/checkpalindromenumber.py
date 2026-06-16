# 73 program CHECK PALINDROME NUMBER
n = int(input("ENTER THE NUMBER NEED TO CHECK PALINDROME : "))

temp = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

if temp == rev:
    print("THE GIVEN NUMBER IS PALINDROME.")
else:
    print("THE GIVEN NUMBER IS NOT PALINDROME.")
