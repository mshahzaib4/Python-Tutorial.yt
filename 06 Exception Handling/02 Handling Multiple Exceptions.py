"""Handling multiple exceptions in programming is a common task, 
especially when you have code that might raise different types of errors. """

try:
    # Your code that might raise exceptions
    a = 10
    b = 2
    result = a / b
except ZeroDivisionError as e:
    print("Cannot divide by zero:", e)
else:
    print("Result:", result)
finally:
    print("This will always execute.")
