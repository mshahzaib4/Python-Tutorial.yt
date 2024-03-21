"""The * symbol, when used in function definitions, indicates that the function can accept a variable number of arguments.
 This is particularly useful when you don't know in advance how many arguments will be passed to a function."""

def add(*args):
    result = 0
    for num in args:
        result += num
    return result

print(add(1, 2, 3))  
print(add(1, 2, 3, 4, 5)) 


def valid_function(arg1, **kwargs):
    print("arg1:", arg1)

    print("Additional keyword arguments (**kwargs):", kwargs)

valid_function("Hello", name="Muhammad Shahzaib",Fullname="Muhammad Shahzaib Yaqoob", age=30)


def valid_function(arg1, *args, **kwargs,):
    print("arg1:", arg1)
    print("Additional positional arguments (*args):", args)
    print("Additional keyword arguments (**kwargs):", kwargs)

# Example usage
valid_function("Hello", 1, 2, 3, name="Muhammad Shahzaib Yaqoob", age=30)



'''When defining a Python function, there are three types of arguments that you should know about:

1. Positional arguments: These are required arguments that must be provided when calling the function. They are specified by name and order in the function definition. 

2. *args: This syntax allows the function to accept any number of additional positional arguments. These arguments are collected into a tuple called args. 

3. **kwargs: This syntax allows the function to accept any number of additional keyword arguments. These arguments are specified as key-value pairs and collected into a dictionary called kwargs. 

It's worth noting that *args and **kwargs are optional and not required in function definitions.'''



