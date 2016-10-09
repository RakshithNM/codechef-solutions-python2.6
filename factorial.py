# program to find factorial of a number

def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x-1)

x = int(raw_input())
print factorial(x)