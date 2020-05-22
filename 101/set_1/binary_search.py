def binary_search(the_list, key=90):
    start = 0
    end = len(the_list) - 1

    while start <= end:
        mid = start + (end - start)//2
        if the_list[mid] == key:
            print("Found the item")
            return
        else:
            if the_list[mid] > key:
                end = mid - 1
            else:
                start = mid + 1
    print("Item not found")


ll = [9, 11, 22, 44, 49, 55, 65, 69, 77, 88, 99, 111]
binary_search(ll)
