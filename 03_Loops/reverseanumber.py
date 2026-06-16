# 69 program REVERSE A NUMBER
n = int(input("ENTER A NUMBER : "))

rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("REVERSED NUMBER :", rev)