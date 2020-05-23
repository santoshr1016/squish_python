def parity_order(arr=[2,1,4,6,3,5,12,7,22,9]):  # This is space complexity of n
    res = []
    for item in arr:
        if not (item % 2):
            res.append(item)
    for item in arr:
        if item % 2:
            res.append(item)
    print(res)


def parity_order_const(arr=[2,1,4,6,3,5,12,7,22,9]):  # This is constant space
    print(arr)
    i = 0
    size = len(arr)
    for idx in range(size):
        if arr[idx] % 2 == 0:
            tmp = arr[i]
            arr[i] = arr[idx]
            arr[idx] = tmp
            i += 1
    print(arr)


print(parity_order())
print(parity_order_const([3,1,2,4]))
print(parity_order_const())