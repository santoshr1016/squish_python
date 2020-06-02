import sys

def solution(dup_list):
    min_item = sys.maxsize
    max_item = -sys.maxsize - 1

    for item in dup_list:
        if item < min_item:
            min_item = item
        elif item > max_item:
            max_item = item

    return min_item, max_item


d_list = [-20, 34, 21, -8, 92, 99999]
print(solution(d_list))