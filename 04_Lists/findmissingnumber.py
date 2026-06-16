# 151 program FIND MISSING NUMBER
n = int(input("ENTER THE RANGE OF ELEMENT IN A LIST : "))
lst = []

for i in range(n-1) :
    lst.append(int(input("ENTER THE ELEMENT : ")))

print("LIST :",lst)

total_sum = int(( n * (n + 1) / 2 ))
list_sum = sum(lst)

missing_number = total_sum - list_sum

print("MISSING NUMBER :",missing_number)