x, y = raw_input().split()
x = int(x)
y = int(y)
ins = []
while x > 0:
    ins.append(int(raw_input()))
    x -= 1
count = 0
for a in ins:
    if a % y == 0:
        count += 1
    else:
        continue
print count