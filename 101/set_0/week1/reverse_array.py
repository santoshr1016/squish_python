def reverse_me(arr=[1,2,3,4,5,6]):
    rev = []
    size = len(arr)-1
    for i in range(size, -1, -1):
        rev.append(arr[i])
    print(rev)


def find_3rd_max(arr=[4,1,5,22,6,11,9,22,3,9,15,25]):
    first_max = 0
    second_max = 0
    third_max = 0
    for item in arr:
        if item == first_max or item == second_max or item == third_max:
            continue
        if item > first_max:
            third_max = second_max
            second_max = first_max
            first_max = item
        elif item > second_max:
            third_max = second_max
            second_max = item
        elif item > third_max:
            third_max = item

    print(first_max)
    print(second_max)
    print(third_max)


print(reverse_me())
# print(find_3rd_max())
