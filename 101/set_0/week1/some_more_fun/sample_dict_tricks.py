prices = {
       'ACME': 45.23,
       'AAPL': 612.78,
       'IBM': 205.55,
       'HPQ': 37.20,
       'FB': 10.75
}

# Getting minimun and maximum

min_price = min(zip(prices.values(), prices.keys()))
print(min_price)

max_price = max(zip(prices.values(), prices.keys()))
print(max_price)

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

# When doing these calculations, be aware that zip() creates an iterator that can only be consumed once.
# For example, the following code is an error:

prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))  # OK
# print(max(prices_and_names))  # ERROR
