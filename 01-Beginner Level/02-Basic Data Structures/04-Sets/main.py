# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding elements
my_set.add(6)
print(my_set)      # Output: {1, 2, 3, 4, 5, 6}

# Removing elements
my_set.remove(3)
print(my_set)      # Output: {1, 2, 4, 5, 6}

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))      # Output: {1, 2, 3, 4, 5}
print(set1.intersection(set2)) # Output: {3}
