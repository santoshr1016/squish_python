def first_non_repeating(s):
    my_dict = dict()
    for ch in s:
        my_dict[ch] = my_dict.get(ch, 0) + 1
    for ch in s:
        if my_dict[ch] == 1:
            print(ch)
            break


s = "aaabbcddde"
first_non_repeating(s)
