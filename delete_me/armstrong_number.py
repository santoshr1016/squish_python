def armstrong(num):
    arr = [int(i) for i in str(num)]
    size = len(arr)
    return num == sum([item ** size for item in arr])


for i in range(999):
    if armstrong(i):
        print(i)
