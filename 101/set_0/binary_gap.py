def binary_gap(n=9):
    lbg = 0
    cbg = -1
    while n:
        if n & 1 == 1:
            if lbg < cbg:
                lbg = cbg
            cbg = 0
        elif cbg != -1:
            cbg += 1
        n = n >> 1
    print(lbg)


binary_gap()