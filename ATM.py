while 1:
    x, y = raw_input().split()
    x = float(x)
    y = float(y)
    if x % 5 != 0:
        print y
        break
    elif x > y:
        print y
        break
    else:
        y -= (x + 0.5)
        print y
