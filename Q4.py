#Q4.	Compare and contrast touples and and list with examples.

#Example to show mutability
List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print(List)

List[3] = 77
print(List)

# code to test that tuples are immutable
tuple1 = (0, 1, 2, 3)
tuple1[0] = 4
print(tuple1)