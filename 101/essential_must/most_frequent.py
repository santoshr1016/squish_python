from collections import Counter


arr = [1, 3, 1, 3, 2, 1, 2, 1]
c = Counter(arr)
print(c.most_common(1))

count_dict = dict()
freq = 0
num = 0
for item in arr:
    count_dict[item] = count_dict.get(item, 0) + 1
    if count_dict[item] > freq:
        freq = count_dict[item]
        num, freq = item, freq
print(num, "->", freq)
