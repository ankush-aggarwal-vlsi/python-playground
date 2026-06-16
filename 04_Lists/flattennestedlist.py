# 154 program FLATTEN NESTED LIST
lst = [1, [2, 3], [4, [5, 6]], 7]

flat_list = []

for i in lst:
    if type(i) == list:
        for j in i:
            flat_list.append(j)
    else:
        flat_list.append(i)

print(flat_list)