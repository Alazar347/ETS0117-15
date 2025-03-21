.upper() converts all characters in a string to uppercase.

Example

text = "hello, world!"
uppercase_text = text.upper()
print(uppercase_text)

Output

HELLO, WORLD!

lower() - Converts all characters in a string to lowercase

Example

text = "Hello World"
print(text.lower())

Output

hello world

str.index(substring)
Same as find(), but raises an error if the substring is not found.

text = "hello world"
print(text.index("world")) # Output: 6

# print(text.index("Python")) # Raises ValueError

str.startswith(substring)
Checks if the string starts with the given substring.

text = "hello world"
print(text.startswith("hello")) # Output: True
print(text.startswith("world")) # Output: False

str.endswith(substring)
Checks if the string ends with the given substring.

text = "hello world"
print(text.endswith("world")) # Output: True
print(text.endswith("hello")) # Output: False

strip() - Removes leading and trailing whitespaces.

Example

text = " Hello World "
print(text.strip()) # Output: "Hello World"

replace() - Replaces a specified substring with another substring.

Example

text = "Hello World"
print(text.replace("World", "Python")) # Output: Hello Python

split() - Splits a string into a list based on a separator.

Example 

text = "apple,banana,orange"
print(text.split(","))  # Output: ['apple', 'banana', 'orange']