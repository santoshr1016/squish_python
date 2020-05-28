def get_sum(l):
    total = 0
    for item in l:
        if type(item) == list:
            total += get_sum(item)
        else:
            total += item
    return total


l = [5,2,[7,-1],3,[6,[-13,8],4]]
print(get_sum(l))
