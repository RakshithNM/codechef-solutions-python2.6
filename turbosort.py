
# sort specific number of inputs in non decreasing order

x = int(raw_input())
nums = []
while x > 0:
    nums.append(int(raw_input()))
    x -= 1
nums.sort()
for sortednum in nums:
    print sortednum
