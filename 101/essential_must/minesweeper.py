def mine_sweeper(bombs, rows, cols):
    matrix = [[0]*cols for i in range(rows)]
    print(matrix)
    for bomb in bombs:
        bomb_row = bomb[0]
        bomb_col = bomb[1]
        matrix[bomb_row][bomb_col] = -1

        for i in range(bomb_row-1, bomb_row+1+1):
            for j in range(bomb_col-1, bomb_col+1+1):
                if 0<=i<rows and 0<=j<cols and matrix[i][j] != -1:
                    matrix[i][j] += 1

    for row in range(rows):
        print(matrix[row])
"""
First Bomb at [0, 0]
[-1, 1, 1, 0]
[1, 1, 1, 0]
[0, 0, 0, 0]
Second Bomb at [0, 1]
[-1, -1, 1, 0]
[2, 2, 1, 0]
[0, 0, 0, 0]
"""

mine_sweeper([[0, 0], [0, 1]], 3, 4)
