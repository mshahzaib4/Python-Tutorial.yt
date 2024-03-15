"""Write a program that inputs a number N and extracts and prints each digit of N in
English e.g. if the input number N is 3546 then the program should print “Three
Five Four Six”."""
num = int(input("Enter the number: "))
print("\n")

revers = 0
num2 = num

while num != 0:
    rem_last = num % 10
    revers = revers * 10 + rem_last
    num = num // 10

while num2 != 0:
    rem2 = num2 % 10

    if rem2 == 0:
        print("Zero ", end="")
    elif rem2 == 1:
        print("One ", end="")
    elif rem2 == 2:
        print("Two ", end="")
    elif rem2 == 3:
        print("Three ", end="")
    elif rem2 == 4:
        print("Four ", end="")
    elif rem2 == 5:
        print("Five ", end="")
    elif rem2 == 6:
        print("Six ", end="")
    elif rem2 == 7:
        print("Seven ", end="")
    elif rem2 == 8:
        print("Eight ", end="")
    elif rem2 == 9:
        print("Nine ", end="")
    
    num2 = num2 // 10

print("\n")
