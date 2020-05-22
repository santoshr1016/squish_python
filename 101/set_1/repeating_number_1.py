def most_repeating_1(the_list):
    size = len(the_list)
    maximum = the_list[0]
    maxCount = 1
    count = [0] * size
    i = int()
    while i < size:
        count[the_list[i]] += 1
        if count[the_list[i]] > maxCount:
            maxCount = count[the_list[i]]
            maximum = the_list[i]
        i += 1
    print(maximum)


ll = [2, 3, 1, 2, 2, 3, 2, 4, 3]
most_repeating_1(ll)
