from collections import Counter
ss = """I figured it out I figured it out from black and white Seconds and hours Maybe they had to take some time"""

d = {}

words = ss.split(' ')
c = Counter(ss)
print(c.most_common())
for item in words:
    d[item] = d.get(item, 0) + 1
print(d)
