l = [3, 1, 1, 3, 0, 0, 2, 3, 3]

print(max(l))

print(min(l))

#추가문제
max_val = l[0]
min_cal = l[0]

for i in l:
    if i > max_val:
        max_val = i
    if i < min_val:
        min_val = i

print(max_val, min_val)

