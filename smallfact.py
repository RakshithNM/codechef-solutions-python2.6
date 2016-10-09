# get a specified number of inputs from the console, find the factorials and print them out

a = int(raw_input())
nums = []
while a > 0:
    nums.append(int(raw_input()))
    a -= 1
def factorial(i):
    if i == 0:
        return 1
    else:
        return i * factorial(i-1)
for i in nums:
    print factorial(i)