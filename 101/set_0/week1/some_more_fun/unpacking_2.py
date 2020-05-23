items = [1, 10, 7, 4, 5, 9]

head, *tail = items
print(head)
print(tail)


def find_sum(items):
    head, *tail = items
    print(head + sum(tail) if tail else head)


find_sum(items)