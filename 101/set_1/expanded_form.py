def expanded_form(num):
    res = []
    op = []
    i = 0
    while num:
        digit = num%10
        res.append(i * 10 + digit)
        num //= 10
    print(res)
    for item in range(len(res), 0, -1):
        item -= 1
        num = res[item]* (10**item)
        if num > 0:
            op.append(str(num))
    return " + ".join(op)


print(expanded_form(70304))
