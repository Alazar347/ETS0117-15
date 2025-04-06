person = {"name": "Alice"}
age = person.setdefault("age", 30)  # Returns 30, adds "age": 30
existing = person.setdefault("name", "Bob")  # Returns "Alice"

print(age)
print(existing)