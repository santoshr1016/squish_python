def unique_in_order(iterable):
    res = []
    seen = set()
    for ch in iterable:
        if ch not in seen:
            if len(seen) > 0:
                seen.clear()
            seen.add(ch)
            res.append(ch)
    print(res)


def unique_in_order(iterable):
    unique = []
    last = ''
    for item in iterable:
        if item != last:
            unique.append(item)
            last = item
    return unique


def unique_in_order(iterable):
    result = [None]

    for item in iterable:
        if item != result[-1]:
            result.append(item)
    return result[1:]


def unique_in_order(iterable):
    k = []
    for i in iterable:
        if k == []:
            k.append(i)
        elif k[-1] != i:
            k.append(i)
    return k

print(unique_in_order('AAAABBBCCDAABBB'))