"""Write a program to print the factorial of a number N input by the user."""

num = int(input("Enter Number : "))
factorial = 1

if num > 0:
    for a in range(1, num + 1):
        factorial *= a
else:
    print("Enter invalid")

print("Factorial is :", factorial)