def simple_repeat(a = "AADBBBCCAAADFGG"):
    print(a)
    result = ""
    size = len(a)
    if size == 0:
        return ""
    if size == 1:
        return a + "1"

    index = 1
    count = 1
    while index < size:
        if a[index] == a[index - 1]:
            count += 1
        else:
            result = result + a[index-1] + str(count)
            count = 1
        index += 1
    result = result + a[index - 1] + str(count)
    print(result)


simple_repeat()
