
# A lambda function that takes one argument
square = lambda x: x * x

print(square(5))  # Output: 25
print(square(8))  # Output: 64


# A lambda function that takes two argument

add = lambda x, y: x + y

print(add(3, 4))  # Output: 7
print(add(-1, 5))  # Output: 4

#  Filtering a List with Lambda

age = [10, 20, 30, 40, 50]

filtered_age = list(filter(lambda x: x >= 20 and x <= 40, age))
print(filtered_age)

add=lambda a,b,c:a+b+c
print(add(1,2,3)) # output  : 6