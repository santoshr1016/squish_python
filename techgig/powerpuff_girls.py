'''
4
2 5 6 3
20 40 90 50
'''

import sys

def main():
    n = int(input())
    items = [int(item) for item in input().split()]
    quant = [int(item) for item in input().split()]

    mapping = zip(items, quant)
    min = sys.maxsize
    for item in mapping:
        num = item[1]//item[0]
        if num < min:
            min = num
    print(min)

main()
