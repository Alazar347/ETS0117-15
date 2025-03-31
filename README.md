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






