from collections import Counter


words = [
       'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
       'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
       'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
       'my', 'eyes', "you're", 'under'
]

c = Counter(words)
top_three = c.most_common(3)
print(top_three)


from operator import itemgetter

rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

print(rows_by_fname)
print(rows_by_uid)

portfolio = [
       {'name':'GOOG', 'shares': 50},
       {'name':'YHOO', 'shares': 75},
       {'name':'AOL', 'shares': 20},
       {'name':'SCOX', 'shares': 65}
    ]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)

