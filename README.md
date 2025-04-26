# upper() converts all characters in a string to uppercase.

Example
```Python
text = "hello, world!"
uppercase_text = text.upper()
print(uppercase_text)
```

Output
```Python
HELLO, WORLD!
```

# lower() - Converts all characters in a string to lowercase

Example

```Python
text = "Hello World"
print(text.lower())
```
Output
```Python
hello world
```
# str.index(substring)
Same as find(), but raises an error if the substring is not found.

Example

```Python
text = "hello world"
print(text.index("world")) # Output: 6

print(text.index("Python")) # Raises ValueError
```

# str.startswith(substring)
Checks if the string starts with the given substring.

Example
```Python
text = "hello world"
print(text.startswith("hello")) # Output: True
print(text.startswith("world")) # Output: False
```

# str.endswith(substring)
Checks if the string ends with the given substring.

Example
```Python
text = "hello world"
print(text.endswith("world")) # Output: True
print(text.endswith("hello")) # Output: False
```

# strip() - Removes leading and trailing whitespaces.

Example
```Python
text = " Hello World "
print(text.strip()) # Output: "Hello World"
```

# replace() - Replaces a specified substring with another substring.

Example
```Python
text = "Hello World"
print(text.replace("World", "Python")) # Output: Hello Python
```

# split() - Splits a string into a list based on a separator.

Example 
```Python
text = "apple,banana,orange"
print(text.split(","))  # Output: ['apple', 'banana', 'orange']
```
# join() - Joins elements of a list into a single string.

Example 
```Python
words = ['Hello', 'Python', 'World']
print(" ".join(words))  # Output: Hello Python World
```
# find() - Returns the index of the first occurrence of a substring, or -1 if not found.

Example 
```Python
text = "Hello World"
print(text.find("World"))  # Output: 6
print(text.find("Python"))  # Output: -1
```
# count() - Counts occurrences of a substring in a string.

Example
```Python
text = "banana"
print(text.count("a"))  # Output: 3
```
# capitalize()
Converts the first character of a string to uppercase and the rest to lowercase.

Example:
```Python
text = "hello world"
print(text.capitalize())  
```
Output:
```Python
Hello world
```

# title()
Converts the first letter of each word to uppercase.

Example:
```Python
text = "hello world from python"
print(text.title())  
```
Output:
```Python
Hello World From Python
```
# isalpha()
Returns True if all characters in the string are alphabetic (letters only, no numbers or symbols), otherwise False.

Example:
```Python
text1 = "HelloWorld"
text2 = "Hello123"

print(text1.isalpha())  # Output: True
print(text2.isalpha())  # Output: False
```

# isdigit()
Checks if all characters in the string are digits (0-9).

Example 
```Python
text1 = "12345"
text2 = "123abc"

print(text1.isdigit())  # Output: True
print(text2.isdigit())  # Output: False
```


# swapcase()
Swaps uppercase characters to lowercase and vice versa.

Example 
```Python
text = "Hello World"
print(text.swapcase())  # Output: hELLO wORLD
```

# zfill(width)
Pads the string with leading zeros until it reaches the specified width.

Example 
```Python
text = "42"
print(text.zfill(5))  # Output: 00042
```

# partition()

The partition() method splits a string into three parts:
The part before the first occurrence of the specified separator.
The separator itself.

The part after the separator.

Example:
```Python
text = "hello world"
print(text.partition(" "))  
```
Output:
```Python
('hello', ' ', 'world')
```

# rjust()
The rjust(width, fillchar) method right-aligns the string by padding it with a specified character (default is space) until it reaches the given width.

Example 
```Python
text = "42"
print(text.rjust(5, "0"))  
```

OutPut: 
```Python
'00042'
```
# casefold()
The casefold() method is similar to lower(), but it is more aggressive in handling case conversion, making it useful for case-insensitive comparisons.

Example 
```Python
text1 = "Hello World"
text2 = "hello world"

print(text1.casefold() == text2.casefold())  # Output: True
```
# str.swapcase()
Description
Swaps uppercase to lowercase and vice versa.

Example 
```Python
text = "Hello World"
print(text.swapcase())  # Output: "hELLO wORLD"
```
# str.lstrip()
Description
Removes leading spaces only.

Example
```Python
text = "  Hello World  "
print(text.lstrip())  # Output: "Hello World  "
```
# str.rstrip()
Description
Removes trailing spaces only.

Example
```Python
text = "  Hello World  "
print(text.rstrip())  # Output: "  Hello World"
```
# isupper()
Description
The isupper() method checks whether all the characters in a string are uppercase. It returns True if all characters are uppercase and there is at least one alphabetic character; otherwise, it returns False.

Return Value
Returns True if all alphabetic characters in the string are uppercase.
Returns False if the string contains lowercase letters or no alphabetic characters.

# islower()
Description
The islower() method checks whether all the characters in a string are lowercase. It returns True if all characters are lowercase and there is at least one alphabetic character; otherwise, it returns False.

Return Value
Returns True if all alphabetic characters in the string are lowercase.
Returns False if the string contains uppercase letters or no alphabetic characters.


# encode()
Description
The encode() method encodes a string using the specified encoding format. By default, it uses 'utf-8'.

Parameters
encoding (optional): The encoding format (e.g., 'utf-8', 'ascii', 'latin-1', etc.). Default is 'utf-8'.

errors (optional): Specifies how to handle encoding errors. Possible values:

'strict' (default): Raises an error for encoding failures.

'ignore': Ignores characters that cannot be encoded.

'replace': Replaces unencodable characters with a replacement character.

Return Value
Returns a bytes object representing the encoded version of the string.

# len() Function

The len() function in Python returns the number of characters in a string.

Syntax:
```Python
len(string)
```
Example:
```Python
text = "Hello, World!"
length = len(text)
print(length)  # Output: 13
```
# Strings (Formatted String Literals)

Introduced in Python 3.6, f-strings provide an efficient and readable way to format strings using expressions inside curly braces {}.

Syntax:
```Python
f"string {expression}"
```
Example:
```Python
name = "Alice"
age = 25
message = f"My name is {name} and I am {age} years old."
print(message)  # Output: My name is Alice and I am 25 years old.
```
# format() Method

The format() method allows formatting strings using placeholders {}.

Syntax:
```Python
"string {}".format(value)
```
Example:
```Python
name = "Bob"
age = 30
message = "My name is {} and I am {} years old.".format(name, age)
print(message)  # Output: My name is Bob and I am 30 years old.
```
# isspace() Method

Description:

The isspace() method in Python is used to check whether all the characters in a given string are whitespace characters. It returns True if the string consists only of whitespace characters (spaces, tabs, newlines, etc.), and False otherwise.

Syntax:
```Python
string.isspace()
```
Return Value:

   - Returns True if the string contains only whitespace characters.
   - Returns False otherwise.

Example: 
```Python
  # Example 1: String with spaces
s1 = "   "
print(s1.isspace())  # Output: True

# Example 2: String with tab and newline
s2 = "\t\n"
print(s2.isspace())  # Output: True

# Example 3: String with non-whitespace characters
s3 = "hello world"
print(s3.isspace())  # Output: False

# Example 4: Empty string
s4 = ""
print(s4.isspace())  # Output: False
```
# isalnum() Method

Description:

The isalnum() method checks if a string consists only of alphanumeric characters (letters and numbers) and contains at least one character. If all characters in the string are either alphabetic (a-z, A-Z) or digits (0-9), it returns True; otherwise, it returns False.

Syntax:
```Python
string.isalnum()
```
Return Value:

   - Returns True if all characters in the string are alphanumeric.
   - Returns False if the string contains special characters, spaces, or is empty.

Example: 
```Python
 # Example 1: String with letters and numbers
s1 = "Python123"
print(s1.isalnum())  # Output: True

# Example 2: String with only letters
s2 = "Python"
print(s2.isalnum())  # Output: True

# Example 3: String with special characters
s3 = "Python@123"
print(s3.isalnum())  # Output: False

# Example 4: String with spaces
s4 = "Python 123"
print(s4.isalnum())  # Output: False

# Example 5: Empty string
s5 = ""
print(s5.isalnum())  # Output: False
```