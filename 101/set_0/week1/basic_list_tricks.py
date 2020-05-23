# arr = map(int, [item for item in input().strip().split()])
# print(list(arr))
#
# arr = [int(arr_temp) for arr_temp in input().strip().split()]
# print(arr)

data = {}
for _ in range(int(input())):
    name, *marks = input().split()
    data[name] = [float(m) for m in marks]
print(data)