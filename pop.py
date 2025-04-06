person = {"name": "Alice", "age": 25}
age = person.pop("age")          # Returns 25, removes "age"
missing = person.pop("city", "Unknown")  # Returns "Unknown"

print(age)
print(missing)