from copy import deepcopy

def find_path(matrix, i, j, rows, cols, dept, visited, res=[]):
    master = []
    if dept == 4:
        res.append(matrix[i][j])
        dept -= 1

    for next_x, next_y in neigbours(i, j, rows, cols):
        if dept>0:
            res.append(matrix[next_x][next_y])
            dept -= 1
            find_path(matrix, next_x, next_y, rows, cols, dept, visited, res)
        else:
            tmp = deepcopy(res)
            master.append(tmp)
            res.pop()





def neigbours(x, y, rows, cols):
    for rel_x, rel_y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        next_x, next_y = x + rel_x, y + rel_y
        if 0 <= next_x < rows and 0 <= next_y < cols:
            yield next_x, next_y

rows = 3
cols = 5
matrix = [[0] * cols for row in range(rows)]
visit = [[0] * cols for row in range(rows)]
idx = 97
for i in range(rows):
    for j in range(cols):
        matrix[i][j] = chr(idx)
        idx += 1
for row in range(rows):
    print(matrix[row])
print("*"*22)
x, y = 0, 0
for i in range(rows):
    for j in range(cols):
        find_path(matrix, i, j, rows, cols, 4, visited=visit)

# find_the_path(matrix, rows, cols, 0, 0)
# for i in range(rows):
#     for j in range(cols):
#         find_the_path(matrix, rows, cols, i, j, [])
        # result.append(find_the_path(matrix, rows, cols, i, j, []))
# print(list(int("".join(map(str, item))) for item in result))
# print(max(result))


