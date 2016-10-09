# output the square of a number as value with the number as key in a dictionary

myDict = {}
x = int(raw_input())
for a in range(1, x + 1):
    myDict[a] = a * a
print myDict
