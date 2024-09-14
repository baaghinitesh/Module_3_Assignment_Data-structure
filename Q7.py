# Q7. Describe how to add, modify, and delete items in a dictionary with examples.

# Adding elemnts in dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)
Dict[0] = 'Nitesh'
Dict[2] = 'jha'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict)

Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ")
print(Dict)

Dict[2] = 'Welcome'
print("\nUpdated key value: ")
print(Dict)

# modify
my_dict = {'name': 'Alice', 'age': 30}
my_dict['city'] = 'New York'
print(my_dict)

#Deleting elements in dictionary
Dict = {1: 'welcome', 'name': 'Nitesh', 'title': 'jha'}

print("Dictionary =")
print(Dict)
del(Dict[1]) 
print("Data after deletion Dictionary=")
print(Dict)

