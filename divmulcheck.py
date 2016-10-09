# Output all numbers that are divisible by 7 and not multiple of 5

arr = []
for a in range(2000, 3001):
    if (a % 7 == 0) and (a / 5 != 0):
        arr.append(a)
        continue
print arr