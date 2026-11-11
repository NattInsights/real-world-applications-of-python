numbers = [1, 2, 3, 4, 5]

pairs = [(x , x ** 2) for x in numbers]

sorted_by_square = sorted(pairs, key=lambda x: x[1], reverse=True)

print(sorted_by_square)    