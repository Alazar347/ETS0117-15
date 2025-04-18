# 1. count()

Syntax:
```Python
tuple.count(value)
```
Description:
Returns the number of times a specified value appears in the tuple.

Example:

```Python
numbers = (1, 2, 3, 2, 4, 2, 5)
print(numbers.count(2))  # Output: 3
```
# 2. index()

Syntax:
```Python
tuple.index(value[, start[, stop]])
```

Description:
Returns the first index of the specified value. If the value is not found, it raises a ValueError. Optional start and stop can limit the search.

Example:

```Python
fruits = ('apple', 'banana', 'cherry', 'banana')
print(fruits.index('banana'))  # Output: 1
With start and stop:


print(fruits.index('banana', 2))  # Output: 3
```

