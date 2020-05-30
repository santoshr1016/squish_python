"""
Arrange 0s and 1s and find majority
"""


def segregate_in_2candidates(array):
    start = 0
    current = 0
    end = len(array) - 1

    while current <= end:
        if array[current] == 0:
            array[start], array[current] = array[current], array[start]
            current += 1
            start += 1
        elif array[current] == 1:
            current += 1
    print(array)


array = [0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1]
segregate_in_2candidates(array)


def segregate_in_3candidates(the_list):
    left = 0
    mid = 0
    right = len(the_list)-1
    while mid <= right:
        if the_list[mid] == 0:
            the_list[left], the_list[mid] = the_list[mid], the_list[left]
            mid += 1
            left += 1
        elif the_list[mid] == 1:
            mid += 1
        else:
            the_list[mid], the_list[right] = the_list[right], the_list[mid]
            right -= 1
    return the_list


the_list = [2,0,1,0,1,1,2,0,1,0,1,1,1,1,0, 2, 2, 1, 0, 1,0,0,2]
print(segregate_in_3candidates(the_list))
