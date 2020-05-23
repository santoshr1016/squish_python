from collections import defaultdict

cities = {'San Francisco': 'US', 'London':'UK',
        'Manchester':'UK', 'Paris':'France',
        'Los Angeles':'US', 'Seoul':'Korea'}

dd = defaultdict(list)

for k, v in cities.items():
    dd[v].append(k)

for k, v in dd.items():
    print(k,":", v)

d2 = {}
for k,v in cities.items():
       d2.setdefault(v,[]).append(k)
print(d2)

ddd = {}
L = [1,2,4,8,16,32,64,128,256,512,1024,32768,65536,4294967296]
for item in L:
    ddd.setdefault(len(str(item)), []).append(item)
print(ddd)

m = list( filter(lambda x:x % 2 == 0, range(10) ) )
print(m)