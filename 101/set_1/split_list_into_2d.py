def split_list(l, split):
    size = len(l)
    res = [l[i:i+split] for i in range(0, size, split)]
    print(res)
    print(len(res))


def split_list_2(l, split):
    size = len(l)
    count = 0
    res = []
    while count < size:
        tmp = []
        for i in range(split):
            tmp.append(l[count])
            count += 1
            if count == size:
                break
        res.append(tmp)
    print(res)


l = [1,2,3,4,5,6,7,8,9,10,11]
split = 5
split_list_2(l, split)
split_list(l, split)