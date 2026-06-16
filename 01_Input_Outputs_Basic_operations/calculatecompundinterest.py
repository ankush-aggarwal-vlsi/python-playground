# 24 program CALCULATE COMPOUND INTEREST
P = float(input("ENTER THE PRINCIPAL AMOUNT (initial amount) : "))
R = float(input("ENTER THE RATE OF INTEREST (per years) : "))
T = float(input("ENTER THE TIME (in years) : " ))
A = P * ((1+(R/100))**T)
CI = A - P
print("THE AMOUNT AFTER",T,"Years will be :",A)
print("THE COMPOUND INTEREST WILL BE :",CI)