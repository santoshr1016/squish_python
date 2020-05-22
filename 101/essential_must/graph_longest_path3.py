from collections import deque
def find_the_path(A, rows, cols, i, j):
    # stack = deque()
    stack = []
    count = 0
    result = []
    seen = set()
    stack.append((i, j))
    while stack:
        if len(result) == 4:
            result = result[1:]
            seen.clear()
        # x, y = stack.popleft()
        x, y = stack.pop()
        result.append(A[x][y])
        seen.add(A[x][y])
        count += 1
        for d in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            next_x, next_y = x + d[0], y + d[1]
            if 0 <= next_x < rows and 0 <= next_y < cols:
                if A[next_x][next_y] not in seen and len(result)< 4:
                    stack.append((next_x, next_y))
                    # result.append(A[next_x][next_y])
                    seen.add(A[next_x][next_y])
                    count += 1
                if len(result) == 4:
                    print(result)
                    break

                    # and A[next - x][next - y] == color):


rows = 3
cols = 5
matrix = [[0] * cols for row in range(rows)]
idx = 97
for i in range(rows):
    for j in range(cols):
        matrix[i][j] = chr(idx)
        idx += 1
for row in range(rows):
    print(matrix[row])
print("*"*22)
find_the_path(matrix, rows, cols, 0, 0)
# for i in range(rows):
#     for j in range(cols):
#         find_the_path(matrix, rows, cols, i, j, [])
        # result.append(find_the_path(matrix, rows, cols, i, j, []))
# print(list(int("".join(map(str, item))) for item in result))
# print(max(result))
