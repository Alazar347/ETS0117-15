# clear()

Description: Removes all elements from the dictionary, leaving it empty.

Syntax:
dict.clear()

Parameters:

  -None

Return Value:

 -None (Modifies the dictionary in place)

Example:
my_dict = {"a": 1, "b": 2, "c": 3}
my_dict.clear()
print(my_dict)  # Output: {}

# copy()

Description:
Returns a shallow copy of the dictionary. Changes to the copy do not affect the original dictionary.

Syntax:
dict.copy()

Parameters:

 -None

Return Value:

 -A new dictionary that is a copy of the original

Example:
original = {"x": 10, "y": 20}
copy_dict = original.copy()
print(copy_dict)  # Output: {'x': 10, 'y': 20}

# fromkeys()

Description:
Creates a new dictionary with the specified keys and a default value.

Syntax:
dict.fromkeys(iterable, value)

Parameters:

 -iterable: A sequence (e.g., list, tuple, set) containing keys for the new dictionary.

 -value (optional): The value assigned to all keys (default is None).

 Return Value:

-A new dictionary with the given keys and assigned values.

Example:
keys = ["name", "age", "city"]
new_dict = dict.fromkeys(keys, "Unknown")
print(new_dict)  
Output: {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}

# get(key[, default])
Description:
Returns the value for the specified key. If the key is not found, it returns the optional default value instead of raising an error.

Syntax:
dict.get(key, default)

Parameters:

 -key: The key to search for.

default (optional): Value to return if the key is not found. Defaults to None.

Example:
person = {'name': 'Alazar', 'age': 21}
print(person.get('name'))        # Output: Alazar
print(person.get('gender'))      # Output: None
print(person.get('gender', 'N/A'))  # Output: N/A

# items()
Description:
Returns a view object that displays a list of dictionary’s key-value tuple pairs.

Syntax:
dict.items()

Example:
person = {'name': 'Alazar', 'age': 21}
for key, value in person.items():
    print(key, value)
Output:
name Alazar
age 21

# keys()

Description:
Returns a view object that displays a list of all the keys in the dictionary.

Syntax:
dict.keys()

Example:

person = {'name': 'Alazar', 'age': 21}
print(person.keys()) 
Output: dict_keys(['name', 'age'])

You can convert it to a list if needed
print(list(person.keys()))  # Output: ['name', 'age']

# pop()

Syntax:
dict.pop(key[, default])

Parameters:

  -key (required): The key of the item to remove.

  -default (optional): The value to return if the key is not found. If not provided and the key doesn't exist, a KeyError is raised.

 Returns:

  -The value associated with the specified key, or the default value if provided.

Example:

person = {"name": "Alice", "age": 25}
age = person.pop("age")          # Returns 25, removes "age"
missing = person.pop("city", "Unknown")  # Returns "Unknown"

# popitem()

Syntax:
dict.popitem()

Parameters:
 -None

Returns:

 -A tuple (key, value) of the last inserted item.

 -Raises KeyError if the dictionary is empty.

Example:

person = {"name": "Alice", "age": 25}
last_item = person.popitem()  # Returns ('age', 25)

# setdefault()

Syntax:
dict.setdefault(key[, default])

Parameters:

 -key (required): The key to search for.
 -default (optional): The value to set if the key is not found. Defaults to None.

Returns:

 -The value of the existing key, or the default value if the key is inserted.

Example:

person = {"name": "Alice"}
age = person.setdefault("age", 30)  # Returns 30, adds "age": 30
existing = person.setdefault("name", "Bob")  # Returns "Alice"