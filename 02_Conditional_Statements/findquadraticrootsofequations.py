# 50 program FIND ROOTS OF QUADRATIC EQUATIONS

try:
    a = float(input("ENTER THE COEFFICIENT OF a : "))
    b = float(input("ENTER THE COEFFICIENT OF b : "))
    c = float(input("ENTER THE COEFFICIENT OF c : "))

    if a == 0:
        print("NOT A QUADRATIC EQUATION")
    else:
        D = (b * b) - (4 * a * c)

        if D > 0:
            root1 = (-b + (D ** 0.5)) / (2 * a)
            root2 = (-b - (D ** 0.5)) / (2 * a)
            print("TWO DISTINCT REAL ROOTS:")
            print("ROOT 1 =", root1)
            print("ROOT 2 =", root2)

        elif D == 0:
            root = -b / (2 * a)
            print("TWO EQUAL REAL ROOTS:")
            print("ROOT =", root)

        else:
            print("NO REAL ROOTS EXIST")

except ValueError:
    print("PLEASE ENTER VALID NUMERIC COEFFICIENTS")

    