a = [11, 22, 3, 1, 5, 9, 87, 33, 54, 7, 8, 23]

# Slicing example
print(a[2:6])
print(a[7:])
print(a[:7])
print(a[:-1])
print(a[-4:])
print(a[-7:-3])
print(a[1:9:2])
print(a[1:-1:5])
print(a[::-1])

# List Comprehension
print([x**2 for x in range(6)])
print([x**2 for x in range(6) if x%2 == 0])

A = [1, 3, 5]
B = ['a', 'b']
AxB = [(i, j) for i in A for j in B]
print(AxB)

# Flatenning the 2D
list_2d = [['a', 'b', 'c'], ['d', 'e', 'f']]
list_1d = [item for row in list_2d for item in row]
print(list_1d)

A = [[1, 2, 3] , [4, 5, 6]]
AA = [[x**2 for x in row] for row in A]
print(AA)