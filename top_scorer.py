def top_scorer(results):
    avg_res = [[]]
    for i in results:
        for j in results[i]:
            print(j)

print(top_scorer([["Nooks", 34, 23, 62], ["Lisa", 18, 55, 23], ["Dee, 45, 26, 98"]]))