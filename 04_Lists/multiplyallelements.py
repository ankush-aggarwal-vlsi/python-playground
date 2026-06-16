# 143 program MULTIPLY ALL ELEMENTS
n = int(input("ENTER THE RANGE OF ELEMENT IN A LIST : "))
lst = []

for i in range(n):
    x = int(input("ENTER THE ELEMENTS : "))
    lst.append(x)

print("LIST :", lst)

element = int(input("ENTER THE ELEMENT TILL THAT THE MULTIPLICATION HAS TO BE DONE : "))
product = 1

if element in lst:
    index = lst.index(element)
    for i in range(index + 1):
        product *= lst[i]
    print("THE MULTIPLICATION OF ELEMENTS WILL BE :", product)
else:
    print("ENTER A VALID ELEMENT FROM THE LIST")