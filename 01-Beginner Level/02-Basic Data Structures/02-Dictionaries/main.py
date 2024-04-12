# Creating a dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Accessing elements
print(my_dict['name'])  # Output: Alice
print(my_dict.get('age')) # Output: 30

# Modifying elements
my_dict['age'] = 25
print(my_dict)          # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Adding new key-value pairs
my_dict['gender'] = 'Female'
print(my_dict)          # Output: {'name': 'Alice', 'age': 25, 'city': 'New York', 'gender': 'Female'}

# Removing key-value pairs
del my_dict['city']
print(my_dict)          # Output: {'name': 'Alice', 'age': 25, 'gender': 'Female'}
