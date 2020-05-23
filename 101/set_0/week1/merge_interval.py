def merge_interval():
    intervals = [[1,3],[4,6],[8,10],[15,18]]
    last = intervals[0]
    res = list()
    res.append(last)
    for item in intervals:
        cur_begin = last[0]
        cur_end = last[1]

        next_begin = item[0]
        next_end = item[1]

        if cur_end >= next_begin:
            last[1] = max(cur_end, next_end)
        else:
            last = item
            res.append(last)
    print(res)


merge_interval()
