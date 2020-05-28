def find_gcd(x, y):
    while (y):
        x, y = y, x % y

    return x


def generalizedGCD(num, arr):
    # WRITE YOUR CODE HERE
    num1 = arr[0]
    num2 = arr[1]
    gcd = find_gcd(num1, num2)

    for i in range(2, len(arr)):
        gcd = find_gcd(gcd, arr[i])

    return gcd
l = [2, 4, 6, 8, 16]
# l = [2, 3, 4, 5, 6]

print(generalizedGCD(4,l))
