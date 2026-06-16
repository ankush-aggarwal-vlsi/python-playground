# 23 program CALCULATE SIMPLE INTEREST
P = float(input("ENTER THE PRINCIPAL AMOUNT(initial amount) : "))
R = float(input("ENTER THE RATE OF INTEREST (per year) : "))
T = float(input("ENTER THE TIME (in years) : "))
SI = (P*R*T)/100
A = P + SI
print("THE SIMPLE INTEREST (SI) will be :",SI)
print("THE TOTAL AMOUNT(A) will be:",A)
