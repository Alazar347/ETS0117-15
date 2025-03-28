text = "Hello, World!"

# Default UTF-8 encoding
encoded_text = text.encode()
print(encoded_text)  # b'Hello, World!'

# Encoding with 'ascii' and ignoring errors
text_with_special = "Hello, 你好"
encoded_text_ignore = text_with_special.encode('ascii', 'ignore')
print(encoded_text_ignore)  # b'Hello, '

# Encoding with 'ascii' and replacing errors
encoded_text_replace = text_with_special.encode('ascii', 'replace')
print(encoded_text_replace)  # b'Hello, ??'
