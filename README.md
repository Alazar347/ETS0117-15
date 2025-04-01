# append() Method

Description:
The append() method adds a single element to the end of a list. It modifies the original list in place.

Syntax:

list.append(element)

Parameters:
 - element: The item to be added to the list.

Return Value:
 - Returns None, but updates the original list.

 Example: 

numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # Output: [1, 2, 3, 4]

# clear() Method

Description:
The clear() method removes all elements from a list, leaving it empty.

Syntax:
list.clear()

Parameters:
   - None

Return Value:
  - Returns None, but modifies the original list to an empty list.

Example: 


fruits = ['apple', 'banana', 'cherry']
fruits.clear()
print(fruits)  # Output: []

# copy() Method

Description:
The copy() method creates a shallow copy of the list. This means that changes to the new list won’t affect the original list.

Syntax:
new_list = list.copy()

Parameters:
   - None

Return Value:
  - Returns a new list that is a copy of the original list.

Example: 

original = [1, 2, 3]
copy_list = original.copy()
copy_list.append(4)

print(original)  # Output: [1, 2, 3]
print(copy_list)  # Output: [1, 2, 3, 4]

 # count()

Description
The count() method returns the number of occurrences of a specified element in the list.

Syntax:
list.count(element)

Parameters

   - element: The value whose occurrences need to be counted in the list.

Return Value

  - Returns an integer representing the number of times the specified element appears in the list.

  Example
  numbers = [1, 2, 3, 4, 2, 2, 5]
  print(numbers.count(2))  # Output: 3

# index()

Description

The index() method returns the first occurrence index of a specified element in the list.

Syntax:
list.index(element, start, end)

Parameters

  - element: The value to be searched in the list.

  - start (optional): The starting index from where to begin the search.

  - end (optional): The ending index where the search stops.

Return Value

  - Returns the index (zero-based) of the first occurrence of the specified element.

  - Raises a ValueError if the element is not found.

Example

fruits = ['apple', 'banana', 'cherry', 'banana']
print(fruits.index('banana'))  # Output: 1

# extend()

Description

The extend() method appends elements from an iterable (such as another list, tuple, or set) to the end of the current list.

Syntax
list.extend(iterable)

Parameters

  - iterable: A collection (list, tuple, set, etc.) whose elements will be added to the end of the list.

Return Value

 - Modifies the original list in place and returns None.

Example: 

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)  # Output: [1, 2, 3, 4, 5, 6]




