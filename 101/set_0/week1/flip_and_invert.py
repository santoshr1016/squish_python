def flip_and_invert(arr=[1,1,1,0,0,0,1]):
    low = 0
    high = len(arr) - 1
    while low <= high:
        if arr[low] == arr[high]:
            arr[low] = 1 - arr[low]
            arr[high] = arr[low]
        low += 1
        high -= 1
    return arr


def flip():
    arr = [
        [1, 1, 0],
        [1, 0, 1],
        [0, 0, 0]
    ]
    # res = [flip_and_invert(row) for row in arr]

    for row in arr:
        low = 0
        high = len(row)-1
        while low <= high:
            if row[low] == row[high]:
                row[low] = 1 - row[low]
                row[high] = row[low]
            low += 1
            high -= 1
    print(arr)
    res = [flip_and_invert(row) for row in arr]
    print(res)

print(flip_and_invert())
flip()

#  arr=[1,1,1,0,0,0,1] #
#  Flip is   [1, 0, 0, 0, 1, 1, 1]
#  invert is [0, 1, 1, 1, 0, 0, 0]
