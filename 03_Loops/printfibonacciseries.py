# 77 program PRINT FIBONACCI SERIES 
n = int(input("ENTER HOW MANY TERMS : "))

a = 0
b = 1

print(a)
print(b)

for i in range(2, n):
    c = a + b
    print(c)
    a = b
    b = c
