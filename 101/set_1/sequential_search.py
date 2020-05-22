def sequencial_search(the_list, key=22):
    for item in the_list:
        if item == key:
            print("Item present in List")
            return
    print("Item not found in List")


ll = [4, 9, 33, 99, 5, 11, 44, 22]
sequencial_search(ll)
