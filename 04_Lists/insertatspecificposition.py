# 166 program INSERT AT SPECIFIC POSITION
n = int(input("ENTER NUMBER OF ELEMENTS : "))
lst = []

for i in range(n):
    x = int(input("ENTER ELEMENT : "))
    lst.append(x)

print("ORIGINAL LIST :", lst)

pos = int(input("ENTER POSITION TO INSERT (0 to n) : "))
element = int(input("ENTER ELEMENT TO INSERT : "))

if pos < 0 or pos > n:
    print("INVALID POSITION")
else:
    lst.insert(pos, element)
    print("LIST AFTER INSERTION :", lst)

