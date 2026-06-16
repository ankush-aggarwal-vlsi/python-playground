# 124 program AVERAGE OF LIST
lst = [1,2,3,4,5]
average = 0
sum = 0
for i in lst :
    sum += i
average = sum / len(lst)
print("LIST : ",lst)
print("AVERAGE OF LIST : ",average)