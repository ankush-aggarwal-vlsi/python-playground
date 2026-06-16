# 72 program PRODUCT OF DIGITS
n = int(input("ENTER THE NUMBER WHOSE PRODUCT NEED TO FIND : "))

product = 1  # Start with 1 because multiplying by 0 will always give 0

while n > 0:
    digit = n % 10       # Get last digit
    product *= digit     # Multiply with product
    n = n // 10          # Remove last digit

print("PRODUCT OF DIGITS IS :", product)
