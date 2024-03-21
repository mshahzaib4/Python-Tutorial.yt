""""The Python return statement is a statement used inside a function or
 method to send the function's result back to the caller"""

def sum(a, b):
    return a + b
 
print(sum(3, 4))   # Output: (7)

############################################################################

def name(Name, Age=20): 
    return Name , Age

print(name("Shahzaib",30)) #Output: ('Shahzaib', 30)

############################################################################

def add_numbers(*args):    
    return  sum(args)

print(add_numbers(1,2,3,4,5)) #Output : 15

############################################################################     