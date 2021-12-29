def linear_search_dictionary(dictionary, target):
    for x in dictionary:
        if dictionary[x] == target:
            print("Found target at key", x)
            return x
    print("Target is not in dictionary")
    return None


my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)
