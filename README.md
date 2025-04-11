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