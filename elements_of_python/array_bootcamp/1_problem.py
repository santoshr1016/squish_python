def place_odd_even(array):
    begin = 0
    end = len(array) - 1
    while begin < end:
        if array[begin] % 2 == 0:
            begin += 1
        else:
            array[begin], array[end] = array[end], array[begin]
            end -= 1
    print(array)


ll = [33, 2, 1, 5, 44, 22, 6, 9, 8, 34, 66, 54, 76, 99, 101, 32]
place_odd_even(ll)
