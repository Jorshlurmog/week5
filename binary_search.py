def binary_search(the_list, target):
    lower_bound = 0
    upper_bound = len(the_list) - 1

    while lower_bound <= upper_bound:
        # Pivot is found using floor division, which returns an answer rounded down to the nearest integer.
        # This is used because list indexes are only in integer format (for example, 2.5 is not a valid index).
        pivot = (lower_bound + upper_bound) // 2
        pivot_value = the_list[pivot]

        if pivot_value == target:
            return pivot
        if pivot_value > target:
            upper_bound = pivot - 1
        else:
            lower_bound = pivot + 1

    return -1


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
name_list = ['John', 2, 3, 4, 'Jacob', 'Jingleheimer', 'Schmidt']
print(binary_search(my_list, 10))
print(binary_search(my_list, 4))
print(binary_search(my_list, 33))


print(name_list.index('Jingleheimer'))
