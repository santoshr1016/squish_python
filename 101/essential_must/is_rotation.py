def is_rotation(l1, l2):
    if len(l1) != len(l2):
        return False
    l1 = sorted(l1)
    l2 = sorted(l2)
    return l1 == l2


def is_rotation2(l1, l2):
    if len(l1) != len(l2):
        return False
    first_l1 = l1[0]
    idx = -1

    for i in range(len(l2)):
        if l2[i] == first_l1:
            idx = i
            break
    print(idx)
    if idx == -1:
        return False
    for i in range(len(l1)):
        j = (idx + i) % len(l1)
        print(j)
        if l1[i] != l2[j]:
            return False
    return True


l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [4, 5, 6, 7, 1, 2, 3]

print(is_rotation(l1, l2))
print(is_rotation2(l1, l2))
