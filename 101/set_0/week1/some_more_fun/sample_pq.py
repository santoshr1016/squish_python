import heapq


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)
        # return f'Item({self.name})'


class PriorityQ:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


pq = PriorityQ()
pq.push(Item('foo'), 1)
pq.push(Item('bar'), 5)
pq.push(Item('spam'), 4)
pq.push(Item('tom'), 1)
pq.push(Item('grok'), 2)
print(pq.pop())
print(pq.pop())
print(pq.pop())
print(pq.pop())
print(pq.pop())

# print("Quotes: {0!r}, Without Quotes: {0!s}".format("cat"))
#
# i = Item('foo')
# print(i)
