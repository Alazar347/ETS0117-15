# 1. add()
Purpose: Adds a single element to the set.

Syntax:
```Python 
set.add(element)
```
Note: If the element already exists, the set remains unchanged.

Example:

``` Python
fruits = {"apple", "banana"}
fruits.add("cherry")
print(fruits)  # Output: {'apple', 'banana', 'cherry'}
```

# 2. union()
Purpose: Combines elements from two or more sets.

Syntax:
```Python 
set1.union(set2, set3, ...)
```
Note: Returns a new set with all unique elements.

Example:

```Python
a = {1, 2, 3}
b = {3, 4, 5}
result = a.union(b)
print(result)  # Output: {1, 2, 3, 4, 5}
```


# 3. intersection()
Purpose: Returns the elements that are common in both sets.

Syntax:
```Python
set1.intersection(set2)
```
Note: Returns a new set with only the shared elements.

Example:

```Python
x = {1, 2, 3}
y = {2, 3, 4}
common = x.intersection(y)
print(common)  # Output: {2, 3}
```

# 4. difference()

Syntax:
```Python
set1.difference(set2)
```
Description:
Returns a new set containing elements that are in set1 but not in set2.

Example:
```Python
a = {1, 2, 3, 4}
b = {3, 4, 5}
print(a.difference(b))  # Output: {1, 2}
```
# 5. symmetric_difference()

Syntax:
```Python
set1.symmetric_difference(set2)
```

Description:
Returns a set with elements that are in either of the sets but not in both.

Example:

```Python
a = {1, 2, 3}
b = {3, 4, 5}
print(a.symmetric_difference(b))  # Output: {1, 2, 4, 5}
```
# 6. discard()

Syntax:
```Python
set.discard(element)
```

Description:
Removes the specified element from the set if it is present. If the element is not found, it does nothing (no error is raised).

Example:
```Python
a = {1, 2, 3}
a.discard(2)
print(a)  # Output: {1, 3}

a.discard(5)  # No error, does nothing
```

# 7. clear()

Description:
Removes all elements from a set, leaving it empty.

Syntax:
```Python
set.clear()
```

Example:
```Python
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)  # Output: set()
```
# 8.copy()

Description:
Returns a shallow copy of the set. The original set remains unchanged.

Syntax:
```Python
new_set = set.copy()
```
Example:
```Python
colors = {"red", "green", "blue"}
colors_copy = colors.copy()
print(colors_copy)  # Output: {'red', 'green', 'blue'}
```
# 9. isdisjoint()

Description:
Checks whether two sets have no elements in common.

Returns:
True if the sets are disjoint (no common elements).
False otherwise.

Syntax:

```Python
set1.isdisjoint(set2)
```
Example:

```Python
a = {1, 2, 3}
b = {4, 5, 6}
c = {3, 4, 5}

print(a.isdisjoint(b))  # Output: True
print(a.isdisjoint(c))  # Output: False
```