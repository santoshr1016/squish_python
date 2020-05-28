def sorted_square(arr):
    start = 0
    end = len(arr) - 1
    result = []

    while start <= end:
        if arr[start]**2 > arr[end]**2:
            result.insert(0, arr[start]**2)
            start = start + 1
        else:
            result.insert(0, arr[end]**2)
            end = end - 1

    print(result)


a = [-6, -4, 1, 2, 3, 5]
sorted_square(a)
