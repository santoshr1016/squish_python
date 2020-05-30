def even_odd(array):
    left_even, right_odd = 0, len(array) - 1
    while left_even < right_odd:
        if array[left_even] % 2:
            array[left_even], array[right_odd] = array[right_odd], array[left_even]
            right_odd -= 1
        else:
            left_even += 1

    print(array)


array = [5, 2, 1, 3, 6, 12, 11, 9, 10, 24, 55, 8, 13, 15]
even_odd(array)