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

isdigit()
Checks if all characters in the string are digits (0-9).

Example 

text1 = "12345"
text2 = "123abc"

print(text1.isdigit())  # Output: True
print(text2.isdigit())  # Output: False


swapcase()
Swaps uppercase characters to lowercase and vice versa.

Example 

text = "Hello World"
print(text.swapcase())  # Output: hELLO wORLD


zfill(width)
Pads the string with leading zeros until it reaches the specified width.

Example 

text = "42"
print(text.zfill(5))  # Output: 00042

partition()
The partition() method splits a string into three parts:

The part before the first occurrence of the specified separator.

The separator itself.

The part after the separator.

Example:

text = "hello world"
print(text.partition(" "))  

Output:

python
('hello', ' ', 'world')

rjust()
The rjust(width, fillchar) method right-aligns the string by padding it with a specified character (default is space) until it reaches the given width.

Example 

text = "42"
print(text.rjust(5, "0"))  


OutPut  

'00042'

casefold()
The casefold() method is similar to lower(), but it is more aggressive in handling case conversion, making it useful for case-insensitive comparisons.

Example 

text1 = "Hello World"
text2 = "hello world"

print(text1.casefold() == text2.casefold())  # Output: True

str.swapcase()
Description
Swaps uppercase to lowercase and vice versa.

Example 

text = "Hello World"
print(text.swapcase())  # Output: "hELLO wORLD"

str.lstrip()
Description
Removes leading spaces only.

Example

text = "  Hello World  "
print(text.lstrip())  # Output: "Hello World  "

str.rstrip()
Description
Removes trailing spaces only.

Example

text = "  Hello World  "
print(text.rstrip())  # Output: "  Hello World"




