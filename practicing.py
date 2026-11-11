# TUPLE UNPACKING

stats = (2, 15, 42)

minimun, maximum, total = min(stats), max(stats), sum(stats)

name, age = ("Nathaniel", 25)

#print(name, age)
#print(minimum, maximum, total)


# SORT BY A TUPLE

scores = [
    ("Alice", 90),
    ("Bob", 72),
    ("Charlie", 95),
    ("David", 81)
]

sort_by_score = sorted(scores, key=lambda x: x[1], reverse=True)

#print(sort_by_score)


# DEFAULTDICT COUNTING

word = "banana"

wc = {}

for letter in word:
    previous_count = wc.get(letter, 0)
    wc[letter] = previous_count + 1

print(wc)
