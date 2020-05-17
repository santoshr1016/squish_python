def reverse_array(the_array, start, end):
    i = start
    j = end
    while i < j:
        the_array[i], the_array[j] = the_array[j], the_array[i]
        i += 1
        j -= 1


def rotate_array(the_array, shift_by=6):
    print(the_array)
    size = len(the_array)
    reverse_array(the_array, 0, shift_by - 1)
    reverse_array(the_array, shift_by, size - 1)
    reverse_array(the_array, 0, size - 1)
    print(the_array)


ll = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33]
rotate_array(ll)
