rows = 3
cols = 5
matrix = [[0]*cols for i in range(rows)]
for i in range(rows):
    for j in range(cols):
        matrix[i][j] = int(input())

for i in range(rows):
    print(matrix[i])
visited = [[False] * cols for i in range(rows)]


def get_region_size(matrix, row, col):
    if row < 0 or col < 0 or row >= rows or col >= cols:
        return 0
    if matrix[row][col] == 0:
        return 0
    size = 1
    matrix[row][col] = 0
    for i in range(row-1, row+1):
        for j in range(col-1, col+1):
            size += get_region_size(matrix, i, j)
    return size


def call_bfs(matrix, row, col, count):
    if row < 0 or col < 0 or row >= rows or col >= cols:
        return count
    if count < 4:
        call_bfs(matrix, row - 1, col, count+1)
        call_bfs(matrix, row + 1, col, count+1)
        call_bfs(matrix, row, col - 1, count+1)
        call_bfs(matrix, row, col + 1, count+1)
    elif count >=4:
        return matrix[row][col]
    # print(matrix[row][col])

count = 0
for i in range(rows):
    count = 0
    for j in range(cols):
        if matrix[i][j] > 0:
            count += 1
            res = str(matrix[i][j]) + str(call_bfs(matrix, i, j, count))
            print(res)
            # size = get_region_size(matrix, i, j)
            # max_region = max(max_region, size)
    print("***")
print(count)
"""

def valid_up(i, j, rows, cols):
    if 0 <= i-1 < rows:
        return True
    return False


def valid_down(i, j, rows, cols):
    if 0 <= i+1 < rows:
        return True
    return False


def valid_left(i, j, rows, cols):
    if 0 <= j-1 < cols:
        return True
    return False


def valid_right(i, j, rows, cols):
    if 0 <= j+1 < cols:
        return True
    return False

"""
"""
9
1
1
0
7
1
0
2
1
0
1
9
1
1
0
"""

"""
1
0
0
0
0
0
0
1
1
1
1
0
1
0
1
"""