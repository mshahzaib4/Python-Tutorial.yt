"""The program must ask the user to enter the value of N and then input N numbers
and show the sum, average, maximum and minimum of the input numbers."""

N = int(input("Enter the value of N: "))

total_sum = 0

for i in range(N):
    num = float(input("Enter number: "))
    total_sum += num
    
    if num > maximum:
        maximum = num
    
    if num < minimum:
        minimum = num

average = total_sum / N
print("Sum:", total_sum)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)
