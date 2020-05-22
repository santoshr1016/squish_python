def is_one_away_same_length(s1, s2):
    count_diff = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count_diff += 1
            if count_diff > 1:
                return False
    return True


def is_one_away_different_length(s1, s2):  # assume s1 is bigger
    count_diff = 0
    idx = 0
    while idx < len(s2):
        if s1[idx + count_diff] == s2[idx]:
            idx += 1
        else:
            count_diff += 1
            if count_diff > 1:
                return False
    return True


def is_one_away(s1, s2):
    size1 = len(s1)
    size2 = len(s2)
    if size1 - size2 >= 2 or size2 - size1 >= 2:
        return False
    elif size1 == size2:
        return is_one_away_same_length(s1, s2)
    elif size1 > size2:
        return is_one_away_different_length(s1, s2)
    else:
        return is_one_away_different_length(s2, s1)


s1 = "abcde"
s2 = "abfde"
# print(is_one_away_same_length(s1="abcde", s2="abfde"))
# print(is_one_away_different_length(s1="abcde", s2="abde"))
print(is_one_away(s1, s2))
