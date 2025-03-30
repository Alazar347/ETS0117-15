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