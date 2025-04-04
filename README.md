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