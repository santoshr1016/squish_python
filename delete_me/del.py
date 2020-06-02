def codeHere():
    # Use the function to return the solution.
    cases = int(input())
    inputData = [item for item in input().split(' ')]

    result = dict()
    size = len(inputData)
    idx = 1
    count = 1
    while idx < size:
        if inputData[idx] == inputData[idx - 1]:
            count += 1
        else:
            result[inputData[idx - 1]] = count
            count = 1
        idx += 1
    result[inputData[idx - 1]] = count
    count = 1
    char = ''
    for k, v in result.items():
        if v > count:
            char, count = k, v
    return char


print(codeHere())



# array = [abs(int(item)) for item in input().split(' ')]
# print(len(array))
#
# end = len(array) - 1
# while end:
#     if array[end] == array[end-1]:
#         end -= 2
#     else:
#         break
# print(array[end])


