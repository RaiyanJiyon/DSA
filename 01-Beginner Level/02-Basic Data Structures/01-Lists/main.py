# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements
print(my_list[0])   # Output: 1
print(my_list[-1])  # Output: 5

# Slicing
print(my_list[1:3]) # Output: [2, 3]

# Modifying elements
my_list[0] = 10
print(my_list)      # Output: [10, 2, 3, 4, 5]

# Adding elements
my_list.append(6)
print(my_list)      # Output: [10, 2, 3, 4, 5, 6]

# Removing elements
my_list.remove(3)
print(my_list)      # Output: [10, 2, 4, 5, 6]
