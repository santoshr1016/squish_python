def some_function(k):
    another_list = []
    for i in range(k):
        if i%2 == 0:
            another_list.append(i**2)
        else:
            another_list.append(i**3)
    return another_list


print(some_function(8))
# Shortening the above using list comprehension
lc = [(i**2) if i%2 == 0 else (i**3) for i in range(8)]
print(lc)

# Flattening the matrix
id_matrix = [[1,0,0],
             [2,0,0],
             [3,0,1]]

result = []
for row in id_matrix:
    for item in row:
        result.append(item)
print(result)
l = [col for row in id_matrix for col in row]
print(l)

# Filtering a list
evens = [item for item in range(1, 10) if item%2 == 0]
print(evens)


