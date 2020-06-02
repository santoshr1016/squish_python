def reformat(array):
    size = len(array) - 1
    out = []
    for i in range(size):
        if array[i] > array[i+1]:
            out = array[i+1:] + array[:i+1]
            break
    print(out)


array = list(range(10))
array = array[4:] + array[:4]
print(array)

reformat(array)
