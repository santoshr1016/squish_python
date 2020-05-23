from collections import deque

d = deque(maxlen=3)
d.append(11)
d.append(22)
d.append(33)
print(d)   # [11, 22, 33] deque([11, 22, 33], maxlen=3)
d.append(44)  # since max length is 3, if new item is added, 11 will go out
print(d)   # deque([22, 33, 44], maxlen=3)
d.append(55)  # 22 popped out
print(d)   # deque([33, 44, 55], maxlen=3)

dd = deque([1, 2, 3, 4, 5])
# Another property is
dd.appendleft(101)
dd.append(102)
print(dd)
dd.pop()
print(dd)
dd.popleft()
print(dd)