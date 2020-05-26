from collections import OrderedDict


def first_non_repeating(s):
    my_dict = dict()
    for ch in s:
        my_dict[ch] = my_dict.get(ch, 0) + 1
    for ch in s:
        if my_dict[ch] == 1:
            print(ch)
            break


def first_non_repeating_using_ordered_dict(s):
    od = OrderedDict()
    for ch in s:
        if ch in od:
            od.get(ch).append(ch)
        else:
            od[ch] = [ch]
    for k, v in od.items():
        if len(v) == 1:
            print(k)
            break


s = "aaabbcddde"
first_non_repeating(s)
first_non_repeating_using_ordered_dict(s)
