from collections import Counter

sentence = "Python is great and python is fun and fun is good"

wf = Counter(sentence.lower().split())

top_3 = wf.most_common(3)

# print(*wf.items())
print(", ".join([x[0] for x in top_3]))