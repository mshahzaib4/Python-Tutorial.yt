"""Dictionaries are a collection of key-value pairs used to store and manage data in Python.Unlike sequences like lists and tuples, 
dictionaries are inherently unordered and use a unique system of keys and values."""

# Empty dictionary
empty_dict = {}

# Dictionary with some data
# Dictionary with some data
my_dict = {
    "name": "Muhammad Shahzaib Yaqoob",
    "age": 19,
    "Country": "Pakistan"
}

print(my_dict["name"])  
print(my_dict["age"])   

# Iterating over values
for value in my_dict.values():
    print(value)

   
    
my_dict = {
    "name": {"Muhammad Shahzaib Yaqoob","Muhammad Zohaib","Muhammad Masab Ali"},
    "age": {19,22,33},
    "Country": {"Pakistan","Pakistan","Pakistan"}
}

for value in my_dict.values():
    print(value)