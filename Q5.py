# Q5. Describe the key features of sets and provide examples of their  uses.

numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = set(numbers)

unique_list = list(unique_numbers)
print(unique_list)

# membership testing
fruits = {"apple", "banana", "cherry"}

if "banana" in fruits:
    print("Banana is in the set")

# sets operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
print(set1 | set2)  # Output: {1, 2, 3, 4, 5}

# Intersection
print(set1 & set2)  # Output: {3}

# Difference
print(set1 - set2)  # Output: {1, 2}

# Symmetric Difference
print(set1 ^ set2)  # Output: {1, 2, 4, 5}


