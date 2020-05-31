s = "sasasdsgdgesdasd"
d = dict()
for item in s:
    d[item] = d.get(item, 0) + 1
print(d)
