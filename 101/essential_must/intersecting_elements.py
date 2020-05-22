def common_elements(l1, l2):
    p1 = 0
    p2 = 0
    res = []
    while p1 < len(l1) and p2 < len(l2):
        if l1[p1] == l2[p2]:
            res.append(l1[p1])
            p1 += 1
            p2 += 1
        elif l1[p1] > l2[p2]:
            p2 += 1
        else:
            p1 += 1
    print(res)


l1 = [1, 3, 4, 6, 7, 9, 10, 11]
l2 = [1, 2, 4, 5, 9, 11]

common_elements(l1, l2)

