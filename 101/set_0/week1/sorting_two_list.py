def sort_two_list(a, b):
    result = []

    i = 0
    j = 0
    size_a = len(a)
    size_b = len(b)

    while i < size_a and j < size_b:
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    if i < size_a:
        result.extend(a[i:])
    if j < size_b:
        result.extend(b[j:])
    return result


def sort_list_second(a, b):
    result = []
    while a and b:
        if a[0] < b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))
    result = result + a + b
    print(result)
    return result


a = [3, 4, 6, 10, 11, 18]
b = [1, 5, 7, 12, 13, 19, 21]

print(sort_two_list(a, b))
print(sort_list_second(a, b))
