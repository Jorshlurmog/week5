import timeit
# timeit() function takes two arguments: some Python code and a number of times for it to run
print(timeit.timeit("[x for x in range(1000000)]", number=1))
print(timeit.timeit("[x for x in range(10000000)]", number=1))
print(timeit.timeit("[x for x in range(100000000)]", number=1))
