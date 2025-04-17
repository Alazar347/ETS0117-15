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

# 10.difference_update()

Description:
Removes all elements of another set (or iterable) from the current set.

 Syntax:
```Python
set1.difference_update(set2)
```
This updates set1 by removing all elements that are also in set2.

Example:
```Python
a = {1, 2, 3, 4, 5}
b = {3, 4, 6}
a.difference_update(b)
print(a)  # Output: {1, 2, 5}
```
Note:
It modifies the original set.
It’s equivalent to: a = a - b, but it doesn’t return a new set.

# 11.intersection_update()

Description:
Updates the current set, keeping only elements found in both sets.

Syntax:
```Python
set1.intersection_update(set2)
```
Example:
```Python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a.intersection_update(b)
print(a)  # Output: {3, 4}
```
Note:
It’s an in-place operation (modifies a).
Equivalent to: a = a & b, but again, no new set is returned.

# 12.issubset()

Description:
Checks if all elements of the current set are in another set.

📖Syntax:
```Python
set1.issubset(set2)
```
Returns True if every element in set1 is in set2, otherwise False.

Example:
```Python
a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))  # Output: True
```
Note:
This does not modify any set.
You can also use the <= operator: a <= b.

# 13.issuperset() Method
Description:
The issuperset() method checks if the calling set contains all elements of another set.
It returns True if it does, otherwise False.

Syntax:
```Python
A.issuperset(B)
```
A is the calling set.
Returns True if every element of B is in A.

 Example:
```Python
A = {1, 2, 3, 4, 5}
B = {2, 3}

print(A.issuperset(B))  # Output: True
print(B.issuperset(A))  # Output: False
```
# 14.pop() Method
 Description:
Removes and returns an arbitrary element from the set.
Since sets are unordered, you can't predict which element will be removed.

Raises a KeyError if the set is empty.

 Syntax:
```Python
set.pop()
```
 Example:
```Python
colors = {'red', 'blue', 'green'}
removed = colors.pop()

print("Removed:", removed)
print("Remaining set:", colors)
```
# 15.remove() Method
 Description:
Removes a specific element from the set.

If the element is not found, it raises a KeyError.

 Syntax:
```Python
set.remove(element)
```
 Example:
```Python
fruits = {'apple', 'banana', 'cherry'}
fruits.remove('banana')

print(fruits)  # Output: {'apple', 'cherry'}

 fruits.remove('orange')  # Would raise KeyError
 ```

# 16.set.update()

Description:
The update() method adds elements from another iterable (like a set, list, or tuple) into the original set. It performs a union, adding all elements from the other set(s) that are not already present in the original.

Syntax:
```Python
set1.update(iterable)
```
Behavior:

Modifies set1 in place.
Adds all unique elements from the iterable.
Keeps existing elements intact.

Example:
```Python
a = {1, 2, 3}
b = {3, 4, 5}
a.update(b)
print(a)  # Output: {1, 2, 3, 4, 5}
```
#  17 set.symmetric_difference_update()
Description:
The symmetric_difference_update() method updates the set by keeping only elements that are not common between the set and the given iterable. In other words, it performs a symmetric difference, removing shared elements and adding only the different ones.

Syntax:
```Python
set1.symmetric_difference_update(iterable)
```
Behavior:

Modifies set1 in place.
Removes elements present in both sets.
Adds elements unique to the other set.

Example:
```Python
a = {1, 2, 3}
b = {3, 4, 5}
a.symmetric_difference_update(b)
print(a)  # Output: {1, 2, 4, 5}
```