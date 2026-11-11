people = [
    {"name": "Alice", "age": 23},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 35}
]

caps_people = [x["name"].upper() for x in people]

print(caps_people)