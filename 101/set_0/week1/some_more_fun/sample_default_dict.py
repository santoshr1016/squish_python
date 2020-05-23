from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
d['a'].append(4)
d['b'].append(4)
print(d)

pairs = [('a', 1), ('a', 2), ('a', 3), ('b', 11), ('b', 22), ('c', 111), ('d', 1232)]
dd = {}
for key, value in pairs:
    if key not in dd:
        dd[key] = []
    dd[key].append(value)
print(dd)

# Using a defaultdict simply leads to much cleaner code:
do = defaultdict(list)
for key, value in pairs:
    do[key].append(value)
print(do)

