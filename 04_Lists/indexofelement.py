# 138 program INDEX OF ELEMENT
n = int(input("ENTER THE RANGE OF ELEMENT IN A LIST : "))
lst = []

for i in range(n) :
    x = input("ENTER THE ELEMENT FOR THE LIST ")
    lst.append(x)

element = input("ENTER THE ELEMENT WHOSE INDEX NUMBER NEED TO FIND IN THE LIST : ")

if element in lst :
    print("THE ELEMENT IS PRESENT IN LIST.")
    print("THE INDEX NUMBER will be",lst.index(element))

else :
    print("THE ELEMENT DOESN'T PRESENT IN THE LIST.")

    