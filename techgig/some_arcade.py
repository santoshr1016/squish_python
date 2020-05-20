'''
1
10
3 6 7 5 3 5 6 2 9 1
2 7 0 9 3 6 0 6 2 6
'''


def winner(arr1, arr2):
    size1 = len(arr1)
    size2 = len(arr2)
    i = 0
    j = 0
    win = 0
    while i < size1 and j < size2:
        if arr1[i] < arr2[j]:
            win += 1
            i += 1
            j += 1
        else:
            j += 1
    return win


def main():
    tc = int(input())
    input()
    for i in range(tc):
        arr1 = [int(item) for item in input().split()]
        arr1.sort()
        arr2 = [int(item) for item in input().split()]
        arr2.sort()

        win1 = winner(arr1, arr2)
        win2 = winner(arr2, arr1)
        if win1 > win2:
            print(win1)
        else:
            print(win2)

main()