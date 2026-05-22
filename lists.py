# List: ordered, mutable, allows duplicate(not unique) elements

fruits_ls = ["cherry", "banana", "apple"]
print(fruits_ls)

empty_list = list()
print(empty_list)

diff_types_ls = [2, 2., True, "apple", "apple"]
print(diff_types_ls)

# Access to elements by index
item_1 = diff_types_ls[0]
print(item_1)
print(fruits_ls[1])

# out of range -> Index Error
try:
    print([len(fruits_ls)])
except(IndexError) as err:
    print("IndexError: "+str(err))

#Negative indexes: from the end to start
print(fruits_ls[-1])

# iterate by the sequence
for el in diff_types_ls:
    print(el)

# Check included
print("banaba" in fruits_ls)
if "lemon" in fruits_ls:
    print("yes")
else:
    print("no")

# length
print(len(fruits_ls))

#append element
print(f"fruit_ls {'has' if 'lemon' in fruits_ls else 'has no'} lemon")
fruits_ls.append("lemon")
print(f"fruit_ls {'has' if 'lemon' in fruits_ls else 'has no'} lemon")

# insert element
fruits_ls.insert(1, "blueberry")
print(fruits_ls)

# pop
item = fruits_ls.pop()
print(item)
print(fruits_ls)

# remove
item = fruits_ls.remove("banana")
print(fruits_ls)
try:
    fruits_ls.remove("milk")
except ValueError as err:
    print(err)

# make empty
empty_ls = fruits_ls.clear()
print(fruits_ls)

fruits_ls = ["cherry", "banana", "apple"]

# reverse list
reversed_fruits_ls = fruits_ls.reverse()
reversed_fruits_ls = list(reversed(fruits_ls))
print(reversed_fruits_ls)
print(reversed_fruits_ls[::-1])

# sort
fruits_ls.sort()
print(fruits_ls)

desc_10 = [i for i in range(10, 0, -1)]
print(desc_10)
asc_10 = sorted(desc_10)
print(asc_10)


# multiple

five_zeros = [0] * 5
print(five_zeros)

#concatenate lists
adding = [101, 102, 103]
five_zeros = five_zeros + adding
print(five_zeros)

#slicing
print(five_zeros[3:8])
print(five_zeros[-3:])
print(five_zeros[::2])

# copying
copy_fruit = fruits_ls
print(copy_fruit)

copy_fruit.append(404)
print(fruits_ls)

#shell copy
copy_fruit = fruits_ls.copy()  # list() ls[::]
copy_fruit.append(505)
print(fruits_ls)

# list comprehension
a = [i**i for i in asc_10 if i%2 == 0]
print(a)