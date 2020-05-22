def rotate_90_formula(i, j, n):
    return j, n - 1 - i


def rotate(matrix, n):
    new_matrix = [[0]*n for item in range(n)]
    for row in range(n):
        for col in range(n):
            i, j = rotate_90_formula(row, col, n)
            new_matrix[i][j] = matrix[row][col]
    print(new_matrix)


n = 3
count = 1
matrix = [[0]*n for item in range(n)]
for row in range(n):
    for col in range(n):
        matrix[row][col] = count
        count += 1
print(matrix)

rotate(matrix, n)

