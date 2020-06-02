def can_jump(arr):
    furthest_reach_so_far, last_index = 0, len(arr) - 1
    i = 0
    while i <= furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, arr[i] + i)
        i += 1
    return furthest_reach_so_far >= last_index


arr = [3, 3, 1, 0, 2, 0, 1]
# arr = [2, 4, 1, 1, 0, 2, 3]
# arr = [3, 2, 0, 0, 2, 0, 1]
print(can_jump(arr))

