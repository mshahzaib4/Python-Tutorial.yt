"""Sets in Python are used to store multiple items in a single variable. It is one of the four built-in data types in Python that is used to store collections of data. The other three are List, Tuple, and Dictionary, each with different qualities and usages."""


# Creating a set with duplicate elements
my_set = {1, 2, 2, 3, 4, 4, 5}

print(my_set)

# Adding and Removing Elements
my_set.add(6)
print(my_set)

my_set.remove(3)
print(my_set)

my_set.discard(7)  
