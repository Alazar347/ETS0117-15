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

join() - Joins elements of a list into a single string.

Example 

words = ['Hello', 'Python', 'World']
print(" ".join(words))  # Output: Hello Python World

find() - Returns the index of the first occurrence of a substring, or -1 if not found.

Example 

text = "Hello World"
print(text.find("World"))  # Output: 6
print(text.find("Python"))  # Output: -1

count() - Counts occurrences of a substring in a string.

Example

text = "banana"
print(text.count("a"))  # Output: 3

capitalize()
Converts the first character of a string to uppercase and the rest to lowercase.

Example:

text = "hello world"
print(text.capitalize())  

Output:
Hello world

title()
Converts the first letter of each word to uppercase.

Example:

text = "hello world from python"
print(text.title())  

Output:
Hello World From Python

isalpha()
Returns True if all characters in the string are alphabetic (letters only, no numbers or symbols), otherwise False.

Example:

text1 = "HelloWorld"
text2 = "Hello123"

print(text1.isalpha())  # Output: True
print(text2.isalpha())  # Output: False