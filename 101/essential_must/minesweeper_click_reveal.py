from queue import Queue


def click_and_reveal(matrix, rows, cols, given_i, given_j):
    q = Queue()
    if matrix[given_i][given_j] == 0:
        matrix[given_i][given_j] = -2
        q.put((given_i, given_j))
    else:
        return
    while not q.empty():
        given_i, given_j = q.get()
        for i in range(given_i-1, given_i+2):
            for j in range(given_j-1, given_j+2):
                if 0 <= i < rows and 0 <= j < cols and matrix[i][j] == 0:
                    matrix[i][j] = -2
                    q.put((i,j))

    for row in range(rows):
        print(matrix[row])


rows = 3
cols = 5
given_i = 0
given_j = 0
matrix = [[0]* cols for row in range(rows)]

matrix[1][1] = 1
matrix[1][2] = 1
matrix[1][3] = 1
matrix[2][1] = 1
matrix[2][2] = -1
matrix[2][3] = 1
for row in range(rows):
    print(matrix[row])
click_and_reveal(matrix, rows, cols, given_i, given_j)

# rows = 4
# cols = 4
# given_i = 1
# given_j = 2
# matrix = [[0]* cols for row in range(rows)]
# matrix[0][0] = -1
# matrix[0][1] = 1
# matrix[1][0] = 1
# matrix[1][1] = 1
# matrix[2][2] = 1
# matrix[2][3] = 1
# matrix[3][2] = 1
# matrix[3][3] = -1
#
# for row in range(rows):
#     print(matrix[row])
# click_and_reveal(matrix, rows, cols, given_i, given_j)