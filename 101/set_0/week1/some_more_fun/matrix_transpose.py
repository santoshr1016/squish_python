X = [[12,7],
    [4 ,5],
    [3 ,8]]

rows = len(X)
cols = len(X[0])
transpose = [[0]*rows for col in range(cols)]
print(transpose)

for row in range(rows):
    for col in range(cols):
        transpose[col][row] = X[row][col]
print(transpose)

# using list comprehension
result = [[X[j][i] for j in range(rows)] for i in range(cols)]
print(result)
