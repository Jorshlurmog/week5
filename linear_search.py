# Function for a linear search.
def linear_search(the_list, target):
    for x in range(len(the_list)):
        if the_list[x] == target:
            print("Found at index", x)
            return x

    print("Target is not in the list")
    # ...............Returns -1 because index must be 0 or greater to be in list range.
    return -1


my_list = [6, 3, 4, 2, 5, 7]
linear_search(my_list, 5)
linear_search(my_list, 3)
linear_search(my_list, 7)
linear_search(my_list, 8)
