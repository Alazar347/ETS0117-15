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

# insert() Method

Description:

The insert() method inserts an element at a specified index in a list.

Syntax:
list.insert(index, element)

Parameters:

    - index: The position where the element should be inserted.

    - element: The value to insert into the list.

Example: 

numbers = [1, 2, 4, 5]
numbers.insert(2, 3)  # Insert 3 at index 2
print(numbers)  # Output: [1, 2, 3, 4, 5]

# pop() Method

Description:

The pop() method removes and returns an element from a specified index. If no index is given, it removes and returns the last element.

Syntax:
element = list.pop(index)

Parameters:

  -index (optional): The position of the element to remove. If omitted, the last element is removed.

Example:

fruits = ['apple', 'banana', 'cherry']
removed_item = fruits.pop(1)  # Remove element at index 1
print(fruits)  # Output: ['apple', 'cherry']
print(removed_item)  # Output: 'banana'

# remove() Method

Description:

The remove() method removes the first occurrence of a specified value from the list.

Syntax:
list.remove(element)

Parameters:

  - element: The value to remove from the list. If the value is not found, a ValueError is raised.

Example:

colors = ['red', 'green', 'blue', 'green']
colors.remove('green')  # Removes the first occurrence of 'green'
print(colors)  # Output: ['red', 'blue', 'green']