# Dictionary: Key:Value pairs,
# unordered(before Python 3.8!!!)
# Mutable
# under the hood - hash table
# type of key - should be hashable!!!
# one key - one value(has no collision)

users_dct = {"name": "Max", "age": 22, "city": "New York"}
print(users_dct)

users_dct_0 = dict(name= "Max", age= 22, city = "New York")
print(users_dct_0)

name = users_dct["name"]
print(name)

# key is not in the dict
try:
    print(users_dct["date"])
except KeyError as err:
    print(err)

# add pair key-value
users_dct["email"] = "example@lll.com"
print(users_dct)
# change value
users_dct["email"] = "example@ooo.com"
print(users_dct)

# del pair
del users_dct["email"]
print(users_dct)

city = users_dct.pop("city")
print(city)
print(users_dct)

last_item = users_dct.popitem()
print(last_item)
print(users_dct)

# check key in dict
print("last_name" in users_dct)


users_dct = {"name": "Max", "age": 22, "city": "New York"}
# looping
for key in users_dct:
    print(key)

for key, value in users_dct.items():
    print(f"user_dct[{key}]: {value}")

print(users_dct.values())

# copy
users_dct_copy = users_dct
print(id(users_dct) == id(users_dct_copy))
print(hash(id(users_dct)) ==  hash(id(users_dct_copy)))

users_dct_copy = users_dct.copy() # dict(users_dct)
print(id(users_dct) == id(users_dct_copy))
print(hash(id(users_dct)) ==  hash(id(users_dct_copy)))

# keys should be hashable (immutable + has hash)
pair_mutable = [1, 2]
pair_immutable = (1, 2)
two_int_sum_dct = {pair_immutable: 3}
print(two_int_sum_dct)
try:
    two_int_sum_dct = {pair_mutable: 3}
    print(two_int_sum_dct)
except TypeError as err:
    print(err)
