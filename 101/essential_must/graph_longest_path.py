from queue import Queue


def find_the_path(matrix, rows, cols, i, j, l):
    if rows < 0 or cols < 0 or i >= rows or j >= cols:
        return None
    else:
        l.append(matrix[i][j])
    if len(l) == 4:
        return l

    if 0 <= i < rows and 0 <= j < cols :
        if find_the_path(matrix, rows, cols, i-1, j, l): # up
            return l
        if find_the_path(matrix, rows, cols, i+1, j, l): # down
            return l
        if find_the_path(matrix, rows, cols, i, j+1, l): # right
            return l
        if find_the_path(matrix, rows, cols, i, j-1,l): # left
            return l
    # return l
    # for i in range(given_i - 1, given_i + 2):
    #     for j in range(given_j - 1, given_j + 2):
    #         if 0 <= i < rows and 0 <= j < cols and count < 4:  # and matrix[i][j] == 0:
    #             l.append(matrix[i][j])
    #             count += 1
    #             # if count == 4:
    #             #     break
    # return int("".join(map(str, l)))
    #
    # q = Queue()
    # if matrix[given_i][given_j] == 0:
    #     matrix[given_i][given_j] = -2
    #     q.put((given_i, given_j))
    # else:
    #     return
    # while not q.empty():
    #     given_i, given_j = q.get()
    #     for i in range(given_i - 1, given_i + 2):
    #         for j in range(given_j - 1, given_j + 2):
    #             if 0 <= i < rows and 0 <= j < cols and matrix[i][j] == 0:
    #                 matrix[i][j] = -2
    #                 q.put((i, j))
    #
    # for row in range(rows):
    #     print(matrix[row])


rows = 3
cols = 5
given_i = 0
given_j = 0
matrix = [[0] * cols for row in range(rows)]
items = [int(item) for item in input().split(' ')]
# 9 1 1 0 7 1 0 2 1 0 1 9 1 1 0
idx = 0
for i in range(rows):
    for j in range(cols):
        matrix[i][j] = items[idx]
        idx += 1
for row in range(rows):
    print(matrix[row])
print("*"*22)
result = []
for i in range(rows):
    for j in range(cols):
        # find_the_path(matrix, rows, cols, i, j, [])
        result.append(find_the_path(matrix, rows, cols, i, j, []))
print(list(int("".join(map(str, item))) for item in result))
# print(max(result))
