def sorted_matrix_search(matrix, key):
    rows = len(matrix)
    cols = len(matrix[0])
    start = 0
    end = (rows * cols) - 1

    while start <= end:
        mid = start + (end - start) // 2
        matrix_mid = matrix[mid // cols][mid % cols]
        if key == matrix_mid:
            return True
        elif key < matrix_mid:
            end = mid - 1
        elif key > matrix_mid:
            start = mid + 1
    return False


def binary_search(arr, key):
    if len(arr) == 0:
        return False

    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if key == arr[mid]:
            return True
        elif key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1

    return False


arr = [3, 11, 19, 23, 26, 31, 39, 44, 50]
print(binary_search(arr, key=31))
print(binary_search(arr, key=10))
print(binary_search(arr, key=89))
print(binary_search(arr, key=25))
print(binary_search(arr, key=3))
print(binary_search(arr, key=11))

matrix = [
    [1, 3, 5, 7],
    [10, 13, 15, 17],
    [21, 26, 29, 37],
    [41, 53, 65, 77],
]

print("matrix search")
print(sorted_matrix_search(matrix, key=26))
print(sorted_matrix_search(matrix, key=22))
print(sorted_matrix_search(matrix, key=3))
print(sorted_matrix_search(matrix, key=65))

