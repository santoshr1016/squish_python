import heapq

nums = [1, 9, 5, 3, -9, 11, 23, 14, 42, 2, 19, 4]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))
portfolio = [
       {'name': 'IBM', 'shares': 100, 'price': 91.1},
       {'name': 'AAPL', 'shares': 50, 'price': 543.22},
       {'name': 'FB', 'shares': 200, 'price': 21.09},
       {'name': 'HPQ', 'shares': 35, 'price': 31.75},
       {'name': 'YHOO', 'shares': 45, 'price': 16.35},
       {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
print(cheap)

expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(expensive)

port_inc = sorted(portfolio, key=lambda x: x['price'])
print(port_inc)

port_dec = sorted(portfolio, key=lambda x: x['price'], reverse=True)
print(port_dec)

nums = [1, 8, 2, 23, 7, -4, 18, 25, 42, 37, 2]
heap = list(nums)
heapq.heapify(heap)
print(heap)
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heap)



