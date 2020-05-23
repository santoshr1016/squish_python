rows = 3
cols = 5
matrix = [[0]*cols for i in range(rows)]
for i in range(rows):
    for j in range(cols):
        matrix[i][j] = int(input())

for i in range(rows):
    print(matrix[i])

visited = [[False] * cols for i in range(rows)]


def call_dfs(matrix, row, col):
    if row < 0 or col < 0 or row >= rows or col >= cols:
        return 0
    if matrix[row][col] == 0:
        return 0
    matrix[row][col] = 0
    call_dfs(matrix, row - 1, col)  # up
    call_dfs(matrix, row + 1, col)  # down
    call_dfs(matrix, row, col - 1)  # left
    call_dfs(matrix, row, col + 1)  # right


count = 0
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 1:
            count += 1
            call_dfs(matrix, i, j)

            # size = get_region_size(matrix, i, j)
            # max_region = max(max_region, size)
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