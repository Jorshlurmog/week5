unsorted_list = [1903, 994, 56, 3, 88]


def bubblesort(the_list):
    high_idx = len(the_list) - 1

    for i in range(high_idx):
        # We create a flag ('list_changed') for the case of the list being changed.
        list_changed = False
        for j in range(high_idx):
            item = the_list[j]
            next = the_list[j+1]

            if item > next:
                the_list[j] = next
                the_list[j + 1] = item
                # We change the flag to True
                list_changed = True

            print(the_list, i, j)
        print(list_changed)
        if list_changed == False:
            break


bubblesort(unsorted_list)
