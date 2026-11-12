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
from collections import defaultdict

word = "banana"

wc = defaultdict(int)

# defaultdict method, much easier than the other method below
for letter in word:
    wc[letter] += 1

#print(wc)
"""
wc = {}

for letter in word:
    previous_count = wc.get(letter, 0)
    wc[letter] = previous_count + 1

print(wc)
"""


# GENERATOR VS LIST COMPREHENSION

squares_list = [x ** 2 for x in range(10)]

squares_gen = (x ** 2 for x in range(10))

"""print(next(squares_gen))
print(next(squares_gen))
print(next(squares_gen))
print(next(squares_gen))
for i, value in enumerate(squares_gen):
    if i == 3:
        print(value)
        break
print(squares_list)
print(squares_gen) # object is created
# in order to access we can
print(list(squares_gen))
"""


# FRIEND RECOMMENDATION PROBLEM

friendships = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

def foaf(user_id):
    direct_friends = friendships[user_id]

    foaf_list = [
        person
        for friend in direct_friends
        for person in friendships[friend]
        if person != user_id and person not in direct_friends
    ]

    return foaf_list

print(foaf(0))
