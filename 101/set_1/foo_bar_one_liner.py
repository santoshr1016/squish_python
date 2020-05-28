
l = ["Santosh" if not x%15 else "San" if not x%3 else "Tosh" if not x%5 else x for x in range(1, 21)]
print(l)

output = []
matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]
n_col = len(matrix[0])
for col in range(n_col):
    output_row = []
    for item in matrix:
        output_row.append(item[col])
    output.append(output_row)

ll = [[item[i] for item in matrix] for i in range(n_col)]

print(output)
print(ll)
