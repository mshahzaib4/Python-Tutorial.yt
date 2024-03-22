
my_list = [1, 2, 3]
my_list.append(4)
print(my_list) 
# Output: [1, 2, 3, 4]

my_list = [1, 2, 3, 2]
my_list.remove(2) 
print(my_list) 
# Output: [1, 3, 2]

my_list = [1, 2, 3, 2, 2]
count_of_2 = my_list.count(2)
print(count_of_2)  # Output: 3

my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # Output: [3, 2, 1]
