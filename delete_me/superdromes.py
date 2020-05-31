def palindrome(binary):
    return binary == binary[::-1]


def superdrome(num):
    binary = str(bin(num))[2:]
    if palindrome(binary) and palindrome(str(num)):
        print(num)
        return 1
    else:
        return 0


n = int(input())
result = [0]
for i in range(1,n+1):
    result.append(result[-1] + superdrome(i))
for i in range(n):
    print(result[i+1], end=' ')

