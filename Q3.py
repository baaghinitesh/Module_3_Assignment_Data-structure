# Q3.	Describe how to acess, modify, and delete elements in a list with examples. 

# a. Acess
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

print(thislist[-1])

# b. Modify
list = ['Iris', 'Orchids', 'Rose', 'Lavender']
list[0]='strowberry'
print(list)

# c. delete

list = ['Iris', 'Orchids', 'Rose', 'Lavender','Lily', 'Carnations']
print(list)
list.remove('Orchids')
print(list)

del list[1]
print(list)
print(list)

list = set(list)
list.discard('Lily')
list=list(list)
print(list)