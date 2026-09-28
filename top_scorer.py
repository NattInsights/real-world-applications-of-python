def top_scorer(scores):
    print(max(scores, key=lambda x: sum(x[1:]) / len(x[1:]))[0])
print(top_scorer([["Nooks", 34, 23, 62], ["Lisa", 18, 55, 23], ["Dee", 45, 26, 98]]))