my_list = [2, 4, 5, 6, 8, 10]
product = 20

# for item in my_list:
#     if product % item:
#         continue
#     other = product//item
#     if other in my_list:
#         print(item, other)
seen = set()
for item in my_list:
    if product % item:
        continue
    else:
        other = product // item
        if other not in seen:
            seen.add(item)
        else:
            print(item, other)
