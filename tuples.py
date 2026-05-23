from sys import getsizeof
from timeit import timeit

# Tuples: ordered, immutable, allows duplicate elements
sequence_tpl = ("Max", 22, "Moscow")
print(type(sequence_tpl))
print(sequence_tpl)

# creation a tuple without parentheses
sequence_tpl = "Max", 22, "Moscow"
print(type(sequence_tpl))
print(sequence_tpl)

sequence_tpl = ("Max", )
print(type(sequence_tpl))
print(sequence_tpl)

sequence_tpl = "Max",
print(type(sequence_tpl))
print(sequence_tpl)

sequence_tpl = tuple(["Max", 22, "Moscow"])
print(type(sequence_tpl))
print(sequence_tpl)


# access elements - by index
item = sequence_tpl[0]
print(item)

print(sequence_tpl[-1])

try:
    print(sequence_tpl[len(sequence_tpl)])
except IndexError as err:
    print(err)


# iterating by for
for el in sequence_tpl:
    print(el)

# check included
print("Max" in sequence_tpl)

# count
apple_letters_tpl = tuple('apple')
print(apple_letters_tpl)
print(apple_letters_tpl.count('a'))

# index
print(apple_letters_tpl.index('a'))

try:
    print(sequence_tpl.index('z'))
except ValueError as err:
    print(err)

# slicing
print(apple_letters_tpl[2:5])
print(''.join(apple_letters_tpl[::-1]))

# unpacking
sequence_tpl = "Max", 22, "Moscow"
name, age, city = sequence_tpl
print(name, age, city)

name, *bullsh, city = sequence_tpl
print(name, city)
print(bullsh)

# compare list vs tuple
# 0, 1, 2, 3, 4., 5., True, "Example"
list_tmp = [0, 1, 2, 3, 4., 5., True, "Example"]
tuple_tmp = (0, 1, 2, 3, 4., 5., True, "Example")
print(getsizeof(list_tmp) , "bytes")
print(getsizeof(tuple_tmp) , "bytes")

print(timeit(stmt="[0, 1, 2, 3, 4., 5., True, 'Example']", number=1000000)) 
print(timeit(stmt="(0, 1, 2, 3, 4., 5., True, 'Example')", number=1000000)) 









