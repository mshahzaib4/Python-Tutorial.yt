""""Write a program that allows the user to specify a sequence of non-negative numbers
terminated by a negative numbers and then show the sum, minimum, average and
maximum of these numbers."""

num = int(input("Enter number: "))
fn = 1

for a in range(1, num + 1):
    fn += fn * (num - a)

print(fn)
