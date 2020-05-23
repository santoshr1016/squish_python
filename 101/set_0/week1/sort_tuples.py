def sort_intervals():
    intervals = [(42, 14), (22, 13), (15, 20), (5, 10), (21, 6), (3, 34), (9, 32), (2, 98), (4, 44)]
    s = sorted(intervals, key=lambda x:x[0])
    print(s)


print(sort_intervals())
